import random
class Stru:
    def __init__(self):
        self.cells = [" "," "," "," "," "," "," "," "," "," "]
        
    def display(self):
        print("  %s  |  %s  |  %s  " %(self.cells[1], self.cells[2], self.cells[3]))
        print(" ---------------")
        print("  %s  |  %s  |  %s  " %(self.cells[4], self.cells[5], self.cells[6]))
        print(" ---------------")
        print("  %s  |  %s  |  %s  " %(self.cells[7], self.cells[8], self.cells[9]))
        
    def update_Cell(self, cell_no, player):
        if self.cells[cell_no]==" ":
            self.cells[cell_no] = player
    def winner(self, player):
        if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
            return True
        if self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
            return True
        if self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
            return True
        if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
            return True
        if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
            return True
        if self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
            return True
        if self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
            return True
        if self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
            return True
stur = Stru()
while True:
    P1 = int(input("X ) : Select number between 1 to 9 "))
    stur.update_Cell(P1, 'X')
    stur.display()
    break
while True:  
    P2 = random.randint(1, 9)
    stur.update_Cell(P2, 'O')
    stur.display()
    break
while True:
    P1 = int(input("X ) : Select number between 1 to 9 "))
    stur.update_Cell(P1, 'X')
    stur.display()
    break
while True:  
    P2 = random.randint(1, 9)
    stur.update_Cell(P2, 'O')
    stur.display()
    break
while True:
    P1 = int(input("X ) : Select number between 1 to 9 "))
    stur.update_Cell(P1, 'X')
    stur.display()
    if stur.winner("X"):
        print("X WINS")
    break
while True:
    P2 = random.randint(1, 9)
    stur.update_Cell(P2, 'O')
    stur.display()
    if stur.winner("O"):
        print("O WINS")
    break
