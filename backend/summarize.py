from transformers import pipeline

import re

summarizer = pipeline("summarization",model = "facebook/bart-large-cnn")


action_triggers = [
    "should", "need to", "must", "have to", "required to", "responsible for",
    "is assigned to", "is expected to", "will", "plan to", "to be done", "schedule to"
]

def dynamic_max_length(chunk, max_ratio=0.13, min_length=30):
    # max_length as ~13% of chunk length or at least min_length
    length = len(chunk.split())
    return max(int(length * max_ratio), min_length)



def extract_action_items(summary, triggers):
    sentences = re.split(r'(?<=[.?!])\s+', summary)
    actions = [
        sentence.strip() for sentence in sentences
        if any(trigger in sentence.lower() for trigger in triggers)
    ]
    return actions

def summarize_text(text):
    chunks = [text[i:i+1000] for i in range(0,len(text),1000)]
    summarizes = []
    
    for chunk in chunks:
        max_len = dynamic_max_length(chunk)
        summary = summarizer(chunk, max_length=max_len, min_length=20, do_sample=False)
        summarizes.extend(summary)
  
    combined_summary = " ".join([s['summary_text'] for s in summarizes])

    action_items = extract_action_items(combined_summary, action_triggers)

    return  combined_summary, action_items