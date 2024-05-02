from tkinter import NW

class Operations:

    @staticmethod
    def copy(frame):
        copy = []
        for row in frame.state:
            copy.append([x for x in row])
        return copy

    @staticmethod
    def Linear(frame):
    	L=[]
    	for row in frame.state:
    	    L.extend(row)
    	return L

    @staticmethod
    def Linear2(state):
    	L=[]
    	for row in state:
    		L.extend(row)
    	return L

    @staticmethod
    def printConsole(frame):
        print(" _______")
        for row in frame.state:
            print(row) 
        print(" -------")         
        print()

    @staticmethod
    def printConsole2(state):
        print(" _______")
        for row in state:
            print(row)
        print(" -------")
        print()

    @staticmethod
    def conv2D(L):
        D = []
        counter = 0
        for i in range(3):  
            D.append([])
            for j in range(3):
                D[i].append(L[counter])
                counter+=1     
        return D


class Affichage:

    def __init__(self, canva , Lpic , window):
        self.canva = canva
        self.window = window
        self.Lpic = Lpic
    

    def afficher (self,liste1):
        canvas_width = 99 * 3
        canvas_height = 99 * 3
        image_width  = 94 
        image_height = 94
        gap = 5
        total_width = 3 * (image_width + gap)
        total_height = 3 * (image_height + gap )
        start_x = (canvas_width - total_width) // 2 
        start_y = (canvas_height - total_height) //2
        x = start_x 
        y = start_y
        for k in range(len(liste1)) :
            void = self.canva.create_image(x,y,anchor=NW,image=self.Lpic[0])
            digit = self.canva.create_image(x,y,anchor=NW,image = self.Lpic[liste1[k]])
            if (k+1) % 3 == 0:
                x = start_x
                y += image_height + gap
            else:
                x += image_width + gap

    

    # def motion (self  ,p , i=1 ):
    # 	node = p[0]
    # 	p=p[1:]
    # 	x=Operations.Linear(node.frame)
    #     D=Operations.conv2D(x)
    # 	print("coup",i," : ",Operations.printConsole2(D))
    # 	self.afficher( x )
    # 	if p:
    #         self.window.after(1500, self.motion, p, i+1)
    # 	else :
    #     	print("Nice Try :) ")
    def motion(self, p, i=1):
        node = p[0]
        p = p[1:]
        x = Operations.Linear(node.frame)
        D = Operations.conv2D(x)
        print("step", i, " : ")
        Operations.printConsole2(D)
        self.afficher(x)
        if p:
         self.window.after(1500, self.motion, p, i+1)
        else:
            print("Nice Try :)")



   




