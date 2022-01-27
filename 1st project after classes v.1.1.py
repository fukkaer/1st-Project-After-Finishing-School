import math



#print(math.pi)

def LePie():
    resultp1 = math.pi
    resultp3 = int(resultp1)
    resultp4 = str(resultp1)
    resultp2 = resultp4[0:10]
    print(resultp2)
#LePie()

#print('\n\n')

def multiplication():
    print('Room Tile cost by m^2 \n\n')
    unit01 = float(input('Please input the cost in € per m^2: '))
    unit02 = float(input('Please input the length of the room: '))
    unit03 = float(input('Please input the Width of the room: '))
    result = unit02 * unit03 * unit01
    print('the cost = ', result, '€')
#def main():
#    try:
   #     multiplication()
  #  except Exception as e:
 #       print(e)
#
#if __name__ == '__main__':
    #main()

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
                        print('(1) Kilograms (2) Poundings (3) Return\n\n')
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
                            loop04 == False
                        elif ci3 != 1 or ci3 != 2 or ci3 != 3:
                            print('invalid')
                except Exception as o:
                    print(o)
            elif cinput == 3:
                try:
                    loop05 = True
                    while loop05 == True:
                        print('(1) Celsius (2) Kelvin (3) (outdated)Farenheit\n\n')
                        ci4 = int(input('select unit to convert from: '))
                        if ci4 == 1:
                            try:
                                print('(1) Kelvin (2) (WHY) Farenheit\n\n')
                                ci41 = int(input('select unit to convert to: '))
                                if ci41 == 1:
                                    ci411 = float(input('input amount of Celsius to convert: '))
                                    ci411answer = ci411 + 273.15
                                    print(ci411, 'Celius', '=', ci411answer,' Kelvin')
                                elif ci41 == 2:
                                    ci412 = float(input('input amount of Celsius to convert: '))
                                    ci412answer = ci412 * 0.5556 + 32
                                    print(ci412, 'Celsius', '=', ci412answer, 'Fahrenheit')
                            except Exception as q:
                                print(q)
                        elif ci4 == 2:
                            try:
                                ci42 = float(input('input amount of Kelvin to convert: '))
                                print('(1) Celsius (2) Fahrenheit\n\n')
                                ci421 = int(input('Select unit to conovert to: '))
                                if ci421 == 1:
                                    ci4211answer = ci42 - 273.15
                                    print(ci42, 'Kelvin', '=', ci4211answer, 'Celsius')
                                elif ci421 == 2:
                                    ci4212answer = ci42 - 273.15 * 1.8 + 32
                                    print(ci42, 'Kelvin', '=', ci4212answer, 'Fahrenheit')
                            except Exception as r:
                                print(r)
                        elif ci4 == 3:
                            try:
                                
                except Exception as p:
                    print(p)
                    
            
    except Exception as m:
        print(m)
def main():
    loop = True
    while loop == True:
        try:
            print('Welcome\n\n(1) Floor Tile Cost Calculation By M^2\n(2) Counting change\n(3) Unit Converter\n(4) Quit')
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
            elif input01 == 4:
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
            elif input01 != 1 or input01 != 2 or input01 != 3 or input01 != 4:
                print('\n\ntry again\n\n')
        except Exception as j:
            print(j)
if __name__ == '__main__':
    main()
