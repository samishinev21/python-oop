class Integer:
    ROMANS = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7, "VIII": 8, "IX": 9, "X": 10, "XIX": 19}
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        try:
            number = int(float_value)
        except ValueError:
            return "value is not a float"
    
        return cls(number)
    
    @classmethod
    def from_roman(cls, value):
        return cls(cls.ROMANS[value])
    
    @classmethod
    def from_string(cls, value):
        if type(value) == str:
            number = int(value)
            return cls(number)
        else:
            return "wrong type"

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))