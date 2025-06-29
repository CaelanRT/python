loop_control = 0

def inch_to_centimeter(inch):
    return inch * 2.54

while loop_control == 0:
    print('What would you like to convert?\n' \
    '1. Inch to Centimeter\n' \
    '2. Centimeter to Inch\n' \
    '3. Farenheit to Celsius\n' \
    '4. Celsius to Farenheit\n' \
    '5. Exit')


    user_choice = int(input())

    match user_choice:
        case 1:
            print('Input value to convert to Centimeter:')
            inch_input = float(input())
            converted_cent = inch_to_centimeter(inch_input)
            print(f'{inch_input} Inches is {converted_cent} Centimeters')
        case 2:
            print('Input value to convert to Inches:')
            cent_input = float(input())
            converted_inch = cent_input *0.3937
            print(f'{cent_input} Centimeters is {converted_inch:.1f} Inches')
        case 3:
            print('Input value to convert to Celsius:')
            far_input = float(input())
            converted_cels = (far_input - 32) * 5 / 9
            print(f'{far_input} Farenheit is {converted_cels:.1f} Celsius')
        case 4:
            print('Input value to convert to Farenheit:')
            cel_input = float(input())
            converted_far = (cel_input * 9/5) + 32
            print(f'{cel_input} Celsius is {converted_far} Farenheit')
        case 5:
            print('Goodbye!')
            loop_control = 1


        