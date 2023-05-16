class Timer:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.id = float(69.0)
            cls._instance.status = 0
            cls._instance.remainingTime = 120
        return cls._instance
