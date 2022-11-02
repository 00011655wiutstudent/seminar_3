decimal = int(input("Enter a decimal number: "))
def decimal_to_octal(decimal):
    octal = 0
    i = 1
    while(decimal != 0):
        octal = octal + (decimal % 8)*i
        decimal = int(decimal / 8)
        i = i * 10
    return octal


print("The octal equivalent is :", decimal_to_octal(decimal))

# Another way to do it

decimal_intput = int(input("Write a decimal number: "))
octal_change = oct(decimal_intput).replace("0o", "")
print("Your decimal {} turned into {} octal".format(decimal_intput, octal_change))
