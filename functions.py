import time
from tkinter import *
import random

from define import *

## 라디오 버튼 프레임 함수들 ##

#라디오 버튼
def radioButtonFunc(var, comboboxSelectAlgorithm, frameGeneralInput, labelShuffleTimes, spinboxShuffleTimes):
    if var.get() == 1:
        comboboxSelectAlgorithm.configure(values=SORT_ALGORITHMS)
        comboboxSelectAlgorithm.set(SORT_ALGORITHMS[0])
        frameGeneralInput.pack()
        labelShuffleTimes.pack(side=LEFT, padx=5, pady=5)
        spinboxShuffleTimes.pack(side=LEFT, padx=5, pady=5)
    elif var.get() == 2:
        comboboxSelectAlgorithm.configure(values=SEARCH_ALGORITHMS)
        comboboxSelectAlgorithm.set(SEARCH_ALGORITHMS[0])
        frameGeneralInput.pack()
        labelShuffleTimes.pack_forget()
        spinboxShuffleTimes.pack_forget()


## 일반 입력 프레임 함수들 ##
def checkbuttonAdvanced(var, frameAdvancedInput):
    if var.get() == True:
        frameAdvancedInput.pack()
    else:
        frameAdvancedInput.pack_forget()
        

def buttonStartFunc(window, frameStarts, canvas, intVarRadioButton, comboboxSelectAlgorithm, spinboxDataSize, spinboxSpeedLimit, spinboxShuffleTimes):
    frameStarts.pack()
    print(intVarRadioButton.get(), comboboxSelectAlgorithm.get(), spinboxDataSize.get(), spinboxSpeedLimit.get(), spinboxShuffleTimes.get())

    datas = list(range(int(spinboxDataSize.get())))

    

    sticks = [None] * int(spinboxDataSize.get())
    sticksWidth = int(CANVAS_WIDTH / len(sticks))


    for i in range(len(sticks)):
        sticks[i] = canvas.create_rectangle((CANVAS_WIDTH / len(sticks) * i), CANVAS_HEIGHT - (CANVAS_HEIGHT / (len(sticks) + 1) * (i + 1)), CANVAS_WIDTH / len(sticks) * i + sticksWidth, CANVAS_HEIGHT, fill="white")


    shape = canvas.create_rectangle(10, 10, 100, 100, fill="yellow")
    canvas.itemconfig(shape, fill="red")

    for i in range(50):
        canvas.move(shape, 5, 0)
        window.update()
        time.sleep(0.1)

## 고급 입력 프레임 함수들 ##