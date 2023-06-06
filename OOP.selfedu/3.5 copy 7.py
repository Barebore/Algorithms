class Box:
    def __init__(self):
        self.things = []

    def add_thing(self, obj):
        self.things.append(obj)

    def get_thing(self):
        return self.things
    
    # ==
    def __eq__(self, other):
        temp1 = self.things[:]
        temp2 = other.things[:]
        result = 0
        for thing in self.things:
            for other_thing in temp2:
                if thing == other_thing:
                    result += 1
                    temp1.pop(temp1.index(thing))
                    temp2.pop(temp2.index(other_thing))

        return len(temp1 == temp2)
    
    # !=
    # def __ne__(self, other):
    #     result = 0
    #     for thing in self.things:
    #         for other_thing in other.things:
    #             if thing == other_thing:
    #                 result += 1
                    
    

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass


    
    # ==
    def __eq__(self, other):
        if self.name.lower() == other.name.lower():
            return True
        return self.mass == other.mass
    
    # !=
    def __ne__(self, other):
        if self.name.lower() == other.name.lower():
            return True
        return self.mass != other.mass