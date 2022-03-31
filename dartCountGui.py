#Package importing
import tkinter as tk

#global variables
inputs=["0", "1"]
score=[]
total = 0

#Functions
def backspace():
    inputs[0] = "0"
    inputs[1] = "1"
    printInput()

def inputNum(number):
    if int(inputs[0]) == 0:+
        inputs[0] = str(number)
    elif int(inputs[0]) < 10 and int(inputs[0] + str(number)) < 21:
        inputs[0] = inputs[0] + str(number)
    printInput()

def enter():
    listOfGlobals = globals()
    #total score
    num = int(listOfGlobals['inputs'][0])
    multi = int(listOfGlobals['inputs'][1])
    
    if num == 50 or num == 25:
        multi = 1
        
    listOfGlobals['total'] += num * multi

    #score board
    scoreString = ""
    if num == 25:
        scoreString= "BULL"
    elif num == 50:
        scoreString="BULLSEYE"
    elif multi == 1:
        scoreString = "S" + listOfGlobals['inputs'][0]
    elif multi == 2:
        scoreString = "D" + listOfGlobals['inputs'][0]
    elif multi == 3:
        scoreString = "T" + listOfGlobals['inputs'][0]

    print(scoreString)
    score.append(scoreString)
    printScore()
    printTotal()
    listOfGlobals['inputs'] = ["0", "1"]
    
def multiplier(factor):
    inputs[1] = str(factor)
    printInput()

def printScore():
    string = "Score:\n"
    for sc in score:
        string = string + sc
        string = string + "\n"
    lbl_score["text"] = string

def printInput():
    string = "Current input: "
    ring = ""
    if inputs[1] == "1":
        ring = "single"
    elif inputs[1] == "2":
        ring = "double"
    elif inputs[1] == "3":
        ring = "triple"
    string = string + inputs[0] + " ring: " + ring
    lbl_input["text"] = string

def printTotal():
    lbl_total["text"] = "Total: " + str(total)
    
#GUI initialization
window = tk.Tk()
window.title("Dart counter")

window.rowconfigure(4, minsize=500, weight=1)
window.columnconfigure(0, minsize=500, weight=1)

#row 0
frm_mult = tk.Frame(window)
frm_mult.grid(sticky="ew", row=0, column=0, padx=10, pady=10)

btn_single = tk.Button(frm_mult, text="Single", command=lambda: multiplier(1))
btn_single.grid(row=0, column=0)

btn_double = tk.Button(frm_mult, text="Double", command=lambda:multiplier(2))
btn_double.grid(row=0, column=1)

btn_triple = tk.Button(frm_mult, text="Triple", command=lambda: multiplier(3))
btn_triple.grid(row=0, column=2)

#row 1
frm_num = tk.Frame(window)
frm_num.grid(sticky="ew", row=1, column=0, padx=10, pady=10)

btn_1 = tk.Button(frm_num, text="1", command=lambda: inputNum(1))
btn_2 = tk.Button(frm_num, text="2", command=lambda: inputNum(2))
btn_3 = tk.Button(frm_num, text="3", command=lambda: inputNum(3))
btn_4 = tk.Button(frm_num, text="4", command=lambda: inputNum(4))
btn_5 = tk.Button(frm_num, text="5", command=lambda: inputNum(5))
btn_6 = tk.Button(frm_num, text="6", command=lambda: inputNum(6))
btn_7 = tk.Button(frm_num, text="7", command=lambda: inputNum(7))
btn_8 = tk.Button(frm_num, text="8", command=lambda: inputNum(8))
btn_9 = tk.Button(frm_num, text="9", command=lambda: inputNum(9))
btn_0 = tk.Button(frm_num, text="0", command=lambda: inputNum(0))

btn_1.grid(row=0, column=0)
btn_2.grid(row=0, column=1)
btn_3.grid(row=0, column=2)
btn_4.grid(row=1, column=0)
btn_5.grid(row=1, column=1)
btn_6.grid(row=1, column=2)
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_0.grid(row=3, column=1)

#row 2
frm_spec = tk.Frame(window)
frm_spec.grid(sticky="ew", row=2, column=0, padx=10, pady=10)

btn_bull = tk.Button(frm_spec, text="Bull", command=lambda: inputNum(25))
btn_bullseye = tk.Button(frm_spec, text="Bullseye", command=lambda:inputNum(50))
btn_enter = tk.Button(frm_spec, text="Enter", command= lambda:enter())
btn_back = tk.Button(frm_spec, text="Backspace", command=backspace)

btn_bull.grid(row=0, column=1)
btn_bullseye.grid(row=0, column=2)
btn_enter.grid(row=0, column=3)
btn_back.grid(row=0, column=4)

#row3
frm_lbl = tk.Frame(window)
frm_lbl.grid(sticky="ew", row=3, column=0, padx=10, pady=10)

lbl_input = tk.Label(frm_lbl, text="Current Input: ")
lbl_score = tk.Label(frm_lbl, text="Score: ")
lbl_total = tk.Label(frm_lbl, text="Total: ")

lbl_input.grid(row=0, column=0)
lbl_score.grid(row=1, column=0)
lbl_total.grid(row=2, column=0)

window.mainloop()
