class UpdateLocation:
    @staticmethod
    def update(w, objId, x, y, vx, vy):
        x += vx
        y += vy
        w.moveObject(objId, x, y)
        return x,y