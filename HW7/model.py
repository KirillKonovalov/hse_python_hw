from string import punctuation
from string import digits
from stop_words import get_stop_words
from nltk.corpus import stopwords
import gensim

punct = punctuation+'©«»—…“”*№–.. '+digits
stop_words_list = get_stop_words('ru')
stop_words_list2 = stopwords.words('russian')
newlist = stop_words_list + stop_words_list2

for word in ["свой"]:
    newlist.append(word)

newlist_set = set(newlist)

with open('mystem_texts.txt', encoding='utf-8') as file1:
    data = file1.read()

clean_text_lst = []
for word in data.split():
    word = word.lower().strip(punct)
    if word not in newlist_set:
        clean_text_lst.append(word)

clean_text = ' '.join(clean_text_lst)

file2 = open('mystem_texts_clean.txt', 'w', encoding='utf-8')
file2.write(clean_text)
file2.close()

file3 = 'mystem_texts_clean.txt'
data = gensim.models.word2vec.LineSentence(file3)
model = gensim.models.Word2Vec(data, size = 300, window = 10, min_count = 2, sg = 0)
model.init_sims(replace = True)
model.save('mystem_texts_model.model')
