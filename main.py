import tkinter
from tkinter import *
from tkinter import messagebox, ttk

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
    doubleVarSpeedLimit = DoubleVar()
    doubleVarSpeedLimit.set(0.000)
    intVarSpinboxShuffleTimes = IntVar()
    intVarSpinboxShuffleTimes.set(10000)


    #프레임 정의
    frameRadiobutton = tkinter.Frame(window)
    frameGeneralInput = tkinter.Frame(window)
    frameAdvancedInput = tkinter.Frame(window)
    frameStarts = tkinter.Frame(window)
    frameCanvas = tkinter.Frame(frameStarts)
    frameHint = tkinter.Frame(frameStarts)
    frameState = tkinter.Frame(frameStarts)
    frameElapsedTime = tkinter.Frame(frameStarts)
    frameEndButtons = tkinter.Frame(frameStarts)


    #라디오 버튼 프레임 내부 정의
    radiobuttonList = [ Radiobutton(frameRadiobutton, text=RADIOBUTTON_TEXT[0], variable=intVarRadioButton, value=1, command=lambda: radioButtonFunc(intVarRadioButton, comboboxSelectAlgorithm, frameGeneralInput, labelShuffleTimes, spinboxShuffleTimes)), 
                        Radiobutton(frameRadiobutton, text=RADIOBUTTON_TEXT[1], variable=intVarRadioButton, value=2, command=lambda: radioButtonFunc(intVarRadioButton, comboboxSelectAlgorithm, frameGeneralInput, labelShuffleTimes, spinboxShuffleTimes))]


    #일반 입력 프레임 내부 정의
    comboboxSelectAlgorithm = ttk.Combobox(frameGeneralInput, textvariable=strVarComboboxSelectAlgorithm, values=[], state="readonly")

    checkbuttonAdvancedInput = ttk.Checkbutton(frameGeneralInput, text=ADVANCED, variable=boolVarCheckButtonAdvanced, command=lambda: checkbuttonAdvanced(boolVarCheckButtonAdvanced, frameAdvancedInput))
    
    buttonStart = Button(frameGeneralInput, text=START, command=lambda: buttonStartFunc(window, frameStarts, canvas, intVarRadioButton, comboboxSelectAlgorithm, spinboxDataSize, spinboxSpeedLimit, spinboxShuffleTimes))


    #고급 입력 프레임 내부 정의
    labelDataSize = Label(frameAdvancedInput, text=DATASIZE)
    spinboxDataSize = Spinbox(frameAdvancedInput, from_=DATASIZE_MIN, to=DATASIZE_MAX, increment=10, textvariable=intVarSpinboxDataSize)

    labelSpeedLimit = Label(frameAdvancedInput, text=SPEED_LIMIT)
    spinboxSpeedLimit = Spinbox(frameAdvancedInput, from_=SPEED_LIMIT_MIN, to=SPEED_LIMIT_MAX, increment=0.001, textvariable=doubleVarSpeedLimit)

    labelShuffleTimes = Label(frameAdvancedInput, text=SHUFFLETIMES)
    spinboxShuffleTimes = Spinbox(frameAdvancedInput, from_=SUFFLE_MIN, to=SUFFLE_MAX, increment=100, textvariable=intVarSpinboxShuffleTimes)


    # 알고리즘 시작 프레임 내부 정의
    canvas = Canvas(frameCanvas, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background="white")




    #프레임 배치
    frameRadiobutton.pack(side=TOP)
    frameGeneralInput.pack_forget()
    frameAdvancedInput.pack_forget()
    frameStarts.pack_forget()
    frameCanvas.pack()
    frameHint.pack()
    frameState.pack()
    frameElapsedTime.pack()
    frameEndButtons.pack()


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


    #알고리즘 시작 프레임 내부 배치
    canvas.pack()



    window.mainloop()


if __name__=="__main__":
    main()