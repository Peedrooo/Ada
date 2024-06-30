class Local:
    def __init__(
            self, name: str,
            load: int = 0,
            supported_load: int = 60,
            sugested_load: int = 80
            ):

        self.name = name
        self.load = load
        self.supported_load = supported_load
        self.sugested_load = sugested_load

    def __str__(self):
        return self.name

    def set_load(self, load):
        self.load = load

    def get_supported_load(self):
        return self.supported_load

    def get_sugested_load(self):
        return self.sugested_load

    def get_all(self):
        return {
            'name': self.name,
            'supported_load': self.supported_load,
            'sugested_load': self.sugested_load
        }
