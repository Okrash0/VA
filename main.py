
import tkinter as tk
import tkinter.ttk as ttk
from random import randint
from unicodedata import name

from sympy import true




def main():

    class Balls:
        def __init__(self, canvas, root):
            self.canvas = canvas
            self.root = root
            self.balls = []
            self.runner = True

        
        class Ball:
            def __init__(self, canvas, root,x, y, r , v=[0,0]):
                self.x0 = x - r
                self.y0 = y - r
                self.x1 = x + r
                self.y1 = y + r
                self.v = v
                self.canvas = canvas
                self.ball = canvas.create_oval(self.x0, self.y0, self.x1, self.y1, fill="red")
                self.root = root



            def move_ball(self):
                dx = self.v[0]
                dy = self.v[1]

                if self.x1 + dx > 700 or self.x0 + dx < 0:
                    dx = -dx
                    self.change_color()

                if self.y1 + dy > 700 or self.y0 + dy < 0:
                    dy = -dy
                    self.change_color()
                
                self.v[0] = dx
                self.v[1] = dy
                self.x1 += dx
                self.x0 += dx
                self.y1 += dy
                self.y0 += dy

                self.canvas.move(self.ball, dx, dy)
                self.canvas.after(30, self.move_ball)

            def change_color(self):
                self.canvas.itemconfig(self.ball, fill=_from_rgb((33,randint(0,255),randint(0,255))))
                print()

        def create_balls(self, n=1):
            for _ in range(n):
                x, y, r = randint(100,600), randint(100,600), randint(1,20)
                v = [randint(-5,5), randint(-5,5)]
                self.balls.append(self.Ball(self.canvas,root,x,y,r,v))


        def move_balls(self):
            if self.runner:
                for i in self.balls:
                    i.move_ball()
                    #i.change_color()

        def check_balls(self):
            n = int(self.root.getvar(name='num_balls'))
            #print(n)
            print(len(self.balls))
            if n > len(self.balls):
                print('yes')
                self.balls = self.balls[:n]
            elif n < len(self.balls):
                print('yeeees')
                self.create_balls(n-len(self.balls))

            self.canvas.after(1000, self.check_balls)



    def _from_rgb(rgb):
        return "#%02x%02x%02x" % rgb  

    root = tk.Tk()

    
    root.resizable(False, False)
    root.geometry('900x700')
    root.title('Balls')

    root.rowconfigure(0, minsize=200, weight=1)
    root.columnconfigure(1, minsize=200, weight=1)

    control_frame = tk.Frame(master=root, relief=tk.RAISED, bd = 2)
    visual_frame = tk.Frame(master=root, width=700, height=700, bg='red')



    # --- Ball Slider ---

    def get_current_value():
        return str(number_of_balls.get())

    def slider_changed(event):
        value_label.configure(text=get_current_value())


    n = 100

    
    start_stop_btn = ttk.Button(master= control_frame,
        text='Start/Stop'
    )
    start_stop_btn.pack()
    
    number_of_balls = tk.IntVar(root, name='num_balls')

    slider_label = ttk.Label(
        master=control_frame,
        text='Number off balls:'
    )
    slider_label.pack()

    slider = ttk.Scale(
        master=control_frame,
        from_= 0,
        to= n,
        orient='horizontal',
        command=slider_changed,
        variable=number_of_balls
    )
    slider.pack()

    value_label = ttk.Label(
        master=control_frame,
        text=get_current_value()
    )
    value_label.pack()


    # --- Visuals ---
    canvas = tk.Canvas(master=visual_frame, width=700, height=700)
    canvas.pack()


    balls = Balls(canvas, root)
    balls.create_balls(2)
    balls.move_balls()
    balls.check_balls()



    # --- Make grid ---
    visual_frame.grid(row=0,column=0, sticky='ns')
    control_frame.grid(row=0, column=1, sticky='nsew')

    root.mainloop()

    

if __name__ == '__main__':
	main()