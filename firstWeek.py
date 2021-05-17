import os
import math

def TA(b, h):
    return (b * h)/2

def TAB(a,b,c):
    
    if a==b and a==c:
        print("Equilateral")

    elif a == b or a==c or b==c:
        print("Isoceles") 

    else:
        print("Scalene")

# All the inputs must be given in english
# Possible inputs: "Rock", "Paper", "Scissors"
def SPR(p1, p2):
    p1 = p1.lower()
    p2 = p2.lower()
    
    # Handeling bad input
    possible_input = ['rock', 'paper', 'scissors']
    if p1 not in possible_input or p2 not in possible_input:
        print("You must enter a valid input!")

    if p1 == p2:
        print('Tie')
    elif p1 == 'rock':
        if p2 == 'paper':
            print('Player 2 wins!')
        else:
            print('Player 1 wins!')
    elif p1 == 'paper':
        if p2 == 'rock':
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
    elif p1 == 'scissors':
        if p2 == 'rock':
            print('Player 2 wins!')
        else:
            print('Player 1 wins!')

def miles_to_km(n):
    return n*1.609344

def conversor(cuantity):
    UNITY = 1.609344
    print("1.- Km -> miles\n2.- Miles -> Km")
    choice = int(input(">>"))
    
    if choice == 1:
        return cuantity/UNITY
    elif choice == 2:
        return cuantity*UNITY
    else:
        print("Invalid input!!!")

def cylinder_volume(r, h):
    return math.pi * r**2 * h

def volume_calculator():
    # IDK what is the second one called in english
    print('1.-Cube\n2.-Parallelepiped\n3.-Cylinder\n4.-Sphere\n5.-Cone')
    choice = int(input('>>'))
    if choice == 1:
        # Must enter a number
        s = int(input('Side units: '))
        return s**3

    elif choice == 2:
        s = int(input('Side units: '))
        h = int(input('Height units: '))
        b = int(input('Base units: '))
        return s*h*b

    elif choice == 3:
        r = int(input('Radius units: '))
        h = int(input('Height units: '))
        return math.pi * r**2 * h
    
    elif choice == 4:
        r = int(input('Radius units: '))
        return 4/3 * math.pi * r**3
    
    elif choice == 5:
        r = int(input('Radius units: '))
        h = int(input('Height units: '))
        return 1/3 * math.pi * r**2 * h
    
    else:
        print("Invalid input mate!")

def changing_rates(maximum, minimum, comp):
    new_comp = 0
    if comp >= minimum and comp <= maximum:
        print(comp)
    else:
        print(comp)
        new_comp = int(input('New number: '))
        changing_rates(maximum, minimum, new_comp)


def main():
    os.system('clear')
    print('Choose a function:\n1.- Area of a Triangle\n2.- Determining the type of triangle\n3.- Scissors paper rock\n4.- Mile to km converter\n5.-Mi-Km and Km-Mi\n6.- Cilinder Volume\n7.- Volume calculator\n8.- Changing ranges')
    
    # Because there is no switch statement I'll use if... for now, later I will add dictionary mapping
    
    redo = False
    
    ch = int(input(">>"))
    
    # Test
    if ch == 1:
        print(TA(5, 4))
    elif ch == 2:
        print(TAB(10, 10, 10))
    elif ch == 3:
        print(SPR('rock', 'Paper'))
    elif ch == 4:
        print(miles_to_km(10))
    elif ch == 5:
        print(conversor(10))
    elif ch == 6:
        print(cylinder_volume(1, 10))
    elif ch == 7:
        print(volume_calculator())
    elif ch == 8:
        print(changing_rates(100, 30, 101))
    else:
        print('Choose a real option!')
    
    # Run the program again
    print("Wanna do it again? (y/N)")
    re = str(input("\n>>"))
    if re.lower() == 'y':
        main()
    else:
        print("Goodbye!")
        quit

if __name__=='__main__':
    main()

