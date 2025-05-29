class SkillFlash:
    def __init__(self,w,obj, COOLDOWN_TIME = 60*60):
        self.obj = obj
        self.w = w
        self.COOLDOWN_TIME = COOLDOWN_TIME
        self.cooldown = 0

    def isReady(self):
        return self.cooldown <= 0

    def flash(self, vx, vy):
        self.obj.x += vx*(1/2)*60
        self.obj.y += vy*(1/2)*60

        objWidth, objHeight = self.w.getSize(self.obj.id)
        print(self.obj.x, objWidth-objWidth)

        if self.obj.x < 0:
            self.obj.x = 0
        elif self.obj.x > self.w.data.width-objWidth:
            self.obj.x = self.w.data.width-objWidth

        if self.obj.y < 0:
            self.obj.y = 0
        elif self.obj.y > self.w.data.height-objHeight:
            self.obj.y = self.w.data.height-objHeight