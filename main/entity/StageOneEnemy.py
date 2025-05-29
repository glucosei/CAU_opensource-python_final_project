from main.entity.BaseEnemy import BaseEnemy


class StageOneEnemy(BaseEnemy):
    def __init__(self,w,x,y):
        super().__init__(w,x,y,100,100,100)
        self.bulletShooter.COOLDOWN_TIME = 3*60


    def update(self):
        if self.bulletShooter.isReady():
            self.bulletShooter.shoot(0,self.x+self.width/2, self.y+self.height)
            self.bulletShooter.cooldown = self.bulletShooter.COOLDOWN_TIME

        if not self.bulletShooter.isReady():
            self.bulletShooter.cooldown -= 1




