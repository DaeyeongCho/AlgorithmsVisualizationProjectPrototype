from define2 import *

def startSimulation(window, sortOrSearchAlgorithm, algorithm, dataSize, speedLimit, shuffleTime, searchValue, labelState, labelElapsedTime):
    data = list(range(1, int(dataSize) + 1))
    running = True
    timer = 0

    if sortOrSearchAlgorithm == 0:
        labelState.configure(text=LABEL_STATE[2])

    else:
        labelState.configure(text=LABEL_STATE[4])
        startTimer(window, running, timer, labelElapsedTime)

    print(data)

# simulation 프레임 타이머 함수
def startTimer(window, running, timer, labelElapsedTime):
    if running:
        timer += 1
        labelElapsedTime.configure(text=str(timer // 1000) + ":" + str(timer % 1000).zfill(3))

    window.after(1, lambda: startTimer(window, running, timer, labelElapsedTime))