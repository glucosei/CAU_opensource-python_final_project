class PositionUpdater:
    @staticmethod
    def update(w, obj ,vx, vy):
        obj.x += vx
        obj.y += vy
        w.moveObject(obj.id, obj.x, obj.y)