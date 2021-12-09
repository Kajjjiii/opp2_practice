class SayHello:
    def __init__(self, target="World"):
        self.target = target

    def say(self):
        print(f"Heloo, {self.target}!!")

if __name__ == '__main__' :
    app = SayHello()
    app.say()
    app = SayHello("someone")
    app.say()       