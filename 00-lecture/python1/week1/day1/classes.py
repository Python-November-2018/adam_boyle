class Human:
    def __init__(self, eye_col, name):
        self.eye_color = eye_col
        self.name = name

    def say_name(self):
            print("Hi, my name is " + self.name

adam = Human("blue", "Adam")
jay = Human('brown', "Jay")

print(adam.name)
print(adam.__dict__)