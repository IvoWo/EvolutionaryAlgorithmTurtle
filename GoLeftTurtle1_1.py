import turtle as tur
import random


population = 10
lenDNA = 40
mutationrate = 0.02
MOVES = ["F", "R", "L"]

screen = tur.Screen()
screen.bgcolor('black')

class Animal(tur.Turtle):

    def __init__(self, track) -> None:
        super().__init__()
        self.track = track
    
    fitness = 0

    def draw(self):
        for c in self.track:
            if c == "F":
                self.forward(10)
            elif c == "R":
                self.right(90)
            elif c == "L":
                self.left(90)
        self.fitness = (- (self.xcor() *  abs(self.xcor()))) 

    # mutates Steps of a Track of an Animal by Mutationrate Chance
    def Mutate(self):
        for i, j in enumerate(self.track):
            possibleMutations = MOVES
            if random.random() < mutationrate:
                possibleMutations.remove(j)
                self.track[i] = random.choice(possibleMutations)
                possibleMutations.append(j)


# provides a random Track
def getTrack():
    a = []
    for i in range (lenDNA):
        a.append(random.choice(MOVES))
    return a

# creates a list of Animals with a random Track
def intitPop():
    AN = []
    for i in range(population):
        a = Animal(getTrack())
        a.hideturtle()
        a.speed(0)
        a.color(f'#{random.randrange(256**3):06x}')
        AN.append(a)
    return AN

# creates a new Population of Animals from an old Population of Animals
def Reproduce(Pop):
    Pool = []
    for A in Pop:
        for i in range(int(A.fitness)):
            Pool.append(A)
    CPool = []
    for i in range (len(Pop)):
        A = random.choice(Pool)
        B = random.choice(Pool)
        midpoint = random.randint(1, len(A.track)-2)
        track = A.track[:midpoint] + B.track[midpoint:]
        C = Animal(track)
        C.speed(0)
        C.hideturtle()
        C.color(f'#{random.randrange(256**3):06x}')
        CPool.append(C)
    return CPool

screen = tur.Screen()
screen.bgcolor('black')
# screen.tracer(0, 0)
Gen = intitPop()


gencounter = 1

while True:
    if gencounter > 1:
        Gen = Reproduce(Gen)
        for A in Gen:
            A.Mutate()
    print('gen = ', gencounter)
    for A in Gen:
        A.draw()
    gencounter += 1
    screen.clear()
    screen.bgcolor('black')
