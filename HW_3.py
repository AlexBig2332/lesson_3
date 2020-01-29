with open('text.txt', mode = 'rt', encoding = 'utf-8') as t:
    text = t.read()

print()
print('   1) методами строк очистить текст от знаков препинания :')
print()
no_sign = ''
sign_list = '. ? ! , ; : - — ( ) " « »'.split()

for i in sign_list:
    text = text.replace(i, no_sign)
print(text)

print()
print('   2) сформировать list со словами (split) :')
words = text.split()
print(words)

print()
print('   3) привести все слова к нижнему регистру (map) :')
temp = list(map(lambda x: x.lower(), words))
print(temp)

print()
print('   3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте :')
print()
text_dict = {a: temp.count(a) for a in temp}
for keys, values in text_dict.items():
    print(keys, values)


print()
print('   4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set);')
print()
pop_words = []
for a in text_dict.values():
    pop_words.append(a)
pop_words.sort()

pop_5words = pop_words[-5:]
for keys, values in text_dict.items():
    if values in pop_5words:
        print(keys, values)

print()
print('   PRO: 5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.')
print()
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
morph_list = list(map(lambda x: morph.parse(x[0])[0].normal_form, temp))
print(morph_list)
