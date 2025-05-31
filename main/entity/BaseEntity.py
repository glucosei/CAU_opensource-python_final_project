


class BaseEntity:
    def __init__(self,w, x, y, width, height):
        self.w = w
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dt = 1/60

    def move(self,dx,dy):
        self.x += dx
        self.y += dy


