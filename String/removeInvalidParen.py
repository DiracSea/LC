class Solution:
    # DFS
    def remove_invalid_parentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [s]

        results = []
        self.remove(s, 0, 0, results)
        return results

    def remove(self,
               str_to_check,
               start_to_count,
               start_to_remove,
               results,
               pair=['(', ')']):
        # start_to_count: the start position where we do the +1, -1 count,
        # which is to find the position where the count is less than 0
        #
        # start_to_remove: the start position where we look for a parenthesis
        # that can be removed

        count = 0
        for count_i in range(start_to_count, len(str_to_check)):
            if str_to_check[count_i] == pair[0]:
                count += 1
            elif str_to_check[count_i] == pair[1]:
                count -= 1

            if count >= 0:
                continue

            # If it gets here, it means count < 0. Obviously.
            # That means from start_to_count to count_i (inclusive), there is an extra
            # pair[1].
            # e.g. if sub_str = ()), then we can remove the middle )
            # e.g. if sub_str = ()()), the we could remove sub_str[1], it becomes (())
            #  or we could remove sub_str[3], it becomes ()()
            # In the second example, for the last two )), we want to make sure we only
            # consider remove the first ), not the second ). In this way, we can avoid
            # duplicates in the results.
            #
            # In order to achieve this, we need this condition
            #  str_to_check[remove_i] == pair[1] and str_to_check[remove_i - 1] != str_to_check[remove_i]
            # But what if str_to_check[start_to_remove] == pair[1], 
            # then remove_i - 1 is out of the range(start_to_remove, count_i + 1)
            # so we need
            # str_to_check[remove_i] == pair[1] and (start_to_remove == remove_i or str_to_check[remove_i - 1] != str_to_check[remove_i])
            for remove_i in range(start_to_remove, count_i + 1):
                if str_to_check[remove_i] == pair[1] and (start_to_remove == remove_i or str_to_check[remove_i - 1] != str_to_check[remove_i]):
                    # we remove str_to_check[remove_i]
                    new_str_to_check = str_to_check[0:remove_i] + str_to_check[remove_i + 1:]

                    # The following part are the most confusing or magic part in this algorithm!!!
                    # I'm too stupid and it took me two days to figure WTF is this?
                    #
                    # So for start_to_count value
                    # we know in str_to_check, we have scanned up to count_i, right?
                    # The next char in the str_to_check we want to look at is of index (count_i + 1) in str_to_check
                    # We have remove one char bewteen start_to_remove and count_i inclusive to get the new_str_to_check
                    # So the char we wanted to look at is of index (count_i + 1 - 1) in the new_str_to_check. (-1 because we removed one char)
                    # That's count_i. BOOM!!!
                    #
                    # Same reason for remove_i
                    # In str_to_check, we decide to remove the char of index remove_i
                    # So the next char we will look at to decide weather we want to remove is of index (remove_i + 1) in str_to_check
                    # we have remove [remove_i] char of the str_to_check to get the new_str_to_check.
                    # So the char we wanted to look at when doing remove is of index (remove_i + 1 - 1) in the new_str_to_check.
                    # That's remove_i. BOOM AGAIN!!!
                    new_start_to_count = count_i
                    new_start_to_remove = remove_i
                    self.remove(new_str_to_check,
                                new_start_to_count,
                                new_start_to_remove,
                                results,
                                pair)

            # Don't underestimate this return. It's very important
            # if inside the outer loop, it reaches the above inner loop. You have scanned the str_to_check up to count_i
            # In the above inner loop, when construct the new_str_to_check, we include the rest chars after count_i
            # and call remove with it.
            # So after the above inner loop finishes, we shouldn't allow the outer loop continue to next round because self.remove in the
            # inner loop has taken care of the rest chars after count_i
            return

        # Why the hell do we need to check the reversed str?
        # Because in the above count calculation, we only consider count < 0 case to remove stuff.
        # The default pair is ['(', ')']. So we only consider the case where there are more ')'  than '('
        # e.g "(()" can pass the above loop
        # So we need to reverse it to ")((" and call it with pair [')', '(']
        reversed_str_to_check = str_to_check[::-1]
        if pair[0] == '(':
            self.remove(reversed_str_to_check, 0, 0, results, pair=[')', '('])
        else:
            results.append(reversed_str_to_check)


    # backtracking 
    def __init__(self): 
        self.valid_expressions = None 
        self.min_removed = None 
        
    def reset(self): 
        self.valid_expression = set() 
        self.min_removed = float('inf')
        
    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left: number of left parentheses till now.
        right: number of right parentheses till now.
        ans: the resulting expression in this particular recursion.
        ignored: number of parentheses ignored in this particular recursion.
    """
    def remaining(self, s, idx, l_count, r_count, expr, rem_count): 
        # if reach the end 
        if idx == len(s): 
            if l_count == r_count: 
                if rem_count <= self.min_removed: 
                    
                    possible_ans = "".join(expr) 
                    
                    if rem_count < self.min_removed: 
                        self.valid_expressions = set() 
                        self.min_removed = rem_count 
                    self.valid_expressions.add(possible_ans) 
        else: 
            current_ch = s[idx] 
            
            if current_ch != '(' and current_ch != ')': 
                expr.append(current_ch) 
                self.remaining(s, idx+1, l_count, r_count, expr, rem_count) 
                expr.pop() 
            else: 
                self.remaining(s, idx + 1, l_count, r_count, expr, rem_count + 1)

                expr.append(current_ch)

                # If the current parenthesis is an opening bracket, we consider it
                # and increment left and  move forward
                if s[idx] == '(':
                    self.remaining(s, idx + 1, l_count + 1, r_count, expr, rem_count)
                elif r_count < l_count:
                    # If the current parenthesis is a closing bracket, we consider it only if we
                    # have more number of opening brackets and increment right and move forward.
                    self.remaining(s, idx + 1, l_count, r_count + 1, expr, rem_count)

                expr.pop()
    def removeInvalidParentheses1(self, s: str):

        # Reset the class level variables that we use for every test case.
        self.reset()

        # Recursive call
        self.remaining(s, 0, 0, 0, [], 0)
        return list(self.valid_expressions)
        