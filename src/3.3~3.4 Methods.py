#     def start(self):
#         print(self.color)
#         print("I started")
# porche = Car()
# porche.color = "Red Sexy Red"
# porche.start()


class Car():

    def __init__(self, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"


class Convertible(Car):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 부모의 __init__ 호출하여 사용 가능. (인자값으로 **kwargs를 쓰겠다.)
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"


class Something(Convertible):
    pass


porche = Convertible(color="green", price="$40")
print(porche.color)


mini = Car()
# print(mini.color, mini.price)
