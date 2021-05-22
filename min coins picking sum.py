#include<bits/stdc++.h>
using namespace std;
class Solution{
	public:
	int MinCoin(vector<int>nums, int amount)
	{
	    int dp[amount+1];
	    dp[0]=0;
	    //for(int i=1;i<=amount;i++)dp[i]=999999999;
	    for(int i=1;i<=amount;i++){
	        dp[i]=999999;
	        for(auto j:nums){
	            if((i-j)>=0) dp[i]=min(dp[i],dp[i-j]+1);
	        }
	    }
	    if(dp[amount]==999999)return -1;
	    return dp[amount];
	}
};
int main(){
	int tc;
	cin >> tc;
	while(tc--){
		int n, amount;
		cin >> n >> amount;
		vector<int>nums(n);
		for(int i = 0; i < n; i++)
			cin >> nums[i];
		Solution ob;
		int ans = ob.MinCoin(nums, amount);
		cout << ans <<"\n";
	}
	return 0;
}
