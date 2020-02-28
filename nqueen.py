class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.res = []
        res, column_index = [], []
        # print self.res
        self.helper(res, column_index, 0, n)
        print "checked"
        return self.res

    def is_valid(self, curr_column, column_index):
        check_list = []
        row_num = len(column_index)
        for pr in range(len(column_index)):
            if column_index[pr] not in check_list:
                check_list.append(column_index[pr])
            row_diff = abs(pr - row_num)
            check_list.append(column_index[pr] + row_diff)
            check_list.append(column_index[pr] - row_diff)
        if curr_column in check_list:
            return False
        return True

    def construct_matrix(self, column_index, N):
        one_result = []
        for i in column_index:
            row_string = "." *i + "Q" + "."*(N-1-i)
            one_result.append(row_string)
            # print row_string
        return one_result

    def helper(self, res, column_index, curr_row, N):
        if len(column_index) == N:
            # print column_index
            self.res.append(self.construct_matrix(column_index, N)[:])
            return
            # print column_index
        else:
            # print curr_row
            for column in range(N):
                if self.is_valid(column, column_index):
                    column_index.append(column)
                    self.helper(res, column_index, curr_row+1, N)
                    column_index.pop()


if __name__ == "__main__":
    nqueen = Solution()
    # nqueen.construct_matrix([0,2,1], 3)
    # if nqueen.is_valid(30, [0,2,1], 3):
    #     print "valid!"
    print nqueen.solveNQueens(4)
