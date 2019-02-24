# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 23:59:49 2019

@author: dasar_000
"""

#%%

#punctuation removal from string and dict input
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~`'''



no_punct = ""
def remove_punct_str(sentence):
    no_punct = ""
    for char in sentence:
        if char not in punctuations:
            no_punct = no_punct + char
    return(' '.join(no_punct.split()))
    


def remove_punct(input1):
    if isinstance(input1,str):
        return remove_punct_str(input1)
    if isinstance(input1,dict):
        temp_dict = {}
        for key,value in input1.items():
            temp_dict.update({key:remove_punct_str(value)})
        return temp_dict
          
input_str = {'Document':"Hello!!!, he said ---and went.",'Document2':"Hello`!!!, ajaa djfa& ^ ad * he-( } said ---and went."}
#input_str = "Hello!!!, he said ---and went."       

        
print(remove_punct(input_str))

#%%
#stop word removal for a string and dict input

from nltk.corpus import stopwords # nltk.download('stopwords')
from nltk import word_tokenize #nltk.download('punkt')

stop_words = set(stopwords.words('english'))
def stop_word_removal_str(sentence):
    return " ".join(x for x in word_tokenize(sentence) if x not in stop_words)
    

def stop_word_removal(input2):
    if isinstance(input2,str):
        return stop_word_removal_str(input2)
    if isinstance(input2,dict):
        temp_dict = {}
        for key,value in input2.items():
            temp_dict.update({key:stop_word_removal_str(value)})
        return temp_dict
        
input_str = {'Document': 'Hello he sad and went', 'Document2': 'Hello ajaa djfa ad he said and went'}
print(stop_word_removal_str('Hello he  said and went'))
print(stop_word_removal('Hello he    said     and     went'))


#%%

#lemmatizing the data 


#%%

#extracting data from any type of document 



#%%

##https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.TfidfVectorizer.html

#input can be file,content  based on approach we need to redefine parameters

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer() 
data = [
     'This is the first document.',
     'This document is the second document.',
     'And this is the third one.',
     'Is this the first document?'
 ]
X = vectorizer.fit_transform(data)
print(vectorizer.get_feature_names())
print(X)
print(vectorizer.set_params)



#%%

##translators 
import translate
from translate import translator
import wikipedia ## https://pypi.org/project/wikipedia/
#print(translator.__doc__)
#translator('en', 'de', 'Hello World!')
##supported_translations.json contauns list of all supported languages
#translate.translation_table()

wikipedia.set_lang("en")
data= wikipedia.page("Cricket")
print(data.content)

#%%
#https://pythonhosted.org/goslate/ -- of all the packages this appears to be relaible .

import goslate,translate,wikipedia
from translate import Translator
gs = goslate.Goslate()


data= wikipedia.page("Cricket")
data = str(data.content)
print(data)

languages = gs.get_languages()
#print(languages['chinese'])
translator = Translator(to_lang="de")
translator.translate(data)




#%%



