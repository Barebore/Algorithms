class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, mem_slots, total_mem_slots = 4):
        self.name  = name
        self.mem_slots = mem_slots
        self.cpu = cpu
        self.total_mem_slots = total_mem_slots
    def get_config(self):
        lst = []
        lst.append(f'Материнская плата: {self.name}')
        lst.append(f'Центральный процессор: {self.cpu.name}, {self.cpu.fr}')
        lst.append(f'Слотов памяти: {self.total_mem_slots}')
        row = ''
        for i in self.mem_slots:
            row += i.name + ' - ' + str(i.volume) + '; '
        lst.append(f'Память: {row[:len(row)-2]}')
        return lst
cpu = CPU('AMD', 1333)
mem1, mem2 = Memory('Kingstone', 4000), Memory('Kingstone', 3000)
mb = MotherBoard('MSI', cpu, [mem1, mem2])
print(mb.get_config())