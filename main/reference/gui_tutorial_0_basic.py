'''
0. 기본적인 gui 모듈 사용 방법 소개

- 중간중간 F5를 눌러 interactive를 켜 둔 다음 진행하면
  IDLE이 함수 호출식 적을 때마다 적당한 툴팁을 읽어 보여줄 거예요
'''

# import문이에요
# - gui_core.py는 여러분이 작성하는 .py 파일과 같은 폴더에 두면 돼요
from main import gui_core as gui

# 'gui 창' 하나를 만들고, 그걸 w에 담고 있어요.
# 아래에 있는 함수 호출식 비슷하게 생긴 수식의 괄호 안에 커서를 두고 Ctrl + \ (백스페이스 왼쪽 글자)를 누르면
# IDLE이, 새 창을 만들 때 어떤 것들을 설정할 수 있는지 보여줄 거예요
# (컴퓨터나 IDLE 버전에 따라 툴팁의 일부만 보여줄 수도 있어요. 그럴 때는 interactive에서 'help(이름) 엔터' 쳐 봐요)
w = gui.Window()


def initialize(timestamp):
    # 나중에 화면에 표시하기 위한 네모 하나를 준비해둘 수 있어요.
    #
    # (중요)
    # w.newRectangle()와 같이 새로운 네모 등등을 준비하기 위해 호출하는 함수들은 마지막에 숫자 하나를 return하도록 되어 있어요.
    # 이 숫자를 잘 담아 두어야 해요. 나중에 '그 네모'를 다루고 싶을 때 '그 네모에 대한 숫자'를 필요로 하기 때문이에요
    #
    # (중요)
    # gui 프로그램 안에서 사용할 Data들은,
    # w.data 의 이름 사전에 이름을 등재해 가며 담아 다루면 편할 거예요
    w.data.number = w.newRectangle(0, 0, 100, 100)


    # initialize()와 update()의 인수 자리에는 현재 시각을 나타내는 float 형식 값이 담겨 있어요.
    # 여기서는 gui 프로그램 실행을 시작하는 시점의 현재 시각을 살짝 담아 두고, 나중에 활용하고 있어요
    w.data.start_time = timestamp


def update(timestamp):
    x, y = w.getPosition(w.data.number)
    w.moveObject(w.data.number, x + 1, y + 1)
    
    # w.setTitle()을 사용해서 gui 창의 제목을 변경할 수 있어요.
    # f'' 와 같은 느낌으로 적어 둔 str literal에 대해서는, 글로 적기는 기니 이따 정리 슬라이드에서 설명해 볼께요
    w.setTitle(f'경과된 시간: {timestamp - w.data.start_time} s')


w.initialize = initialize
w.update = update

w.start()
