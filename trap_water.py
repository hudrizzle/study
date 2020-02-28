class Solution(object):
    def _trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # brutal force
        # for each element, calculate how much water it stores?
        ans =  0
        for i in range(len(height)):
            print "iteration: " + str(i)
            # get left and right max
            lmax, rmax = 0, 0

            for l in range(i, -1, -1):
                lmax = max(lmax, height[l])
            for r in range(i, len(height)):
                rmax = max(rmax, height[r])

            # print(rmax)
            print lmax, height[i], rmax
            min_v = min(lmax, rmax)
            if  min_v> height[i]:
                ans += min_v - height[i]
                print "current ans:" + str(ans)
        return ans

    def __trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # loop from left and right once while keep the max from the end.
        lmax, rmax = 0, 0
        left_list , right_list = [], []

        for l in range(len(height)):
            lmax = max(lmax, height[l])
            if lmax - height[l] > 0:
                curr_left = lmax - height[l]
            else:
                curr_left = 0
            left_list.append(curr_left)

        for r in range(len(height)-1, -1, -1):
            rmax = max(rmax, height[r])
            print height[r]

            if rmax - height[r] > 0:
                curr_right = rmax -height[r]
            else:
                curr_right = 0
            print curr_right
            print ""
            right_list.append(curr_right)
        right_list = right_list[::-1]
        # print height
        # print right_list
        # print left_list

        res = 0
        for ii in range(len(height)):
            res += min(left_list[ii], right_list[ii])
        print res
        return res

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # use stack to store indexs.
        # push if new index heigth < top
        # else: pop and calculate the water amount.

        if len(height) <= 2:
            return 0

        stack = []
        ans = 0
        curr = 0
        while curr < len(height):
            print "index: ", str(curr)
            while stack and height[stack[-1]] < height[curr]:
                # do calculation
                top_stack_index = stack[-1]
                stack.pop()
                if not stack: break
                distance = curr - stack[-1] -1
                bounded_height = min(height[curr], height[stack[-1]]) - height[top_stack_index]
                ans += distance*bounded_height
                if curr == 6:
                    print bounded_height, distance
                # print distance, bounded_height
            stack.append(curr)
            print stack
            print ans
            curr += 1
        return ans


check = Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
check.trap(height)

# for height in test_cases:
#     check.trap(height)
