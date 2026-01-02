import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self,root):
        self.root=root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False,False)

        self.expression = ""

        self.display = tk.Entry(
            root,
            font=('Arial', 24),
            borderwidth=2,
            relief="solid",
            justify='right'
        )
    
        self.display.grid(row=0,column=0,columnspan=4,padx=10,pady=20,ipady=20)
        
        self.create_buttons()  

    def create_buttons(self):
        buttons=[
            ('C',1,0,'#FF6B6B'), ('⌫',1, 1, '#FFA500'), ('√',1,2,'#4ECDC4'),   ('÷', 1, 3,'#95E1D3'),
            ('7',2,0,'#F7F7F7'), ('8',2,1,'#F7F7F7'),     ('9',2,2,'#F7F7F7'),   ('×',2,3,'#95E1D3'),
            ('4',3,0,'#F7F7F7'), ('5',3,1,'#F7F7F7'),     ('6',3,2,'#F7F7F7'),   ('-',3,3,'#95E1D3'), 
            ('1',4,0,'#F7F7F7'), ('2',4,1,'#F7F7F7'),     ('3',4,2,'#F7F7F7') ,   ('+', 4, 3, '#95E1D3'),
            ('±',5,0,'#4ECDC4'), ('0',5,1,'#F7F7F7'),     ('.',5,2,'#F7F7F7'),   ('=',5,3,'#38B6FF'),
            ('x²',6,0,'#4ECDC4'),('xʸ',6,1,'#4ECDC4'),    ('%',6,2,'#4ECDC4'),   ('()',6,3,'#4ECDC4'),                                         
        ]
        
        for (text,row,col,color) in buttons:
            button = tk.Button(
                self.root,
                text=text,
                font=('Arial',18,'bold'),
                width=5,
                height=1,
                bg=color,
                activebackground='#D3D3D3',
                command=lambda t=text: self.on_button_click(t)
            )
            button.grid(row=row,column=col,padx=5,pady=5)  

    def on_button_click(self,char):
        if char =='C':
            self.expression=""
            self.update_display("")

        elif char == '⌫':
            self.expression = self.expression[:-1]
            self.update_display(self.expression)

        elif char == '=':
            self.calculate()

        elif char == '√':
            try:
                result = math.sqrt(float(self.expression))
                self.expression = str(result)
                self.update_display(self.expression)
            except:
                messagebox.showerror("Error", "Invalid input for square root")
            
        elif char == 'x²':
            try:
                result = float(self.expression) ** 2
                self.expression = str(result)
                self.update_display(self.expression)
            except:
                messagebox.showerror("Error", "Invalid input for square")
            
        elif char == 'xʸ':
            # Power operation
            self.expression += "**"
            self.update_display(self.expression)

        elif char == '±':
            try:
                if self.expression:
                    result = -float(self.expression)
                    self.expression = str(result)
                    self.update_display(self.expression)
            except:
                messagebox.showerror("Error", "Invalid input")

        elif char == '()':
            open_count = self.expression.count('(')
            close_count=self.expression.count(')')

            if open_count == close_count:
                self.expression += '('
            else:
                self.expression +=')'
            self.update_display(self.expression)

        elif char == '%':
            try:
                result = float(self.expression)/100
                self.expression = str(result)
                self.update_display(self.expression)
            except:
                messagebox.showerror("Error", "Invalid input for percentage")

        elif char == '×':
            self.expression += "*"
            self.update_display(self.expression)
            
        elif char == '÷':
            self.expression += "/"
            self.update_display(self.expression)
            
        else:
            # Numbers and basic operators
            self.expression += str(char)
            self.update_display(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            self.update_display(self.expression)
        except ZeroDivisionError:
            messagebox.showerror("Error","Cannot divide by zero!")
            self.expression=""
            self.update_display("")
        except:
            messagebox.showerror("Error", "Invalid expression")
            self.expression=""
            self.update_display("")

    def update_display(self,value):
        self.display.delete(0,tk.END)
        self.display.insert(0,value)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
