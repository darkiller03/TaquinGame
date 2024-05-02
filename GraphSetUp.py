from tkinter import * 
from Operations import Operations


class GraphSetUp:
    
    def __init__(self, func_dict,cus):
        self.window = cus.window
        self.Lpic = cus.Lpic 
        self.func1 = func_dict['func1']
        self.func2 = func_dict['func2']
        self.func3 = func_dict['func3']
        self.func4 = func_dict['func4']
        self.start = Operations.Linear2(cus.first_state)
        self.can = cus.canva

    

    def windowStyle(self):
        self.window['bg'] ='white'
        self.window.title(' Projet IA')


        
    def canStyle(self):
        # LAff = list([0,1,2,3,4,5,6,7,8])
        canvas_width = 99 * 3
        canvas_height = 99 * 3
        image_width  = 94 
        image_height = 94
        gap = 5
        # can =Canvas( self.window,width = canvas_width,height=canvas_height,bg='gray92')
        self.can.pack( side =TOP, padx =10, pady =10)
        total_width = 3 * (image_width + gap)
        total_height = 3 * (image_height + gap )
        start_x = (canvas_width - total_width) // 2 
        start_y = (canvas_height - total_height) //2
        x = start_x 
        y = start_y
        Button(self.window,text='Shuffle',command=self.func1).pack(side=LEFT,padx= (60,0))
        Button(self.window , text='Breadth',command=self.func2).pack(side=LEFT )
        Button(self.window , text='Depth',command=self.func3).pack(side=LEFT)
        Button(self.window,text='ASearch',command=self.func4).pack(side=LEFT)

        
        for k in range(len(self.Lpic)) :
            void = self.can.create_image(x,y,anchor=NW,image=self.Lpic[0])
            digit = self.can.create_image(x,y,anchor=NW,image=self.Lpic[self.start[k]])
            if (k+1) % 3 == 0:
                x = start_x
                y += image_height + gap
            else:
                x += image_width + gap
        self.can.pack()
        self.window.mainloop()
        # return can

