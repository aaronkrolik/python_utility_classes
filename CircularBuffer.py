'''
Created on Oct 30, 2013

@author: aaronkrolik
'''

class CircularBuffer(object):
    def __init__(self):
        self.row1 = []
        self.matrix = []
        self.row1len=0
    def append(self, input):
        self.row1.append(input)
        self.row1len+=1
    def circulantFromList(self, lst):
        self.row1=lst
        self.row1len=len(lst)
    def generateCirculant(self):
        tempDoubleArray = self.row1 + self.row1
        count=self.row1len
        while count>0:
            self.matrix.append(tempDoubleArray[count:count+self.row1len])
            count-=1
    def printMatrix(self):
        for row in self.matrix:
            print row
        print "\n"
            
if __name__ == "__main__":     
    x = CircularBuffer()
    x.append(5)
    x.append(6)
    x.append(7)
    x.append(8)
    x.generateCirculant()
    x.printMatrix()