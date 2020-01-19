import requests
from bs4 import BeautifulSoup
import os
import time 
import random 
import csv
import pymorphy2
from nltk import word_tokenize
from string import punctuation

current_dir = os.path.abspath(os.getcwd())
os.makedirs(current_dir + '\\root\\plain text\\2019')
os.makedirs(current_dir + '\\root\\parsed text\\2019')

url = 'https://www.svoboda.org/news/2019/'

with open(current_dir + '\\root\\meta_data.csv', 'a', encoding='UTF-8') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['path','author','date','source','title','url','wordcount'])
    
count_n = 1
count_p = 1
morph = pymorphy2.MorphAnalyzer()
    
for month in range(1, 13):  
    os.mkdir(current_dir + '\\root\\plain text\\2019\\' + str(month))
    os.mkdir(current_dir + '\\root\\parsed text\\2019\\' + str(month))
    path_to_file = current_dir + '\\root\\plain text\\2019\\' + str(month) + '\\'
    
    for day in range(1,32):
        date = str(day) + '.' + str(month) + '.' + '2019'
        path_to_file = current_dir + '\\root\\plain text\\2019\\' + str(month) + '\\'
        time.sleep(random.randint(1,6))
        r = requests.get(url + '/' + str(month) + '/' + str(day))
        content = r.content
        html = content.decode('UTF-8')
        soup = BeautifulSoup(html, "lxml")
        
        for link in soup.find_all('a', attrs={'class':'img-wrap'}):
            time.sleep(random.randint(1,6))
            l = 'https://www.svoboda.org'
            web_link = link.get('href')
            page = requests.get(l + web_link)
            web = l + web_link
            content2 = page.content
            html2 = content2.decode('UTF-8')
            soup2 = BeautifulSoup(html2, "lxml")
            
            try:
                heading = soup2.find('h1', attrs={'class':'pg-title'})
                article_name = heading.get_text() 
                article = soup2.find('div', attrs={'id':'article-content'})
                
                news_list = []
                for p in article.find_all('p'):
                    parts = p.get_text()
                    news_list.append(parts)
                    news = ''
                    news = news.join(news_list)
                    
                list_of_news_words = []
                news_words = word_tokenize(news)
                for word in news_words:
                    if word not in punctuation:
                        list_of_news_words.append(word)
                length = len(list_of_news_words)
                
                article_path = path_to_file + str(count_n) + '.txt'
                with open(article_path, 'w', encoding='UTF-8') as file:
                    count_n += 1
                    file.write(news)
                    
                with open(current_dir + '\\root\\meta_data.csv', 'a', encoding='UTF-8') as csvfile:
                    filewriter = csv.writer(csvfile, delimiter=';')
                    filewriter.writerow([article_path, 'no author', date,'svoboda.org', article_name, web, length])
                    
                path_for_parse = current_dir + '\\root\\parsed text\\2019\\'
                parsed_words = []
                words = word_tokenize(news)
                for word in words:
                    parsed_word = str(morph.parse(word)[0])
                    parsed_words.append(parsed_word)
                    parsed_news = ''
                    parsed_news = parsed_news.join(parsed_words)
                
                with open(path_for_parse + str(month) + '\\' + str(count_p) + '.txt' , 'w', encoding='UTF-8') as parse_file:
                    count_p += 1
                    parse_file.write(parsed_news)
                
        
            except:
                pass 
