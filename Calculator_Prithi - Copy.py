from hwx import gui
import math

state = {"input":""}

Lineedit = gui.LineEdit(placeHolderText='')
Lineedit.set("")
    
def ToPerformCalculation():
    Variable = Lineedit.get()
    Variable = eval(Variable)
    Lineedit.set(Variable)
    state["input"] = ""
    
def OnClick(PushButtonValue):
    if state["input"] != "":
        state["input"] += str(PushButtonValue)
    else:
        state["input"] = Lineedit.get() + str(PushButtonValue)
    
    Lineedit.set(state["input"])
    
def GetValue():   
    Input = Lineedit.get()
    if "." in Input:
        return float(Input)
    return int(Input)
   

def OnebyX():    
    Value = GetValue()
    state["value"] = 1/Value
    Lineedit.set(state["value"])

def SquareRoot():
    Value = GetValue()
    state["value"] = math.sqrt(Value)
    Lineedit.set(state["value"])
   
def SquaretheValue():
    Value = GetValue()
    state["value"] = Value*Value
    Lineedit.set(state["value"])
    
def ClearAll():
    Lineedit.set("")
    
def Cancelslot():
    Value = Lineedit.get()
    Value = Value[:-1]
    Lineedit.set(Value)
    
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
        gui.Button('.',command=lambda e: OnClick('.')),
    ),
)

layout4 = gui.VBoxLayout(
    border=5,
    spacing=3,
    children=(
        gui.Button('/', command=lambda e: OnClick('/')),
        gui.Button('X',command=lambda e: OnClick('*')),
        gui.Button('-', command=lambda e: OnClick('-')),
        gui.Button('+', command=lambda e: OnClick('+')),
        gui.Button('=', command=ToPerformCalculation),
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
