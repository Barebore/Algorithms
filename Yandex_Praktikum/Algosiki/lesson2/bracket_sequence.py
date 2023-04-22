class Bracket:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

def is_correct_bracket_seq(bracket_seq):
    bracket_dict = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    def get_key_by_value(val):
        temp_dict = dict(zip(bracket_dict.values(), bracket_dict.keys()))
        return temp_dict[val]
    data = Bracket()
    for bracket in bracket_seq:
        if bracket in bracket_dict.keys():
            data.push(bracket)
        if bracket in bracket_dict.values():
            if data.pop() == get_key_by_value(bracket):
                continue
            else:
                return False
    return data.is_empty()

print(is_correct_bracket_seq(input()))