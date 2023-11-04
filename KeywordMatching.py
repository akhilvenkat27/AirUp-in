pip install spacy
import spacy
from collections import Counter
from string import punctuation
nlp = spacy.load("en_core_web_sm")
def get_hotwords(text):
    result = []
    pos_tag = ['PROPN', 'ADJ', 'NOUN'] 
    doc = nlp(text.lower()) 
    for token in doc:
        if(token.text in nlp.Defaults.stop_words or token.text in punctuation):
            continue
        if(token.pos_ in pos_tag):
            result.append(token.text)
    return result
new_text = """AirUp is a startup investment support-based SaaS application. Entrepreneurs can showcase their ideas and projects, seeking the necessary funding to bring them to fruition. Simultaneously, investors can explore various ideas pitched by entrepreneurs and find promising deals that align with their interests and financial goals. This platform streamlines the process of securing funding and discovering potential ground-breaking innovation by providing a centralized hub for connecting entrepreneurs and investors.
"""
l=[]
output = set(get_hotwords(new_text))
most_common_list = Counter(output).most_common(10)
for item in most_common_list:
  l.append(item[0])
print(l)

# Checking for 80% clone
l=['startup', 'funding', 'platform', 'objectives', 'reality', 'fosters', 'hub', 'airup', 'investors', 'ideas']
x=[[],['startup', 'funding', 'platform', 'hub', 'airup', 'potential', 'support', 'investors', 'ideas', 'investment']]
for i in x:
  c=0
  for j in l:
    for k in i:
      if j==k:
        c+=1
  if c==len(i)*0.8:
    print("possible clone")
