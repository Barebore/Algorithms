import re

class Morph:
    def __init__(self, *args, **kwargs):
        self.dict_words = list(args)

    def add_word(self, word):
        if word not in self.dict_words:
            self.dict_words.append(word)

    def get_words(self):
        return tuple(self.dict_words)
    
    def __eq__(self, other):
        return other.lower() in self.dict_words
    
    def __ne__(self, other):
        return other.lower() not in self.dict_words
    
dict_words = [Morph('связь', 'связи', 'связью', 'связи', 'связей', 'связям', 'связями', 'связях'),
              Morph('формула', 'формулы', 'формуле', 'формулу', 'формулой', 'формул', 'формулам', 'формулами',
                    'формулах'),
              Morph('вектор', 'вектора', 'вектору', 'вектором', 'векторе', 'векторы', 'векторов', 'векторам',
                    'векторами', 'векторах'),
              Morph('эффект', 'эффекта', 'эффекту', 'эффектом', 'эффекте', 'эффекты', 'эффектов', 'эффектам',
                    'эффектами', 'эффектах'),
              Morph('день', 'дня', 'дню', 'днем', 'дне', 'дни', 'дням', 'днями', 'днях')]

text = input()
text = re.sub(r'[–?!,.;]', '', text)
result = 0
for word in text.split():
    for morph in dict_words:
        if morph == word:
            # print(word)
            result += 1
print(result)