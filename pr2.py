#print("hello world\n"*100)
print('enter the value')
n=input()
print("u have entered:",n+'10') #this will do concatenate
print("u have entered:",int(n)+10) #typecasting

string="{} {} {}".format('hi','helllo','good') #for change formate
print(string)

string="{1} {0} {2}".format('hi','helllo','good')
print(string)

string="{l} {y} {f}".format(l='hi',y='helllo',f='good')
print(string)

# Formatting of Integers
String1 = "{0:b}".format(16)
print("\nBinary representation of 16 is ")
print(String1)
# Formatting of Floats
String1 = "{0:e}".format(1654.64586)
print("\nExponent representation of 165.6458 is ")
print(String1)
# Rounding off Integers
String1 = "{0:.3f}".format(1/6)
print("\none-sixth is : ")
print(String1)
