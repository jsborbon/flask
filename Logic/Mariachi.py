from Logic.Instrument import *
from Logic.Fiddle import *
from Logic.Guitar import *
from Logic.Guitarron import *
from Logic.Trompet import *
from Logic.Vihuela import *


class Mariachi:

    instrumento = Instrument()
    listInstrument = [
        Fiddle(),
        Guitar(),
        Guitarron(),
        Trompet(),
        Vihuela()
    ]

    def assignInstrument(self, numInstrumento):
        """Asigna un instrumento al mariachi"""
        self.instrumento = self.listInstrument[numInstrumento]
        return self.instrumento.NAME

    def tuneInstrument(self):
        """afina el instrumento del mariachi"""
        return self.instrumento.tune()

    def playInstrument(self):
        """El mariachi toca"""
        return self.instrumento.play()
