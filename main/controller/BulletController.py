"""
프로그램 이름: BulletController.py(Bullet 인스턴스 제어 모듈)
작성자: 임재욱
프로그램 설명: 각 Bullet 인스턴스의 속도를 고려하여 해당 프레임에서의 위치를 갱신합니다.
사용 방법: BulletController 인스턴스를 생성한 뒤,
         매 프레임마다 BulletController.update()를 호출하세요
"""



from main.entity.utils.PositionUpdater import PositionUpdater

class BulletController:
    """
    각 Bullet인스턴스의 위치를 갱신하는 클래스입니다.

    Attributes:
        w (Window): GUI창 객체. Bullet 위치 갱신 및 삭제에 사용됩니다.
    """

    def __init__(self, w):
        """
        BulletController 인스턴스를 초기화합니다.

        Args:
            w (Window): GUI 창 객체
        """
        self.w = w


    def update(self):
        """
        각 Bullet인스턴스의 속도를 고려하여 위치를 갱신합니다.
        화면 밖으로 나갔다면 bullet인스턴스를 삭제합니다.

        Returns:
            None
        """


        for bullet in self.w.data.bulletList:
            PositionUpdater.update(self.w, bullet, 0, bullet.v )

            if bullet.y < -100 or bullet.y > 950:
                bullet.onDeath()
