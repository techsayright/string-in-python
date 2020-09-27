text="python langauge"
print(text)

#String can be access
print(text[2])

#String is an immutable..it cant be change
#text[0]='g'

#string support value slicing
print(text[0:3])

#string can be represented in single, double or triple quotes
text='Hello'
print(text)
text="hello"  #this both are same things

text= "'let's learn python"
print(text)

text='i love "pyhton"'
print(text)

demo='''hello 
my name is darshan
i love python'''
print(demo)

t1="Good"
t2="Morning"
print(t1+t2)
print(t1+' '+t2)

n=34
#print(n+t1)
#we have to convert n var into string..then we can do sum of it
n1=str(n)
print(n1)
print(n1+t1)

#string function
print("i love python".title())
print("i love python".lower())
print("i love python".upper())
print("i love python".istitle()) #we can also use islower(),isuppeer(),isalpha(),isalnum(),isdecimal(),isdigit()...
                                #which is return true or false

print("i love python".find("love"))
print("i love python".replace("love",'like'))



