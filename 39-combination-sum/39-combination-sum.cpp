class Solution {
public:
    void helper(vector<int>arr,int tar,int ind,vector<int>temp,vector<vector<int>>&res)
    {
        if(ind==arr.size())
        {
            if(tar==0)
            {
                res.push_back(temp);
            }
            return;
        }
        if (tar>=arr[ind])
        {
            temp.push_back(arr[ind]);
            helper(arr,tar-arr[ind],ind,temp,res);
            temp.pop_back();
        }
        helper(arr,tar,ind+1,temp,res);
        
    }
    vector<vector<int>> combinationSum(vector<int>& arr, int tar) {
        
        vector<vector<int>>res;
        vector<int>temp;
        helper(arr,tar,0,temp,res);
        return res;
        
    }
};