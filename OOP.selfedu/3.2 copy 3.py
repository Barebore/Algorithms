class DigitRetrive:
    def __call__(self, string: str):
        try:
            return int(string)
        except ValueError:
            return None
st = DigitRetrive()

print(st(213.3))