def a_function(string):
    return len(string)
print("length of the string function is:",a_function("function"))
print("length of the string python is:",a_function("python"))

def square(item_list):
    square=[]
    for l in item_list:
        square.append(l**2)
    return square

#for calling the defined function
my_list=[2,3,4]
print(square(my_list))


#default argument
def function(n1,n2=20):
    print("number 1 is:",n1)
    print("number 2 is:",n2)

#calling the function and passinmg only one argument
print("passing only one argument")
function(30)

#calling the function and passing only two argument
print("passing only two argument")
function(30,50)


