from string import punctuation
from string import digits
from stop_words import get_stop_words
from nltk.corpus import stopwords
import gensim

punct = punctuation+'©«»—…“”*№–.. '+digits
stop_words_list = get_stop_words('en')
stop_words_list2 = stopwords.words('english')
newlist = stop_words_list + stop_words_list2

for word in ["said", "one", "man", "like", "back", "told", "see", "looked", "men", "never", "made", "©", "eyes", "hair",
             "face", "fingers", "around", "saw", "asked", "he's", "he’s", "that’s", "want", "i'm", "i’m", "i’ll", "thing",
             "might", "don’t", "can’t", "can't", "us", "much", "that's", "yes", "no", "think", "thought", "it's", "always", "wanted",
             "perhaps", "voice", "taken", "called", "come", "say", "you’re", "it’s", "nothing", "get", "gave", "put", "better",
             "give", "tell", "go", "ever", "even", "replied", "others", "without", "coming"]:
    newlist.append(word)

newlist_set = set(newlist)

with open('got.txt', encoding='utf-8') as file1:
    data = file1.read()

clean_text_lst = []
for word in data.split():
    word = word.lower().strip(punct)
    if word not in newlist_set:
        clean_text_lst.append(word)

clean_text = ' '.join(clean_text_lst)

file2 = open('got_clean.txt', 'w', encoding='utf-8')
file2.write(clean_text)
file2.close()

file3 = 'got_clean.txt'
data = gensim.models.word2vec.LineSentence(file3)
model = gensim.models.Word2Vec(data, size = 300, window = 10, min_count = 2, sg = 0)
model.init_sims(replace = True)
model.save('got_model.model')
