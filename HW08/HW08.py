vowels = "аяюеёоыэуи"
s_cons = "лр"

def event(i, word):
    if i == len(word) - 1: #последняя буква в слове
        return "end"

    if word[i] not in vowels: #согласные
        if word[i] == 0: #в начале слова
            return "cont"

        elif word[i - 1] in vowels:  #гласная/согласная
            if (word[i + 1] in s_cons) and (i + 1 == len(word) - 1):
                return "cont" #согласная/сонорная
            elif (word[i + 1] in s_cons) and (i + 2 == len(word) - 1):
                return "cont" #согласная/мягкий сонорный
            elif word[i + 1] in vowels:
                return "cont" #гласная/согласная/гласная
            elif (word[i + 1] not in vowels) and (i + 1 == len(word) - 1):
                return "cont" #согласная/согласная
            else:
                return "end" #гласная/согласная/согласная
        else:
            return "cont" #согласная после согласной


    else:
        if word[i + 1] in vowels:
            return "end"  #гласная/гласная
        else:
            if i + 1 == len(word) - 1:
                return "cont"  #гласная/согласная
            if (word[i + 2] in s_cons) and (i + 2 == len(word) - 1):
                return "end"  #гласная/согласная/сонорная
            if (word[i + 2] in s_cons) and (i + 3 == len(word) - 1):
                return "end"  #гласная/согласная/сонорна
            elif word[i + 2] in vowels:
                return "end" #гласная/согласная/гласная
            else:
                return "cont" # гласная/согласная/согласная


def letter_state(letter):
    state = "consonant"
    if letter in vowels:
        state = "vowel"
    return state

def end(syll, letter):
    return "{}({})".format(string + letter, syll), ""

def cont(syll, letter):
    return string + letter, syllable + letter

table = {
    ("vowel", "end"): ["open", end],
    ("vowel", "cont"): ["-", cont],
    ("consonant", "end"): ["close", end],
    ("consonant", "cont"): ["-", cont]
}

test_words = ["корабль", "кремль", "трава", "представительство", "воля", "ответ"]

for word in test_words:
    string = ''
    syllable = ''
    for i, letter in enumerate(word):
        state = letter_state(letter)
        syll, action = table[state, event(i, word)]
        string, syllable = action(syll, letter)
    print(string)
