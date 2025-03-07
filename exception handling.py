#arthmetic exception without exception
r=10/0
print(r)
#try except block
try:
    r=10/0
except ZeroDivisionError:
    print("error: cannot divide by zero!")
#without try block
def raise_exception():
    raise ValueError("exception from the method")
raise_exception()
#multiple except blocks
try:
    num=int(input(""))
    r=10/num
except ZeroDivisionError:
    print(" error: cannot divide by zero")
except ValueError:
    print("error: please enter a valid number")
except Exception as e:
    print(" other error is occured:",e)
#throw exception
def negative(number):
   if number>0:
        raise ValueError("error:positive numbers not allow")
negative(-6)
#own exception program
class myexception(exception):
    raise myexception("this is my exception message")
#finally block
finally:
    print("this is executed")
#filenotfound exception
    file=open("non_existing_file.txt","r")
#classnotfound exception
    import nonexistent_module
#IO exception
try:
    with open("readonly_file.txt","r") as file:
        file.write("trying erite readonly mode")
except IOError as e:
    print("IOExecption occured:",e)
#class s:
    def__init__(S):
        S.n="python"
    obj=s()
    print(obj.age)

    
    
