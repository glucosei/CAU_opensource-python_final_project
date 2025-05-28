class KeyboardHandler:
        def __init__(self,w):
            self.w = w
            self.prev_keys = dict()

        def is_pressed(self,key: str) -> bool:
            return self.w.keys[key]

        def is_just_pressed(self,key: str) -> bool:
            now = self.w.keys[key]
            before = self.prev_keys.get(key, False)
            return now and not before

        def is_just_released(self,key: str) -> bool:
            now = self.w.keys[key]
            before = self.prev_keys.get(key, False)
            return not now and before

        def update(self):
            self.prev_keys = self.w.keys.copy()
