line1 = input().split()
a = int(line1[0])
b = int(line1[1])
c = int(line1[2])


mx = (a+b+abs(a-b))/2
mx = (mx+c+abs(mx-c))/2
print('%d eh o maior'%(mx))