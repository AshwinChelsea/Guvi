#include<stdio.h>
int main()
{
	int rows,columns,i,j,temp;
	scanf("%d",&rows);
	scanf("%d",&columns);
	int *row_list=new int[rows];
	int *column_list=new int[columns];
	for(i=0;i<rows;i++)
	row_list[i]=1;
	for(j=0;j<columns;j++)
	column_list[j]=1;
	for(i=0;i<rows;i++)
	{
		for(j=0;j<columns;j++)
		{
			scanf("%d",&temp);
			if(temp==0)
			{
			  row_list[i]=0;
			  column_list[j]=0;	
			}			
		}
	}
	for(i=0;i<rows;i++)
	{
		for(j=0;j<columns;j++)
		{
	     if(row_list[i]==1 &&column_list[j]==1)	
	     printf("1 ");
	     else
	     printf("0 ");
	    }
	    printf("\n");
    }	 
	return 0;
}
