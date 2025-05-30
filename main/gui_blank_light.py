'''
gui 모듈을 사용하기 위한 기본 구조를 미리 적어 둔 파일입니다.

- 여러분은 이 아래에 있는, 함수 initialize()와 update()에 대한
  함수 정의 내용물을 구성함으로써 프로그램을 구성해야 해요

- 중간중간 F5를 눌러 interactive를 켜 둔 다음 진행하면
  IDLE이 함수 호출식 적을 때마다 적당한 툴팁을 읽어 보여줄 거예요
'''

import gui_core as gui
from main.entity import *
from main.input import *
from main.controller import *

w = gui.Window()


def initialize(timestamp):
    '적절한 설명 메시지'
    w.data.keyboardHandler = KeyboardHandler(w)
    w.data.mouseHandler = MouseHandler(w)
    w.data.player = Player(w,(w.data.width/2)-50,750,100,100,100, w.data.keyboardHandler)
    w.data.bulletController = BulletController(w)
    w.data.collisionController = CollisionController(w)
    w.data.enemyController = EnemyController(w)

def update(timestamp):
    '''
    여러 줄짜리
    설명 메시지
    '''
    w.data.player.update()
    w.data.keyboardHandler.update()
    w.data.bulletController.update()
    w.data.collisionController.update()
    w.data.enemyController.stageOneUpdate()

w.initialize = initialize
w.update = update
w.moveWindow(0,0)
w.start()
