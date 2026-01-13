# Function to convert integer to Roman numeral
def int_to_roman(num):
    roman_dict = {
        1000: "M", 900: "CM",
        500: "D", 400: "CD",
        100: "C", 90: "XC",
        50: "L", 40: "XL",
        10: "X", 9: "IX",
        5: "V", 4: "IV",
        1: "I"
    }    
    roman = ""
    for value in roman_dict:
        while num >= value:
            roman += roman_dict[value]
            num -= value
    return roman

# Function to convert Roman numeral to integer
def roman_to_integer(roman):
    roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }
    total = 0
    prev_value = 0
    
    for char in reversed(roman.upper()):
        value = roman_dict.get(char, 0)
        
        if value < prev_value:
            total -= value
        else:
            total += value
        
        prev_value = value
    
    return total

# Main program loop
print(40*"=")
print ("Welcome to the Roman Numeral Converter!")
print(40*"=")
while True:
    operation=input("Enter '1' to convert Integer to Roman \n"\
                    "Enter'2' to convert Roman to Integer\n"\
                    "Enter 'q' to quit\n"\
                    "Choose operation: ")
    print(40*"=")
    if operation.lower()=="q":
        print("     Exiting the program.")
        print()
        print("--------Visit Again!--------")
        print(40*"=")
        break
    if operation=="1":
        #  Take user input
        number = int(input("Enter a number (1 to 1000): "))
        
        if 1 <= number <= 1000:
            print("Roman numeral:", int_to_roman(number))
            print(40*"=")
        else:
            print("Please enter a number between 1 and 1000.")
            print(40*"=")

    elif operation=="2":
        # ---- User Input ----
        roman_num = input("Enter a Roman number (I to M): ")
        
        result = roman_to_integer(roman_num)
        
        if 1 <= result <= 1000:
            print("Integer value:", result)
            print(40*"=")
        else:
            print("Invalid Roman numeral or out of range (1–1000)")
            print(40*"=")
    else:
        print("Invalid operation. Please try again.")
        continue  
        
        