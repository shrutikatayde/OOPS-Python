# Hierarchical Inheritance


class A:
    def __init__(self, flower):
        self.flower = flower

    def display_flower(self):
        print(f"Flower name : {self.flower}")


class B(A):
    def __init__(self, flower, color):
        super().__init__(flower)
        self.color = color

    def display_color(self):
        super().display_flower()
        print(f"Flower Color : {self.color}")


class C(A):
    def __init__(self, flower, size):
        A.__init__(self, flower)

        self.size = size

    def display_size(self):
        print(f"Flower Size : {self.size}")


res = C("rose", "small")
ress = B("Rose", "red")


ress.display_color()
res.display_size()
