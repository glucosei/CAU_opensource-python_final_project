class MouseHandler:
    def __init__(self, w):
        self.w = w


    def is_pressed(self, button: int) -> bool:
        return self.w.mouse_buttons[button]

    def get_position(self):
        return self.w.mouse_position_x, self.w.mouse_position_y
