class Tidish:
    def __init__(self, word):
        self.word = word

    def stem(self):
        w = self.word
        if w.endswith('тыдыщ'):
            normal_form = w[:-5]
        elif w.endswith('эго'):
            normal_form = w[:-3]
        elif w.endswith('рио'):
            normal_form = w[:-3]
        else:
            normal_form = w
        return normal_form

    def case(self):
        w = self.word
        with open('dict_S.json', encoding='utf-8') as f:
            s_dict = f.read()
            stem_word = self.stem()
            if stem_word in s_dict:
                if w.endswith('тыдыщ'):
                    case_form = 'Косвенный'
                else:
                    case_form = 'Номинативный'
            else:
                case_form = 'Нет падежа'

        return case_form

    def tense(self):
        w = self.word
        with open('dict_V.json', encoding='utf-8') as f2:
            v_dict = f2.read()
            stem_word = self.stem()
            if stem_word in v_dict:
                if w.endswith('эго'):
                    tense = 'Прошедшее время'
                elif w.endswith('рио'):
                    tense = 'Будущее время'
                else:
                    tense = 'Настоящее время'
            else:
                tense = 'Нет времени'

        return tense

w_count = 0
analysis = []
with open('test.txt', encoding='utf-8') as f:
    t = f.read()
    for w in t.split():
        w_analysis = []
        w_count += 1
        ana = Tidish(w)
        w_analysis.append('Номер слова: {}'.format(w_count))
        w_analysis.append('Слово: {}'.format(w))
        w_analysis.append('Основа: {}'.format(ana.stem()))
        w_analysis.append('Падеж: {}'.format(ana.case()))
        w_analysis.append('Время: {}'.format(ana.tense()))
        analysis.append(w_analysis)

with open('analysis.txt', 'w', encoding='utf-8') as fw:
    for lst in analysis:
        fw.write(', '.join(lst) + '\n')
