generate_sentence_prompt = \
"""
Please generate a single sentence for each group in the provided list,
ensuring that it captures the central meaning of the group while preserving its core essence.
Return the output as a list and format it exactly as shown in the example.

Data: {provided_data}

Example output format: ['สภาพอากาศวันนี้ดีมาก', 'ฉันชอบอ่านหนังสือเกี่ยวกับปัญญาประดิษฐ์', 'การเดินทางช่วยเปิดมุมมองใหม่ๆ']
"""