num = 12500

def convert_number():
    print("Binary :", bin(num))
    print("Octal :", oct(num))
    print("Hex :", hex(num))

def format_number():
    print("Comma Format :", format(num, ","))

def scientific():
    print("Scientific Notation :", format(num, ".2e"))

convert_number()
format_number()
scientific()