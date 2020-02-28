class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        swap_check = False
        current_min = nums[-1]
        min_index = -1
        for i in range(len(nums) -2, -1, -1):
            # check i and i+1
            print i
            current_min = min(current_min, nums[i+1])
            if current_min == nums[i+1]: min_index = i+1
            if nums[i+1] > nums[i]:
                print "chekc"
                nums[min_index], nums[i] = nums[i], nums[min_index]
                swap_check = True
                break
        print nums
        # put i+1 to correct position
        for j in range(i+1, len(nums) -1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

        if not swap_check:
            nums =  nums.reverse()
        print nums

class Solution1(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <=1:
            return

        for i in range(len(nums) -1, 0, -1):
            # check i and i-1
            if nums[i] > nums[i-1]:
                for j in range(len(nums) -1, i-1, -1):
                    if nums[j] > nums[i-1] :
                        print j, i-1
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        break
            break
        print i
        if i == len(nums) -1:
            self.reserve_list(nums,0)
        else:
            self.reserve_list(nums, i)
        print nums
        return

    def reserve_list(self, nums, start):
        i, j = start, len(nums) -1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1


if __name__ == "__main__":
    np = Solution1()
    # nqueen.construct_matrix([0,2,1], 3)
    # if nqueen.is_valid(30, [0,2,1], 3):
    #     print "valid!"
    test_case = [[3,2,1], [1, 2, 3]]
    for tc in test_case:
        np.nextPermutation(tc)
