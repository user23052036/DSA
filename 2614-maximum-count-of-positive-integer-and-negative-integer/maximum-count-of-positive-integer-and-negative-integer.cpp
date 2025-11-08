class Solution 
{
public:
    int maximumCount(vector<int>& nums) 
    {
        int low=0, high=nums.size()-1;

        while(low <= high)
        {
            int mid = low + (high-low)/2;
            if(nums[mid]<0) low = mid+1;
            else high = mid-1;
        }
        //after this iteration high will be pointing at the negative indx 
        //and low will be pointing at the positive indx

        // wealso have to skip 0 as its not positive so use upper bound for it
        if(low <= nums.size()-1 && nums[low] == 0) low = UB(nums,low,0);

        if((high+1) > (nums.size()-low)) return high+1;
        return nums.size()-low;
    }

private:
    int UB(vector<int>&nums, int low, int target)
    {
        int high = nums.size()-1;
        
        while(low <= high)
        {
            int mid = low + (high-low)/2;

            if(nums[mid] == 0) low = mid+1;
            else high = mid-1;
        }
        return low;
    }
};