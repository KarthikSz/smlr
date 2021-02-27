import json
import logging

import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

logger = logging.getLogger(__name__)


def summarize(text):
    """
    Returns the summarized text for the input text using torch and T5 transformers
    """
    
    model = T5ForConditionalGeneration.from_pretrained('t5-small')
    tokenizer = T5Tokenizer.from_pretrained('t5-small')
    device = torch.device('cpu')

    preprocess_text = text.strip().replace("\n","")
    t5_prepared_Text = "summarize: "+preprocess_text
    logger.info("Original text preprocessed: \n" + preprocess_text)

    tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)

    summary_ids = model.generate(tokenized_text,
                                        num_beams=4,
                                        no_repeat_ngram_size=2,
                                        min_length=30,
                                        max_length=100,
                                        early_stopping=True)

    output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    logger.info("Summarized text: \n" + output)

    return output
