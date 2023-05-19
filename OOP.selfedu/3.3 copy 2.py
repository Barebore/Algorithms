class WordString:
    def __init__(self, word=''):
        self._string = word
    
    def __len__(self):
        return len(self.string.split())
    
    def __call__(self, index):
        return self.string.split()[index]
    
    @property
    def string(self):
        return self._string
    
    @string.setter
    def string(self, value):
        self._string = value

    @string.deleter
    def string(self):
        del self._string

words = WordString()
words.string = "Курс по Python ООП"
n = len(words)
first = "" if n == 0 else words(0)
print(words.string)
print(f"Число слов: {n}; первое слово: {first}")