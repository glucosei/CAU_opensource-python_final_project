class HpBarController:
    def __init__(self, w):
        self.w = w

    def update(self):
        for hpBar in self.w.data.hpBarList:
            hpBar.update()