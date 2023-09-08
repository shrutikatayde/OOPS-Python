class MultiLevel:
    def __init__(self, dish, category):
        self.dish = dish
        self.category = category

    def show_details(self):
        print(f"Dish Name :  {self.dish}")
        print(f"Category : {self.category}")


class MultiLevelChild(MultiLevel):
    def __init__(self, dish, color):
        MultiLevel.__init__(self, dish, category="Sweet")
        self.color = color

    def show_details(self):
        MultiLevel.show_details(self)
        print(f"Color : {self.color}")


class MultilevelChildsChild(MultiLevelChild):
    def __init__(self, dish, isjuicy):
        MultiLevelChild.__init__(self, dish, color="Red")
        self.isjuicy = isjuicy

    def show_details(self):
        MultiLevelChild.show_details(self)
        print(f"Is it Juicy : {self.isjuicy}")


# result = MultiLevel("Gulab Jamoon", "Sweet")
# result.show_details()

result3 = MultilevelChildsChild("Gulab jamoom", "Yes")
result3.show_details()

print(MultilevelChildsChild.mro())
