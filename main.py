from tkinter import * 
from GraphSetUp import GraphSetUp
from Customizer import Customizer
from Operations import Operations
from Resolver import Resolver
from Frame import Frame


canvas_width = 99 * 3
canvas_height = 99 * 3
window = Tk()
can =Canvas( window,width = canvas_width,height=canvas_height,bg='gray92')
photos=[]
for i in range(0,9):
	photos.append(PhotoImage(file="./assets/"+str(i)+"-solid"+".png"))

default = [[1,2,3],[4,5,6],[7,8,0]]
cus = Customizer(default,can,photos,window)
cus.firstSetting()
cus.finalSetting()
print("Starting Point : ")
Operations.printConsole2(cus.first_state)
print("Ending Point : ")
Operations.printConsole2(cus.final_state)
# start = Operations.Linear2(cus.first_state)
frame = Frame(cus.first_state , cus)
resolver = Resolver(frame,cus)


def func1():
	cus.shuffle()
	frame.firstFrameupdate()

def func2():
	resolver.BFSearch()

def func3():
	resolver.DFSearch()

def func4():
	resolver.ASearch()

func_dict = {
	'func1': func1,
	'func2': func2,
	'func3' : func3,
	'func4' : func4
}


Graph = GraphSetUp(func_dict,cus)
Graph.windowStyle()
Graph.canStyle()