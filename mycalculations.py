import modern_robotics as mr
import numpy as np
import math
import pandas as pd

# function to convert degrees to radian
def degtorad(vals):
    rads = lambda x : (x * math.pi)/180
    radian = np.array([rads(xi) for xi in vals])
    return radian


# function to get an array
def array(n1,n2, typpe = 'arr' ):
    Alist = []
    for i in range(n1):
        list = []
        print("\nEnter column values of row {}:".format(i+1))
        for j in range(n2):
            c = float(input("c{}:".format(j)))
            list.append(c)
        Alist.append(list)
    ar = np.array(Alist)
    print("\n{}".format(ar))
    check = input("\nCheck correctness of inputs: choose 1 or 2 \n 1. correct\n 2. not correct\n")
    if check == '1':
        ar = ar
        Alist = Alist
    elif check == '2':
        print("\nEnter values again")
        ar = array(n1,n2, typpe = input("arr or list"))
        return ar
    if typpe == 'arr':
        return ar
    elif typpe == 'list':
        return Alist


def rotInv():
    n1 = int(input("How many rows are in your rotation matrix?\n"))
    n2 = int(input("How many columns are in your rotation matrix?\n"))
    R = array(n1,n2)
    invR = mr.RotInv(R)
    return invR

def vecToso3():
    n1,n2 = 3,1
    omg = array(n1,n2)
    so3mat = mr.VecToso3(omg)
    return so3mat

def so3toVec():
    n1,n2 = 3,3
    so3mat = array(n1,n2)
    omg = mr.so3ToVec(so3mat)
    return omg

def axisAng3():
    n1,n2 = 1,3
    expc3 = array(n1,n2)
    [omghat,theta] = mr.AxisAng3(expc3)
    return [omghat,theta]

def matrixExp3():
    n1,n2 = 3,3
    so3mat = array(n1,n2)
    R = mr.MatrixExp3(so3mat)
    return R

def matrixLog3():
    n1,n2 = 3,3
    R = array(n1,n2)
    so3mat = mr.MatrixLog3(R)
    return so3mat

def rpToTrans():
    n1,n2 = 3,3
    print("\nEnter rotation matrix")
    R = array(n1,n2)
    print("\nEnter position vector")
    n1,n2 = 3,1
    p = array(n1,n2)
    T = mr.RpToTrans(R,p)
    return T

def transToRp():
    n1,n2 = 4,4
    T = array(n1,n2)
    [R,p] = mr.TransToRp(T)
    return R,p

def invTrans():
    n1,n2 = 4,4
    T = array(n1,n2)
    invT = mr.TransInv(T)
    return invT

def vecTose3():
    n1,n2 = 6,1
    V = array(n1,n2)
    se3mat = mr.VecTose3(V)
    return se3mat

def se3TOvec():
    n1,n2 = 4,4
    se3mat = array(n1,n2)
    V = mr.se3ToVec(se3mat)
    return V

def adjoint():
    n1,n2 = 4,4
    T = array(n1,n2)
    AdT = mr.Adjoint(T)
    return AdT

def screwToAxis():
    h = float(input("Enter pitch value:\n"))
    n1,n2 = 1,3
    print("\nEnter point q values")
    q = array(n1,n2)
    print("\nEnter unit vector s")
    s = array(n1,n2)
    S = mr.ScrewToAxis(q,s,h)
    return S

def axisAng6():
    n1,n2 = 6,1
    expc6 = array(n1,n2)
    [S,theta] = mr.AxisAng6(expc6)
    return S,theta

def matrixExp6():
    n1,n2 = 4,4
    se3mat = array(n1,n2)
    T = mr.MatrixExp6(se3mat)
    return T

def matrixLog6():
    n1,n2 = 4,4
    T = array(n1,n2)
    se3mat = mr.MatrixLog6(T)
    return se3mat



class kinematics:

    def angle(b):
        ang = input("\nWill your angles be in radian or degree? choose a NUMBER from the choices!\n 1. radian\n 2. degree\n")
        if ang == '1':
            print("Enter  the list of joint values, thetalist.")
            thetalist = array(1,b, typpe = 'list')
        elif ang == '2':
            print("Enter  the list of joint values, thetalist.")
            theta = array(1,b, typpe = 'list')
            thetalist = []
            for i in range (len(theta[0])):
                thetalist.append((theta[0][i]*math.pi)/180)
        return thetalist

    def FKinbodyOrSpace():
        print("\nEnter Zero position of the end-effector, M")
        n1,n2 = 4,4
        M = array(n1,n2)
        b = int(input("\nHow many joint values?\n"))
        print("\nEnter the list of joint screws, Blist expressed in the end-effector frame or Slist expressed in the fixed-space frame") 
        bslist = array(6,b, typpe = 'list')
        thetalist = kinematics.angle(b)
        T = mr.FKinBody(M,bslist,thetalist)
        return T
    
    def velKin():
        b = int(input("\nHow many joint values?\n"))
        thetalist = kinematics.angle(b)
        print("\nEnter the list of joint screws, Blist expressed in the end-effector frame or Slist expressed in the fixed-space frame") 
        bs = input(" 1. space Jacobian\n 2. body Jacobian?\n")
        bslist = array(6,b, typpe = 'list')
        if bs == '1':
            J = mr.JacobianSpace(bslist,thetalist)
        elif bs == '2':
            J = mr.JacobianBody(bslist,thetalist)
        return J

    def ikin():
        print("\nEnter Zero position of the end-effector, M")
        n1,n2 = 4,4
        M = array(n1,n2)
        print("\nEnter desired end-effector configuration")
        T = array(n1,n2)
        b = int(input("\nHow many joint values?\n"))
        print("\nEnter the list of joint screws, Blist expressed in the end-effector frame or Slist expressed in the fixed-space frame") 
        bs = input(" 1. space frame\n 2. body frame?\n")
        bslist = array(6,b, typpe = 'list')
        thetalist0 = kinematics.angle(b)
        eomg = int(input("Enter tolerance eomg:\n"))
        ev = int(input("Enter tolerance ev:\n"))
        if bs == '1':
            [thetalist,success] = mr.IKinSpace(bslist,M,T,thetalist0,eomg,ev)
        elif bs == '2':

            [thetalist,success] = mr.IKinBody(bslist,M,T,thetalist0,eomg,ev)
        return [thetalist,success]


class matrix:

    def get_array1():
        n1 = int(input("How many rows are in your first array?\n"))
        n2 = int(input("How many columns are in your first array?\n"))
        array1 = array(n1,n2)
        print("array1 = {}".format(array1))
        return array1,n1,n2

    # code to find transpose of a matrix
    def transpose():
        array1 = matrix.get_array1()[0]
        result = np.array(array1[0, :])
        for row in array1[1:]:
            result = np.c_[result, np.array(row)]
        print("\nThe transpose is:\n{}".format(result))
        return result

    # code to find determinant of a matrix
    def determinant():
        array1 = matrix.get_array1()[0]
        result = np.linalg.det(array1)
        print("The determinant is", result)
        return result

    # code to find inverse of a matrix
    def inverse():
        array1 = matrix.get_array1()[0]
        result = np.linalg.inv(array1)
        print("The inverse is", result)
        return result

    # matrix multiplication by a constant
    def multConst():
        array1 = matrix.get_array1()[0]
        c = float(input("\nInput constant:\n"))
        result = c * array1
        print("The resulting array is", result)
        return result

    # matrix division by a constant
    def divConst():
        array1 = matrix.get_array1()[0]
        c = float(input("\nInput constant:\n"))
        result = (1 / c) * array1
        print("The resulting array is", result)
        return result

    # addition of two matrices
    def addArray():
        array1 = matrix.get_array1()[0]
        n1,n2 = matrix.get_array1()[1], get_array1()[2]
        print("\nSecond array")
        array2 = array(n1,n2)
        print("\narray2 = {}".format(array2))
        result = np.add(array1, array2)
        print("The resulting array is", result)
        return result

    # multiplication of two matrices
    def multmat():
        array1 = matrix.get_array1()[0]
        n1,n2 = matrix.get_array1()[1], get_array1()[2]
        print("\nSecond array")
        array2 = array(n1,n2)
        print("\narray2 = {}".format(array2))
        result = np.multiply(array1, array2)
        print("The resulting array is", result)
        return result

    # finding dot product
    def dotprod():
        array1 = matrix.get_array1()[0]
        n1 = int(input("\nHow many rows are in your second array?\n"))
        n2 = int(input("\nHow many columns are in your second array?\n"))
        array2 = array(n1,n2)
        print("\narray2 = {}".format(array2))
        try:
            result = np.dot(array1, array2)
            print("The resulting array is", result)
        except:
            correction = input("\ndimension of matrices to be multiplied must be in the order of nxm * mxz. Please "
                               "check your matrices again.\n\narray1 = {}\narray2 = {}\n\nare they the right arrays "
                               "in the right order?:\n".format(array1, array2))
            if correction in agree:
                print("Well, something is definitely wrong with them :(\n")
            elif correction in disagree:
                print("Let's try again then\n")
                matrix.dotprod()
        return result



    
# adding operation
def add():
    sum = 0
    n = int(input("\nHow many numbers would you like to add?\n"))
    for num in range(n):
        number = input("\nEnter number:\n")
        sum = sum + float(number)
    print("\nThe sum is {}".format(sum))
    return sum


# subtracting operation
def subtract():
    diff = int(input("\nEnter First Number:\n"))
    n = int(input("\nHow many numbers would you like to subtract from this number?\n"))
    for num in range(n):
        number = input("\nEnter number:\n")
        diff = diff - float(number)
    print("\nThe result is {}".format(diff))
    return diff


# multiplying operation
def multiply():
    mult = 1
    n = int(input("\nHow many numbers would you like to multiply?\n"))
    for num in range(n):
        number = input("\nEnter number:\n")
        mult = mult * float(number)
    print("\nThe product is {}".format(mult))
    return mult


# dividing operation
def divide():
    dividend = float(input("\nEnter number to be divided:\n"))
    divisor = float(input("\nEnter divisor number:\n"))
    try:
        quotient = dividend / divisor
        intgr = dividend // divisor
        remainder = dividend % divisor
        print("\nThe result is {}, integer value of {} with a remainder of {}".format(quotient, intgr, remainder))
        return quotient
    except:
        if divisor == 0.0:
            print("divisor number can't be zero")
            divide()
        else:
            print("Something went wrong. Please check the numbers you entered,\n {} / {}".format(dividend,divisor))


        




