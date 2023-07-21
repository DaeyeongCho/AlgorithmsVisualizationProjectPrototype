import tkinter
from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

from define import *
from functions import *



def main():
    #윈도우 창 정의
    window = Tk()
    window.title(TITLE)
    window.geometry(GEOMETRY)
    window.resizable(width=FALSE, height=FALSE)


    #입력 타입 정의
    intVarRadioButton = IntVar()

    strVarComboboxSelectAlgorithm = StringVar()
    boolVarCheckButtonAdvanced = BooleanVar()

    intVarSpinboxDataSize = IntVar()
    intVarSpinboxDataSize.set(100)
    intVarSpinboxShuffleTimes = IntVar()
    intVarSpinboxShuffleTimes.set(10000)
    intVarSpeedLimit = IntVar()
    intVarSpeedLimit.set(0)


    #프레임 정의
    frameRadiobutton = tkinter.Frame(window)
    frameGeneralInput = tkinter.Frame(window)
    frameAdvancedInput = tkinter.Frame(window)


    #라디오 버튼 프레임 내부 정의
    radiobuttonList = [ Radiobutton(frameRadiobutton, text=RADIOBUTTON_TEXT[0], variable=intVarRadioButton, value=1, command=lambda: radioButtonFunc(intVarRadioButton, comboboxSelectAlgorithm, frameGeneralInput, labelShuffleTimes, spinboxShuffleTimes)), 
                        Radiobutton(frameRadiobutton, text=RADIOBUTTON_TEXT[1], variable=intVarRadioButton, value=2, command=lambda: radioButtonFunc(intVarRadioButton, comboboxSelectAlgorithm, frameGeneralInput, labelShuffleTimes, spinboxShuffleTimes))]


    #일반 입력 프레임 내부 정의
    comboboxSelectAlgorithm = ttk.Combobox(frameGeneralInput, textvariable=strVarComboboxSelectAlgorithm, values=[], state="readonly")

    checkbuttonAdvancedInput = ttk.Checkbutton(frameGeneralInput, text=ADVANCED, variable=boolVarCheckButtonAdvanced, command=lambda: checkbuttonAdvanced(boolVarCheckButtonAdvanced, frameAdvancedInput))
    
    buttonStart = Button(frameGeneralInput, text=START, command=lambda: buttonStartFunc())


    #고급 입력 프레임 내부 정의
    labelDataSize = Label(frameAdvancedInput, text=DATASIZE)
    spinboxDataSize = Spinbox(frameAdvancedInput, from_=DATASIZE_MIN, to=DATASIZE_MAX, increment=10, textvariable=intVarSpinboxDataSize)

    labelSpeedLimit = Label(frameAdvancedInput, text=SPEED_LIMIT)
    spinboxSpeedLimit = Spinbox(frameAdvancedInput, from_=SPEED_LIMIT_MIN, to=SPEED_LIMIT_MAX, increment=1, textvariable=intVarSpeedLimit)

    labelShuffleTimes = Label(frameAdvancedInput, text=SHUFFLETIMES)
    spinboxShuffleTimes = Spinbox(frameAdvancedInput, from_=SUFFLE_MIN, to=SUFFLE_MAX, increment=100, textvariable=intVarSpinboxShuffleTimes)



    #프레임 배치
    frameRadiobutton.pack()
    frameGeneralInput.pack_forget()
    frameAdvancedInput.pack_forget()


    #라디오버튼 프레임 내부 배치
    for radiobuttons in radiobuttonList:
        radiobuttons.pack(side=LEFT, padx=30, pady=5)


    #일반 입력 프레임 내부 배치
    comboboxSelectAlgorithm.pack(side=LEFT, padx=5, pady=5)

    checkbuttonAdvancedInput.pack(side=LEFT, padx=10, pady=5)
    
    buttonStart.pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)


    #고급 입력 프레임 내부 배치
    labelDataSize.pack(side=LEFT, padx=5, pady=5)
    spinboxDataSize.pack(side=LEFT, padx=5, pady=5)

    labelSpeedLimit.pack(side=LEFT, padx=5, pady=5)
    spinboxSpeedLimit.pack(side=LEFT, padx=5, pady=5)

    labelShuffleTimes.pack(side=LEFT, padx=5, pady=5)
    spinboxShuffleTimes.pack(side=LEFT, padx=5, pady=5)



    window.mainloop()


if __name__=="__main__":
    main()