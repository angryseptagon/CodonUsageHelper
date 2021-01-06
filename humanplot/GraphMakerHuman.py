# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 16:19:11 2019

@author: Radhanath
"""

import numpy as np
import matplotlib.pyplot as plt

datafloat = np.loadtxt('Human Codon Usage.txt',usecols = (2,3,4),skiprows = 5)
datas = np.genfromtxt('Human Codon Usage.txt',dtype='str',usecols = (0,1), skip_header = 5)
fraction = datafloat.T[2][:]
prot = np.unique(datas.T[0])
for i in prot:
    plt.figure()
    indices = np.where(datas.T[0][:] == i)
    plt.bar(np.arange(len(indices[0])) +1,fraction[indices],tick_label = datas.T[1][indices],color = "green")
    plt.title(str(i)+" Codon Use in Human Olfactory Receptors")
    plt.ylabel("Fraction Used (0-1)")
    plt.xlabel("Codons")
    plt.savefig("ORCodonUsageHumanResidue#"+str(i)+".png")