print('python code evaluated in emacs')

class Animal:
    def move(self):
        print('move')

def run(a):
    print('run')

animal = Animal()

animal.move()

animal.move = run

animal.move(animal);
