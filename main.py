from pprint import pprint
from flask import Flask, render_template, request
from collections import Counter
from utils.similarity import group_similar_sentences
from dotenv import load_dotenv
import os
from groq import Groq
from utils.default_sentences import default_sentences
from utils.sentence_prompt import generate_sentence_prompt
import re

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    default_threshold = 0.4

    if request.method == 'POST':
        user_sentences = request.form.get('sentences', '')
        threshold = request.form.get('threshold', default_threshold, type=float)
        sentences_list = [s.strip() for s in user_sentences.split('\n') if s.strip()]
        if not sentences_list:
            sentences_list = default_sentences.copy()
            user_sentences = '\n'.join(default_sentences)
    else:
        sentences_list = default_sentences.copy()
        threshold = default_threshold
        user_sentences = '\n'.join(default_sentences)

    grouped_sentences = group_similar_sentences(sentences_list, threshold=threshold)

    load_dotenv()
    client = Groq(api_key=os.getenv('GROQ_API_KEY'))
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", 'content': generate_sentence_prompt.format(provided_data=grouped_sentences)}],
        model="deepseek-r1-distill-llama-70b",
    )
    text = chat_completion.choices[0].message.content
    match = re.search(r'</think>\s*(.*)', text, re.DOTALL)
    if match:
        extracted_text = eval(match.group(1).strip())
        pprint(extracted_text)
        project_data = [{"text": a, "count": len(b)} for a, b in zip(extracted_text, grouped_sentences)]
    else:
        counter = Counter()
        project_data = []
        for group in grouped_sentences:
            representative_text = group[0]
            counter[representative_text] = len(group)
        project_data = [{"text": text, "count": count} for text, count in counter.items()]

    pprint(project_data)
    return render_template("index.html", data=project_data, sentences=user_sentences, threshold=threshold)

if __name__ == "__main__":
    app.run(debug=True)
