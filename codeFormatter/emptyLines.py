import numpy as np
class Triangle:

    # By side lengths
    equilateral = []
    scalene = []
    isoceles = []

    def __init__(self, a, b, c):

        self.A = a
        self.B = b
        self.C = c
        
        if (a==b) and (b==c):
            
            Triangle.equilateral.append(self)
            
            
        elif (a!=b) and (b!=c) and (a!=c):
            
            Triangle.scalene.append(self)
            
            
        else:
            Triangle.isoceles.append(self)
    def heronsArea(self):
        #This calculates the area of the triangles by side length
        P=self.A+self.B+self.C
        Q=-self.A+self.B+self.C
        U=self.A-self.B+self.C
        V=self.A+self.B-self.C
        area = 0.25*np.sqrt(P*Q*U*V)
        return area