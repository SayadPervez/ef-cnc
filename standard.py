from functions import *
import constants as const
import algorithm1,algorithm2
from visualization import *
from visualization import arr2png as a2p
import time
from matplotlib import pyplot as plt
from shapes import *

if(const.sampl!=10):
    pass
    #raise Exception("\"sampl\" value not set to standard value 10.\nSet \"sampl = 10\" in constants.py to coninue ...")

def alg1Large():
    print("\na1-L starting:")
    canvasLarge = Canvas(1080,720)
    shapesLarge = [ 
                Square(70) ,
                Rectangle(100,50) , 
                Circle(50) ,
                Cone(120,150) ,
                Cone(120,40)
            ]
    s = time.time()
    c = canvasLarge
    li = shapesLarge
    print("Starting algorithm")
    out = algorithm1.run(c,li,log_=True,constCompute=10)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg1Small():
    print("\na1-S starting:")
    canvas = Canvas(108,72)
    shapes    = [ 
                Square(7) ,
                Rectangle(10,5) , 
                Circle(5) ,
                Cone(12,15) ,
                Cone(12,4)
            ]
    s = time.time()
    c = canvas
    li = shapes
    print("Starting algorithm")
    out = algorithm1.run(c,li,log_=True,constCompute=100)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg2Large():
    print("\na2-L starting:")
    canvasLarge = Canvas(1080,720)
    shapesLarge = [ 
                Square(70) ,
                Rectangle(100,50) , 
                Circle(50) ,
                Cone(120,150) ,
                Cone(120,40)
            ]
    s = time.time()
    c = canvasLarge
    li = shapesLarge
    print("Starting algorithm")
    out = algorithm2.run(c,li,log_=True,constCompute=10)
    e = time.time()
    #a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def alg2Small():
    print("\na2-S starting:")
    canvas = Canvas(108,72)
    shapes    = [ 
                Square(40) ,
                Rectangle(100,25) , 
                Circle(7) ,
                Cone(17,20) ,
                Cone(12,4)
            ]
    s = time.time()
    c = canvas
    li = shapes
    print("Starting algorithm")
    out = algorithm2.run(c,li,log_=True,constCompute=100)
    e = time.time()
    a2p(out).show()
    print(f"Time taken : {e-s} seconds")
    return(e-s)

def RUN():
    x = ['a1-S','a2-S','a1-L','a2-L']
    y = []
    #y.append(alg1Small())
    y.append(alg2Small())
    print(y[0])
    return("")
    #y.append(alg1Large())
    #y.append(alg2Large())
    print("Plotting ...")
    plt.bar(x, height=y, alpha=0.8 , color=['red','green','red','green'])
    plt.title("Algorithm Comparison for Small and Large Canvas")
    plt.xlabel("Algorithms")
    plt.ylabel("Time taken")
    plt.show()

RUN()