def convert_to_sample(qna):
    """
    Custom converter that preserves JSON answers and concatenates context and question into the prompt.
    """
    prompt = ""
    if "context" in qna:
        prompt += qna["context"].strip() + "\n"
    prompt += qna["question"].strip()

    return {
        "text_prompt": prompt,
        "text_completion": qna["answer"].strip()
    }

