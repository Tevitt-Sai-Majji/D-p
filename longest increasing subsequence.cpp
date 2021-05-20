#include<bits/stdc++.h>
using namespace std;
class Solution
{
    public:
    int ceilArr(int tail[], int l, int r, int x){
    while(l < r){
        int m = l + (r-l)/2;
        if(tail[m] >= x)r = m;
        else l = m + 1;
    }
    return r;
}
    int longestSubsequence(int n, int arr[])
    {
        int len = 1;
        int tail[n];
        tail[0] = arr[0];
        for(int i = 1; i < n; i++){
            if(arr[i] > tail[len-1])tail[len++] = arr[i];
        else{
            int c = ceilArr(tail, 0, len-1, arr[i]);
            tail[c] = arr[i];
        }
    }
    return len;
}
};
int main()
{
    int t,n;
    cin>>t;
    while(t--)
    {
        cin>>n;
        int a[n];
        for(int i=0;i<n;i++)
            cin>>a[i];
        Solution ob;
        cout << ob.longestSubsequence(n, a) << endl;
    }
}
