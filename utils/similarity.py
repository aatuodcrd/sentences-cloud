from difflib import SequenceMatcher

def is_similar(text1, text2, threshold=0.8):
    ratio = SequenceMatcher(None, text1, text2).ratio()
    return ratio >= threshold

def group_similar_sentences(sentences, threshold=0.8):
    grouped = []
    for sentence in sentences:
        found = False
        for group in grouped:
            if is_similar(sentence, group[0], threshold):
                group.append(sentence)
                found = True
                break
        if not found:
            grouped.append([sentence])
    return grouped