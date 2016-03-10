def BinSearch(list,list_length,num):
 if(list_length>0):
  start=0;
  end=list_length-1;  
  mid=int((start+end)/2);
  while(start<end):
   mid=int((start+end)/2);
   if(num==list[mid]):
    return 0;      
   elif(num<list[mid]):
    end=mid-1;
   else:
    start=mid+1;
  mid=int((start+end)/2);   
  if(num>list[mid]):
   list.insert(mid+1,num);      
  else: 
   list.insert(mid,num);
  return 1;
 elif(list_length==0):
  list.append(num);
  return 1;
n=input();
n=int(n);
List=[];
List_Length=0;
Ans_List={};
for itr in range(0,n):
 num=input();
 num=int(num);
 if(BinSearch(List,List_Length,num)==1):
  List_Length+=1;
 else:
  Ans_List[str(num)]="";
Ans_Key=Ans_List.keys();
print("DUPLICATES:");
for Num in Ans_Key:
 print(Num);
