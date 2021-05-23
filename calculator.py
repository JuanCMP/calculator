from tkinter import Tk, Text, Button ,END, re

class Interface:
    
    def __init__(self, window):
        
        self.window=window
        self.window.title("Calculator")
        self.display = Text(window, state="disabled", width=25, height=3, background="snow", foreground="white", font=("Helvetica",15))
        self.display.grid(row=0, column=0, columnspan=2, padx=1, pady=1)
        self.operation=''
        
        button7 = self.made_button(7)
        button8 =self.made_button(8)
        button9 =self.made_button(9)
        button_delete =self.made_button(u'\u232B', typing=False)
        button4 =self.made_button(4)
        button5 =self.made_button(5)
        button6 =self.made_button(6)
        button_divide =self.made_button(u'\u00F7')
        button1 =self.made_button(1)
        button2 =self.made_button(2)
        button3 =self.made_button(3)
        button_mult =self.made_button('*')
        button_dot =self.made_button('.')
        button0 =self.made_button(0)
        buttonsum =self.made_button('+')
        button_sub =self.made_button('-')
        button_equals =self.made_button('=', typing=False, width=10, height=2)
        
        buttons = [button7,button8,button9,button_delete,button4,button5,button6,button_divide,button1,button2,button3,button_mult,button_dot,button0,buttonsum,button_sub,button_equals]
        counter=0
        for row in range(1, 5):
            for column in range(4):
                buttons[counter].grid(row=row, column=column)
                counter += 1
        buttons[16].grid(row=5, column=0, columnspan=4)
        return
       
    
    def made_button(self, value, typing=True, width=4, height=1):
        
        return Button(self.window, text=value, width=width, height=height, font=('Helvetica', 15), command=lambda:self.click(value, typing))

    
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
            self.operation+=str(text)
            self.showDisplay(text)
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
