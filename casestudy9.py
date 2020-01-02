from tkinter import *

entry_box = ""

def press(x):
    global entry_box
    entry_box = entry_box + str(x)
    operation.set(entry_box)

def equals():
    try:
        global entry_box
        answer = str(eval(entry_box))
        operation.set(answer)
        entry_box = ""
    except:
        operation.set("Uh-oh Something went wrong :(")
        entry_box = ""

def clear():
    global entry_box
    entry_box = ""
    operation.set("")

if __name__ == "__main__":
        
    window = Tk()

    window.title("Calculinator")
    window.geometry("350x250")
    operation = StringVar()
    operation_field = Entry(window, textvariable=operation)
    operation_field.grid(columnspan=4, ipadx=70)
    operation.set("3+3=6")
    button1 = Button(window, text=' 1 ', fg='black', bg='grey', command=lambda: press(1), height=2, width=4)
    button1.grid(row=2, column=0)

    button2 = Button(window, text=' 2 ', fg='black', bg='grey', command=lambda: press(2), height=2, width=4)
    button2.grid(row=2, column=1)

    button3 = Button(window, text=' 3 ', fg='black', bg='grey', command=lambda: press(3), height=2, width=4)
    button3.grid(row=2, column=2)

    button4 = Button(window, text=' 4 ', fg='black', bg='grey', command=lambda: press(4), height=2, width=4)
    button4.grid(row=3, column=0)

    button5 = Button(window, text=' 5 ', fg='black', bg='grey', command=lambda: press(5), height=2, width=4)
    button5.grid(row=3, column=1)

    button6 = Button(window, text=' 6 ', fg='black', bg='grey', command=lambda: press(6), height=2, width=4)
    button6.grid(row=3, column=2)

    button7 = Button(window, text=' 7 ', fg='black', bg='grey', command=lambda: press(7), height=2, width=4)
    button7.grid(row=4, column=0)

    button8 = Button(window, text=' 8 ', fg='black', bg='grey', command=lambda: press(8), height=2, width=4)
    button8.grid(row=4, column=1)

    button9 = Button(window, text=' 9 ', fg='black', bg='grey', command=lambda: press(9), height=2, width=4)
    button9.grid(row=4, column=2)

    button0 = Button(window, text=' 0 ', fg='black', bg='grey', command=lambda: press(0), height=2, width=4)
    button0.grid(row=5, column=1)

    plus = Button(window, text=' + ', fg='black', bg='orange', command=lambda: press("+"), height=2, width=4)
    plus.grid(row=2, column=3)

    minus = Button(window, text=' - ', fg='black', bg='orange', command=lambda: press("-"), height=2, width=4)
    minus.grid(row=3, column=3)

    multiply = Button(window, text=' * ', fg='black', bg='orange', command=lambda: press("*"), height=2, width=4)
    multiply.grid(row=4, column=3)

    divide = Button(window, text=' / ', fg='black', bg='orange', command=lambda: press("/"), height=2, width=4)
    divide.grid(row=5, column=3)

    equal = Button(window, text=' = ', fg='black', bg='orange', command=equals, height=2, width=4)
    equal.grid(row=6, column=3)

    clear = Button(window, text='Clear', fg='black', bg='orange', command=clear, height=2, width=4)
    clear.grid(row=5, column=2)
    
    window.mainloop()
