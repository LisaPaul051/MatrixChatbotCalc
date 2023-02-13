import mycalculations as m
import time
from datetime import date

agree = ["yes", "yeah", "yep", "sure", "ya", "yup"]
disagree = ["no", "nope", "not really", "not at the moment"]


# class that handles calling of rigid body calculations' functions
class rigidbodymotions:

    def rotations():
        print("\nSO(2), SO(3) - Special Orthogonal group")
        print("\nChoose NUMBER of operation you would like to do")
        operation = input(" 1. Compute the inverse of the rotation matrix R.\n 2. "
                         "Find the 3 × 3 skew-symmetric matrix corresponding to a 3 vector.\n 3. "
                        "Find the 3-vector corresponding to the 3×3 skew-symmetric matrix so3mat.\n 4. "
                        "Extract the rotation axis ˆω and the rotation amount θ from the 3-vector ˆωθ of "
                        "exponential coordinates for rotation, expc3.\n 5. "
                        "Compute the rotation matrix R ∈ SO(3) corresponding "
                        "to the matrix exponential of so3mat ∈ so(3).\n 6. "
                        "Compute the matrix logarithm so3mat ∈ so(3) of the rotation matrix R ∈ SO(3)\n 7. "
                        "Extract the rotation matrix and position vector from a homogeneous transformation matrix T\n 8. "
                        "Back\n\n")
        if operation == '1':
            ans = m.rotInv()
        elif operation == '2':
            ans = m.vecToso3()
        elif operation == '3':
            ans = m.so3toVec()
        elif operation == '4':
            ans = m.axisAng3()
        elif operation == '5':
            ans = m.matrixExp3()
        elif operation == '6':
            ans = m.matrixLog3()
        elif operation == '7':
            ans = m.transToRp()
        elif operation == '8':
              rigidbodymotions.choices()  
        else:
            print("\nPlease read the instructions carefully!")
            rigidbodymotions.rotations()
        return ans
    
    def rigid_body_motions():
        print("\nSE(2), SE(3) - Special Euclidean group")
        print("\nChoose NUMBER of operation you would like to do")
        operation = input(" 1. Build the homogeneous transformation matrix T corresponding to a rotation matrix"
                          "R ∈ SO(3) and a position vector p ∈ R3\n 2. "
                          "Compute the inverse of a homogeneous transformation matrix T.\n 3. "
                          "Find the se(3) matrix corresponding to a 6-vector twist V.\n 4. "
                          "Find the 6-vector twist corresponding to an se(3) matrix se3mat.\n 5. "
                          "Compute the 6 × 6 adjoint representation [AdT ] of the homogeneous transformation matrix T.\n 6. "
                          "Find a normalized screw axis representation S of a screw described by a unit vector s in "
                          "the direction of the screw axis, located at the point q, with pitch h.\n 7. "
                          "Extract the normalized screw axis S and the distance traveled along the screw θ " 
                          "from the 6-vector of exponential coordinates Sθ.\n 8. "
                          "Compute the homogeneous transformation matrix T ∈ SE(3) corresponding to the "
                          "matrix exponential of se3mat ∈ se(3).\n 9 "
                          "Compute the matrix logarithm se3mat ∈ se(3) of the homogeneous transformation matrix T ∈ SE(3).\n 10. "
                          "Back\n\n")
            
        if operation == '1':
            ans = m.rpToTrans
        elif operation == '2':
            ans = m.invTrans()
        elif operation == '3':
            ans = m.vecTose3()
        elif operation == '4':
            ans = m.se3TOvec()
        elif operation == '5':
            ans = m.adjoint()
        elif operation == '6':
            ans = m.screwToAxis()
        elif operation == '7':
            ans = m.axisAng6()
        elif operation == '8':
            ans = m.matrixExp6()
        elif operation == '9':
            ans = m.matrixLog6()
        elif operation == '10':
            rigidbodymotions.choices()
        else:
            print("\nPlease read the instructions carefully!")
            rigidbodymotions.rigid_body_motions()
        return ans

    # function to choose subtopic from rigid body motions topics
    def choices():
        print("\nChoose Sub-Topic Number")
        sub_topic = input(" 1. Rotations\n 2. Rigid-Body Motions\n 3. Back\n\n")
        if sub_topic == '1':
            answer = rigidbodymotions.rotations()

        elif sub_topic == '2':
            answer = rigidbodymotions.rigid_body_motions()
        elif sub_topic == '3':
            main()
        return answer
  

# function that calls kinematics calculations' functions
def kinematics():
    print("\nChoose Sub-Topic Number")
    sub_topic = input(" 1. Forward Kinematics given Joint Screws expressed in the body frame or space frame\n"
                      " 2. Body Jacobian or Space Jacobian, given Joint Screws and thetalist \n 3. Inverse Kinematics using Newton-Raphson iteration\n 4. Back\n\n")
    if sub_topic == '1':
        answer = m.kinematics.FKinbodyOrSpace()

    elif sub_topic == '2':
        answer = m.kinematics.velKin()

    elif sub_topic == '3':
        answer = m.kinematics.ikin()
    elif sub_topic == '4':
        main()


# function to select a robotics topic or return to previous menu 
def main():
    print("Choose Topic Number")
    topic = input(" 1. Rigid-Body Motions\n 2. Kinematics\n 3. Back\n\n")
    if topic == '1':
        answer = rigidbodymotions.choices()
        print(answer)
    elif topic == '2':
        answer = kinematics()
        print(answer)
    elif topic == '3':
        question()




# function that calls simple mathematics operations
def simple_math():
    print("What operation?\n>add\n>sub\n>mult\n>div\n>matrix")
    choice = input("\n>")
    choice = choice.lower()
    if choice == "add":
        m.add()
    elif choice == "sub":
        m.subtract()
    elif choice == "mult":
        m.multiply()
    elif choice == "div":
        m.divide()
    elif choice == "matrix":
        matrix()



# funtion that handles matrix operations
def matrix():
    action = input("\nEnter index of the operation you would like to do with your array1\n1. array1 Transpose\n2. "
                   "determinant of array1\n3. inverse of array1\n4. array1 times a constant\n5. array1 divide a "
                   "constant\n6. array1 + array2\n7. array1 x array2\n8. dot product(array1, array2)\n9. Back\n")

    if action == '1':
        m.matrix.transpose()
    if action == '2':
        m.matrix.determinant()
    elif action == '3':
        m.matrix.inverse
    elif action == '4':
        m.matrix.multConst()
    elif action == '5':
        m.matrix.divConst()
    elif action == '6':
        m.matrix.addArray()
    elif action == '7':
        m.matrix.multmat()
    elif action == '8':
        m.matrix.dotprod()
    elif action == '9':
        simple_math()





# function that takes user's queries
def question():
    print("\ninquiry on?\n>date\n>time\n>simple math\n>robotics\n>matrix\n")
    msg = input("topic of your inquiry:\n")
    M = msg.lower()

    if M == "time":
        t = int(time.strftime("%H"))

        print("The time is", t)
        if t < 12:
            print("It's a brand new day! Let's hope we get through it in one piece :)")
        elif t < 19:
            check_in = input("How has your day been so far?\n")
            C = check_in.lower()
            if C in ['good', 'fine', 'great', 'fantastic', 'okay', 'not bad', 'wonderful', 'amazing']:
                print("That's great!")
            else:
                print("Oh! alright...")
        elif t < 22:
            eat = input("Have you had your dinner?\n")
            E = eat.lower()
            if E in agree:
                print("Good.")
            elif E in disagree:
                print("You need to eat!")
            else:
                print("I don't know what to say")
        else:
            print("It's pretty late, you should sleep.")

    elif M == "date":
        d = str(date.today())
        print("Today's date is" + ' ' + d)
        q = input("\nIs today a special day?\n")
        q = q.lower()
        if q in agree:
            s = input("Really?! What's special about it?\n")
            print("That's cool!")
        elif q in disagree:
            print("Okay.")
        else:
            print("I don't think I have a response to that {} :)".format(name))

    elif M == "simple math":
        simple_math()

    elif M == "robotics":
        main()

    elif M == "matrix":
        matrix()

    else:
        print("I don't think I'm programmed to do that {}. Sorry!".format(name))



    
                       
                



    


        
        

