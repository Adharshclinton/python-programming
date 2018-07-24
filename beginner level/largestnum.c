#include<stdio.h>
int main()
{
  int N[10],temp;
  int i;
  for(i=0;i<10;i++)
  {
    scanf("%d",&N[i]);
  }
  temp=N[0];
  for(i=0;i<10;i++)
  {
    if(N[0]<N[i])
    {
      temp=N[i]);
    }
  }
  printf("the largest number is %d",temp);
}
