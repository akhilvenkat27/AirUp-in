!python -m spacy download en_core_web_sm
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
def textSummarizer(text, percentage):
    nlp = spacy.load('en_core_web_sm')
    doc= nlp(text)
    tokens=[token.text for token in doc]
    freq_of_word=dict()
    for word in doc:
        if word.text.lower() not in list(STOP_WORDS):
            if word.text.lower() not in punctuation:
                if word.text not in freq_of_word.keys():
                    freq_of_word[word.text] = 1
                else:
                    freq_of_word[word.text] += 1
    max_freq=max(freq_of_word.values())
    for word in freq_of_word.keys():
        freq_of_word[word]=freq_of_word[word]/max_freq
    sent_tokens= [sent for sent in doc.sents]
    sent_scores = dict()
    for sent in sent_tokens:
        for word in sent:
            if word.text.lower() in freq_of_word.keys():
                if sent not in sent_scores.keys():                            
                    sent_scores[sent]=freq_of_word[word.text.lower()]
                else:
                    sent_scores[sent]+=freq_of_word[word.text.lower()]
    len_tokens=int(len(sent_tokens)*percentage)
    summary = nlargest(n = len_tokens, iterable = sent_scores,key=sent_scores.get)
    final_summary=[word.text for word in summary]
    summary=" ".join(final_summary)
    return summary
final_summary = textSummarizer("#you input here", 0.25)
print(final_summary)

"""Example:  
Input:
AirUp is a startup investment support-based SaaS application. Entrepreneurs can showcase their ideas and projects, seeking the necessary funding to bring them to fruition. Simultaneously, 
investors can explore various ideas pitched by entrepreneurs and find promising deals that align with their interests and financial goals. 
This platform streamlines the process of securing funding and discovering potential ground-breaking innovation by providing a centralized hub for connecting entrepreneurs and investors.

Output:
This platform streamlines the process of securing funding and discovering potential ground-breaking innovation by providing a centralized hub for connecting entrepreneurs and investors.
"""
