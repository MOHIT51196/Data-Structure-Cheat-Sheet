import sys
head="CHEAT SHEET"

#-------------------SPARSE MATRIX CODE-------------------

def sparsemat() :
	prog='''
#include<stdio.h>
#include<conio.h>

void represent(int A[4][4], int m , int n)
{
   int i,j;
   printf("\n\t\n-----MATRIX REPESENTATION-------\n\n");
   for(i=0;i<m;i++)
   {
      printf("\n-------------------------\n|");

    for(j=0;j<n;j++)
    {
    if(A[i][j]==0)
    {	printf("   %d   |",A[i][j]);    }
    else
    {	printf("      |");               }
        }
    }
}


int main()
{
int A[4][4],m,n,s=0,i,j;
clrscr();
printf("\n\nEnter the order m x n of the sparse matrix\n");
scanf("%d %d",&m,&n);
printf("\n\nEnter the elements in the sparse matrix (mostly zeroes) \n\n ");
for(i=0;i<m;i++)
{
 for(j=0;j<n;j++)
 {
  printf("\nEnter the value : >");
  scanf("%d",&A[i][j]);
 }
}

printf("\nThe sparse matrix is given by \n");
 printf("Value i j\n");
 for(i=0;i<m;i++)
{
 for(j=0;j<n;j++)
{
if(A[i][j]==0)
{
    printf("\nAt postion x= %d and y= %d value obtained : > %d",i,j,A[i][j]);
}
}
}
represent(A,m,n);
 printf("\n\nprogrammed by MOHIT MALHOTRA");
 getch();
 return 0;
}
'''
	return prog


#-------------------LINEAR LINKED LIST CODE-------------------

def linearlinklist() :
	prog='''
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

struct node
{
    int info;
    struct node *next;
} *start, *last, *temp;


void insert(int) ;
void del(int,int);
void count();
void disp();
int search(int);
void create();


void main()
{
    char chr='y';
    int val,ch,pos;
    printf("\n\n-------------LINKED LIST------------\n");

    create();

    do
    {
	printf("\n\nChoose one of the following options ...\n\n");
	printf("\n1.INSERT a node in the list");
	printf("\n2.DELETE a node from the list");
	printf("\n3.COUNT the number of nodes in the list");
	printf("\n4.DISPLAY the numerous nodes the list");

	fflush(stdin);
	printf("\n\nEnter a choice : >");
	scanf("%d",&ch);

	switch(ch)
	{
	    case 1  :   printf("\nEnter the value to insert : >");
                    scanf("%d",&val);
                    insert(val);
                    break;

	    case 2  :   printf("\nEnter the value to delete : >");
                    scanf("%d",&val);
                    printf("\n\nEnter the position from where you want to delete \n(IF NOT KNOWN PRESS '0' IT WILL SEARCH THE ELEMENT AUTOMATICALLY)");
                    scanf("%d",&pos);
                    del(val,pos);
                    break;

	    case 3  :   printf("\nPress any key to count the number of nodes ......\n");
                    getch();
                    count();
                    break;

	    case 4  :   printf("\nPress any key to display the nodes ........");
                    getch();
                    disp();
                    break;

	    default  :  printf("\n\n\t[!] INVALID REQUEST ");


	}

      fflush(stdin);

      printf("\n\nDO YOU WANT TO CONTINUE (Y/N) : > ");
      scanf("%s",&chr);

      //printf("\nchoice is %s",chr);


    }while(chr=='y'||chr=='Y');

    getch();
}

//-------------------INITIATION CODE---------------------

void create()
{
    start=last=NULL;
}

//-------------------INSERTION CODE---------------------

void insert(int val)
{
    temp=(struct node *)malloc(sizeof(struct node));
    temp->info=val;
    temp->next=NULL;

    if(start==NULL)
    {
	start=last=temp;
	printf("\n\n\t[*] FIRST NODE INSERTION SUCCESSFULL");
    }

    else
    {
	last->next=temp;
	last=temp;
	printf("\n\n\t[*] NODE INSERTION SUCCESSFULL");
    }

 return;
}

//-------------------SEARCHING CODE---------------------

int search(int val)
{
    int pos,i;

    if(start==NULL)
    {
	printf("\n\n\t[!] ERROR ! NO NODE EXIST\n(node counter stays at ZERO)");
	return -1 ;
    }

    else
    {
	    printf("\nSearching.............");
	    for(temp=start,i=1;temp!=NULL&&temp->info!=val;temp=temp->next,i++);

	    if((temp!=NULL)&&(temp->info==val))
	     {
		printf("\n[*] VALUE DETECTED AT POSTION : > %d",i);
		pos=i;
	     }

	    else
		pos=-1;
    }

    return pos;
}

//-------------------DELETEION CODE---------------------

void del(int val, int pos)
{
    int i;
    struct node *p, *q;

    if(start==NULL)
    {
	if(start==NULL)
	printf("\n\n\t[!] ERROR ! NO NODE EXIST\n(node counter stays at ZERO)");
	return;
    }

    if(pos==0)
	    pos=search(val);

    if(pos!=-1)
    {

	for(p=q=start,i=1;(p!=NULL&&p->info!=val),i!=pos;p=p->next,i++)
			    q=p;

	if(p->info!=val)
    {
        printf("\n\n\t[!] POSITION N VALUE DOESNT MATCH");
        return;
    }

    if(p==start)
     {
             start=start->next;
             printf("\n\n\t[*] DELETION OF NODE SUCCESSFULL");
             return;
     }

	else
    {
            if((p!=NULL)&&(i==pos))
         {
             q->next=p->next;
             printf("\n\n\t[*] DELETION OF NODE SUCCESSFULL");
             return;
         }

        else
            printf("\n\n\t[!] ERROR ! NO SUCH VALUE EXIST....");

        }
    }
    else
	printf("\n\n\t[!] ERROR ! NO SUCH VALUE EXIST....");

}

//-------------------NODE COUNTING CODE---------------------

void count()
{
    int counter=0;
    if(start==NULL)
     {
	 printf("\n\n\t[!] ERROR ! NO NODE EXIST\n(node counter stays at ZERO)");
	return;
     }

    printf("\nCounting the nodes.........");
    for(temp=start;temp!=NULL;temp=temp->next)
	    counter++;

    printf("\nNUMBER OF NODES IN THE LINKED LIST : > %d",counter);

}
//-------------------LIST DISPLAY CODE---------------------

void disp()
{
    if(start==NULL)
    {    printf("\n\n\t[!] ERROR ! NO NODE EXIST\n(node counter stays at ZERO)");
	return;
    }
    printf("\n");
    for(temp=start;temp!=NULL;temp=temp->next)
        printf("[ %d ] -->",temp->info);

}
'''
	return prog



#-------------------DOUBLY LINKED LIST CODE-------------------

def dblylinklist() :
	prog='''
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

/*
programmed by MOHIT MALHOTRA
*/

//SELF REFERENTIAL STRUCTURE

struct dlist
{
    int a;
    struct dlist *prev;
    struct dlist *next;
};

struct dlist *temp,*last,*start;

void insert();
void dlt();
void disp();
void insert_beg(struct dlist*);
void insert_bet(struct dlist*);
void insert_end(struct dlist*);


void main()
{
   int ch;
   //start=last=NULL;
   do
   {

       printf("\n\nPROGRAM FOR DOUBLY LINK LIST\n\n");
       printf("\n1.INSERT a node in the list");
       printf("\n2.DISPLAY all the nodes from the list");
       printf("\n3.DELETE a node from the list");
       printf("\n4.COUNT the nodes from the list");
       printf("\n5.EXIT the program now");
       printf("\n\nEnter the choice to perform : > ");
       scanf("%d",&ch);

       switch(ch)
       {
           case 1:      insert();
                        break;
           case 2:      disp();
                        break;
           case 3:      dlt();
                        break;
//           case 4:      count();
  //                      break;
           case 5:      exit(0);

       }

    fflush(stdin);
   }while(ch<5);

   free(temp);
getch();
}


void insert()
{   int val,pch;
    char chr;
    //struct dlist *temp;
    do
   {

    printf("\nEnter a value for the node : > ");
    scanf("%d",&val);

    //allocating the memory a new node
    temp= (struct dlist *)malloc(sizeof(struct dlist));
    temp->a=val;
    temp->next=NULL;
    temp->prev=NULL;

    if(start==NULL)   //for checking if list exist or not
    {   start=last=temp;
        printf("\nLinklist's first node is created....");
    }
    else
    {
        printf("\n1.To perform insertion at the beginning");
        printf("\n2.To perform insertion at the end");
        printf("\n3.To perform insertion in between the node");
        printf("\n\nEnter a choice to perform : > ");
        scanf("%d",&pch);

        if(pch==1)      insert_beg(temp);
        else if(pch==2) insert_end(temp);
        else if(pch==3) insert_bet(temp);
        else            printf("\n[!]INVALID ENTRY....");

    }

    fflush(stdin);
    printf("\n\nDo you wanna create more nodes (Y/N) : >");
    scanf("%s",&chr);

  }while(chr=='y'||chr=='Y');
return;

}//end of the insert function

void insert_end(struct dlist *temp)
{
        last->next=temp;
        temp->prev=last;
        last=temp;
        return;

}
void insert_beg(struct dlist *temp)
{
         temp->next=start;
         start->prev=temp;
         start=temp;
         return;
}

void insert_bet(struct dlist *temp)
{
        int pos;
        struct dlist *p;
        printf("\nEnter a position at which node should be inserted : > ");
        scanf("%d",&pos);
        int i;
        //to traverse through the list and reach the position
        for(p=start,i=1;p!=NULL&&i!=pos;p=p->next,i++);

        temp->next=p;
        temp->prev=p->prev;
        p->prev->next=temp;
        p->prev=temp;
        return;
}

void disp()
{   int pch;

    if(start==NULL)  printf("\n\n[!] NO NODE IS PRESENT ,ITS A EMPTY LINKLIST.....");
    else
    {
        printf("\n1.DISPLAY the nodes of the list in a ascending order");
        printf("\n2.DISPLAY the nodes of the list in a descending order");
        printf("\n\nEnter a choice to perform : > ");
        scanf("%d",&pch);

        if(pch==1)
        {   printf("\nELEMENTS OF DOUBY LINK LIST IN ASCENDING ORDER ARE : \n");
            for(temp=start;temp!=NULL;temp=temp->next)
            printf("\n%d",temp->a);
        }

        else if(pch==2)
        {   printf("\nELEMENTS OF DOUBY LINK LIST IN DESCENDING ORDER ARE : \n");
            for(temp=last;temp!=NULL;temp=temp->prev)
            printf("\n%d",temp->a);

        }
        else printf("\n[!]INVALID ENTRY....");

    }
 return;
}//end of display function

void dlt()
{   int pch,val;
    char c;
     do
   {

    printf("\nEnter a value for the node to delete : > ");
    scanf("%d",&val);

    struct dlist *p;

    if(start==NULL)   //for checking if list exist or not
    {
        printf("\nThere isnt any node delete from the list....");
    }
    else
    {
        printf("\n1.To perform deletion at the beginning");
        printf("\n2.To perform deletion at the end");
        printf("\n3.To perform deletion of any node in between the list ");
        printf("\n\nEnter a choice to perform : > ");
        scanf("%d",&pch);

        if(pch==1)
        {
           start=start->next;
           start->prev=NULL;
        }
        else if(pch==2)
        {
           last=last->prev;
           last->next=NULL;
        }
        else if(pch==3)
        {
            printf("\nEnter the value of the node : > ");
            scanf("%d",&val);

            //to traverse to that position in the list
            for(temp=start;temp->a!=val;p=p->next);

            temp->prev->next=temp->next;
            temp->next->prev=temp->prev;
        }

        else            printf("\n[!]INVALID ENTRY....");

    }
    free(p);

    printf("\nDo you wanna delete more nodes (Y/N) : >");
    scanf("%c",&c);

  }while(c!='n'||c!='N');

return;

}//end of the delete function

'''
	return prog

#-------------------1D MATRIX MENU CODE-------------------

def oneDarrays() :
	prog='''
 #include <stdio.h>
#include <conio.h>
#include <process.h>
# define s 5

void create(int);
void insert(int,int,int,int);
void del(int,int,int);
void disp(int,int);

void create(int A[])
{
   for(int i=1;i<=s;i++)
  {
  printf("\n Enter the element at position %d in the array : >",i);
  scanf("%d",&A[i]);

  }//end of the loop

printf("\nARRAY CREATED\n\n");

} //end of create func

void insert(int A[],int &size,int num,int pos)
{       size=size+1;
    for(int i=pos;i<=size;i++)
    A[i+1]=A[i];

    A[pos]=num;

} //end of insert func

void del(int A[],int &size,int val,int pos)
{       int count=0;
    for(int i=1;i<=size;i++)
   {
    if(A[pos]==val)
     {
    size=s-1;
    count++;
    for(int j=pos;j<=s-1;j++)
    A[j]=A[j+1];
      }
    }//end of the loop

    if(count!=0)    printf("\n Deleted value is %d",val);
    else 		printf("\nElement not found");

} //end of delete func

void disp(int A[],int size)
{
 printf("\nElements of the array are : >\n");
 for(int i=1;i<=size;i++)   printf("%d \n",A[i]);


} //end of display func

void main()
{  clrscr();
   int A[s],ch,val,pos,size=5;
do
{
   printf("\n\n----------ARRAY PROGRAM----------\n\n");
   printf("\n1. To create an array");
   printf("\n2. To insert the values in an array");
   printf("\n3. To delete a value from an array");
   printf("\n4. To display the resultant array");
   printf("\n5. To exit the program");
   printf("\n\nEnter your choice : >");
   scanf("%d",&ch);

   switch(ch)
 {
   case 1: printf("\nFor creating the array : \n");
       create(A);
       break;

   case 2: printf("\nEnter the value to insert in the array : >");
       scanf("%d",&val);
       printf("\nEnter the position where the value is to be entered : >");
       scanf("%d",&pos);
       insert(A,size,val,pos);
       break;

   case 3:  printf("\nEnter the value to be deleted from an array : >");
        scanf("%d",&val);
        printf("\nEnter the pos of element to delete from an array: >") ;
        scanf("%d",&pos);       //in case there are multiple elements with same values
        del(A,size,val,pos);
        break;

   case 4:   printf("To display the elements of the resultant array : >");
         disp(A,size);
         break;

   case 5: exit(0);
 }



}while(ch<5);

getch();
}	'''
	return prog


#-------------------2D MATRIX MENU CODE-------------------

def twoDarrays() :
	prog=''' 
 #include<iostream.h>
#include<conio.h>
void main()
{ int ch;char cont='y';
while(cont=='y'||cont=='Y')
{
cout<<"1.sum up 2 array in third array"<<endl;
cout<<"2.display row elements of array"<<endl;
cout<<"3.display column elements of array"<<endl;
cout<<"4.display sum of row elements"<<endl;
cout<<"5.display sum of column elements"<<endl;
cout<<"6.display diagonal elements of matrix"<<endl;
cout<<"7.display multiplication of two matrix"<<endl;
cout<<"8.display transpose of the matrix"<<endl;
cout<<"9.display elements of lower and upper triangle"<<endl;
cout<<"10.display sum of diagonal elements"<<endl;

cout<<"enter your choice-";
cin>>ch;
switch(ch)
{
case 1:

int A[2][2],B[2][2],C[2][2],p,b;
cout<<"enter the rows of matrix-";
    cin>>p;
cout<<"enter columns of marix-";
    cin>>b;
cout<<"enter the first matrix"<<endl;
    for(int k=0;k<p;k++)
{  	for(int m=0;m<b;m++)
{	cin>>A[k][m];
    cout<<endl;         }
                 }
}
cout<<"enter the second matrix"<<endl;
    for(k=0;k<p;k++)
{  	for(m=0;m<b;m++)
{	cin>>B[k][m];
    cout<<endl;          }
                }

    for(int i=0;i<p;i++)
{ 	for(int j=0;j<b;j++)
{	C[i][j]=A[i][j]+B[i][j];    }
                    }
    for(i=0;i<b;i++)
{ 	cout<<endl;
    for(j=0;j<b;j++)
{	cout<<C[i][j]<<'\t';        }
                    }
break;

case 2:

int A[2][2],u;
cout<<"enter the size of square matrix-";
    cin>>u;
    for(int i=0;i<u;i++)
{    	for(int j=0;j<u;j++)
{     	cin>>A[i][j];              }
                     }
    for(i=0;i<u;i++)
{ 	cout<<"element of"<<i<<"row are-"<<endl;
    for(j=0;j<u;j++)
{	cout<<A[i][j]<<endl;      }
                     }
break;

case 3:

int A[2][2],k;
cout<<"enter size of square matrix-";
    cin>>k;
    for(int i=0;i<k;i++)
{ 	for(int j=0;j<k;j++)
{	cin>>A[i][j];
    cout<<endl;              }
                     }

    for(i=0;i<k;i++)
{ 	cout<<"element of"<<i<<"column are-"<<endl;
    for(j=0;j<k;j++)
{	cout<<A[j][i]<<endl;      }
                     }
break;

case 4:

int A[2][2],l,sr=0;
cout<<"enter the size of square matrix-";
    cin>>l;
    for(int i=0;i<l;i++)
{ 	for(int j=0;j<l;j++)
{	cin>>A[i][j];              }
                      }
for (i=0;i<l;i++)
{       cout<<endl;
    for(j=0;j<l;j++)
{	sr=sr+A[i][j];
    cout<<"sum of"<<i<<"row elements-"<<sr;
                   }
                      }
break;

case 5:

int A[2][2],r,sc=0;
cout<<"enter the size of square matrix-";
    cin>>r;
    for(int i=0;i<r;i++)
{	for(int j=0;j<r;j++)
{	cin>>A[i][j];       	   }
                      }
    for(i=0;i<r;i++)
{	for(j=0;j<rj++)
{  	sc=sc+A[j][i];;
    cout<<"sum of"<<i<<"column elements-"<<sc;
                   }
                      }
break;

case 6:

int A[3][3],a;
cout<<"enter the size of the square matrix-";
    cin>>a;
    for(int i=0;i<a;i++)
{	for(int j=0;j<a;j++)
{ 	cin>>A[i][j];              }
                      }
cout<<"elements of left diagonal are-"<<endl;
    for(i=0;i<a;i++)
{ 	for(j=0;j<a;j++)
{ 	if(i==j)
    cout<<A[i][j]<<endl;             }
                      }
cout<<"elements of the right diagonal are-"<<endl;
    for(i=0;i<a;i++)
{	for(j=0;j<aj++)
{ 	if((i+j)==(a+1))
    cout<<A[i][j]<<endl;     	   }
                      }
break;

case 7:

int A[3][3],B[3][3],C[3][3],m,n,p,q;
cout<<"enter number of rows of matrix-";
    cin>>m;
    cout<<endl;
cout<<"enter number of columns of matrix-";
    cin>>n;
    cout<<endl;
cout<<"enter first matrix-"<<endl;
    for(int i=0;i<m;i++)
{ 	for(int j=0;j<n;j++)
{ 	cin>>A[i][j];                }
                        }
cout<<"enter number of rows of second matrix-";
    cin>>p;
cout<<endl;
cout<<"enter number of columns of second matrix-";
    cin>>q;
cout<<endl;
    for(i=0;i<p;i++)
{ 	for(j=0;j<q;j++)
{       cin>>B[i][j];                }
                         }
cout<<"resultant matrix is-"<<endl;
for(i=0;i<m;i++)
{  cout<<endl;
for(j=0;j<q;j++)
{  	if(n==p)
    C[i][j]=(A[i][j]*B[i][j])+(A[i][j+1]*B[i+1][j]);
    cout<<C[i][j]<<'\t';
                   }
                      }
break;

case 8:

int A[3][3],m,n;
cout<<"enter the number of rows of matrix-";
    cin>>m;
cout<<"enter number of column of matrix-";
    cin>>n;
cout<<"enter the matrix elements-";
    for(int i=0;i<m;i++)
{ 	for(int j=0;j<n;j++)
{ 	cin>>A[i][j];		   }
                      }
cout<<"provided matrix-"<<endl;
    for(i=0;i<m;i++)
{ 	cout<<endl;
    for(j=0;j<n;j++)
{ 	cout<<A[i][j]<<'\t';       }
                      }
cout<<"transpose of provided matrix-"<<endl;
    for(i=0;i<m;i++)
{  	cout<<endl;
    for(j=0;j<n;j++)
{ 	cout<<A[j][i]<<'\t';       }
                      }
break;
case 9:

int A[3][3],m;
cout<<"enter size of square matrix-";
    cin>>m;
    for(int i=0;i<m;i++)
{ 	for(int j=0;j<m;j++)
{ 	cin>>A[i][j];          	   }
                      }
cout<<"elements of upper triangle are-"<<endl;
    for(i=0;i<m;i++)
{ 	for(j=0;j<m;j++)
{   	if(i<j)
{ 	cout<<A[i][j]<<endl;    }
                   }
                      }
cout<<"elements of lower triangle-"<<endl;
    for(i=0;i<m;i++)
{ 	for(j=0;j<m;j++)
{   	if(i>j)
{ 	cout<<A[i][j]<<endl;    }
                   }
                      }
break;
case 10:

int A[3][3],w,dr=0,dc=0;
cout<<"enter the size of square matrix-";
    cin>>w;
cout<<"enter elements of matrix-"<<endl;
    for(int i=0;i<w;i++)
{ 	for(int j=0;j<w;j++)
{ 	cin>>A[i][j];               }
                      }
    for(i=0;i<w;i++)
{ 	for(j=0;j<w;j++)
{ 	if(i==j)
{  	dr=dr+A[i][j];          }
    else if((i+j)=(w+1))
{  	dc=dc+A[i][j];          }
    else
{  	dr=0;dc=0;              }
                    }
                      }
cout<<"sum of right diagonal elements is-"<<dc;
cout<<"sum of left diagonal elements is-"<<dr;
    break;

}//end of switch case


cout<<"do you wanna continue (y/n)";
cin>>cont;
}//end of while


getch();
}//end of main function       '''

	return prog
		
#-------------------SELECTION SORT CODE-------------------

def selectsort() :
	prog='''
/* **********************PROGRAM FOR SELCTION SORT**********************
******************************************************************    */


#include <stdio.h>
#include <conio.h>
#define N 50


void select_sort(int A[],int size)
{
    int small,pos,i,j,temp;

    for(i=0;i<size-1;i++)
    {
        small=A[i];
        pos=i;

        for(j=i+1;j<size;j++)
        {
            if(small>A[j])
            {
                small=A[j];  pos=j;
            }
        }

        if(pos!=i)
        {
        // swaping of the two numbers

        temp=A[pos];
        A[pos]=A[i];
        A[i]=temp;
        }
    }

    printf("\n\n-------------AFTER SORTING-------------\n\n");

    for(i=0;i<size;i++)
        printf("\nThe value at %d is : > %d",i,A[i]);
   
   printf("\n\n\nTASK SUCCESSFUL.....");
   printf("\n\nprogrammed by MOHIT MALHOTRA");

    return;
}

int main()
{
    int A[N],i,n;
    clrscr();
    printf("\n\n-----------SELECTION SORT-------------\n\n");


    printf("Enter the size of the array: >");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("\nEnter the value at %d : > ",i);
        scanf("%d",&A[i]);
    }

    printf("\n\npress any key to initiate sorting...\n");
    getch();

    printf("\n\n-------------BEFORE SORTING-------------\n\n");
    for(i=0;i<n;i++)
        printf("\nThe value at %d is : > %d",i,A[i]);

    printf("\n\nSorting.........\n\n");
    select_sort(A,n);

    getch();
    return 0;
}
'''
	return prog

#-------------------INSERTION SORT CODE-------------------

def insertsort() :
	prog='''
/* **********************PROGRAM FOR INSERTION SORT**********************
******************************************************************    */

#include <stdio.h>
#include <stdlib.h>
#define N 20

void insert_sort(int A[],int size)
{
    int temp, i, j;

    for(i=0;i<size;i++)
    {
        temp=A[i];
        j=i-1;

        while((temp<A[j])&&(j>=0))
        {
            A[j+1]=A[j];
            j=j-1;
        }

        A[j+1]=temp;
    }

    printf("\n\n-------------AFTER SORTING-------------\n\n");

    for(i=0;i<size;i++)
        printf("\nThe value at %d is : > %d",i,A[i]);

    printf("\n\n\nTASK SUCCESSFUL.....");
    printf("\n\nprogrammed by MOHIT MALHOTRA");
    return;
}

int main()
{
    int A[N],i,n;
    printf("\n\n-----------INSERTION SORT-------------\n\n");


    printf("Enter the size of the array: >");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    printf("\nEnter the value at %d : > ",i);
    scanf("%d",&A[i]);
    }

    printf("\n\npress any key to initiate sorting...\n");
    getch();

    printf("\n\n-------------BEFORE SORTING-------------\n\n");
    for(i=0;i<n;i++)
    printf("\nThe value at %d is : > %d",i,A[i]);

    printf("\n\nSorting.........\n\n");
    insert_sort(A,n);

    getch();
    return 0;

}
'''

	return prog

#-------------------MERGE SORT CODE-------------------

def mergesort() :
	prog='''
                /* **********************PROGRAM FOR MERGE SORT**********************
                ******************************************************************    */

                #include <stdio.h>
                #include <stdlib.h>
                #define N 20

                int temp [N];       //TO IGNORE THE SEGMENTATION FAULTS

                void partition(int a[], int low, int high)
                {
                    int mid=(low+high)/2;

                    if(low<high)
                    {
                    partition(a,low,mid);
                    partition(a,mid+1,high);
                    mergesort(a,low,mid,high);
                    }
                }

                void mergesort(int A[],int low,int mid,int high)
                {
                    int i,mi,lo,k;
                    mi=mid+1;
                    lo=low;
                    i=low;


                    while((low<=mid)&&(mi<=high))
                    {
                    if(A[lo]<=A[mi])
                    {
                        temp[i]=A[lo];
                        lo++;
                    }
                    else
                    {
                        temp[i]=A[mi];
                        mi++;
                    }
                    i++;
                    }

                    if(lo>mid)
                    {
                    for(k=mi;k<=high;k++)
                    {
                        temp[i]=A[k];
                        i++;
                    }
                    }

                    else
                    {
                    for(k=lo;k<=mid;k++)
                    {
                        temp[i]=A[k];
                        i++;
                    }
                    }

                    for(k=low;k<=high;k++)
                    A[k]=temp[k];

                  return;

                }


                int main()
                {
                    int A[N],i,n;
                    printf("\n\n-----------MERGE SORT-------------\n\n");


                    printf("Enter the size of the array: >");
                    scanf("%d",&n);

                    for(i=0;i<n;i++)
                    {
                    printf("\nEnter the value at %d : > ",i);
                    scanf("%d",&A[i]);
                    }

                    printf("\n\npress any key to initiate sorting...\n");
                    getch();

                    printf("\n\n-------------BEFORE SORTING-------------\n\n");
                    for(i=0;i<n;i++)
                    printf("\nThe value at %d is : > %d",i,A[i]);

                    printf("\n\nSorting.........\n\n");
                    partition(A,0,n-1);

                    printf("\n\n-------------AFTER SORTING-------------\n\n");

                    for(i=0;i<n;i++)
                    printf("\nThe value at %d is : > %d",i,A[i]);

                    printf("\n\n\nTASK SUCCESSFUL.....");
                    printf("\n\nprogrammed by MOHIT MALHOTRA");

                    getch();
                    return 0;
                }
	'''

	return prog

#-------------------RADIX SORT CODE-------------------

def radixsort() :
	prog='''
/* **********************PROGRAM FOR RADIX SORT**********************
******************************************************************    */

#include <stdio.h>
#include <stdlib.h>
#define  N  30


int length_detect(int a [], int n)
{
    int i,max=a[0],count=0;

    for(i=0;i<n;i++)
    {
        if(max<a[i])    max=a[i];
    }

    do
    {
    count++;
    max=max/10;

    } while(max!=0);

return count ;
}

void radix_sort(int A[],int size)
{
    int C[N],small, pos,temp, i, j, k, length;

    length=length_detect(A,size);
    //printf("\nLENGTH OF THE ELEMENT : %d\n",length);

    for(i=0;i<size;i++)
        C[i]=A[i];

    for(k=1;k<=length;k++)
    {
       for(i=0;i<size;i++)
       {
       small=A[i]%10;
       pos=i;

       for(j=i+1;j<size;j++)
       {
           if(small>A[j])
           {    small=A[j]%10;
            pos=j;
           }
       }
       if(pos!=i)
       {
           temp=A[pos];
           A[pos]=A[i];
           A[i]=temp;

           temp=C[pos];
           C[pos]=C[i];
           C[i]=temp;
       }

       }

       for(i=0;i<size;i++)
       {
       A[i]=A[i]/10;
       }
    }


    printf("\n\n-------------AFTER SORTING-------------\n\n");

    for(k=0;k<size;k++)
    printf("\nThe value at %d is : > %d",k,C[k]);

   printf("\n\n\nTASK SUCCESSFUL.....");
   printf("\n\nprogrammed by MOHIT MALHOTRA");

   return;
}

int main()
{
    int A[N],i,n;
    clrscr();
    printf("\n\n-----------RADIX SORT-------------\n\n");


    printf("Enter the size of the array: >");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    printf("\nEnter the value at %d : > ",i);
    scanf("%d",&A[i]);
    }

    printf("\n\npress any key to initiate sorting...\n");
    getch();

    printf("\n\n-------------BEFORE SORTING-------------\n\n");
    for(i=0;i<n;i++)
    printf("\nThe value at %d is : > %d",i,A[i]);

    printf("\n\nSorting.........\n\n");
    radix_sort(A,n);

    //printf("\n\n\nTASK SUCCESSFUL.....");

    getch();
    return 0;
}
'''
	return prog

#-------------------SHELL SORT CODE-------------------

def shellsort() :
	prog='''
/* **********************PROGRAM FOR SHELL SORT**********************
******************************************************************    */

#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#define N 30


void shell_sort(int a[],int size)
{
    int i=0,j=0,k=0,temp;

    for(k=size/2;k>0;k/=2)
    {
        for(j=k;j<size;j++)
        {
            for(i=j-k;i>=0;i-=k)
            {
                if(a[i+k]<a[i])
                   {
                       temp=a[i+k];
                       a[i+k]=a[i];
                       a[i]=temp;
                   }
                else
                    break;
            }
        }
    }


}


int main()
{
    int A[N];
    printf("\n\n-----------RADIX SORT-------------\n\n");
    int i,n;

    printf("Enter the size of the array: >");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        printf("\nEnter the value at %d : > ",i);
        scanf("%d",&A[i]);
    }

    printf("\n\npress any key to initiate sorting...\n");
    getch();

    printf("\n\n-------------BEFORE SORTING-------------\n\n");
    for(i=0;i<n;i++)
        printf("\nThe value at %d is : > %d",i,A[i]);

    printf("\n\nSorting.........\n\n");

    shell_sort(A,n);

    printf("\n\n-------------AFTER SORTING-------------\n\n");
    for(i=0;i<n;i++)
        printf("\nThe value at %d is : > %d",i,A[i]);

    printf("\n\n\nTASK SUCCESSFUL.....");
    printf("\n\n\nprogrammed by MOHIT MALHOTRA");

    getch();
    return 0;
}
'''

	return prog


#-------------------HEAP SORT CODE----------------------

def heapsort() :
	prog='''
/* **********************PROGRAM FOR HEAP SORT**********************
******************************************************************    */

#include <stdio.h>
void main()
{
	int heap[10], no, i, j, c, root, temp;
	printf("\n\n----------- HEAP SORT ------------\n\n");
	printf("\n Enter no of elements :");
	scanf("%d", &no);
	printf("\n Enter the noumbers one by one .........\n ");
	for (i = 0; i < no; i++)
	{
	    printf("\nElement at %d is : >  ",i);
	    scanf("%d",&heap[i]);
	}
	for (i = 1; i < no; i++)
	{
		c = i;
		do
		{
			root = (c - 1) / 2;
                if (heap[root] < heap[c])   /* to create MAX heap array */
			{
				temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			c = root;
		} while (c != 0);
	}
	printf("\n\n-------------BEFORE SORTING-------------\n\n");
	for (i = 0; i < no; i++)
		printf("%d\t ", heap[i]);
	for (j = no - 1; j >= 0; j--)
	{
		temp = heap[0];
            heap[0] = heap[j];    /* swap max element with rightmost leaf element */
		heap[j] = temp;
		root = 0;
		do
		{
                c = 2 * root + 1;    /* left node of root element */
			if ((heap[c] < heap[c + 1]) && c < j-1)
				c++;
                if (heap[root]<heap[c] && c<j)    /* again rearrange to max heap array */
			{
				temp = heap[root];
				heap[root] = heap[c];
				heap[c] = temp;
			}
			root = c;
		} while (c < j);
	}
	printf("\n\n-------------AFTER SORTING-------------\n\n");
	for (i = 0; i < no; i++)
		printf("\t %d", heap[i]);
		printf("\n\n\nTASK SUCCESSFUL.....");
	printf("\n\n Complexity : \n Best case = Avg case = Worst case = O(n logn) \n");
	getch();
}
'''

	return prog


#-------------------QUICK SORT CODE-------------------

def quicksort() :
	prog='''
/* **********************PROGRAM FOR QUICK SORT**********************
******************************************************************    */

#include <stdio.h>
#include <stdlib.h>
#define N 30


void quick_sort(int A[],int lb,int ub)
{
    int pivot=A[lb];
    int i=lb+1,j=ub,temp;

    if(lb<ub)
    {
        while(i<j)
        {
            while(A[i]<pivot)   i++;
            while(A[j]>pivot)   j--;

            if(i<j)
            {
                temp=A[i];
                A[i]=A[j];
                A[j]=temp;
            }
        }

        // SWAPING THE PIVOTAL VALUE AT THE END
        temp=A[j];
        A[j]=A[lb];
        A[lb]=temp;

        // SORTING THE LEFT SEGMENT
        quick_sort(A,lb,j-1);

        // SORTING THE RIGHT SEGMENT
        quick_sort(A,j+1,ub);
    }
return;
}

int main()
{
    int A[N], i, n;
    clrscr();
    printf("\n\n-----------QUICK SORT-------------\n\n");


    printf("Enter the size of the array: >");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
    printf("\nEnter the value at %d : > ",i);
    scanf("%d",&A[i]);
    }

    printf("\n\npress any key to initiate sorting...\n");
    getch();

    printf("\n\n-------------BEFORE SORTING-------------\n\n");
    for(i=0;i<n;i++)
    printf("\nThe value at %d is : > %d",i,A[i]);

    printf("\n\nSorting.........\n\n");
    quick_sort(A,0,n-1);

    printf("\n\n-------------AFTER SORTING-------------\n\n");

    for(i=0;i<n;i++)
    printf("\nThe value at %d is : > %d",i,A[i]);

    printf("\n\n\nTASK SUCCESSFUL.....");
    printf("\n\nprogrammed by MOHIT MALHOTRA");

    getch();
    return 0;
}
'''
	return prog


#-------------------SORTING MENU CODE-------------------

def sorting() :
	print'''\n\n------------SORTING ALGORITHMS----------------\n\n
	1.SLECTION SORTING 
    	2.INSERTION SORTING 
    	3.MERGE SORTING
    	4.RADIX SORTING
	5.QUICK SORT
	6.SHELL SORTING
	7.HEAP SORT'''
	sh= input( "\n\nEnter the project number you want to generate : >  ")

	if sh==1 :
		sortcode=selectsort()
	elif sh==2 :
		isortcode=nsertsort()
	elif sh==3 :
		sortcode=mergesort()
	elif sh==4 :
		sortcode=radicsort()
	elif sh==5 :
		sortcode=quicksort()
	elif sh==6 :
		sortcode=shellsort()
	elif sh==7:
		sortcode=heapsort()
	else :
		print "\n[!] INVALID REQUEST"

	return sortcode

#-------------------LINEAR QUEUE CODE-------------------

def lqueues() :
	prog='''

#include<stdio.h>
#include<conio.h>
#include<process.h>
#define N 5

void insert(int);
void delet();
void print();
void count();

struct queue
{
int a[N];
int front;
int rear;
}q;


void main()
{
 int ch,val;
 char ch1;
 q.front=-1;
 q.rear=-1;

 clrscr();

do{
 clrscr();
 printf("
--------QUEUE PROGRAM--------

");
 printf("
1.To Insert in the queue");
 printf("
2.To Delete a value from the queue");
 printf("
3.To Print the resultant queue");
 printf("
4.To Count the elements of queue");
 printf("
5.To Exit the program");
 printf("

Enter your choice : > ");
 scanf("%d",&ch);

switch(ch)
  {
    case 1:	printf("
Enter the value which is to be inserted : > ");
        scanf("%d",&val);
        insert(val)	;
        break;

    case 2:	delet();
        break;

    case 3:	print();
        break;

    case 4:	count();
        break;

    case 5:	exit(0);

    default: printf("
Invalid entry");

    }

 printf("
Do you wish to continue(y/n) : > ");
 scanf("%s",&ch1);
}while(ch1=='y'||ch1=='Y');

getch();
}

 void insert(int val)
 {

    if(q.rear==N-1)	printf("
Queue Full");

    else		q.a[++(q.rear)]=val;
 }    //end of insert func

 void delet()
 {
   if(q.front==q.rear) 	printf("
Queue Empty");

   else
        printf("
The deleted element is :> %d",q.a[++(q.front)]);
 }    //end of delete func


 void print()
 {
   if(q.front==q.rear)    printf("
Queue is Empty");

   else
    {  int i;
      printf("
The elements of the queue are: >
");

      for(i=(q.front+1);i<=q.rear;++i)
      printf("%d
",q.a[i]);
    }
 } //end of print func

 void count()
 {
    int c;

   if(q.front==q.rear)	  printf("
Queue is Empty");

   else
    {
       c=q.rear-q.front;
       printf("
The number of elements in the queue are : > %d",c);
    }
 } //end of count func		'''

	return prog


#-------------------CIRCULAR QUEUE CODE-------------------

def cqueues() :
	prog='''//------------------------------------------------------------------CIRCULAR QUEUE---------------------------------------------------------------

#include<conio.h>
#include<stdio.h>
#define N 5

int val;

struct queue
{
	int a[N];
	int front,rear;
}q;

void insert(int val)
{
	if(q.front==(q.rear+1)%N)
        printf("\n\t[!] QUEUE IS FULL");
	else
	{
        q.a[q.rear]=val;
        q.rear=((q.rear+1)%N);
        printf("\n\t[!] INSERTION TASK SUCCESSFUL\n");
    }
}

void delet()
{
	if(q.front==q.rear)
		printf("\n\t[!] QUEUE IS EMPTY");
	else
		{

         printf("\nVALUE DELETED : > %d",q.a[q.front]);
         q.front=(q.front+1)%N;
         printf("\n\t[!] DELETION TASK SUCCESSFUL\n");
        }
}


void print()
{
	int i;
    if(q.front==q.rear)
	{
	    	printf("\n\t[!] QUEUE IS EMPTY");
	    	return;
	}
    printf("The elements of CIRCULAR QUEUE are : \n\n");
	for(i=q.front;i<=q.rear-1;i=(i+1)%N)
            printf("%d\n",q.a[i]);

}


void main()
{
	int a,p;
	char s;

	q.front=q.rear=0;
	do{

	printf("\n\n-------------CIRCULAR QUEUE---------------\n\n");

    printf("\nSelect the operation you want to perfom(1/2/3/4) :\n");
    printf("\n1.PUSH the element in the Circular Queue");
    printf("\n2.POP the element from the Circular Queue");
    printf("\n3.DISPLAY the element from the Circular Queue");
    printf("\n4.EXIT from the program");
    printf("\n\nEnter the choice : >  ");
	scanf("%d",&p);
	switch(p)
	{
		case 1 :   	printf("\nEnter the element :\n");
                    scanf("%d",&a);
                    insert(a);
                    break;

		case 2 :    delet();
                    break;

		case 3 :    printf("\nTraversing through cicular queue ..........\n\n");
                    print();
                    break;

        case 4 :    printf("\n\nExiting from the program..........");
                    exit(0);

		default :   printf("\n\t[!] INVALID ENTRY\n");

	}
    fflush(stdin);
    printf("\n\nDO YOU WANT TO CONTINUE (y/n)? : >  ");
    scanf("%s",&s);
	}while(s=='y'||s=='Y');

	getch();
}
'''
	return prog

#-------------------PRIORITY QUEUE CODE-------------------

def pqueues() :
	prog='''//-------------------------PRIORITY QUEUE CODE-------------------------


/*
 * C Program to Implement Priority Queue to Add and Delete Elements
 */
#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#define N 5

void insert_by_prior(int);
void delete_by_prior();
void Qcreate();
void display_pqueue();

struct queue
{
    int pri_que[N];
    int front, rear;
}q;

void main()
{
    int n, ch;
//    clrscr();
    printf("\n\n-------------PRIORITY QUEUE IMPLEMENTATION PROGRAM---------------\n\n");
    printf("\n1. Insert an element into the Queue");
    printf("\n2. Delete an element from the Queue");
    printf("\n3. Display the elements of the Queue");
    printf("\n4. Exit the program");

   Qcreate();

    while (1)
    {
	printf("\n\nEnter your choice : ");
	scanf("%d", &ch);

	switch (ch)
	{
	case 1:
	    printf("\n Enter value to be inserted in the Queue : >");
	    scanf("%d",&n);
	    insert_by_prior(n);
	    break;
	case 2:
	    delete_by_prior(n);
	    break;
	case 3:
	    display_pqueue();
	    break;
	case 4:
	    exit(0);
	default:
	    printf("\n---------INVALID ENTRY---------");
	}
    }
}

/* Function to create an empty priority queue */
void Qcreate()
{
    q.front = q.rear = 0;
}

/* Function to insert value into priority queue */
void insert_by_prior(int data)
{
    if(q.front==(q.rear+1)%N)
        printf("\n\t[!] QUEUE IS FULL");
	else
	{
        q.pri_que[q.rear]=data;
        q.rear=((q.rear+1)%N);
        printf("\n\t[!] INSERTION TASK SUCCESSFUL\n");
    }
}


/* Function to display queue elements */
void display_pqueue()
{
    int i;
    if(q.front==q.rear)
	{
	    	printf("\n\t[!] QUEUE IS EMPTY");
	    	return;
	}
    printf("The elements of PRIORITY QUEUE are : \n\n");
	for(i=q.front;i<=q.rear-1;i=(i+1)%N)
            printf("%d\n",q.pri_que[i]);
}

/* Function to delete an element from queue */
void delete_by_prior()
{
    int i,min,pos;

    if(q.front==q.rear)
	{
	    printf("\n\t[!] QUEUE IS EMPTY");
		return ;
    }

    for (i = q.front; i <= q.rear-1; i=(i+1)%N)
    {

	if (min >q.pri_que[i])
            min =q.pri_que[i];
            pos=i;
    }

    for (i=pos; i < q.rear; i=(i+1)%N)
        q.pri_que[i] = q.pri_que[i + 1];

	printf("\nVALUE DELETED : > %d",min);
	printf("\n\t[!] DELETION TASK SUCCESSFUL\n");

}
'''
	return prog

#-------------------ARRAY MENU SELECTION-------------------

def arrays() :
	print ''' \n \n
		1.1 DIMENSIONAL ARRAY 
   	 	2.2 DIMENSIONAL MATRIX '''
	ch= input( "\n\nEnter the project number you want to generate : >  ")

	if  ch==1  :
 		matcode=oneDarrays()
	elif ch==2 :
		matcode=twoDarrays()	

	return matcode

#-------------------QUEUE MENU SELECTION-------------------

def queues() :
	print ''' \n \n	
		1.LINEAR QUEUE 
   	 	2.CIRCULAR QUEUE
		3.PRIORITY QUEUE'''
	ch= input( "\n\nEnter the project number you want to generate : >  ")


	if  ch==1  :
 		listcode=lqueues()
	elif ch==2 :
		listcode=cqueues()
	elif ch==3 :
		listcode=pqueues()	

	return listcode

#-------------------LINKED LIST MENU SELECTION-------------------

def linklist() :
	print ''' \n \n
		1.LINEAR LINKED LIST 
   	 	2.DOUBLY LINKED LIST'''
	ch= input( "\n\nEnter the project number you want to generate : >  ")


	if  ch==1  :
 		listcode=linearlinklist()
	elif ch==2 :
		listcode=dblylinklist()	

	return listcode



#-------------------LINEAR STACK  CODE-------------------

def lstack() :
	prog='''
//-------------------LINEAR STACK  CODE-------------------


#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
#define N 5

struct Stack
{
    int a[N];
    int top;
}s;

void push(int val)
{
    if(s.top==N-1)
	printf("\n[!] STACK IS FULL");

    else
    {
	s.a[++s.top]=val;
	printf("\n\t[!] INSERTION TASK SUCCESSFUL\n") ;
    }
}

void traverse()
{
    int i;

    if(s.top==N-1)
	printf("\n\n[!] STACK IS FULL");

    printf("\nElements of the stack are : > \n");

    for(i=s.top;i>=0;i--)
    {
	printf("%d\n",s.a[i]);
    }

}// end of the traverse function

int pop()
{
    if(s.top==-1)
    {
        printf("\n\n[!] STACK IS FULL");
        return -1;
    }
    else
        return(s.a[s.top--]);


}// end of the pop function


int main()
{
    int val,ch;
    s.top=-1;

     do{
       printf("\n\n-----------LINEAR STACK---------------\n\n ");

       printf("\nCHOOSE ANY ONE OF THE GIVEN OPTIONS BELOW:");
       printf("\n1.  PUSH one element in the stack");
       printf("\n2.  SHOW all the elements of the stack ");
       printf("\n3.  POP out one element from the given stack");
       printf("\n4.  To exit the program ");
       printf("\n\n Enter the choice : > ");

       scanf("%d",&ch);

      switch(ch)
      {     case 1: printf("\nEnter a value which you want to push in the stack : > ");
                    scanf("%d",&val);
                    push(val);
                    break;

            case 2: traverse();
                    break;

            case 3: val= pop();
                    if(val!=-1)
                    {   printf("\nPopped value is : > %d\n",val);
                        printf("\n\t[!] DELETION TASK SUCCESSFUL\n") ;
                    }

                    else 	       printf("\nOperation unsuccessful");
                    break;

            case 4: exit(0);

     }//end of switch case

        }while(ch!=4);

    printf("\n\n\nprogrammed by MOHIT MALHOTRA");
    return 0;
}
'''
	return prog


#-------------------DOUBLE SIDED STACK  CODE-------------------

def dstack() :
	prog='''
//--------------------------------2 SIDED STACK---------------------------------

#include <stdio.h>
#include<conio.h>
#define N 5

//Self Referential structure

struct Stack
{
    int a[N];
    int top1, top2;
}s;


void push1(int val)
{
        if(s.top2-s.top1==1)
            printf("\n\n\t[!] STACK IS FULL\n");
        else
            {
                s.top1++;
                s.a[s.top1]=val;
                printf("\n\t[!] INSERTION TASK SUCCESSFUL\n");
            }
}

void push2(int val)
{
        if(s.top2-s.top1==1)
            printf("\n\n\t[!] STACK IS FULL\n");
        else
            {
                s.top2--;
                s.a[s.top2]=val;
                printf("\n\t[!] INSERTION TASK SUCCESSFUL\n");
            }
}

void pop1()
{
    if(s.top1==-1)
        printf("\n\t[!] STACK IS EMPTY from side 1\n");
    else
        {
            printf("\nVALUE DELETED : %d\n",s.a[s.top1]);
            s.top1--;
            printf("\n\t[!] DELETION TASK SUCCESSFUL\n");
        }
}

void pop2()
{
    if(s.top2==N)
        printf("\n\t[!] STACK IS EMPTY from side 2\n");
    else
        {
            printf("\nVALUE DELETED : > %d",s.a[s.top2]);
            s.top2++;
            printf("\n\t[!] DELETION TASK SUCCESSFUL\n");
        }
}


void traverse1()
{
    int i;
    if(s.top1==-1)
    {
        printf("\n\t[!] STACK IS EMPTY from side 1\n");
        return;
    }
    printf("The elements of stack from side 1 are : \n\n");
    for(i=s.top1;i>=0;i--)
        printf("%d\n",s.a[i]);
}

void traverse2()
{
    int i;
    if(s.top2==N)
    {
        printf("\n\t[!] STACK IS EMPTY from side 2\n");
        return;
    }
    printf("The elements of stack from SIDE 2 are : \n\n");
    for(i=s.top2;i<N;i++)
        printf("%d\n",s.a[i]);
}

int main()
{
    int val,p;
    s.top1=-1;
    s.top2=N;
    char s;
	do
    {   printf("\n\n-------------2 SIDED STACK---------------\n\n");
        printf("\nSelect the operation you want to perfom(1/2/3/4/56) :\n");
        printf("\n1.PUSH the element from side 1 ");
        printf("\n2.PUSH the element from side 2");
        printf("\n3.POP the element from side 1 ");
        printf("\n4.POP the element from side 2");
        printf("\n5.DISPLAY the elments from side 1");
        printf("\n6.DISPLAY the elments from side 2");
        printf("\n\nEnter the choice : >  ");
        scanf("%d",&p);

        switch(p)
        {
            case 1 :    printf("Enter the value : ");
                        scanf("%d",&val);
                        push1(val);
                        break;

            case 2 :    printf("Enter the value : ");
                        scanf("%d",&val);
                        push2(val);
                        break;

            case 3 :    pop1();
                        break;

            case 4 :    pop2();
                        break;

            case 5 :    printf("\nTraversing through side 1 ..........\n\n");
                        traverse1();
                        break;

            case 6 :    printf("\nTraversing through side 2 ..........\n\n");
                        traverse2();
                        break;

            default :   printf("\n\t[!] INVALID REQUEST");
                        break;
        }
        fflush(stdin);
        printf("\n\nDO YOU WANT TO CONTINUE (y/n)? : >  ");
        scanf("%s",&s);
    } while(s=='y'||s=='Y');

	printf("\n\n\t programmed by MOHIT MALHOTRA");
	getch();

    return 0;

}
'''
	return prog


#-------------------STACK MENU SELECTION CODE-------------------

def stacksmenu() :
	print ''' \n \n
		1.LINEAR STACK
   	 	2.DOUBLE SIDED STACK'''
	ch= input( "\n\nEnter the project number you want to generate : >  ")


	if  ch==1  :
 		listcode=lstack()
	elif ch==2 :
		listcode=dstack()	

	return listcode

#-------------------INFIX EVALUTION-------------------------

def infix() :
	prog='''
#include <stdio.h>
#include <ctype.h>
#include <conio.h>
#include <process.h>
#include <string.h>
#define N 10

//stack for the evaluation of the expression

struct stack
{
    int a[N];
    int top;
}s;

char post[N],pre[N];

//function declarations for the code

void evalpost();
void evalpre();
void push(int );
int pop();
void oprtr(char ,int );



void main()
{
    int chi;
    s.top=-1;

//    clear;
    printf("\n\nINFIX EXPRESSION CONVERSION AND EVALUATION\n");
    printf("\n1. Evaluation of POSTFIX expression");
    printf("\n2. Evaluation of PREFIX expression");
    printf("\n\nEnter the choice : > ");
    scanf("%d",&chi);

    if(chi==1)
    {
	printf("\nEnter the Postfix expression : >");
	scanf("%s",&post);
	evalpost();

    }

    else if(chi==2)
    {
	printf("\nEnter the Prefix expression : >");
	scanf("%s",&pre);
	evalpre();

    }

    else printf("\nINVALID SUBMISSION....");


    printf("\n\nprogrammed by MOHIT MALHOTRA");

    getch();
}


//push function for stack operation

void push(int op)
{
    //if the stack is full
    if(s.top==N)   printf("\nSTACK WILL OVERLOAD\nENTRY UNSUCCESSFUL....");

    else
    {
	s.a[++s.top]=op;
	printf("\nOPERATION SUCCESSFUL....");
    }
}


//pop function for the stack operation

int pop()
{
	int val;

	//if stack is completely empty
	if(s.top==-1)
	{
	    printf("\nSTACK IS EMPTY\nOPERATION UNSUCCESSFUL....");
        getch();
	    //forced termination of the program
	    exit(0);
	}
	else
	{
	    val=s.a[s.top];
	    s.top=s.top-1;

	}

    return val;
}


//evaluation of the operator in the expression

void oprtr(char opr,int dec)
{
    int x1,x2,res;


   if(dec==1)
   {

      switch(opr)
    {
	case '*' :      x2=pop();
                    x1=pop();
                    res=x1*x2;
                    push(res);
                    break;

	case '/' :      x2=pop();
                    x1=pop();
                    res=x1/x2;
                    push(res);
                    break;

	case '+' :      x2=pop();
                    x1=pop();
                    res=x1+x2;
                    push(res);
                    break;

	case '-' :      x2=pop();
                    x1=pop();
                    res=x1-x2;
                    push(res);
                    break;

	case '^' :      x2=pop();
                    x1=pop();
                    res=x1^x2;
                    push(res);
                    break;

	case '%' :      x2=pop();
                    x1=pop();
                    res=x1%x2;
                    push(res);
                    break;

	default  :      printf("\n\nINVALID CHARACTER IN THE EXPRESSION ");
                    break;

    }//end of switch cas
   }

   else if(dec==-1)
   {

      switch(opr)
    {
	case '*' :      x1=pop();
                    x2=pop();
                    res=x1*x2;
                    push(res);
                    break;

	case '/' :      x1=pop();
                    x2=pop();
                    res=x1/x2;
                    push(res);
                    break;

	case '+' :      x1=pop();
                    x2=pop();
                    res=x1+x2;
                    push(res);
                    break;

	case '-' :      x1=pop();
                    x2=pop();
                    res=x1-x2;
                    push(res);
                    break;

	case '^' :      x1=pop();
                    x2=pop();
                    res=x1^x2;
                    push(res);
                    break;

	case '%' :      x1=pop();
                    x2=pop();
                    res=x1%x2;
                    push(res);
                    break;

	default  :      printf("\n\nINVALID CHARACTER IN THE EXPRESSION ");
                    break;

    }//end of switch case

   }
    return;

}


//for the evaluation of the postfix expression

void evalpost()
{
    int val ,i;

    for(i=0;post[i]!='\0';i++)
    {
	if(isdigit(post[i]))
	   {
            val=post[i]-'0';
            push(val);
	   }
	else    oprtr(post[i],1);

    }

    printf("\nRESULT OF THE POSTFIX EVALUATION =  %d",pop());
}


//for the evaluation of the prefix expression

void evalpre()
{

    int i,val;

    /*for traversing till the end of the expression
    for(i=0;pre[i]!='\0';i++);
    i--;
    */
    for(i=strlen(pre)-1;i>=0;i--)
    {
        if( isdigit(pre[i]) )
           {
                val=pre[i]-'0';
                push(val);
           }

        else    oprtr(pre[i],-1);

    }

    printf("\nRESULT OF THE PREFIX EVALUATION =   %d",pop());

}
'''
	return prog

#-----------------BINARY TREE CODE------------------------

def bintree() :
	prog='''

//PROGRAM TO PERFORM BASIC OPERATIONS ON A BINARY SEARCH TREE

#include<stdio.h>
#include<conio.h>

struct tree

{

      struct tree *left;

      int info;

      struct tree *right;

};

void insert(struct tree **ptr,int item)

{

      if(*ptr==NULL)

      {

               *ptr=(struct tree *)malloc(sizeof(struct tree));

               (*ptr)->left=(*ptr)->right=NULL;

               (*ptr)->info=item;

               printf("\n\n\t[*] INSERTION TASK SUCCESSFULL\n");

               return;

      }

      else

      {

               if(item<(*ptr)->info)

               {

                         insert(&((*ptr)->left),item);

               }

               else

               {

                         insert(&((*ptr)->right),item);

               }
                printf("\n\n\t[*] INSERTION TASK SUCCESSFULL\n");

               return;

      }

}

void delete_tree(struct tree **ptr,int item)

{

      struct tree *move,*back,*temp;

      if(*ptr==NULL)

      {

               printf("\n\t[!] EMPTY TREE");

               return;

      }

      else

      {

               move=*ptr;

               back=move;

               while(move->info!=item)

               {

                         back=move;

                         if(item<move->info)

                         {

                                  move=move->left;

                         }

                         else

                         {

                                  move=move->right;

                         }

               }

               if(move->left!=NULL&&move->right!=NULL)

               {

                         temp=move->right;

                         while(temp->left!=NULL)

                         {

                                  back=temp;

                                  temp=temp->left;

                         }

                         move->info=temp->info;

                         move=temp;

               }

               if(move->left==NULL&&move->right==NULL)

               {

                         if(back->right==move)

                         {

                                  back->right=NULL;

                         }

                         else

                         {

                                  back->left=NULL;

                         }

                         free(move);

                         return;

               }

               if(move->left==NULL&&move->right!=NULL)

               {

                         if(back->left==move)

                         {

                                  back->left=move->right;

                         }

                         else

                         {

                                  back->right=move->right;

                         }

                         free(move);
                        printf("\n\n\t[!] NODE DELETED FROM THE TREE\n");
                         return;

               }

               if(move->left!=NULL&&move->right==NULL)

               {

                         if(back->left==move)

                         {

                                  back->left=move->left;

                         }

                         else

                         {

                                  back->right=move->left;

                         }

                         free(move);

                         return;

               }

      }

}

void preorder(struct tree *ptr)

{

      struct tree *move;

      move=ptr;

      if(ptr==NULL)

      {

               printf("\n\t[!] EMPTY TREE");

               return;

      }

      if(move!=NULL)

      {

               printf(" %d ",move->info);

               preorder(move->left);

               preorder(move->right);

      }

      else

               return;

}

void inorder(struct tree *ptr)

{

      struct tree *move;

      move=ptr;

      if(ptr==NULL)

      {

               printf("\n\t[!] EMPTY TREE");

               return;

      }

      if(move!=NULL)

      {

               inorder(move->left);

               printf(" %d ",move->info);

               inorder(move->right);

      }

      else

      return;

}

void postorder(struct tree *ptr)

{

      struct tree *move;
      move=ptr;

      if(ptr==NULL)

      {

               printf("\n\t[!] EMPTY TREE");

               return;

      }

      if(move!=NULL)

      {

               postorder(move->left);

               postorder(move->right);

               printf(" %d ",move->info);

      }

      else

               return;

}

void main()

{
      struct tree *root=NULL;
      int item,ch,order;
      char choice,ch1;

      do

      {

               printf("\n\n____________TREE MENU_______________\n\n");

               printf("\n1.Insert the element in the Tree");

               printf("\n2.Delete the element from the Tree");

               printf("\n3.Traversal through Tree");

               printf("\n4.Exit from the code");

               printf("\n\nEnter your choice   :  > ");

               scanf("%d",&ch);

   switch(ch)

    {

             case 1: printf("\nEnter the element to be inserted   :         ");

                      scanf("%d",&item);

                      insert(&root,item);

                      break;

             case 2: printf("\nEnter the element to be deleted    :         ");

                      scanf("%d",&item);

                      delete_tree(&root,item);

                      break;

             case 3: printf("\n\na.Preorder Traversal");

                      printf("\nb.inorder Traversal");

                      printf("\nc.Postorder Traversal");

                      printf("\nEnter your choice   : >  ");

                      scanf("%s",&ch1);

                      printf("\n\nTree  :  ");

                      switch(ch1)

                      {

                                case 'a':   printf("\n\tPREORDER TRAVERSAL\n");
                                            preorder(root);
                                            break;

                                case 'b':   printf("\n\tINORDER TRAVERSAL\n");
                                            inorder(root);
                                            break;

                                case 'c':   printf("\n\tPOSTORDER TRAVERSAL\n");
                                            postorder(root);
                                            break;

                      }
                     break;

            default: exit(0);

               }

       fflush(stdin);

      }while(ch!=4);

getch();
}
'''

	return prog

#-------------------GRAPH TRAVERSAL BFS & DFS----------------------

def graphtrav() :
	prog='''
/* C program to implement BFS(breadth-first search) and DFS(depth-first search) algorithm */

#include<stdio.h>
#include <conio.h>


int q[20],top=-1,front=-1,rear=-1,a[20][20],vis[20],stack[20];
int delete();
void add(int item);
void bfs(int s,int n);
void dfs(int s,int n);
void push(int item);
int pop();

void main()
{
int n,i,s,ch,j;
char c;

printf("\n\n--------GRAPH TRAVERSAL PROGRAM---------\n\n");
printf("\nENTER THE NUMBER VERTICES : > ");
scanf("%d",&n);

printf("\n\t[*] NOTE: enter '1' for connection and '0' for no connection\n\n");

for(i=1;i<=n;i++)
{
    for(j=1;j<=n;j++)
        {
        printf("IF %d HAS A NODE WITH %d  : >    ",i,j);
        scanf("%d",&a[i][j]);
        }
}
printf("\n\n---------THE ADJACENCY MATRIX IS--------------\n");

for(i=1;i<=n;i++)
{
    for(j=1;j<=n;j++)
            printf(" %d",a[i][j]);

    printf("\n");
}

do
    {
    for(i=1;i<=n;i++)
            vis[i]=0;

    printf("\nMENU TO CHOOSE THE TRAVERSAL MODE\n");
    printf("\n1.B.F.S TRAVERSAL");
    printf("\n2.D.F.S TRAVERSAL");
    printf("\n\nENTER YOUR CHOICE");
    scanf("%d",&ch);
    printf("\n\nENTER THE SOURCE VERTEX : > ");
    scanf("%d",&s);

    switch(ch)
    {
        case 1: bfs(s,n);
                break;

        case 2: dfs(s,n);
                break;

        default : printf("\n\t[!] INVALID REQUEST");

    }

    printf("\n\nDO U WANT TO CONTINUE(Y/N) ? ");

    scanf("%s",&c);
    }while((c=='y')||(c=='Y'));

    getch();
}


//**************BFS(breadth-first search) code**************//
void bfs(int s,int n)
{
int p,i;
add(s);
vis[s]=1;

p=delete();

if(p!=0)
    printf(" %d",p);

while(p!=0)
{
    for(i=1;i<=n;i++)
    if((a[p][i]!=0)&&(vis[i]==0))
    {
    add(i);
    vis[i]=1;
    }
    p=delete();
    if(p!=0)
    printf(" %d ",p);
}

for(i=1;i<=n;i++)
    {
    if(vis[i]==0)
        bfs(i,n);
    }
}

void add(int item)
{
if(rear==19)
    printf("QUEUE FULL");
else
    {
        if(rear==-1)
        {
        q[++rear]=item;
        front++;
        }
        else
        q[++rear]=item;
    }
}

int delete()
{
int k;

if((front>rear)||(front==-1))
    return(0);
else
    {
        k=q[front++];
        return(k);
    }
}


//***************DFS(depth-first search) code******************//
void dfs(int s,int n)
{
int i,k;

push(s);

vis[s]=1;

k=pop();

if(k!=0)
    printf(" %d ",k);

while(k!=0)
{
    for(i=1;i<=n;i++)
    {
        if((a[k][i]!=0)&&(vis[i]==0))
        {
            push(i);
            vis[i]=1;
        }
    }

    k=pop();
    if(k!=0)
        printf(" %d ",k);
}
for(i=1;i<=n;i++)
    {   if(vis[i]==0)
            dfs(i,n);
    }
}

void push(int item)
{
if(top==19)
    printf("Stack overflow ");
else
    stack[++top]=item;
}

int pop()
{
int k;

if(top==-1)
    return(0);

else
{
    k=stack[top--];
    return(k);
}
}
'''

	return prog


#--------------------------------------------------------------------
#-------------------MAIN PROGRAM SCRIPT-------------------
#--------------------------------------------------------------------
print '\n\n'
print head.center(75,'-')

print ''' \n\n
	1.SORTING ALGORITHMS
    	2.SPARSE MATRIX 
    	3.ARRAYS 
    	4.QUEUE
	5.LINKED LISTS 
	6.STACKS
	7.INFIX EVALUATION
	8.BINARY TREE 
	9.GRAPH TRAVERSAL (BFS and DFS both way)
'''
ch= input( "\n\nEnter the project number you want to generate : >  ")


if  ch==1  :
 	code=sorting()
	filename="sorting.C"
elif ch==2 :
	code=sparsemat()
	filename="sparse_matrix.C"
elif ch==3 :
	code=arrays()
	filename="array.C"
elif ch==4 :
	code=queues()
	filename="queue.C"
elif ch==5 :
	code=linklist()
	filename="LinkedList.C"
elif ch==6 :
	code=stacksmenu()
	filename="Stacks.C"

elif ch==7 :
	code=infix()
	filename="Infix_evaluation.C"

elif ch==8 :
	code=bintree()
	filename="Binary_tree.C"

elif ch==9 :
	code=graphtrav()
	filename="Graph_Traversal.C"

else : 
	print "[!]INVALID ENTRY"


#opening the file to read
try:
	file=open(filename,"w+")

except IOError:
	print "\n[!] ERROR FILE CAN BE REACHED"
	sys.exit()

file.write(code)

print "[*]CODE SUCCESSFULLY WRITTEN IN THE FILE \nfile name :  >   "+filename
print "\n[*] NOTE : FILE IS GENERATED IN THE CURRENT DIRECTORY WHERE THE CODE IS RUNNING"

file.close();

input("\n\n\n   Press any key to exit the code.................")