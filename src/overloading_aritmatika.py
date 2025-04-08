class Color:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f"red: {self.red} | green: {self.green} | blue: {self.blue}"

    def __add__(self, other):
        return Color (
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue
        )

color_1 = Color(10, 20, 30)
color_2 = Color(1, 2, 3)

print(color_1 + color_2)