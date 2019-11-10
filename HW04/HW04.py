import re

def professors(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    result = re.findall('<th class="plainlist">Преподавател.+</th>\n<td class="plainlist">\n(\d+)', text)
    with open('professors.tsv', 'a', encoding='utf-8') as rslt:
        data = rslt.write(str(result[0])+'\t')
    print('Количество преподавателей:', result[0])

filename1 = input('Введите название документа с университетом:')
professors(filename1)

def capital(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    result = re.findall('data-wikidata-property-id="P36"><a href="https://ru.wikipedia.org/wiki/.+" title=".*">(\w+)', text)
    with open('capitals.tsv', 'a', encoding='utf-8') as rslt:
        data = rslt.write(str(result[0])+'\t')
    print("Столица этой страны:", result[0])

filename2 = input('Введите название документа со страной:')
capital(filename2)

def time_zone(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    
    result = re.findall('data-wikidata-property-id="P421"><a href=".+" class="mw-redirect" title="(.+)"', text)
    with open('timezones.tsv', 'a', encoding='utf-8') as rslt:
        data = rslt.write(str(result[0])+'\t')
    print("Часовой пояс этого города:", result[0])

filename3 = input('Введите название документа с городом:')
time_zone(filename3)
