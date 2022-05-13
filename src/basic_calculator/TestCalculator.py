class TestCalculator:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2

    @staticmethod
    def add(val1, val2):
        return val1 + val2

    def addval(self):
        return self.val1 + self.val2

    @classmethod
    def addval2(cls, val1, val2):
        return cls.add(val1, val2)

