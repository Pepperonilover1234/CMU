x = int(input())
z = 12
y = 0
while x <= 12 or x >= 2:
    if x > 12:
        print("//ผิดเงือนไข ให้รับใหม")
        break
    
    for i in range(z):
        
        y += 1 
        ans = x * y
        print (x,"x",y,ans)
    break