n=input();
n=int(n);
Ans_Flag=0;
for itr in range(0,n):
 num=input();
 num=int(num);
 if(num==itr and Ans_Flag==0):
  Ans=num;
  Ans_Flag=1;
if(Ans_Flag==1):
 print(Ans);
else:
 print("No Elements Found"); 
