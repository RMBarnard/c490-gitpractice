import my_object

class MyDerivedObject(MyObject):
    def --init(self):
        super().init()

    def __str__(self):
        return self.greeting
