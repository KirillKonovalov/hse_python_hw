import random

def noun_sing_m():
    '''Функция выбирает случайное существительное в единственном числе мужского рода'''
    with open ('nomsing_m.txt', 'r', encoding='cp1251') as f:
        words = f.read()
        nouns_sing = words.split()
    return random.choice(nouns_sing)

def noun_sing_f():
    '''Функция выбирает случайное существительное в единственном числе женского рода'''
    with open ('nomsing_f.txt', 'r', encoding='cp1251') as f:
        words = f.read()
        nouns_sing = words.split()
    return random.choice(nouns_sing)

def noun_plur():
    '''Функция выбирает случайное существительное во множественном числе'''
    with open ('nomplur.txt', 'r', encoding='cp1251') as f:
        words = f.read()
        nouns_plur = words.split()
    return random.choice(nouns_plur)

def random_noun(noun_sing_m, noun_sing_f, noun_plur):
    '''Функция выбирает случайное существительное из 3'''
    words = noun_sing_m + ' ' + noun_plur + ' ' + noun_sing_f
    random_n = words.split()
    result = random.choice(random_n)
    return result

def adjective(word):
    '''Функция комбинирует случайно комбинирует прилагательные с уществительными'''
    with open ('nomsing_m.txt', 'r', encoding='cp1251') as m:
        words = m.read()
        nouns_sing_m = words.split()
    with open ('nomsing_f.txt', 'r', encoding='cp1251') as f:
        words = f.read()
        nouns_sing_f = words.split()
    with open ('nomplur.txt', 'r', encoding='cp1251') as pl:
        words = pl.read()
        nouns_sing_plur = words.split()
    if word in nouns_sing_m:
        with open ('adjectives_m.txt', 'r', encoding='cp1251') as adjm:
            adjs = adjm.read()
            adjectives_m = adjs.split()
            adj_m = random.choice(adjectives_m)
            return adj_m + ' ' + word
    elif word in nouns_sing_f:
        with open ('adjectives_f.txt', 'r', encoding='cp1251') as adjf:
            adjs = adjf.read()
            adjectives_f = adjs.split()
            adj_f = random.choice(adjectives_f)
            return adj_f + ' ' + word
    else: 
        with open ('adjectives_pl.txt', 'r', encoding='cp1251') as adjpl:
            adjs = adjpl.read()
            adjectives_pl = adjs.split()
            adj_pl = random.choice(adjectives_pl)
            return adj_pl + ' ' + word
        
def adverb():
    '''Функция выбирает случайное наречие'''
    with open ('adverbs.txt', 'r', encoding='cp1251') as f:
        words = f.read()
        adverbs = words.split()
    return random.choice(adverbs)

def intensifier(adv):
    '''Функция случайно выбирает интесифаер для наречия'''
    with open ('intensifiers.txt', 'r', encoding='cp1251') as f:
        words = f.read()
        intensifiers = words.split()
        random_intensifier = random.choice(intensifiers)
        result = random_intensifier + ' ' + adv
    return result

def verb_of_thought(subj):
    '''Функция случайно выбирает глагол мысли'''
    if subj.endswith('ы') or subj.endswith('и'):
        with open ('verb_of_thought_plur.txt', 'r', encoding='cp1251') as f:
            words = f.read()
            verbs_pl = words.split()
            random_verb_pl = random.choice(verbs_pl)
            return subj + ' ' + random_verb_pl
    else:
        with open ('verb_of_thought_sing.txt', 'r', encoding='cp1251') as s:
            words = s.read()
            verbs_s = words.split()
            random_verb_s = random.choice(verbs_s)
            return subj + ' ' + random_verb_s
        
def verb_of_action(subj):
    '''Функция случайно выбирает глагол действия'''
    if subj.endswith('ы') or subj.endswith('и'):
        with open ('verb_of_action_plur.txt', 'r', encoding='cp1251') as f:
            words = f.read()
            verbs_pl = words.split()
            random_verb_pl = random.choice(verbs_pl)
            return subj + ' ' + random_verb_pl
    else:
        with open ('verb_of_action_sing.txt', 'r', encoding='cp1251') as s:
            words = s.read()
            verbs_s = words.split()
            random_verb_s = random.choice(verbs_s)
            return subj + ' ' + random_verb_s

def random_sentence_positive():
    '''Функция для случайного утвердительного предложения'''
    sentence = verb_of_thought(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))).capitalize() +\
               ', что ' + verb_of_action(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))) +\
               ' ' + intensifier(adverb()) + '.'
    return sentence

def verb_of_thought_negative(subj):
    '''Функция случайно выбирает отрицательный глагол мысли'''
    if subj.endswith('ы') or subj.endswith('и'):
        with open ('verb_of_thought_plur.txt', 'r', encoding='cp1251') as f:
            words = f.read()
            verbs_pl = words.split()
            random_verb_pl = random.choice(verbs_pl)
            return subj + ' не ' + random_verb_pl
    else:
        with open ('verb_of_thought_sing.txt', 'r', encoding='cp1251') as s:
            words = s.read()
            verbs_s = words.split()
            random_verb_s = random.choice(verbs_s)
            return subj + ' не ' + random_verb_s
        
def random_sentence_negative():
    '''Функция для случайного отрицательного предложения'''
    sentence = verb_of_thought_negative(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))).capitalize() +\
               ', что ' + verb_of_action(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))) +\
               ' ' + intensifier(adverb()) + '.'
    return sentence

def random_question():
    '''Функция для случайного вопроса'''
    sentence = verb_of_thought(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))).capitalize() +\
               ', что ' + verb_of_action(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))) +\
               ' ' + intensifier(adverb()) + '?'
    return sentence

def random_sentence_conditional():
    '''Функция для случайного предложения условия'''
    sentence = 'Если ' + verb_of_action(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))) +\
               ', то ' + verb_of_action(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))) +\
               ' ' + intensifier(adverb()) + '.'
    return sentence

def random_imperative():
    '''Функция для случайного побудительного предложения'''
    sentence = 'Пусть ' + verb_of_action(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))) + ' ' + intensifier(adverb()) +\
               ', a ' + verb_of_action(adjective(random_noun(noun_sing_m(), noun_sing_f(), noun_plur()))) +\
               ' ' + intensifier(adverb()) + '.'
    return sentence

def random_sentences():
    '''Функция для случайных предложений всех типов в случайном порядке'''
    sentences = [random_sentence_positive(), random_sentence_negative(), random_question(), random_sentence_conditional(), random_imperative()]
    for s in random.sample(sentences, len(sentences)):
        print(s)

def main():
    '''Это главная функция, из неё вызывается всё остальное'''
    print(random_sentences())
    return 0

if __name__ == '__main__':
    main()
