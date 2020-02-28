class Solution(object):
    def isMatch(self, s, p):
        res = []
        one = ""
        self.string = s
        self.dfs(res, one, 0, len(p), p)
        # return res
        # print res
        if s in res:
            return True

        return False


    def dfs(self, res, one, curr_pos, N, p):
        if curr_pos == N:
            res.append(one[:])
            print one
            return
        else:
            # print curr_pos
            if p[curr_pos] == ".":
                for l in self.string:
                    one += l
                    self.dfs(res, one, curr_pos+1, N, p)
                    one = one[:-1]
            elif p[curr_pos] == "*":

                curr_one = one[:]
                if one[-1] == ".":
                    for l in self.string:
                        add_string = l
                        one[-1] = add_string
                        for i in range(len(self.string)):
                            one += add_string*i
                            self.dfs(res, one, curr_pos+1, N, p)
                            one = curr_one[:]####
                else:
                    add_string = one[-1]
                    for i in range(len(self.string)):
                        one += add_string*i
                        self.dfs(res, one, curr_pos+1, N, p)
                        one = curr_one[:]####
            else:
                one += p[curr_pos]
                self.dfs(res, one, curr_pos+1, N, p)


if __name__ == "__main__":
    # nqueen.construct_matrix([0,2,1], 3)
    # if nqueen.is_valid(30, [0,2,1], 3):
    #     print "valid!"
    check = Solution()
    if check.isMatch("ab", ".*"):
        print "Match"
    else:
        print "Not Match"
    # print "s"[-1]
