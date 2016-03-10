def TotalTranslation(input_seq):
 Total_Seq=0;
 input_seq_len=len(input_seq);
 Seq_Itr=0;
 Seq_Stack_Init=[];
 Seq_Stack_Len=[];
 for itr in range(0,input_seq_len):
  Seq_Stack_Init.append(0);
  Seq_Stack_Len.append(1); 
 input_seq_len-=1;
 Seq_Itr+=1;
 while(1):
  while(Seq_Itr>0):
   Next_Start_Pos=Seq_Stack_Init[Seq_Itr-1]+Seq_Stack_Len[Seq_Itr-1];
   Next_Seq_Len=Next_Start_Pos+1;
   if(Next_Seq_Len>input_seq_len):
    break;
   Seq_Stack_Init[Seq_Itr]=Next_Start_Pos;
   Seq_Stack_Len[Seq_Itr]=1;
   Seq_Itr+=1;
   if(Next_Seq_Len==input_seq_len):
    Total_Seq+=1;
    break;   
  while(Seq_Itr>0):   
   Prev_Start_Pos_Start=Seq_Stack_Init[Seq_Itr-1];  
   if(Seq_Stack_Len[Seq_Itr-1]==1 and Prev_Start_Pos_Start+2<=input_seq_len+1):
    num=input_seq[Prev_Start_Pos_Start:Prev_Start_Pos_Start+2];
    num=int(num);
    if(num<=26):
     Seq_Stack_Len[Seq_Itr-1]=2;
     if(Prev_Start_Pos_Start+2>=input_seq_len):
      Total_Seq+=1;
     break;   
   Seq_Itr-=1;         
  if(Seq_Itr<=0):
   break;
 return Total_Seq;    
input_seq=input();
print(TotalTranslation(input_seq));
