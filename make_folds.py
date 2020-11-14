#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import glob
import itertools

folds = sorted(glob.glob("xa*"))

for fold in range(10):
    print(folds)
    test, valid, *train = folds
    os.system("cat {} > train{}.tsv".format(" ".join(train), fold))
    os.system("cat {} > test{}.tsv".format(test, fold))
    os.system("cat {} > valid{}.tsv".format(valid, fold))
    folds = folds[1:] + [folds[0]]

