from hwx import gui
import math

state = {"value" : 0,"test":0,"input":"","PreviousValue":""}

Lineedit = gui.LineEdit(placeHolderText='')
Lineedit.set("0")
    
def ToPerformCalculation(Flag, Variable):
    if Flag == 0:
        state["PreviousValue"] = Variable

    elif Flag == 1:  
        state["value"] = state["PreviousValue"] + Variable

    elif Flag == 2:  
        state["value"] = state["PreviousValue"] - Variable

    elif Flag == 3:  
        state["value"] = state["PreviousValue"] * Variable

    elif Flag == 4:  
        if Variable != 0:
            state["value"] = state["PreviousValue"] / Variable
               
		
def OnClick(PushButtonValue):
    Lineedit.set("0")
    Variable = PushButtonValue
    if state["input"] != "" :
        state["input"] += str(Variable)
    else:
        state["input"] = Variable
    Lineedit.set(state["input"])
    ToPerformCalculation(state["test"],(int)(state["input"]))
    
def GetValue():   
    Input = Lineedit.get()
    if "." in Input:
        return float(Input)
    return int(Input)
    
def SetValue():
    state["PreviousValue"] = GetValue()
    state["input"] = ""

             
def Add():
    SetValue()
    state["test"] = 1
    

def Subtract():
    SetValue()
    state["test"] = 2

def Multiply():
    SetValue()
    state["test"] = 3

def Divide():
    SetValue()
    state["test"] = 4

def OnebyX():    
    Value = GetValue()
    state["value"] = 1/Value

def SquareRoot():
    Value = GetValue()
    state["value"] = math.sqrt(Value)
   
def SquaretheValue():
    Value = GetValue()
    state["value"] = Value*Value
    
    
def ClearAll():
    state["value"] = 0
    state["test"] = 0
    state["PreviousValue"] = 0
    state["input"] = ""
    Lineedit.set("0")
    
def Cancelslot():
    Value = Lineedit.get()
    Value = Value[:-1]
    Lineedit.set(Value)


def Result():
    Lineedit.set(state["value"])
    
LineEditLayout = gui.VBoxLayout(
    children=(Lineedit,)
)

layout1 = gui.VBoxLayout(
    border=5,
    spacing=3,
    children=(
        gui.Button('1/x',command = OnebyX),
        gui.Button('7', command=lambda e: OnClick('7')),
        gui.Button('4', command=lambda e: OnClick('4')),
        gui.Button('1', command=lambda e: OnClick('1')),
        gui.Button('+/-'),
    ),
)

layout2 = gui.VBoxLayout(
    border=5,
    spacing=3,
    children=(
        gui.Button('Cancel',command = Cancelslot),
        gui.Button('XSquare',command =SquaretheValue),
        gui.Button('8', command=lambda e: OnClick('8')),
        gui.Button('5', command=lambda e: OnClick('5')),
        gui.Button('2', command=lambda e: OnClick('2')),
        gui.Button('0', command=lambda e: OnClick('0')),
    ),
)

layout3 = gui.VBoxLayout(
    border=5,
    spacing=3,
    children=(
        gui.Button('Clear',command = ClearAll),
        gui.Button('SquarerootX',command = SquareRoot),
        gui.Button('9', command=lambda e: OnClick('9')),
        gui.Button('6', command=lambda e: OnClick('6')),
        gui.Button('3', command=lambda e: OnClick('3')),
        gui.Button('.'),
    ),
)

layout4 = gui.VBoxLayout(
    border=5,
    spacing=3,
    children=(
        gui.Button('Divide', command=Divide),
        gui.Button('X', command=Multiply),
        gui.Button('-', command=Subtract),
        gui.Button('+', command=Add),
        gui.Button('=', command=Result),
    ),
)

layout = gui.GridLayout(
    children=(layout1, layout2, layout3, layout4)
)

dialog = gui.Dialog(
    name="Calculator",
    children=(LineEditLayout, layout),
)

show(dialog)
