class Graph:
    LIMIT_Y = list(range(0,11))

    def set_data(self, data):
        self.data = data
    
    def draw(self):
        print(*list(filter(lambda x: x in self.LIMIT_Y,self.data)))
    

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

