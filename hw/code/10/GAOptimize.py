__author__ = 'Venkatesh'

from models.SettingModel import GASetting
from optimizers.de import de


if __name__ == '__main__':

    for model in [GASetting]:
        mod = model()
        for i,optimizer in enumerate([de]):
            optimizer(mod,50,3,0.3)