class Singleton:
    _instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def getValue(self) -> str:
        return self.val

    def setValue(self, value: str) -> None:
        self.val = value

