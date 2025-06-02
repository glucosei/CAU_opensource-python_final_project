class StageNotifier:
    def __init__(self,w):
        self.w = w
        self.ids = [w.newImage(-10, -10, f"resource/stage{stage}.png", new_width=505//3, new_height=230//3, isVisible = False) for stage in range(1, 11)]

    def changeStage(self,stage):
        if stage == 1:
            self.w.showObject(self.ids[0])
        else:
            self.w.hideObject(self.ids[stage-2])
            self.w.showObject(self.ids[stage-1])


