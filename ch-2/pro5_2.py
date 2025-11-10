Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> def is_prime(n)
...     if n<=1:
...         return False;
...     for i in range(2,int(n**2)+1)
...         if n % i == 0
...             return False
...             
...     return True
...     
...  start = int(input("enter a staring number :- "))
...  end =  int(input("enter a ending number :- "))
...  
...  print("staring number :- ",start,"ending number :- ",end)
...  
...  for num in range(start,end+1)
...     if is_prime(n)
