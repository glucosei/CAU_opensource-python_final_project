"""
프로그램 이름: CollisionController.py(충돌 제어 모듈)
작성자: 임재욱
프로그램 설명: 게임 내 모든 충돌을 감지하고,
            충돌 시 데미지 계산, 오브젝트 제거 등의 후속 동작을 수행합니다.
사용 방법: CollisionController 인스턴스를 생성한 뒤,
         매 프레임마다 BulletController.update()를 호출하세요
"""



class CollisionController:
    """
    충돌을 감지하고 후속동작을 수행하는 클래스입니다.

    Attributes:
        w (Window): GUI창 객체, 오브젝트 인스턴스들에 대한 위치 파악 및 삭제에 사용됩니다.
    """


    def __init__(self, w):

        """
        CollisionController 인스턴스를 초기화합니다.

        Args:
            w (Window): GUI창 객체

        Returns:
            None
        """

        self.w = w



    def _isColliding(self,ax, ay, aw, ah, bx, by, bw, bh):
        """
        (private메서드) 두 오브젝트가 충돌하는지 검사합니다.(aabb방식)

        Args:
            ax (int): a 오브젝트의 x좌표
            ay (int): a 오브젝트의 y좌표
            aw (int): a 오브젝트의 너비
            ah (int): a 오브젝트의 높이
            bx (int): b 오브젝트의 x좌표
            by (int): b 오브젝트의 y좌표
            bw (int): b 오브젝트의 너비
            bh (int): b 오브젝트의 높이

        Returns:
            bool: 두 오브젝트가 충돌하면 True, 그렇지 않으면 False
        """

        return (
                ax < bx + bw and ax + aw > bx and
                ay < by + bh and ay + ah > by
        )




    def update(self):
        """
        다음의 모든 인스턴스 쌍에 대한 충돌 여부를 검사합니다.: (Bullet,Enemy), (Bullet,Player), (Enemy,Player)
        충돌 시 데미지에 따라 인스턴스의 hp를 조절합니다.
        hp가 0이 된 Enemy 인스턴스와 충돌한 Bullet 인스턴스를 삭제합니다.

        Returns:
            None
        """

        px, py = self.w.getPosition(self.w.data.player.id)
        pw, ph = self.w.getSize(self.w.data.player.id)
        bulletsToRemove = []
        enemysToRemove = []

        for bullet in self.w.data.bulletList:

            bx, by = self.w.getPosition(bullet.id)
            bw, bh = self.w.getSize(bullet.id)

            for enemy in self.w.data.enemyList:
                ex, ey = self.w.getPosition(enemy.id)
                ew, eh = self.w.getSize(enemy.id)

                if self._isColliding(bx, by, bw, bh, ex, ey, ew, eh):
                    enemy.onHit(bullet.damage)
                    self.w.deleteObject(bullet.id)
                    bulletsToRemove.append(bullet)

            if self._isColliding(bx, by, bw, bh, px, py, pw, ph):
                self.w.data.player.onHit(bullet.damage)
                self.w.deleteObject(bullet.id)
                bulletsToRemove.append(bullet)



        for bullet in bulletsToRemove:
            if bullet in self.w.data.bulletList:
                self.w.data.bulletList.remove(bullet)



        for enemy in self.w.data.enemyList:
            ex, ey = self.w.getPosition(enemy.id)
            ew, eh = self.w.getSize(enemy.id)
            if self._isColliding(px,py,pw,ph,ex,ey,ew,eh):
                enemy.onHit(10)
                self.w.data.w.data.player.onHit(10)


        for enemy in self.w.data.enemyList:
            if enemy.hp<=0:
                enemysToRemove.append(enemy)


        for enemy in enemysToRemove:
            if enemy in self.w.data.enemyList:
                self.w.data.enemyList.remove(enemy)
                self.w.deleteObject(enemy.id)

