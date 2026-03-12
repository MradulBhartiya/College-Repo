#include<iostream>
using namespace std;

int ques1(int n)
{
    int count = 0;
    while(n)
    {
        if((n & 1) == 1) count++;
        n = n>>1;
    }
    return count;
}
int ques2(int n)
{
    int result = 0;
    for(int i = 0; i<32; i++)
    {
        if((n & 1) == 1) result = result<<1 | 1;
        else result = result<<1 | 0;
        n = n>>1;
    }
    return result;
}
int ques3(int n)
{
    int result = 1;
    while(n--)
    {
        result = result*2;
    }
    return result;
}
int main()
{
    int n;
    cin>>n;
    cout<<ques1(n);
    cout<<ques2(n);
    cout<<ques3(n); 

    return 0;
}