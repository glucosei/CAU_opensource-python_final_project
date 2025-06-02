from main.entity.BaseEnemy import BaseEnemy
from main.entity.utils import PositionUpdater


class EnemyTypeB(BaseEnemy):
    def __init__(self,w,x,y):
        super().__init__(w,x,y,50,50,20)
        self.bulletShooter.COOLDOWN_TIME = 3*60
        self.bulletShooter.damage = 30
        self.bulletShooter.speedY = 15/60
        self.w.recolorObject(self.id, 'purple')
        self.vx = 0/60
        self.vy = 45/60


    def update(self):
        PositionUpdater.update(self.w, self, self.vx, self.vy)
        if self.bulletShooter.isReady():
            self.bulletShooter.shoot(self.x+self.width/2, self.y, self.vy, 1)
            self.bulletShooter.cooldown = self.bulletShooter.COOLDOWN_TIME

        else:
            self.bulletShooter.cooldown -= 1




