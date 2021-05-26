from tkinter import Tk, Text, Button ,END, re, Label

class Interface:
    
    def __init__(self, window):
        
        self.window = window
        self.window.title("Calculator")
        self.display = Text(window, state="disabled", width=28, height=3, background="snow", foreground="black", font=("Helvetica",15))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5) 
        Label(window, text="scientific calculator", font=("Terminal",10)).grid(row=1, columnspan=2)
        self.operation = ''
        
        button7 = self.made_button(7)
        button8 = self.made_button(8)
        button9 = self.made_button(9)
        button_delete = self.made_button(u'\u232B', typing=False)
        button4 = self.made_button(4) 
        button5 = self.made_button(5)
        button6 = self.made_button(6)
        button_divide = self.made_button(u'\u00F7')
        button1 = self.made_button(1)
        button2 = self.made_button(2)
        button3 = self.made_button(3)
        button_mult = self.made_button('*')
        button_dot = self.made_button('.')
        button0 = self.made_button(0)
        buttonsum = self.made_button('+')
        button_sub = self.made_button('-')
        button_equals = self.made_button('=', typing=False, width=5, height=1)
        
        #New features
        button_sroot = self.made_button(u'\u221A', typing = False)
        button_pow = self.made_button(u'\u02C4')
        button_percentaje = self.made_button(u'\u0025', typing=False)
        button_sin = self.made_button('sin')
        button_cos = self.made_button('cos')
        button_tan = self.made_button('tan')
        button_log = self.made_button('log')
        button_ln = self.made_button('ln')
        button_fac = self.made_button('!')
        button_obrackets = self.made_button('(')
        button_cbrackets = self.made_button(')')
        button_pi = self.made_button(u'\u03C0')
        button_euler = self.made_button(u'\u212F')
        

        buttons = [
            button_log, button_ln, button_fac, button_percentaje,
            button_obrackets, button_cbrackets, button_pi, button_euler,
            button_sroot, button_pow, button_dot, button_divide,
            button7, button8, button9, button_mult,
            button4, button5, button6, button_sub,
            button1, button2, button3, buttonsum,
            button0, button_equals,button_sin, button_cos, button_tan, button_delete   
            ]
        
        buttons[26].grid(row=2, column=0) #sen
        buttons[27].grid(row=2, column=1) #cos
        buttons[28].grid(row=2, column=2) #tan
        buttons[29].grid(row=2, column=3) # del

        counter=0
        for row in range(3, 9):
            for column in range(4):
                buttons[counter].grid(row=row, column=column)
                counter += 1
        return 
         
    
    def made_button(self, value, typing=True, width=5, height=1):
        return Button(self.window, text=value, width=width, height=height, font=('Helvetica', 15), command=lambda:self.click(value, typing), activebackground='gray2', activeforeground='green2', relief='groove')

    
    def click(self,text,typing):
        
        if not typing:
            if text=="=" and self.operation!="":
                self.operation=re.sub(u"\u00F7", "/", self.operation)
                result=str(eval(self.operation))
                self.operation=""
                self.displayClear()
                self.showDisplay(result)
            elif text==u"\u232B":
                self.operation=""    
                self.displayClear()
        else:
            self.operation+=str(text) # wtf?
            self.showDisplay(text)    # 
        return
    
    #Borra el contenido de la pantalla de la calculadora
    def displayClear(self):
        self.display.configure(state="normal")
        self.display.delete("1.0", END)
        self.display.configure(state="disabled")
        return
    

    #Muestra en la pantalla de la calculadora el contenido de las operaciones y los resultados
    def showDisplay(self, value):
        self.display.configure(state="normal")
        self.display.insert(END, value)
        self.display.configure(state="disabled")
        return 



main_window=Tk()
calculator=Interface(main_window)
main_window.mainloop()
