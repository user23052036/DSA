class Solution 
{
private:
    int lowerBound(const vector<int>&a, int x) 
    {
        int low = 0, high = a.size()-1;
        
        while (low <= high) 
        {
            int mid = low + (high-low)/2;

            if (a[mid] >= x) high = mid-1;
            else low = mid+1;
        }
        return low;
    }

    int upperBound(const vector<int>& a, int x) 
    {
        int low = 0, high = a.size()-1;

        while (low <= high) 
        {
            int mid = low + (high-low)/2;
            
            if (a[mid] > x) high = mid-1;
            else low = mid+1;
        }
        return low;
    }

public:
    int maximumCount(vector<int>& nums) 
    {
        int neg = lowerBound(nums,0);                    // count of negatives
        int pos = nums.size() - upperBound(nums,0); // count of positives
        return max(neg,pos);
    }
};
