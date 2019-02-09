class Village:
    def __init__(self, x, y, name) -> None:
        self.x = x
        self.y = y
        self.name = name

    def __str__(self) -> str:
        return self.name
