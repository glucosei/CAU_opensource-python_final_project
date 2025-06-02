class KeyboardHandler:
        def __init__(self,w):
            self.w = w
            self.prev_keys = dict()

        def isPressed(self,key: str) -> bool:
            return self.w.keys[key]

        def isJustPressed(self,key: str) -> bool:
            now = self.w.keys[key]
            before = self.prev_keys.get(key, False)
            return now and not before

        def isJustReleased(self,key: str) -> bool:
            now = self.w.keys[key]
            before = self.prev_keys.get(key, False)
            return not now and before

        def update(self):
            self.prev_keys = self.w.keys.copy()
