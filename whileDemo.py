number=10
while number<=15:
    print(number)
    number+=1
#to control loop execution -->break,continue,else,pass
    print("--------Break--------------")
for i in range(20):
    if i==5:
        break;#stop the loop at 5
    print(i)
print("------Continue----------------")
for x in range(5):
    if x==2:
        continue;#skip 2
    print(x)
 
print("------else----------------")
for y in range(3):
    print(y)
else:
    print("Loop completed")
print("------pass----------------")
for z in range(3):
    if i==1:
        pass#placeholder,does nothing
    print(z)

 

