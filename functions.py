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

    if sortOrSearchAlgorithm == 0:
        labelState.configure(text=LABEL_STATE[2])
        shuffleStick(window, canvas, data, dataSize, shuffleTime)
        window.update()
        labelState.configure(text=LABEL_STATE[3])

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
        canvas.moveto(data[drawTwoStick[0]], CANVAS_WIDTH * drawTwoStick[0] / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * data[drawTwoStick[0]] / dataSize + 1)
        canvas.moveto(data[drawTwoStick[1]], CANVAS_WIDTH * drawTwoStick[1] / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * data[drawTwoStick[1]] / dataSize + 1)
        window.update()
        canvas.itemconfig(data[drawTwoStick[0]], fill="white")
        canvas.itemconfig(data[drawTwoStick[1]], fill="white")
        