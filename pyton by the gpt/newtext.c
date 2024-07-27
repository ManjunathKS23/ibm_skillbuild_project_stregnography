#include<stdio.h>
int main()
{
    int a[9]={77,88,55,77,44,22,33,4,5};
    int i,j;
    //printf("enter the number ");
    //scanf("%d",&n);
    for(i=0;i<=9;i++)
    {
        for(j=1;j<=9;j++)
        {
            if(a[i]==a[j])
            {


                printf("repeted in the position  %d is %d %d is %d",i,a[i],j,a[j]);
                return;
            }
        }

    }


}