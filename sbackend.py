start=int(input("Enter lower limit"))
end=int(input("Enter upper limit"))
dict={}
def prime(start,end):

    for i in range(start,end+1):
     count=0
     for j in range(1,i+1):
        if(i%j==0):
         count=count+1
     if(count==2):
        decimal=bin(i)
        a=str(decimal)
        d={i:a}
        dict.update(d)
     else:
        lst=[]
        for k in range(1,i+1):
            
            if(i%k==0):
                lst.append(k)
                d={i:lst}
                dict.update(d)
    print(dict)      
prime(start,end)          

    
    
            




