from math import sqrt
from sympy import *
from tkinter import Tk, Label, Button, Entry, Frame

class Uncert_Calc:
    def __init__(self, master):
        self.master = master
        master.title('Uncertainty Propagation Calc')
        master.iconbitmap('favicon.ico')

        self.frame = Frame()
        self.frame.grid(padx=20, pady=20)

        #instantiate widgets
        self.formula_label = Label(self.frame, text='Enter Formula: ')
        self.formula_entry = Entry(self.frame)
        self.submit_formula = Button(self.frame, text='Continue', command=self.generateEntries)
        
        self.answer_label = Label(self.frame, text='')

        #show widgets
        self.formula_label.grid(row=0)
        self.formula_entry.grid(row=0, column=1)
        self.submit_formula.grid(row=0, column=2, padx=10)

        self.variables = [] #symbols in function
        self.values = [] #values of the symbols
        self.uncertainties = [] #uncertainties of those values
        self.subsitutions = [] #for subs() sympy function
        self.entries = [] #generated entries
        #special functions
        self.special_2 = ('ln')
        self.special_3 = ('cos','sin','tan','sec','csc','cot','log')
        self.special_4 = ('acos','asin','atan','asec','acsc','acot')

    def generateEntries(self):
        #clear any existing entries, and the rest of the lists
        del self.entries[:]
        del self.variables[:]
        del self.values[:]
        del self.uncertainties[:]
        del self.subsitutions[:]
        
        for widget in self.frame.grid_slaves(): #grid_slaves() returns all widgets in grid
            if int(widget.grid_info()['row']) > 0:
                widget.grid_forget()

        #get formula
        funct = self.formula_entry.get()
        i = 0
        while i < len(funct): #determine variables in function
            if funct[i:i+2] in self.special_2:
                i+=2
            elif funct[i:i+3] in self.special_3:
                i+=3
            elif funct[i:i+4] in self.special_4:
                i+=4
            if funct[i].isalpha() and funct[i] not in self.variables:
                self.variables.append(funct[i])
            i+=1
            
        #create entries
        i=1 #row number
        for variable in self.variables: #set variables as symbols in sympy, create values and uncertanties list
            var(variable)
            Label(self.frame, text="Enter the value and uncertainty for '" + variable +"': '").grid(row=i)
            entry = Entry(self.frame)
            entry.grid(row=i, column=1)
            self.entries.append(entry)
            i+=1
            
        #submit button and view answer
        submit = Button(self.frame,text='Submit',command=lambda: self.calcUncert(funct))
        submit.grid(row=i,padx=10,pady=10)

    def calcUncert(self,f):
        funct = f
        sumR = 0
        
        del self.uncertainties[:]
        del self.values[:]
        
        for entry in self.entries:
            val_uncert=entry.get().split()
            self.values.append(float(val_uncert[0]))
            self.uncertainties.append(float(val_uncert[1]))

        for j in range(len(self.variables)): #create subsitutions list
            self.subsitutions.append((self.variables[j], self.values[j]))
        for i in range(0,len(self.values)): #calculate propogated uncertainty
            sumR += (diff(funct, self.variables[i]).subs(self.subsitutions) * self.uncertainties[i])**2
        result = sympify(funct).subs(self.subsitutions)
        self.answer_label['text'] = 'Answer: ' + str(round(result,3)) + ' +/- ' + str(round(sqrt(sumR),3))
        self.answer_label.grid(row=self.frame.grid_size()[1]-1, column=1)

#run gui            
root = Tk()
gui = Uncert_Calc(root)
root.mainloop()
