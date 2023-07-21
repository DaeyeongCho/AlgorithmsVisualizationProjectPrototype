from tkinter import *

from define import *

## 라디오 버튼 프레임 함수들 ##

#라디오 버튼
def radioButtonFunc(var, comboboxSelectAlgorithm, frameGeneralInput, labelShuffleTimes, spinboxShuffleTimes):
    if var.get() == 1:
        comboboxSelectAlgorithm.configure(values=SORT_ALGORITHMS)
        comboboxSelectAlgorithm.set(SELECT_ALGORITHM[0])
        frameGeneralInput.pack()
        labelShuffleTimes.pack(side=LEFT, padx=5, pady=5)
        spinboxShuffleTimes.pack(side=LEFT, padx=5, pady=5)
    elif var.get() == 2:
        comboboxSelectAlgorithm.configure(values=SEARCH_ALGORITHMS)
        comboboxSelectAlgorithm.set(SELECT_ALGORITHM[1])
        frameGeneralInput.pack()
        labelShuffleTimes.pack_forget()
        spinboxShuffleTimes.pack_forget()


## 일반 입력 프레임 함수들 ##
def checkbuttonAdvanced(var, frameAdvancedInput):
    if var.get() == True:
        frameAdvancedInput.pack()
    else:
        frameAdvancedInput.pack_forget()
        

def buttonStartFunc():
    pass



## 고급 입력 프레임 함수들 ##