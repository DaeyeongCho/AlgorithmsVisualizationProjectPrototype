import tkinter, random, time
from tkinter import *
from tkinter import messagebox, ttk

from define import *

## 전역 변수 ##
running = False # simulation 프레임 타이머 작동 여부
timer = 0 # simulation 프레임 타이머 시간
started = False

# 시작 버튼 클릭 시 동작
def startSimulation(window, canvas, sortOrSearchAlgorithm, algorithm, dataSize, speedLimit, shuffleTime, searchValue, labelState, labelElapsedTime, buttonEnd):
    global running
    global timer
    global started

    data = []

    if not started:
        startTimer(window, labelElapsedTime)
        started = True

    for i in range(dataSize):
        data.append([i + 1, canvas.create_rectangle(0, 0, CANVAS_WIDTH / dataSize, CANVAS_HEIGHT * (i + 1) / dataSize, fill="white")])

    stickRelocation(canvas, data, dataSize)

    if sortOrSearchAlgorithm == 0:
        labelState.configure(text=LABEL_STATE[2])
        shuffleStick(window, canvas, data, dataSize, shuffleTime)
        labelState.configure(text=LABEL_STATE[5])
        window.update()
        time.sleep(1)
        window.update()
        labelState.configure(text=LABEL_STATE[3])
        running = True
        if algorithm == SORT_ALGORITHMS[0]:
            bubbleSort(window, canvas, data, dataSize, speedLimit)
        else:
            pass
        labelState.configure(text=LABEL_STATE[7])
    else:
        labelState.configure(text=LABEL_STATE[4])
        running = True
        if algorithm == SEARCH_ALGORITHMS[0]:
            linearSearch(window, canvas, data, dataSize, searchValue, speedLimit)
        else:
            pass

    running = False
    timer = 0

    buttonEnd[1].config(state="normal")
    buttonEnd[2].config(state="normal")


# simulation 프레임 타이머 함수
def startTimer(window, labelElapsedTime):
    global timer

    if running:
        timer += 1
        labelElapsedTime.configure(text=str(timer // 1000) + ":" + str(timer % 1000).zfill(3))

    window.after(1, lambda: startTimer(window, labelElapsedTime))


# canvas의 막대 그래프 순서에 따라 재배치
def stickRelocation(canvas, data, dataSize):
    for i in data:
        canvas.moveto(i[1], CANVAS_WIDTH * data.index(i) / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * i[0] / dataSize + 1)


# 정렬 알고리즘에서 막대 섞기 함수
def shuffleStick(window, canvas, data, dataSize, shuffleTime):
    drawTwoStick = []

    for i in range(shuffleTime):
        drawTwoStick = random.sample(data, 2)
        exchangePairStick(window, canvas, data, dataSize, drawTwoStick[0][0] - 1, drawTwoStick[1][0] - 1, 0, "red", "red")

# 두 막대 교환 함수
def exchangePairStick(window, canvas, data, dataSize, attentionStickIndex, compareStickIndex, speedLimit = 0, attentionStickColor = "red", compareStickColor = "blue"):
    canvas.itemconfig(data[attentionStickIndex][1], fill=attentionStickColor)
    canvas.itemconfig(data[compareStickIndex][1], fill=compareStickColor)
    window.update()
    if speedLimit != 0:
        time.sleep(speedLimit)
    data[attentionStickIndex], data[compareStickIndex] = data[compareStickIndex], data[attentionStickIndex]
    canvas.moveto(data[attentionStickIndex][1], CANVAS_WIDTH * attentionStickIndex / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * data[attentionStickIndex][0] / dataSize + 1)
    canvas.moveto(data[compareStickIndex][1], CANVAS_WIDTH * compareStickIndex / dataSize + 1, CANVAS_HEIGHT - CANVAS_HEIGHT * data[compareStickIndex][0] / dataSize + 1)
    window.update()
    if speedLimit != 0:
        time.sleep(speedLimit)
    canvas.itemconfig(data[attentionStickIndex][1], fill="white")
    canvas.itemconfig(data[compareStickIndex][1], fill="white")

# 두 막대를 교환하지 않고 색상만 표현하는 함수
def notExchangePairStick(window, canvas, data, dataSize, attentionStickIndex, compareStickIndex, speedLimit = 0, attentionStickColor = "red", compareStickColor = "blue"):
    canvas.itemconfig(data[attentionStickIndex][1], fill=attentionStickColor)
    canvas.itemconfig(data[compareStickIndex][1], fill=compareStickColor)
    window.update()
    if speedLimit != 0:
        time.sleep(speedLimit)
    window.update()
    if speedLimit != 0:
        time.sleep(speedLimit)
    canvas.itemconfig(data[attentionStickIndex][1], fill="white")
    canvas.itemconfig(data[compareStickIndex][1], fill="white")

# 막대 색상 빨간 색으로
def changeColorRed(window, canvas, data, stickIndex, speedLimit = 0):
    canvas.itemconfig(data[stickIndex][1], fill="red")
    window.update()
    if speedLimit != 0:
        time.sleep(speedLimit)

# 막대 색상 파란 색으로
def changeColorBlue(window, canvas, data, stickIndex, speedLimit = 0):
    canvas.itemconfig(data[stickIndex][1], fill="blue")
    window.update()
    if speedLimit != 0:
        time.sleep(speedLimit)


# 막대 색상 노란 색으로
def changeColorYellow(window, canvas, data, stickIndex, speedLimit = 0):
    canvas.itemconfig(data[stickIndex][1], fill="yellow")
    window.update()
    if speedLimit != 0:
        time.sleep(speedLimit)


# 막대 색상 흰 색으로
def changeColorWhite(window, canvas, data, stickIndex, speedLimit = 0):
    canvas.itemconfig(data[stickIndex][1], fill="white")
    window.update()
    if speedLimit != 0:
        time.sleep(speedLimit)


## ====================== 정렬 알고리즘 ====================== ##
def bubbleSort(window, canvas, data, dataSize, speedLimit):
    for i in range(dataSize):
        for y in range(dataSize - 1, i, -1):
            if data[y][0] < data[y - 1][0]:
                exchangePairStick(window, canvas, data, dataSize, y, y - 1, speedLimit)
            elif speedLimit != 0:
                notExchangePairStick(window, canvas, data, dataSize, y, y - 1, speedLimit)
            else:
                continue
        changeColorYellow(window, canvas, data, i)


## ====================== 탐색 알고리즘 ====================== ##
def linearSearch(window, canvas, data, dataSize, searchValue, speedLimit):
    for i in data:
        changeColorRed(window, canvas, data, i[0], speedLimit)
        if i[0] == searchValue:
            changeColorYellow(window, canvas, data, i[0], speedLimit)
            break
        else:
            changeColorWhite(window, canvas, data, i[0], 0)

