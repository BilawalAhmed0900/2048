from __future__ import print_function, division

import sys    
import os
import time
import random
import datetime
import msvcrt

def getchar():
   return msvcrt.getch()
        
def first_None_Zero(_list, start_index):
        for index in range(start_index, len(_list)):
            if _list[index] != 0:
                return index
                
        return None

def rand_to_location(number):
    return [(number // 4) % 4, number % 4]
        

class table:
    def __init__(self):
        self.table = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.isfail = 0
        self.score = 0
        try:
            file = open("score", "rb")
            self.high = int.from_bytes(file.read(8), byteorder="little")
            file.close()
        except:
            self.high = 0
        
        
    def _print(self):
        for row in self.table:
            for element in row:
                if element:
                    print("| {:5d} |".format(element), end="\t")
                else:
                    print("| {:5s} |".format("    _"), end="\t")
            print("")
        print("\nBest Score: {}\tCurrent Score: {}".format(self.high, self.score), end="")
            
    def goDirection(self, direction):
        if direction == 2 or direction == 3:
            c_r_1 = self.table[0]
            c_r_2 = self.table[1]
            c_r_3 = self.table[2]
            c_r_4 = self.table[3]
            if direction == 3:
                c_r_1 = c_r_1[::-1]
                c_r_2 = c_r_2[::-1]
                c_r_3 = c_r_3[::-1]
                c_r_4 = c_r_4[::-1]
        elif direction == 0 or direction == 1:
            c_r_1 = [row[0] for row in self.table]
            c_r_2 = [row[1] for row in self.table]
            c_r_3 = [row[2] for row in self.table]
            c_r_4 = [row[3] for row in self.table]
            if direction == 1:
                c_r_1 = c_r_1[::-1]
                c_r_2 = c_r_2[::-1]
                c_r_3 = c_r_3[::-1]
                c_r_4 = c_r_4[::-1]   
        
        temp_table = [c_r_1, c_r_2, c_r_3, c_r_4]
        index = 0
        for c_r in temp_table:
            for index in range(0, 3):
                first_none_zero = first_None_Zero(c_r, index + 1)
                if first_none_zero != None and c_r[index] == 0:
                    c_r[index] = c_r[first_none_zero]
                    c_r[first_none_zero] = 0
                    self.isfail = 0
                elif first_none_zero != None and c_r[index] == c_r[first_none_zero]:
                    c_r[index] *= 2
                    self.score += c_r[index]
                    c_r[first_none_zero] = 0
                    self.isfail = 0
                elif first_none_zero == None:
                    self.isfail = index
           
        if direction == 2 or direction == 3:
            if direction == 3:
                for counter in range(0, 4):
                    temp_table[counter] = temp_table[counter][::-1]
            self.table = temp_table
        elif direction == 0 or direction == 1:
            if direction == 1:
                for counter in range(0, 4):
                    temp_table[counter] = temp_table[counter][::-1]
            self.table[0] = [row[0] for row in temp_table]
            self.table[1] = [row[1] for row in temp_table]
            self.table[2] = [row[2] for row in temp_table]
            self.table[3] = [row[3] for row in temp_table]                   
        
        is_filled = True
        for row in self.table:
            for element in row:
                if element == 0:
                    is_filled = False
        
        if is_filled == False:
            while True:
                random.seed(datetime.datetime.now())
                location = rand_to_location(random.randint(0, 16))
                if self.table[location[0]][location[1]] == 0:
                    self.table[location[0]][location[1]] = 2
                    break
        else:
            if ((self.table[0][0] != self.table[0][1] and self.table[0][0] != self.table[1][0]) and
                (self.table[3][3] != self.table[3][2] and self.table[3][3] != self.table[2][3]) and
                (self.table[0][3] != self.table[0][2] and self.table[0][3] != self.table[1][3]) and
                (self.table[3][0] != self.table[3][1] and self.table[3][0] != self.table[2][0])):
                    for row in range(1, 3):
                        for element in range(1, 3):
                            if (self.table[row][element] == self.table[row][element + 1] or
                               self.table[row][element] == self.table[row][element - 1] or
                               self.table[row][element] == self.table[row + 1][element] or
                               self.table[row][element] == self.table[row - 1][element]):
                                    is_filled = False
            else:
                is_filled = False
            if is_filled == True:
                if self.score > self.high:
                    file = open("score", "wb")
                    file.write((self.score).to_bytes(8, byteorder="little"))
                    file.close()
                sys.exit(0)
        
    def goUp(self):
        self.goDirection(0)
        
    def goDown(self):
        self.goDirection(1)
      
    def goLeft(self):
        self.goDirection(2)
    
    def goRight(self):
        self.goDirection(3)
        
    def update(self, input):
        if input == "w" or input == "W":
            self.goUp()
        elif input == "s" or input == "S":
            self.goDown()
        elif input == "d" or input == "D":
            self.goRight()
        elif input == "a" or input == "A":
            self.goLeft()
                            
        os.system("cls")
        self._print()

def main():
    os.system("cls")
    my_table = table()
    my_table._print()
    while True:
        try:
            input = getchar().decode()
        except:
            break
        
        if input == "c" or input == "C":
            os.system("cls")
            break
            
        my_table.update(input)
        
    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(-1);
