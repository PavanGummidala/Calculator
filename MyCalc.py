from tkinter import *

expression = ""

#to store all the values given in the entry
def press(num):
    # to save the data and access it globally
    global expression
    #Storing the value given from the entry box in expression and concatenates with the previous value
    expression = expression + str(num)
    #the value will be updated everytime the concatination and updates in storevar
    storevar.set(expression)

def clear():
    # To clear the data from Entry box
    global expression
    expression=""
    storevar.set("")

def equal():
    try:
        #Taken the total expression store in expression
        global expression
        #Evaluating the expression and performing the mathimatical operation using eval and storing it in total
        total=str(eval(expression))
        #Assinging the entry box value to total value
        storevar.set(total)
        #Erasing or setting to empty for the value stored in sxpression
        expression = ""
    except:
        #incase if any error occurs then we will display the error message
        expression.set("Error")
        expression=""


if __name__ == '__main__':
    screen = Tk()
    screen.configure(background='powder blue')
    screen.title("Calculator")
    screen.geometry("330x200")

# -----Intialising Entry, Buttons and placed in a positions using grid
    storevar = StringVar()
    exp = Entry(screen,relief=GROOVE,bd=15,text=storevar).grid(columnspan=4,ipadx=65)
    storevar.set('Enter')

    button1 = Button(screen, text=' 1 ', fg='black', bg='white', height=1, width=7, command = lambda: press(1)).grid(row=2, column=0)
    button2 = Button(screen, text=' 2 ', fg='black', bg='white', height=1, width=7, command = lambda: press(2)).grid(row=2, column=1)
    button3 = Button(screen, text=' 3 ', fg='black', bg='white', height=1, width=7, command = lambda: press(3)).grid(row=2, column=2)
    badd    = Button(screen, text=' + ', fg='black', bg='white', height=1, width=7, command = lambda: press("+")).grid(row=2, column=3)
    button4 = Button(screen, text=' 4 ', fg='black', bg='white', height=1, width=7, command = lambda: press(4)).grid(row=3, column=0)
    button5 = Button(screen, text=' 5 ', fg='black', bg='white', height=1, width=7, command = lambda: press(5)).grid(row=3, column=1)
    button6 = Button(screen, text=' 6 ', fg='black', bg='white', height=1, width=7, command = lambda: press(6)).grid(row=3, column=2)
    bsubt   = Button(screen, text=' - ', fg='black', bg='white', height=1, width=7, command = lambda: press("-")).grid(row=3, column=3)
    button7 = Button(screen, text=' 7 ', fg='black', bg='white', height=1, width=7, command = lambda: press(7)).grid(row=4, column=0)
    button8 = Button(screen, text=' 8 ', fg='black', bg='white', height=1, width=7, command = lambda: press(8)).grid(row=4, column=1)
    button9 = Button(screen, text=' 9 ', fg='black', bg='white', height=1, width=7, command = lambda: press(9)).grid(row=4, column=2)
    bmulti  = Button(screen, text=' * ', fg='black', bg='white', height=1, width=7, command = lambda: press("*")).grid(row=4, column=3)
    button0 = Button(screen, text=' 0 ', fg='black', bg='white', height=1, width=7, command = lambda: press(0)).grid(row=5, column=0)
    bclear  = Button(screen, text=' clear ', fg='black', bg='white', height=1, width=7, command = clear).grid(row=5, column=1)
    bequal  = Button(screen, text=' = ', fg='black', bg='white', height=1, width=7, command = equal).grid(row=5, column=2)
    bdiv    = Button(screen, text=' / ', fg='black', bg='white', height=1, width=7, command = lambda: press("/")).grid(row=5, column=3)

    #To intialize the window/frame
    screen.mainloop()