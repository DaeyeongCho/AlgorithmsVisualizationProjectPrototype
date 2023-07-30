import tkinter
from tkinter import *
from tkinter import messagebox, ttk

from define import *
from functions import *

def main():
## ====================== 정의 ====================== ##

    # 윈도우 창 정의
    window = Tk()
    window.title(TITLE)
    window.geometry(GEOMETRY)
    window.resizable(width=FALSE, height=FALSE)

    # 입력 타입 정의
    intVarRadioButtonSelectAlgorithm = IntVar()
    strVarComboboxSelectAlgorithm = StringVar()
    boolVarCheckbuttonAdvancedMenu = BooleanVar()

    intVarSpinboxDataSize = IntVar()
    intVarSpinboxDataSize.set(DATA_SIZE_DEFAULT)
    doubleVarSpeedLimit = DoubleVar()
    doubleVarSpeedLimit.set(SPEED_LIMIT_DEFAULT)
    intVarShuffleTimes = IntVar()
    intVarShuffleTimes.set(SHUFFLE_TIMES_DEFAULT)
    intVarSearchValue = IntVar()
    intVarSearchValue.set(SEARCH_VALUE_DEFAULT)

    # 프레임 정의
    frameGeneralMenu = tkinter.Frame(window)
    frameAdvancedMenu = tkinter.Frame(window)
    frameSimulation = tkinter.Frame(window)

    frameSimulationHint = tkinter.Frame(frameSimulation)
    frameSimulationState = tkinter.Frame(frameSimulation)
    frameSimulationElapsedTime = tkinter.Frame(frameSimulation)
    frameSimulationEndButtons = tkinter.Frame(frameSimulation)

    # General Menu 프레임 하위 위젯 정의
    radioButtonSelectAlgorithm = [ Radiobutton(frameGeneralMenu, text=RADIO_BUTTON_SELECT_ALGORITHM[0], variable=intVarRadioButtonSelectAlgorithm, value=0, command=lambda: radioButtonSelectAlgorithmFunc(intVarRadioButtonSelectAlgorithm)),
                                   Radiobutton(frameGeneralMenu, text=RADIO_BUTTON_SELECT_ALGORITHM[1], variable=intVarRadioButtonSelectAlgorithm, value=1, command=lambda: radioButtonSelectAlgorithmFunc(intVarRadioButtonSelectAlgorithm)) ]
    
    comboboxSelectAlgorithm = ttk.Combobox(frameGeneralMenu, textvariable=strVarComboboxSelectAlgorithm, values=SORT_ALGORITHMS, state="readonly")
    comboboxSelectAlgorithm.set(SORT_ALGORITHMS[0])

    checkbuttonAdvancedMenu = ttk.Checkbutton(frameGeneralMenu, text=ADVANCED_MENU, variable=boolVarCheckbuttonAdvancedMenu, command=lambda: checkbuttonAdvancedMenuFunc(boolVarCheckbuttonAdvancedMenu))

    buttonStart = Button(frameGeneralMenu, text=START, command=lambda: bottonStartFunc())
    
    # Advanced Menu 프레임 하위 위젯 정의
    labelDataSize = Label(frameAdvancedMenu, text=DATA_SIZE)
    spinboxDataSize = Spinbox(frameAdvancedMenu, from_=DATA_SIZE_MIN, to=DATA_SIZE_MAX, increment=DATA_SIZE_INCREMENT, textvariable=intVarSpinboxDataSize, width=SPIN_BOX_WIDTH, command=lambda: spinboxDataSizeFunc())

    labelSpeedLimit = Label(frameAdvancedMenu, text=SPEED_LIMIT)
    spinboxSpeedLimit = Spinbox(frameAdvancedMenu, from_=SPEED_LIMIT_MIN, to=SPEED_LIMIT_MAX, increment=SPEED_LIMIT_INCREMENT, textvariable=doubleVarSpeedLimit, width=SPIN_BOX_WIDTH)

    labelShuffleTimes = Label(frameAdvancedMenu, text=SHUFFLE_TIMES)
    spinboxShuffleTimes = Spinbox(frameAdvancedMenu, from_=SHUFFLE_TIMES_MIN, to=SHUFFLE_TIMES_MAX, increment=SHUFFLE_TIMES_INCREMENT, textvariable=intVarShuffleTimes, width=SPIN_BOX_WIDTH)

    labelSearchValue = Label(frameAdvancedMenu, text=SEARCH_VALUE)
    spinboxSearchValue = Spinbox(frameAdvancedMenu, from_=SEARCH_VALUE_MIN, to=int(intVarSpinboxDataSize.get()), increment=SEARCH_VALUE_INCREMENT, textvariable=intVarSearchValue, width=SPIN_BOX_WIDTH)

    # Simulation 프레임 하위 위젯 정의
    canvas = Canvas(frameSimulation, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, background=CANVAS_COLOR)

    labelHint = [ Label(frameSimulationHint, text=LABEL_HINT[0], foreground=LABEL_HINT_COLOR[0]),
                  Label(frameSimulationHint, text=LABEL_HINT[1], foreground=LABEL_HINT_COLOR[1]),
                  Label(frameSimulationHint, text=LABEL_HINT[2], foreground=LABEL_HINT_COLOR[2])]
    
    labelState = [ Label(frameSimulationState, text=LABEL_STATE[0]),
                   Label(frameSimulationState, text=LABEL_STATE[1]) ]

    labelElapsedTime = [ Label(frameSimulationElapsedTime, text=ELAPSED_TIME[0]),
                         Label(frameSimulationElapsedTime, text=ELAPSED_TIME[1]) ]
    
    buttonEnd = [ Button(frameSimulationEndButtons, text=END_BUTTONS[0], command=lambda: buttonStopFunc()),
                  Button(frameSimulationEndButtons, text=END_BUTTONS[1], command=lambda: buttonReplayFunc()),
                  Button(frameSimulationEndButtons, text=END_BUTTONS[2], command=lambda: buttonEndFunc()),]



## ====================== 프로그램 ====================== ##

    # General Menu 프로그램
    def radioButtonSelectAlgorithmFunc(intVar):
        if intVar.get() == 0:
            comboboxSelectAlgorithm.configure(values=SORT_ALGORITHMS)
            comboboxSelectAlgorithm.set(SORT_ALGORITHMS[0])
            labelShuffleTimes.pack(side=LEFT, padx=(10, 0))
            spinboxShuffleTimes.pack(side=LEFT, padx=(2, 0))
            labelSearchValue.pack_forget()
            spinboxSearchValue.pack_forget()
        else:
            comboboxSelectAlgorithm.configure(values=SEARCH_ALGORITHMS)
            comboboxSelectAlgorithm.set(SEARCH_ALGORITHMS[0])
            labelShuffleTimes.pack_forget()
            spinboxShuffleTimes.pack_forget()
            labelSearchValue.pack(side=LEFT, padx=(10, 0))
            spinboxSearchValue.pack(side=LEFT, padx=(2, 0))

    def checkbuttonAdvancedMenuFunc(boolVar):
        if not boolVar.get():
            frameAdvancedMenu.pack_forget()
        else:
            frameAdvancedMenu.pack(side=TOP)

    def bottonStartFunc():
        frameSimulation.pack(side=BOTTOM, pady=(0, 10))
        sortOrSearchAlgorithm = intVarRadioButtonSelectAlgorithm.get()
        algorithm = strVarComboboxSelectAlgorithm.get()
        dataSize = intVarSpinboxDataSize.get()
        speedLimit = doubleVarSpeedLimit.get()
        shuffleTime = intVarShuffleTimes.get()
        searchValue = intVarSearchValue.get()

        radioButtonSelectAlgorithm[0].config(state="disabled")
        radioButtonSelectAlgorithm[1].config(state="disabled")
        comboboxSelectAlgorithm.config(state="disabled")
        checkbuttonAdvancedMenu.config(state="disabled")
        buttonStart.config(state="disabled")
        spinboxDataSize.config(state="disabled")
        spinboxSpeedLimit.config(state="disabled")
        spinboxShuffleTimes.config(state="disabled")
        spinboxSearchValue.config(state="disabled")

        startSimulation(window, canvas, sortOrSearchAlgorithm, algorithm, dataSize, speedLimit, shuffleTime, searchValue, labelState[1], labelElapsedTime[1])

    # Advanced Menu 프로그램
    def spinboxDataSizeFunc() :
        spinboxSearchValue.config(to=int(intVarSpinboxDataSize.get()))

    # Simulation 프로그램
    def buttonStopFunc():
        pass

    def buttonReplayFunc():
        pass

    def buttonEndFunc():
        pass


## ====================== 배치 ====================== ##

    # 프레임 패킹
    frameGeneralMenu.pack(side=TOP)
    frameAdvancedMenu.pack_forget()
    frameSimulation.pack_forget()

    # General Menu 패킹
    radioButtonSelectAlgorithm[0].pack(side=LEFT)
    radioButtonSelectAlgorithm[1].pack(side=LEFT)
    comboboxSelectAlgorithm.pack(side=LEFT, padx=(10, 0))
    checkbuttonAdvancedMenu.pack(side=LEFT, padx=(10, 0))
    buttonStart.pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)

    # Advanced Menu 패킹
    labelDataSize.pack(side=LEFT)
    spinboxDataSize.pack(side=LEFT, padx=(2, 0))
    labelSpeedLimit.pack(side=LEFT, padx=(10, 0))
    spinboxSpeedLimit.pack(side=LEFT, padx=(2, 0))
    labelShuffleTimes.pack(side=LEFT, padx=(10, 0))
    spinboxShuffleTimes.pack(side=LEFT, padx=(2, 0))
    labelSearchValue.pack_forget()
    spinboxSearchValue.pack_forget()

    # Simulation 패킹
    canvas.pack()

    frameSimulationHint.pack(side=TOP)
    frameSimulationState.pack(side=TOP)
    frameSimulationElapsedTime.pack(side=TOP)
    frameSimulationEndButtons.pack(side=TOP)

    labelHint[0].pack(side=LEFT)
    labelHint[1].pack(side=LEFT)
    labelHint[2].pack(side=LEFT)

    labelState[0].pack(side=LEFT)
    labelState[1].pack(side=LEFT)

    labelElapsedTime[0].pack(side=LEFT)
    labelElapsedTime[1].pack(side=LEFT)

    buttonEnd[0].pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)
    buttonEnd[1].pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)
    buttonEnd[2].pack(side=LEFT, padx=5, pady=5, ipadx=15, ipady=3)


    window.mainloop()

if __name__=="__main__":
    main()