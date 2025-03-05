class Bird:
    def fly(self):
        return "Flying"

class Sparrow (Bird):
    pass

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError ("Penguins can't fly!")