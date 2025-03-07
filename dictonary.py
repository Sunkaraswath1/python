#create dictonary
ss={1:"a",2:"b",3:"c",4:"d",5:"e"}
print("dictionary:",ss)
#adding dictonary
ss[6]="f"
print("after adding:",ss)
#updating dictonary
ss[2]="z"
print("after updating:",ss)
#accessing dictonary
print("ss:",ss[2])
#creating nested dictonary
nested_ss={"A":{1:"a",2:"b"},"B":{3:"c",4:"d"}}
print("nested dictonary:",nested_ss)
#accessing dictonary
print("A:",nested_ss["B"])
print("B:",nested_ss["B"][4])
#printing keys
print("keys dictonary:",ss.keys())
print("keys nested dictonary:",nested_ss.keys())
del ss[4]
print("after deleting 5:",ss)
