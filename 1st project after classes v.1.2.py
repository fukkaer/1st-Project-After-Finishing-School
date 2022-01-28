import math
import random


#print(math.pi)

def LePie():
    resultp1 = math.pi
    resultp3 = int(resultp1)
    resultp4 = str(resultp1)
    resultp2 = resultp4[0:10]
    print(resultp2)

def multiplication():
    print('Room Tile cost by m^2 \n\n')
    unit01 = float(input('Please input the cost in € per m^2: '))
    unit02 = float(input('Please input the length of the room: '))
    unit03 = float(input('Please input the Width of the room: '))
    result = unit02 * unit03 * unit01
    print('the cost = ', result, '€')

def changeunit():
    print('shopping debug software\n\n')
    unit001 = float(input('Input the total cost of all items: '))
    unit002 = float(input('Input the amount of cash given: '))
    unit003 = unit002 - unit001
    print('Change = ', unit003, '€. Have a nice day.')

def unitconverter():
    print('\n\nWelcome to the unit converter.\n\n')
    try:
        print('(1)length\n(2)Weight\n(3)Temperature\n(4)return\n\n')
        cinput = int(input('Please Select measurement to convert from: '))
        loop02 = True
        while loop02 == True:
            if cinput == 1:
                try:
                    loop03 = True
                    while loop03 == True:
                        print('(1)Meters (2) Feet (3) Return\n\n')
                        ci2 = int(input('Select Unit to convert from: '))
                        if ci2 == 1:
                            ci21 = float(input('input amount of meters to convert to feet: '))
                            ci21answer = ci21 / 3.281
                            print(ci21answer)
                        elif ci2 == 2:
                            ci22 = float(input('input amount of feet to convert to meters: '))
                            ci22answer = ci22 * 3.281
                            print(ci22answer)
                        elif ci2 == 3:
                            loop03 == False
                        elif ci2 != 1 or ci2 != 2 or ci2 != 3:
                            print('invalid')
                except Exception as n:
                    print(n)
            elif cinput == 2:
                try:
                    loop04 = True
                    while loop04 == True:
                        print('(1) Kilograms (2) Pounds (3) Return\n\n')
                        ci3 = int(input('select unit to convert from: '))
                        if ci3 == 1:
                            ci31 = float(input('input amount of KG to convert to lbs: '))
                            ci31answer = ci31 * 2.205
                            print(ci31answer)
                        elif ci3 == 2:
                            ci32 = float(input('input amount of lbs to convert to KG: '))
                            ci32answer = ci32 / 2.205
                            print(ci32answer)
                        elif ci3 == 3:
                            loop04 = False
                            break
                        elif ci3 != 1 or ci3 != 2 or ci3 != 3:
                            print('invalid')
                except Exception as o:
                    print(o)
            elif cinput == 3:
                try:
                    loop05 = True
                    while loop05 == True:
                        print('\n\n(1) Celsius (2) Kelvin (3) Farenheit (4) Return\n\n')
                        ci4 = input('select unit to convert from: ')
                        if ci4 == '1' or ci4 == 'c' or ci4 == 'celsius':
                            try:
                                print('(1) Kelvin (2) Farenheit\n\n')
                                ci41 = input('select unit to convert to: ')
                                if ci41 == '1' or ci41 == 'k' or ci41 == 'kelvin':
                                    ci411 = float(input('input amount of Celsius to convert: '))
                                    ci411answer = ci411 + 273.15
                                    print(ci411, 'Celius', '=', ci411answer,' Kelvin')
                                elif ci41 == '2' or ci41 == 'f' or ci41 == 'farenheit' or ci41 == 'fahrenheit':
                                    ci412 = float(input('input amount of Celsius to convert: '))
                                    ci412answer = ci412 * 1.8 + 32
                                    print(ci412, 'Celsius', '=', ci412answer, 'Fahrenheit')
                            except Exception as q:
                                print(q)
                        elif ci4 == '2' or ci4 == 'k' or ci4 == 'kelvin':
                            try:
                                ci42 = float(input('input amount of Kelvin to convert: '))
                                print('(1) Celsius (2) Fahrenheit\n\n')
                                ci421 = input('Select unit to convert to: ')
                                if ci421 == '1' or ci421 == 'c' or ci421 == 'celsius':
                                    ci4211answer = ci42 - 273.15
                                    print(ci42, 'Kelvin', '=', ci4211answer, 'Celsius')
                                elif ci421 == '2' or ci421 == 'fahrenheit' or ci421 == 'f':
                                    ci4212answer = ci42 - 273.15 * 1.8 + 32
                                    print(ci42, 'Kelvin', '=', ci4212answer, 'Fahrenheit')
                            except Exception as r:
                                print(r)
                        elif ci4 == '3' or ci4 == 'f' or ci4 == 'fahrenheit' or ci4 == 'farenheit':
                            try:
                                ci43 = float(input('input amount of Farenheit to convert: '))
                                print('\n(1) Celsius (2) Kelvin\n\n')
                                ci431 = input('Select unit to convert to: ')
                                if ci431 == '1' or ci431 == 'c' or ci431 =='celsius':
                                    ci4311Answer = ci43 - 32 * 0.5556
                                    print(ci43, 'Farenheit', '=', ci4311Answer, 'Celsius')
                                elif ci431 == '2' or ci431 == 'k' or ci431 == 'kelvin':
                                    ci4312Answer = ci43 - 32 * 5 / 9 + 273.15
                                    print(ci43, 'Farenheit', '=', ci4312Answer, 'Kelvin')
                            except Exception as v:
                                print(v)
                        elif ci4 == 4 or ci4 == 'return' or ci4 == 'quit':
                            loop05 == False
                            loop02 = True
                            break
                except Exception as p:
                    print(p)
            elif cinput == 4:
                loop02 = False
                break
            
    except Exception as m:
        print(m)

def coin_flip():
    landed = ''
    loop06 = True
    while loop06 == True:
        try:
            flipinput = input('Flip Again? Y/N: ')
            if flipinput == 'y':
                landed = random.randint(1,2)
                if landed == 1:
                    print('Coin Landed on Tails.\n\n')
                elif landed == 2:
                    print('Coin Landed on Heads.\n\n')
            elif flipinput == 'n':
                loop06 = False
        except Exception as t:
            print('Error in coin flip module. Error location t\n\n')
            print(t)
def main():
    loop = True
    while loop == True:
        try:
            print('Welcome\n\n(1) Floor Tile Cost Calculation By M^2\n(2) Counting change\n(3) Unit Converter\n(4) Coin Flip\n(5) Quit')
            input01 = int(input('Choose which program you would like to start: '))
            if input01 == 2:
                try:
                    changeunit()
                except Exception as f:
                    print(f)
            elif input01 == 1:
                try:
                    multiplication()
                except Exception as g:
                    print(g)
            elif input01 == 5:
                try:
                    input02 = input('Are you sure you want to Quit (y/n)?: ')
                    if input02 == 'y':
                        try:
                            print('goodbye')
                            loop == False
                            break
                        except Exception as h:
                            print(h)
                    elif input02 == 'n':
                        try:
                            print('action cancelled')
                            pass
                        except Exception as i:
                            print(i)
                    elif input02 != 'n' or input02 != 'y':
                        print('action cancelled')
                        pass
                except Exception as k:
                    print(k)
            elif input01 == 3:
                try:
                    unitconverter()
                except Exception as l:
                    print(l)
            elif input01 == 4:
                try:
                    coin_flip()
                except Exception as u:
                    print('\n\nError in coin flip module via main function. Error u\n\n')
                    print(u)
            elif input01 != 1 or input01 != 2 or input01 != 3 or input01 != 4 or input01 != 5:
                print('\n\ntry again\n\n')
        except Exception as j:
            print(j)
if __name__ == '__main__':
    main()
