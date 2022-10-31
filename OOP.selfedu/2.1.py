class Clock:
    def __init__(self, time = 0):
        self.__time = time

    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
        
    def get_time(self):
        return self.__time
    
    def __check_time(tm):
        if type(tm) == int and 100000>tm>=0:
            return True
        else:
            False

clock = Clock(4530)