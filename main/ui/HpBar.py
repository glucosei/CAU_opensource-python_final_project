class HpBar:
    def __init__(self, w, obj):
        self.w = w
        self.MAX_HP = obj.hp
        self.obj = obj
        self.objWidth, self.objHeight= w.getSize(obj.id)
        self.maxHpId = w.newRectangle(obj.x,obj.y+self.objHeight,self.objWidth,10, fill_color='gray')
        self.currentHpId = w.newRectangle(obj.x,obj.y+self.objHeight,self.objWidth,10, fill_color='blue')
        w.raiseObject(self.maxHpId)
        w.raiseObject(self.currentHpId)

    def update(self):
        self.w.resizeObject(self.currentHpId, (self.obj.hp/self.MAX_HP)*self.objWidth, 10)
        self.w.moveObject(self.currentHpId, self.obj.x, self.obj.y+self.objHeight)
        self.w.moveObject(self.maxHpId, self.obj.x, self.obj.y+self.objHeight)
