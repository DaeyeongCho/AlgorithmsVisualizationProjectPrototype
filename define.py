## 윈도우 창 ##
TITLE = "정렬/탐색 알고리즘 시뮬레이터"
GEOMETRY = "1280x720"

## General Menu 프레임 하위 위젯 ##
RADIO_BUTTON_SELECT_ALGORITHM = [ "정렬 알고리즘", "탐색 알고리즘" ]

SORT_ALGORITHMS = ["버블 정렬", "선택 정렬", "삽입 정렬", "병합 정렬", "힙 정렬", "퀵 정렬"]
SEARCH_ALGORITHMS = ["선형 탐색", "이진 탐색"]

ADVANCED_MENU = "고급"

START = "시작"

## Advanced Menu 프레임 하위 위젯 ##
SPIN_BOX_WIDTH = 10

DATA_SIZE = "데이터 크기"
DATA_SIZE_DEFAULT = 100
DATA_SIZE_MIN = 10
DATA_SIZE_MAX = 300
DATA_SIZE_INCREMENT = 1

SPEED_LIMIT = "속도 제한(s)"
SPEED_LIMIT_DEFAULT = 0.000
SPEED_LIMIT_MIN = 0.000
SPEED_LIMIT_MAX = 1.000
SPEED_LIMIT_INCREMENT = 0.001

SHUFFLE_TIMES = "섞는 횟수(회)"
SHUFFLE_TIMES_DEFAULT = 1000
SHUFFLE_TIMES_MIN = 0
SHUFFLE_TIMES_MAX = 100000
SHUFFLE_TIMES_INCREMENT = 100

SEARCH_VALUE = "탐색 값(0:랜덤)"
SEARCH_VALUE_DEFAULT = 0
SEARCH_VALUE_MIN = 0
SEARCH_VALUE_INCREMENT = 1

## Simulation 프레임 하위 위젯 ##
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
CANVAS_COLOR = "white"

LABEL_HINT = ["주목", "비교", "픽스드"]
LABEL_HINT_COLOR = ["red", "blue", "yellow"]

LABEL_STATE = ["상태 : ", "---", "섞는 중...", "정렬 중...", "탐색 중...","섞기 완료!" , "정렬 완료!", "탐색 완료!"]

ELAPSED_TIME = ["시간(s:ms)", "--:---"]

END_BUTTONS = ["정지", "다시하기", "닫기"]