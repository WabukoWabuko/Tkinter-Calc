


from tkinter import *

main_window = Tk()

#numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0

#text input area
e = Entry(main_window, width= 50, borderwidth= 25)
e.grid(row= 0, column= 0, columnspan= 3, padx= 30 )

list_of_numbers = []

#function to activate buttons
def number_input(number):
    current_value = e.get()
    e.delete(0, END)
    e.insert(f"{current_value} + {number}")


def clear_value():
    list_of_numbers.clear()
    e.delete(0, END)

def sum_of_values():
    num1 = e.get()
    list_of_numbers.append(number)
    e.delete(0, END)

def equals():
    num1 = e.get()
    list_of_numbers.append(int(num1))
    e.delete(0, END)

    SUM = 0
    for values in list_of_numbers:
        SUM += int(values)

    e.insert(0, int(SUM))


#button
bttn9 = Button(main_window, text= "9", padx= 40, pady= 20, command= lambda : number_input(9), background=("lightblue") )
bttn9.grid(row= 1, column= 0)
bttn8 = Button(main_window, text= "8", padx= 40, pady= 20, command= lambda : number_input(8) )
bttn8.grid(row= 1, column= 1)
bttn7 = Button(main_window, text= "7", padx= 40, pady= 20, command= lambda : number_input(7) )
bttn7.grid(row= 1, column= 2)

bttn6 = Button(main_window, text= "6", padx= 40, pady= 20, command= lambda : number_input(6) )
bttn6.grid(row= 2, column= 0)
bttn5 = Button(main_window, text= "5", padx= 40, pady= 20, command= lambda : number_input(5) )
bttn5.grid(row= 2, column= 1)
bttn4 = Button(main_window, text= "4", padx= 40, pady= 20, command= lambda : number_input(4) )
bttn4.grid(row= 2, column= 2)

bttn3 = Button(main_window, text= "3", padx= 40, pady= 20, command= lambda : number_input(3) )
bttn3.grid(row= 3, column= 0)
bttn2 = Button(main_window, text= "2", padx= 40, pady= 20, command= lambda : number_input(2) )
bttn2.grid(row= 3, column= 1)
bttn1 = Button(main_window, text= "1", padx= 40, pady= 20, command= lambda : number_input(1) )
bttn1.grid(row= 3, column= 2)

bttn0 = Button(main_window, text= "0", padx= 40, pady= 20, command= lambda : number_input(0) )
bttn0.grid(row= 4, column= 0)

bttn_add = Button(main_window, text= "+", padx= 40, pady= 20, command= sum_of_values)
bttn_add.grid(row= 4, column= 1)
bttn_clear = Button(main_window, text= "clr", padx= 40, pady= 20, command= clear_value)
bttn_clear.grid(row= 5, column= 1)
bttn_equals = Button(main_window, text= "=", padx= 40, pady= 20, command= equals)
bttn_equals.grid(row= 5, column= 2)

main_window.mainloop()

