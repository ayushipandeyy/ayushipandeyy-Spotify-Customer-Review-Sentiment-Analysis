#!/usr/bin/env python
# coding: utf-8

# # <font color = 'purple'>We are now creating your own python library to clean a text</font>
# > - <font size =3, color = 'green'>While finishing, you can directly import this library to clean the text
# > - <font size =3, color = 'green'>You don't have to build the library from scratch; just continue to develope it based on the library I built.
# > - <font size =3, color = 'green'>It's unnecessay to run these functions/cells here because no errors will show up even if there are errors here. Guess why?

# # <font color = 'purple'>Let's read through them without running them.</font>

# In[1]:


get_ipython().system('pip install spacy')
import nltk
import spacy
import re
from nltk.corpus import wordnet
from nltk.tokenize.toktok import ToktokTokenizer


# In[ ]:


tokenizer = ToktokTokenizer()
raw_list = nltk.corpus.stopwords.words('english')
stopwords = set(raw_list)-{"not","no"}


# In[ ]:


CONTRACTION_MAP = {
    "ain't": "is not","aren't": "are not","can't": "cannot","can't've": "cannot have","'cause": "because","could've": "could have","couldn't": "could not","couldn't've": "could not have","didn't": "did not","doesn't": "does not","don't": "do not","hadn't": "had not","hadn't've": "had not have","hasn't": "has not","haven't": "have not","he'd": "he would",
    "he'd've": "he would have","he'll": "he will","he'll've": "he he will have","he's": "he is","how'd": "how did","how'd'y": "how do you","how'll": "how will","how's": "how is","I'd": "I would","I'd've": "I would have","I'll": "I will","I'll've": "I will have","I'm": "I am","I've": "I have","i'd": "i would","i'd've": "i would have","i'll": "i will","i'll've": "i will have","i'm": "i am","i've": "i have","isn't": "is not","it'd": "it would","it'd've": "it would have","it'll": "it will","it'll've": "it will have","it's": "it is","let's": "let us","ma'am": "madam","mayn't": "may not","might've": "might have","mightn't": "might not", "mightn't've": "might not have","must've": "must have","mustn't": "must not","mustn't've": "must not have","needn't": "need not","needn't've": "need not have","o'clock": "of the clock","oughtn't": "ought not","oughtn't've": "ought not have", "shan't": "shall not","sha'n't": "shall not", "shan't've": "shall not have","she'd": "she would","she'd've": "she would have","she'll": "she will", "she'll've": "she will have","she's": "she is","should've": "should have","shouldn't": "should not","shouldn't've": "should not have","so've": "so have","so's": "so as","that'd": "that would","that'd've": "that would have","that's": "that is", "there'd": "there would","there'd've": "there would have","there's": "there is",
    "they'd": "they would","they'd've": "they would have","they'll": "they will","they'll've": "they will have","they're": "they are", "they've": "they have", "to've": "to have","wasn't": "was not", "we'd": "we would", "we'd've": "we would have","we'll": "we will","we'll've": "we will have","we're": "we are","we've": "we have","weren't": "were not","what'll": "what will","what'll've": "what will have","what're": "what are","what's": "what is","what've": "what have","when's": "when is","when've": "when have","where'd": "where did","where's": "where is","where've": "where have","who'll": "who will", "who'll've": "who will have", "who's": "who is", "who've": "who have", "why's": "why is","why've": "why have", "will've": "will have", "won't": "will not","won't've": "will not have","would've": "would have","wouldn't": "would not","wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would","y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have","you'd": "you would","you'd've": "you would have","you'll": "you will", "you'll've": "you will have", "you're": "you are","you've": "you have"
}


# In[ ]:


def my_lowercase (text):
    text = text.lower()
    return text


def my_expanding (text, mapping):
    for key, value in mapping.items():
        text = re.sub(key, value, text)
    return text

def my_stopwords (text):
    tokens = tokenizer.tokenize(text)
    filtered_tokens = [token for token in tokens if token not in stopwords]
    text = ' '.join(filtered_tokens)
    return text
   

def my_specialChar_remover(text):
    pattern = r"[@$#:)'!]"
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text
    
def my_annoyingChar_remover (text):
    text = re.sub(r'[\t\r\n|]+', '', text)
    text = re.sub(' +',' ',text)            # ' +' matches sequences of one or more consecutive spaces.
    text = re.sub(r"[^a-zA-Z\s]", '', text)
    return text
    

# you can continue to build individual functions to:
#### lemmatizaton
#### correct misspelled words
#### remove special characters
#### remove accented characters
#### ...


# In[ ]:


def myText_normalizer (corpus, f1 = True, f2 = True, f3 = True, f4 = True, f5= True, f6=True):
    normalized_corpus = []
    for doc in corpus:
        if f1:
            doc = my_lowercase(doc)   
        if f2:
            doc = my_expanding(doc,CONTRACTION_MAP)
        if f3:
            doc = my_stopwords (doc)
        if f4:
            doc = my_specialChar_remover(doc)
        if f5:
            doc = my_annoyingChar_remover (doc)
        
        normalized_corpus.append(doc)
    return normalized_corpus


# In[ ]:




