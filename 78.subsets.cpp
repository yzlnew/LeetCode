class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> result;
        result.push_back(vector<int>());
        for(int& x : nums){
            int size = result.size();
            for(int i=0; i<size; i++){
                vector<int> subset = result.at(i);
                subset.push_back(x);
                result.push_back(subset);
            }
        }
        return result;
    }
};
