from Logic.Instrument import Instrument as i


class Guitarron(i):
    NAME = "Guitarron"

    def tune(self):
        super().tune()
        return self.NAME + " is tuned"

    def play(self):
        super().play()
        return self.NAME + " is Playing"
