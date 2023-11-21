import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import nltk 

nltk.download()

def read_input(xlsx_file):
    return pd.read_excel(xlsx_file, header=0, dtype=str)
        
def url_content(url):
    response=requests.get(url)
    if response.status_code==200:
        url_content=response.text
        return url_content
    else:
        return ("Failed to get the url content")

def extract_article_content(file):
    title= file.find("h1")
    content = file.find('div',
             {'class': lambda x: x 
                       and "td-post-content" in x.split()
             })
    return title.text, content.text

def stop_words(article_text, stop_dir):
    stop_files= os.listdir(stop_dir)
    for s_file in stop_files:
        read_file=pd.read_csv(s_file,header=None,usecols=0)
        for word in read_file:
            word.split(()[0])
            no_stop=re.sub(f"{word}","", article_text)
    return no_stop

def positive_negative_score(file_path_nw,file_path_pw, article_text_exclude_stop):
    with open(file_path_nw) as nw:
            words= nltk.word_tokenize(article_text_exclude_stop)
            intersection_n= len(set(nw) & set(words))
    with open(file_path_pw) as nw:
            words= nltk.word_tokenize(article_text_exclude_stop)
            intersection_p= len(set(nw) & set(words))
    return intersection_n, intersection_p

def polarity_score(negative_score, positive_score):
    den=(positive_score + negative_score + 0.000001)
    num= positive_score-negative_score
    value_ps=  num / den
    return value_ps

def subjectivity_score(negative_score, positive_score, article_text_exclude_stop):
    total_words= len(nltk.word_tokenize(article_text_exclude_stop))
    den=total_words + 0.000001
    num= positive_score-negative_score
    value_ss= num/den
    return value_ss
                                   
def main():
    xlsx_df=read_input("Input.xlsx")
    for index, row in xlsx_df.iterrows():
            print(row)
            html_content=url_content(row['URL'])
            file= BeautifulSoup(html_content, "html.parser")
            article_title, article_text= extract_article_content(file)
            # what to do in case of Error:404 page not found
            with open(f"ArticleFiles/{row['URL_ID']}.txt", "w", encoding="utf-8") as url_file:
                url_file.write(f'{article_title}\n')
                url_file.write(article_text)
            article_text_exclude_stop= stop_words(article_text,"StopWords")
            negative_score, positive_score= positive_negative_score("MasterDictionary/negative-words.txt", "MasterDictionary/positive-words.txt", article_text_exclude_stop ) 
            polarity_score= polarity_score(negative_score,positive_score )
            subjectivity_score= subjectivity_score(negative_score,positive_score,article_text_exclude_stop)      
            print("Negative Score:", negative_score)
            print("Positive Score:", positive_score)
            print("Polarity Score:", polarity_score)
            print("Subjectivity Score:", subjectivity_score)       
if __name__ == '__main__':
    main()
