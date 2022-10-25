import sys

# здесь объявляется класс StreamData
class StreamData:
    def create(self,fields, ist_values):
        if len(fields) != len(ist_values):
            return False
        
        dic2 = dict(zip(fields, ist_values))
        
        for i, key in enumerate(fields):
            setattr(self,key, ist_values[i])

        return True
    
class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))  # считывание списка строк из входного потока
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()