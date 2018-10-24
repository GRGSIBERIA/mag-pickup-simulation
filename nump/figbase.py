#-*- encoding: utf-8
import csv
import numpy as np
import matplotlib.pyplot as plot

class FigBase:
    def __init__(self, path, radius, _height):
        self.positions = []
        self.original_bws = []
        with open(path, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                self.positions.append(float(row[0]) * 10)   # 単位がセンチメートル
                self.original_bws.append(float(row[1]))
        
        self.sigma = 1
        self.psi = radius
        self.height = _height
        self.origin = np.array([0, 0, self.height])
        self.bws = []
        self.xlabel = ""
    
    def showComputeBw(self):
        plot.plot(self.positions, self.bws, "-x")
        plot.show()
    
    def showComputeOriginBw(self):
        plot.plot(self.positions, self.original_bws, "-x")
        plot.show()
    
    def showCompareBw(self):
        a = self.original_bws / np.max(self.original_bws)
        b = self.bws / np.max(self.bws)
        plot.plot(self.positions, a, "-x", label="Original")
        plot.plot(self.positions, b, "-x", label="Theoretical values")
        plot.xlabel(self.xlabel)
        plot.ylabel("-> Magnetic field [G]")
        plot.legend()
        plot.show()
    
    def printSigma(self):
        a = np.array(self.original_bws) / np.array(self.bws)
        plot.plot(self.positions, a, "-x")
        plot.xlabel(self.xlabel)
        plot.ylabel("-> $\\sigma$")
        plot.show()
    
    def showCompareBz(self):
        #単純に直径だけ引いた部分との差を取っているだけでは？
        pass
        