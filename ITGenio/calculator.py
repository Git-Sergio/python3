#$ python3 calculator.py


from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Calculator")

#logik calculator
def calc(key):
    global memory
    if key == "=":
#Виключаємо написання букв
        str1 = "-+*/.0123456789"
        if calc_entry.get() [0] not in str1:
            calc_entry.insert(END, "Перший символ не число!")
            messagebox.showerror("Ошибка!", "Ви ввели не число!")
#Рахунок
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Ошибка!")
            messagebox.showerror("Ошибка!", "Перевір правильність данних")
#Очистити поле
    elif key == "C":
        calc_entry.delete(0, END)
#Змінна +-
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)

#button
bttn_list = [
    "C", "^", "%", "/",
    "7", "8", "9", "*",
    "4", "5", "6", "-",
    "1", "2", "3", "+",
    "0", ".", "-/+", "="
]
#     "7", "8", "9", "+", "-",
#     "4", "5", "6", "*", "/",
#     "1", "2", "3", "-/+", "=",
#     "0", ".", "C", "", ""
r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd).grid(row=r, column=c)
    c += 1
    if c>3:
        c=0
        r += 1

calc_entry = Entry(root, width=33)
calc_entry.grid(row=0, column=0, columnspan=5)

root.mainloop()
