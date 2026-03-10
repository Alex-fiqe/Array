n=input()
m=len(n)
n[0].isupper()
h=n[1:-1]
h.isdigit()
if m==8 and n[0] and n[m-1] and h and 100000<=int(h)<=999999:
  print("Yes")
else:
  print("No")
