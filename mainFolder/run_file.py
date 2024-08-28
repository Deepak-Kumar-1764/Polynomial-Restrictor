""" Assignment - 1
    Group -7
    Polynomial Restrictor
    Group Member- Deepak Kumar   [2103308]
                  Thaksen Karote [2103121]
                  Lalit Kumar    [2103139]
"""




import tkinter as tk  
from typing import List, Dict
import main_restrict_poly_code as rp

class PolynomialRestrictorGUI:

    #*  GUI Creation   *#
    def __init__(self):
        self.coefficients = []
        self.partial_assignment = {}
        self.restricted_coeffs = []
    
        self.window = tk.Tk()
        # icon = tk.PhotoImage(file = 'iss.png')
        self.window.title("Polynomial Restrictor")
        self.window.geometry('1600x900')
        self.window.config(background="#E7BFA2")
        # self.window.iconphoto(False,icon)

        lebel0 = tk.Label(self.window,
                    text="Assighnment -1 [Coding Theory]",
                    font =('Arial',40,'bold'),
                    fg = "white",
                    bg = 'black',
                     )

        lebel0.grid(row=0, column=0, padx=10, pady=10)
        lebel0.place(x=300,y = 13)

        # Create the input widgets
        lebel1 = tk.Label(self.window,
                    text="Enter the coefficients (ex: 1+x1*x3+2*x1^3):",
                    font =('Arial',20,'bold'),
                    fg = "blue",
                    bg = '#A9F0EA',
                    width = 36,
                     )

        lebel1.grid(row=0, column=0, padx=10, pady=10)
        lebel1.place(x=20,y = 150)
        self.poly_entry = tk.Entry(self.window, width=30,font = ('Arial',22))
        self.poly_entry.place(x=650,y=150)
        self.poly_entry.focus()
       
        lebel2 = tk.Label(self.window,
                    text="Enter the Field k:",
                    font =('Arial',20,'bold'),
                    fg = "blue",
                    bg = '#A9F0EA',
                    width = 35,
                    padx = 7
                    )

        lebel2.grid(row=1, column=0,sticky='W',padx = 10,pady = 4)
        lebel2.place(x=20,y = 220)

        self.prime_entry = tk.Entry(self.window, width=30,font = ('Arial',22))
        self.prime_entry.place(x=650,y=220)
        self.prime_entry.focus()
 

        lebel3 = tk.Label(self.window,
                    text="Enter the partial assignment (ex: x1=1, x2=2):",
                    font =('Arial',20,'bold'),
                    fg = "blue",
                    bg = '#A9F0EA', 
                    width = 35,
                    padx = 7)

        lebel3.grid(row=2, column=0,sticky='W',padx = 10,pady = 5)
        lebel3.place(x=20,y = 300)

        self.partial_assign_entry = tk.Entry(self.window, width=30,font = ('Arial',22))
        self.partial_assign_entry.place(x=650,y=300)
        self.partial_assign_entry.focus()

        lebel4 = tk.Label(self.window,
                    text="Restricted Polynomial:",
                    font =('Arial',20,'bold'),
                    fg = "blue",
                    bg = '#A9F0EA',
                    width = 35,
                    padx = 7,
                    )

        lebel4.grid(row=3, column=0,sticky='W',padx = 10,pady = 5)
        lebel4.place(x=20,y = 400)
        
        # Create the button widget
        self.restricted_coeffs_text = tk.Text(self.window, width=30,height=4,font = ('Arial',22))
        self.restricted_coeffs_text.place(x=650,y=400)

        self.button = tk.Button(self.window,
                                text="Restrict Polynomial",
                                font =('Arial',20,'bold'),
                                relief='raised',
                                fg= 'green',
                                bg = 'white',
                                bd = 20,
                                padx = 5,
                                pady = 5,
                                command=self.call_fun)
        self.button.grid(row=4, column=1, padx=0, pady=400)
        self.button.place(x = 600,y = 650)
        
        self.window.mainloop()
    
    #Example usage
    def call_fun(self):

        polynomial = self.poly_entry.get() #"1+x1*x3+x1 +x1*x2 +x1*x2*x3"
        pr = int(self.prime_entry.get())
        input_string = self.partial_assign_entry.get() #"x2=3,x1=0"
        coefficients = rp.parse_polynomial(polynomial,pr)
        
        print(coefficients)
        self.res0 = []
        self.res0 = rp.print_polynomial(coefficients)
        print(self.res0)
        if input_string != "":
            self.res = []
            variables_values=rp.parse_variable_input(input_string)
            print(variables_values)

            coefficients1= rp.partially_polynomial(polynomial,variables_values,pr)
            self.res = rp.print_polynomial(coefficients1)
            
            self.restricted_coeffs_text.delete(1.0, tk.END)
            self.restricted_coeffs_text.insert(tk.END, "".join(str(c) for c in self.res))
        else:
            self.restricted_coeffs_text.delete(1.0, tk.END)
            self.restricted_coeffs_text.insert(tk.END,"".join(str(c) for c in self.res0))
PolynomialRestrictorGUI()
