class MouseHandler:
    def __init__(self, w):
        self.w = w
        self.prev_mouse_buttons = [False, False, False]  # 좌, 우, 휠버튼 상태 초기화

    def update(self):
        # 매 프레임마다 이전 상태를 저장해둠
        self.prev_mouse_buttons = self.w.mouse_buttons[:]

    def isPressed(self, button: int) -> bool:
        return self.w.mouse_buttons[button]

    def isJustPressed(self, button: int) -> bool:
        return (not self.prev_mouse_buttons[button]) and self.w.mouse_buttons[button]


    def getPosition(self):
        return self.w.mouse_position_x, self.w.mouse_position_y
