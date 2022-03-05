// { Driver Code Starts
#include<bits/stdc++.h> 
using namespace std; 

 // } Driver Code Ends
class Solution
{
public:

    void helper(vector<int>arr,int sum,int ind,vector<int>&res)
    {
        if(ind==arr.size()){
        res.push_back(sum);
        return;
        }
        helper(arr,sum+arr[ind],ind+1,res);
        helper(arr,sum,ind+1,res);
    }
    vector<int> subsetSums(vector<int> arr, int N)
    {
        vector<int>res;
        helper(arr,0,0,res);
        return res;
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        vector<int> arr(N);
        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }
        Solution ob;
        vector<int> ans = ob.subsetSums(arr,N);
        sort(ans.begin(),ans.end());
        for(auto sum : ans){
            cout<< sum<<" ";
        }
        cout<<endl;
    }
    return 0;
}  // } Driver Code Ends