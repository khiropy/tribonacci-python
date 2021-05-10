def tribonacci(s,n):
    rslt = [None] * n
    rslt[0:3]=s
    if n==0:
       rslt=[]
    elif n==1:
         rslt=s[0:1]
    else:
        for i in range(3, n):
           rslt[i] = rslt[i - 2] + rslt[i - 1] + rslt[i - 3]
    print(rslt)
    return 
