from Logic.Instrument import Instrument as i


class Guitar(i):
    NAME = "Guitar"

    def tune(self):
        super().tune()
        return self.NAME + " is tuned"

    def play(self):
        super().play()
        return self.NAME + " is Playing"
