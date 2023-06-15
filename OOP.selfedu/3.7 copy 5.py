class GamePole:
    def __new__(self, *args, **kwargs):
        pass

    def __init__(self, size):
        self.size = size
        self.pole = [[0 for _ in range(size)] for _ in range(size)]