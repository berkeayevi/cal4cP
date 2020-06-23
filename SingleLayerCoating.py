def amplitudesq(x,y):
    a = ((x-y)/(x+y))**2
    return a
n=1
n1=1.4862
n2=2.8505

I1=amplitudesq(n,n1)
I01= 1 - I1
I21= I01* amplitudesq(n1,n2)
t = I21*amplitudesq(n1,n)
I2 = I21-t

result = I1+ I2- 2*((I1*I2)**(1/2))
print(result)
