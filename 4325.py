#unpacking tuple
'''fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)'''
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits#if we add * it take values up to cherry
  
print(green)
print(tropic)
print(red)
a=[1,2,3,4,5,6,7,8,9,10]
a[1]="sai"
a.append("venkat sir")
a.insert(0,"art")
print(a)
a.remove("venkat sir")
print(a)