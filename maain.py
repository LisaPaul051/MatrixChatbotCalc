import callcalculations as rc
from random import randint

# function that repeats the question function
def again():
    again = input("\nAny other inquiry?\n")
    again = again.lower()
    while again in agree:
        rc.question()
        again = input("\nAny other inquiry?\n")
        again = again.lower()
    else:
        if again in disagree:
            print("Alright. Glad I could help you {}. Bye!".format(name))
            quit()
        else:
            print ("I don't think I'm programmed to answer that {}. Sorry!".format(name))
            again()




# main body that starts the program
name = input("-----Welcome to AskMe-----\n-----My name is Magoti-----\nAnd you are?\n")
greetings = ['Habari', 'Hello', 'Hola!']
greeting = greetings[randint(0, 2)] + ' ' + name
print("\n" + greeting)

agree = ["yes", "yeah", "yep", "sure", "ya", "yup"]
disagree = ["no", "nope", "not really", "not at the moment"]


q = input("Do you have an inquiry?\n")
q = q.lower()
if q in agree:
    rc.question()
    again()

else:
    print("\nOkay. You know where to find me incase you change your mind")
    time.sleep(3)
    qn = input("\nchanged your mind yet?\n")
    if qn in agree:
        print('yay!')
        rc.question()
        again()

    else:
        print("alright uncurious {}! goodbye then".format(name))
        quit()





