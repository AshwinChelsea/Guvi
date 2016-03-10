def SpecialCase(list,mid,list_len,str1,com_len):
 itr=mid;
 while(1):
  temp_str=list[itr];
  if((len(temp_str)>com_len) and (temp_str[0:com_len]==str1)):
    itr-=1;
  else:
   break;
  if(itr<0):
   itr=0;
   break;
 temp_num1=list[itr]+str1;
 temp_num1=int(temp_num1);
 temp_num2=str1+list[itr];
 temp_num2=int(temp_num2);
 if(temp_num1>temp_num2):
  list.insert(itr+1,str1);
 else:
  list.insert(itr,str1);    
def cmp(str1,str2,list,list_len,mid):
 str1_len=len(str1);
 str2_len=len(str2);
 if(str1_len<str2_len):
  itr_len=str1_len;
 else:
  itr_len=str2_len; 
 for str_itr in range(0,itr_len):
  if(str1[str_itr]<str2[str_itr]):
   return 1;
  elif(str1[str_itr]>str2[str_itr]):
   return -1; 
 if(str2_len!=str1_len): 
  SpecialCase(list,mid,list_len,str2,itr_len);
  return 2;
 return 0; 
def BinSearch(list,list_length,str1):
 if(list_length>0):
  start=0;
  end=list_length-1;  
  mid=int((start+end)/2);
  while(start<end):
   mid=int((start+end)/2);   
   cmp_val=cmp(list[mid],str1,list,list_length,mid);
   if(cmp_val==0):
    return 0;
   elif(cmp_val==1):
    end=mid-1;
   elif(cmp_val==-1):   
    start=mid+1;
   else:
    return 1;
  mid=int((start+end)/2);   
  cmp_val=cmp(list[mid],str1,list,list_length,mid);
  if(cmp_val==-1):
   list.insert(mid+1,str1);
   return 1;   
  elif(cmp_val==1): 
   list.insert(mid,str1);
   return 1;
  elif(cmp_val==2):
   return 1;
  else:
   return 0;
 elif(list_length==0):
  list.append(str1);
  return 1;
n=input();
n=int(n);
List=[];
List_Length=0;
for itr in range(0,n):
 num=input();
 if(BinSearch(List,List_Length,num)==1):
  List_Length+=1;
Ans="";
for Str_Itr in List:
 Ans+=Str_Itr;
print(int(Ans)); 