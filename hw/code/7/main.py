from __future__ import division
__author__ = 'Venkatesh'

from GolinskiModel import Golinski
from de import DiffEvol

if __name__ == '__main__':
    model = Golinski()
    opt = DiffEvol()
    opt.de(model)