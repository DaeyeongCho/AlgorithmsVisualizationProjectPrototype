import tkinter, random
from tkinter import *
from tkinter import messagebox, ttk
from time import sleep

from define import *

def startSimulation(window, canvas, sortOrSearchAlgorithm, algorithm, dataSize, speedLimit, shuffleTime, searchValue, labelState, labelElapsedTime):
    running = True
    timer = 0
    data = list(range(1, dataSize + 1))
    for i in range(dataSize):
        canvas.create_rectangle(0, 0, CANVAS_WIDTH / dataSize, CANVAS_HEIGHT * (i + 1) / dataSize, fill="white")
    
    stickRelocation(canvas, data, dataSize)

    # window.update()

    # time.sleep(1)

    # canvas.itemconfig(data[1], fill="blue")
    # canvas.itemconfig(data[3], fill="blue")

    # window.update()

    # time.sleep(1)

    # data[1], data[3] = data[3], data[1]

    # stickRelocation(canvas, data, dataSize)

    # window.update()

    # time.sleep(1)

    # canvas.itemconfig(data[1], fill="white")
    # canvas.itemconfig(data[3], fill="white")

    if sortOrSearchAlgorithm == 0:
        labelState.configure(text=LABEL_STATE[2])
        shuffleStick(window, canvas, data, dataSize, shuffleTime)

    else:
        labelState.configure(text=LABEL_STATE[4])
        startTimer(window, running, timer, labelElapsedTime)


# simulation 프레임 타이머 함수
def startTimer(window, running, timer, labelElapsedTime):
    if running:
        timer += 1
        labelElapsedTime.configure(text=str(timer // 1000) + ":" + str(timer % 1000).zfill(3))

    window.after(1, lambda: startTimer(window, running, timer, labelElapsedTime))

# canvas의 막대 그래프 순서에 따라 재배치
def stickRelocation(canvas, data, dataSize):
    for i in data:
        canvas.moveto(i,  CANVAS_WIDTH * data.index(i) / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * i / dataSize + 1)
    pass
    # for i in range(dataSize):
    #     canvas.moveto(data[i][1], CANVAS_WIDTH * data[i][0] / dataSize - CANVAS_WIDTH / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * (i + 1) / dataSize + 1)

# 막대 섞기 함수
def shuffleStick(window, canvas, data, dataSize, shuffleTime):
    drawTwoStick = []

    for i in range(shuffleTime):
        drawTwoStick = random.sample(data, 2)
        drawTwoStick[0] -= 1
        drawTwoStick[1] -= 1
        canvas.itemconfig(data[drawTwoStick[0]], fill="red")
        canvas.itemconfig(data[drawTwoStick[1]], fill="red")
        window.update()
        data[drawTwoStick[0]], data[drawTwoStick[1]] = data[drawTwoStick[1]], data[drawTwoStick[0]]
        stickRelocation(canvas, data, dataSize)
        window.update()
        canvas.itemconfig(data[drawTwoStick[0]], fill="white")
        canvas.itemconfig(data[drawTwoStick[1]], fill="white")

    print(data)