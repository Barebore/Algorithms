# здесь объявляются все необходимые классы
class Graph:
    is_show = True
    def __init__(self, data):
        self.data = data[:]
    def set_data(self, data):
        if self.is_show == False:
            return print('Отображение данных закрыто')
        self.data = data
    def show_table(self):
        if self.is_show == False:
            return print('Отображение данных закрыто')
        print(f'Графическое отображение данных: {self.data}')
    def show_bar(self):
        if self.is_show == False:
            return print('Отображение данных закрыто')
        print(f'Столбчатая диаграмма: {self.data}')
    def set_show(self, fl_show):
        self.is_show = fl_show
# считывание списка из входного потока (эту строку не менять)
data_graph = [1,2,3]

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()