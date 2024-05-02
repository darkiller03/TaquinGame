import math
import random
from Operations import *
class Customizer: 
     def __init__(self, default_state, canva ,Lpic,window):
        self.default_state = default_state
        self.first_state = default_state
        self.final_state = default_state
        self.canva = canva
        self.Lpic = Lpic
        self.window = window



     def firstSetting(self):  
         first = []
         I = input("Do you want to Customize your start Point (Y/N) : ")
         if (I == 'Y') or (I =='y'):
             for i in range(3):
                 first.append([])
                 for j in range(3):			        
                     first[i].append(int(input("T[" + str(i) + "][" + str(j) + "]: ")))
             self.first_state = first

        
        
    
     def finalSetting(self):
        final = []
        I = input("Do you want to Customize your final Point (Y/N) : ")
        if (I == 'Y') or (I =='y'):
            for i in range(3):
                final.append([])  # Initialize an empty list for each row
                for j in range(3):
                    final[i].append(int(input("T[" + str(i) + "][" + str(j) + "]: ")))
            self.final_state = final


     def shuffle(self):
        aff = Affichage(self.canva , self.Lpic , self.window)
        linear = Operations.Linear2(self.first_state)
        counter = len(linear)
        while(counter > 0):
            index = math.floor(random.random() * counter)
            counter= counter -1
            linear[counter] , linear[index] = linear[index] , linear[counter]
        aff.afficher(linear)
        self.first_state = Operations.conv2D(linear)
        print("New Starting Point After Shuffling : ")
        Operations.printConsole2(self.first_state)