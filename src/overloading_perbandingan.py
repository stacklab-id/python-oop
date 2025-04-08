class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f"red: {self.red} | green: {self.green} | blue: {self.blue}"

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue

color_1 = Color(10, 20, 30)
color_2 = Color(10, 20, 30)

print(color_1 == color_2)