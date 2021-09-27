* IS NUMBER PALINDROME
    - check to see if the number is a palindrom including negative numbers
    - 1, 121, 2222, 12321 yes
    - 12, 120, 12312 -121 no  
    * SOLUTION 1 CHNAGE NUM TO STRING 
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            numString = str(x)
            numLen = len(numString)
            middle = floor(numLen/2)
            print(x%5)
            for i in range(0,middle,1):
                if numString[i] != numString[(numLen-i)-1]:
                    return False
            return True

    #SUMMARY
    #1.Change the int into a string
    #2.Get len of numString 
    #3.We want to compare moving from two direction front->back and back->front
    # but we need a mid way point to know where to stop 
    #4. Get middle by doing floor() of len of numString 
    #5. Loop up until middle and compare string[i] != string[(numLen-i)-1] 
    * SOLUTION 2 DONT CHANGE TO STRING
    class Solution:
        def isPalindrome(self, x: int) -> bool:
            if x < 0 or (x % 10 == 0 and x != 0):
                return False 
            
            revertedNum = 0 
            while(x > revertedNum):
                revertedNum = revertedNum*10 + x%10 
                x = floor(x/10)

            return x == revertedNum or x == floor(revertedNum/10)

    #SUMMARY
    #1. Take out the edge cases: 
        #any number < 0 will be false
        #any number ending with 0 will be false other than 0 
    #2. What we want to think is we have two numbers: the original and the reverted
    #3. Initialize reverted = 0 
    #4. We want to remove the last value of x and add it to reverted
    #5. We want to keep removing while(x>reverted)
    #6. we add the last digit of x to reverted by doing 
        #reverted = reverted*10 + x%10
        #remember x%10 will give you the remainder so:
            #2%10 = 2; 10%10 = 0; 124%10 = 4
    #7. We remove the last digit from x by simply doing x=floor(x/10)
    #8. Return x == revertedNum for even length x 
        # return x == floor(revertedNum/10) for odd length x

* ROMAN NUMERAL TO INTEGER VALUE 
    Input: s = "III" Input: s = "IV" Input: s = "IX" Input: s = "LVIII" Input: s = "MCMXCIV"
    Output: 3       Output: 4       Output: 9        Output: 58         Output: 1994
    class Solution:
        def romanToInt(self, s: str) -> int:
            converter = {"I": 1,"V": 5, "X":10, "L":50,"C":100,"D":500,"M":1000 }
            returnValue = converter[s[0]]
            for i in range(1,len(s),1):
                previous = converter[s[i-1]]
                current = converter[s[i]]
                if( previous < current):
                    returnValue -= previous * 2
                returnValue += current
            return returnValue

    # SUMMARY
    # 1. Make a dict, the key is the roman str & the value is the numerical value.
    # 2. Initialize the returnValue to be the first value of the string.
    # 3. Loop through the string and adding the value of each string to the return value.
    # 4. Before adding the string check to see if the previous value was smaller than the current value.
    # Adding right to left we need to check that the previous value is smaller than the current value 
    # Adding left to right we would check to see that previous value is greater than the current value 

* LONGEST COMMON PREFIX
    Input: strs = ["flower","flow","flight"] Input: strs = ["dog","racecar","car"] Input: strs = [] Input: strs = ["abc"]
    Output: "fl"                            Output: ""                             Output: ""       Output: "abc"   
    #MY SOLUTION
    class Solution:
        def longestCommonPrefix(self, strs: List[str]) -> str:
            if len(strs) == 0: return ""
            if len(strs) == 1: return strs[0]
            longestPrefix = ""
            shortestLen = len(strs[0])
            for word in strs:
                if len(word) < shortestLen:
                    shortestLen = len(word)
            count = 0;
            while(count < shortestLen):
                currentLetter = strs[0][count]
                for word in strs[1:]:
                    if word[count] != currentLetter:
                        return longestPrefix
                longestPrefix += currentLetter
                count+=1
            return longestPrefix
    # SUMMARY
    # 1. find the shortest string 
    #       we do this to avoid going out of bounds when comparing
    # 2. Loop thorugh every string and compare its ith char to the current char
    # 3. If the current char doesnt equal the ith char than return what there is so far
    # 4. If the shortest str is the same as longest prefix than that will be returned

    #OPTIMIZED SOLUTION 
    def longestCommonPrefix(self, strs):
            if not strs:
                return ""
            shortest = min(strs,key=len)
            for i, ch in enumerate(shortest):
                for other in strs:
                    if other[i] != ch:
                        return shortest[:i]
            return shortest 

* PARANTHESES PAIRS
    ''' Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        
        Input: s = "()[]{}" Input: s = "() Input: s = "([)] Input: s = "{[]}""
        Output: true        Output: true   Output: false    Output: true"
    '''
    class Solution:
        def isValid(self, s: str) -> bool:
            if len(s) % 2 != 0:
                return False
            stack = []
            pairs = {")":"(", "]":"[","}":"{"}
            for paren in s:
                if paren == "(" or paren == "[" or paren == "{":
                    stack.append(paren)
                else:
                    if len(stack) == 0 or pairs[paren] != stack[-1]:
                        return False
                    else:
                        stack.pop()
            return len(stack) == 0
    # SUMMARY 
    # Check if str is even, if its not than there cant be pairs 
    # We want to create a stack and add to it everyt time there is an opening tag
    # When there is a closing tag we compare the last paran on the stack
    # If they match, are a pair, than pop from the stack 
    # At the end if the stack is empty than the str did have valid paran pairs

* MERGE TWO SORTED LISTS 
    '''
        Merge two sorted linked lists and return it as a sorted list. 
        The list should be made by splicing together the nodes of the first two lists.
        Input: l1 = [1,2,4], l2 = [1,3,4]
        Output: [1,1,2,3,4,4]  
    '''
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            head = current = ListNode(0)
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 or l2
            return head.next

    # SUMMARY
    # We need the head node to stay at the head witha dummy node with val 0
    # Make the current node equal to the same head node but current is the one thats going to keep moving
    # While l1 and l2 are not None keep going, this means that if either one of them becomes None then exit 
    # Inside compare l1 and l2, which ever is less is the one that current will point to next
    # At the end if either l1 or l2 is None current will point to the rest of the one that isnt None

* REMOVE DUPLICATES FROM SORTED ARRAY 
    '''
        The problem states that we should remove any duplicate values from an array of nums without creating a new list.
        We should also return the new length of the list. But in reality the problem is built in a way that the unique values
        should be at the front of the array and the duplicate should be at the end. Returning the amount of uniqiue values will
        display that many indecis of the array. So we can come up with solution that uses .remove() and one that doesnt use it.
    '''
    - WITH REMOVE
    class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums):
            current = nums[0]
            for num in nums[1:]:
                if num == current:
                    nums.remove(num)
                else:
                    current = num
        return len(nums)
    - WITHOUT REMOVE
    def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) == 0: return 0
    current_index = 0
    for i in range(0,len(nums),1):
        if nums[i] != nums[current_index]:
            current_index += 1
            nums[current_index] = nums[i]
    return current_index+1

    # SUMMARY 
    # The first value will automatically be unique so the the index will be set to 0
    # We will then iterate through the list until we find a value that is diff from the current value
    # We then increase the current index and set the new value to nums[current_index]
    # After we are done we will have moved all the unique values to the front
    # The current index + 1 will also reflect the amount of unique values

* PLUS ONE 
    '''
        The problem states that we have a list of integers that represent a whole number: [1,2,3] is 123.
        We need to add 1 to the number and return it as a list so [1,2,3] -> [1,2,4].
        It gets more complicated with [1,9] -> [2,0] [1,9,9] -> [2,0,0] [9,9] -> [1,0,0]
    '''
    * MY PYTHON SOLUTION
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            num = 0
            tens = 1
            for i in range(len(digits)-1,-1,-1):
                num += tens*digits[i]
                tens *= 10
            num += 1
            return [int(i) for i in str(num)]
        else:
            digits[-1] = digits[-1] + 1
            return digits
        # SUMMARY
        # If the last digit in the list is < 9 than just ++1 to the last digit and return the whole list
        # Else we want to convert the list into an integer
        # Do this by looping through the list in reverse order and adding the current number * the current tens place
            # [1,2,3] i = 3 num = 0 tens = 1 num+=tens*i so it will be 3+20+100 = 123
        # Once we have an integer just do integer+=1
        # After turn the integer into a string and then loop through that string and append each value to a list

    * C++ SOLUTION
        vector<int> plusOne(vector<int>& digits) {
            for (int i=digits.size(); i--; digits[i] = 0)
                if (digits[i]++ < 9)
                    return digits;
            digits[0]++;
            digits.push_back(0);
            return digits;
        }
        #SUMMARY: Unlike my solution this one simply manipulates the vector
        # Loop through the list and if the current value is < 9 than just increment by 1 and return the entire vector
            #This works because once we have found the digit to increment we dont need to keep going
        # Else if the number isnt < 9 that means its a 9 so incrementing would turn it into a 0 and thats what the loop does
        # The outside will only be reached if the number is a 9 99 999 etc, which will make the vector look like 000
        # We then replace the first 0 with 1 so 000->100 and then add a 0 at the end, so 999 -> 000 -> 100 -> 1000
    
* ADD BINARY 
    '''
        Given two binary strings a and b, return their sum as a binary string.
        Input: a = "11", b = "1"
        Output: "100"
        Input: a = "1010", b = "1011"
        Output: "10101"
    '''
    * MY SOLUTION
    class Solution:
        def addBinary(self, a: str, b: str) -> str:
            if len(a) >= len(b):
                upper, bottom = a, b
            else:
                upper, bottom = b, a
            
            carry = 0
            result = ""
            for i in range(len(upper)):
                indx = len(upper)-i-1
                if i+1 > len(bottom):
                    if carry + int(upper[indx]) > 1:
                        carry = 1
                        result = "0" + result
                    elif carry + int(upper[indx]) == 1:
                        carry = 0
                        result = "1" + result
                    else:
                        carry = 0
                        result = "0" + result
                else:
                    if int(upper[indx]) + carry > 1:
                        carry = 1
                        temp = 0
                    elif int(upper[indx]) + carry == 1:
                        carry = 0
                        temp = 1
                    else:
                        temp = 0
                    if temp + int(bottom[len(bottom)-i-1]) > 1:
                        carry = 1
                        result = "0" + result
                    elif temp + int(bottom[len(bottom)-i-1]) == 1:
                        result = "1" + result
                    else:
                        result = "0" + result
            if carry == 1:
                result = "1" + result
                        
            return result
    * BETTER SOLUTION
    class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ''

        a = list(a)
        b = list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            result += str(carry %2)
            carry //= 2

        return result[::-1]

* 94 EASY BINARY TREE IN ORDER 
    '''
        Given the root of a binary tree, return the inorder traversal of its nodes' values.
        #NOTE: Inorder traversal of a B-tree means the order is LNR

        Input: root = [1,null,2,3]
        Output: [1,3,2]
        Example 2:

        Input: root = []
        Output: []
        Example 3:

        Input: root = [1]
        Output: [1]
    '''
    #SOLUTION 1 RECURSIVE 
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: 
            return []
        else:
            return [self.inorderTraversal(root.left)] + [root.val] + [self.inorderTraversal(root.right)]

    class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.dfs(root,result)

        def dfs(self, root, result)-> List[int]:
        if root == None:
            return []
        else:
            result = self.dfs(root.left, result)
            result.append(root.val)
            return self.dfs(root.right, result)

    class Solution:
        def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], [] 
        while root != None and stack != []:
            while root != None:
            stack.append(root)
            root = root.left 
            root = stack.pop() 
            result.append(root.val)
            root = root.right
        return result 

* 100 EASY SAME TREE 
    '''
    Given the roots of two binary trees p and q, write a function to check if they are the same or not.

    Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Input: p = [1,2], q = [1,null,2]
    Output: false
    '''

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True 
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

* 101 EASY SYMMETRICAL TREE 
    '''
        Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
        1
        /   \
    2      2
    /   \  /   \
    3    4 4    3
    Valid
    1
    /  \
    Valid
    '''

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def isSymmetric(self, root: Optional[TreeNode]) -> bool:
            return self.helper(root.left,root.right)
            
        def helper(self, one:[TreeNode], two:[TreeNode]) -> bool:
            if not one and not two:
                return True
            if not one or not two or  one.val != two.val: 
                return False
            if one.val != two.val:
                return False
            return self.helper(one.left,two.right) and self.helper(one.right, two.left)

* 108 EASY SORTED ARRAY TO HEIGHT BALANCED BINARY TREE
    '''
    Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.
    A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.
    Explanation: 
        Height Balanced means that each side of a tree or subtree cannot differe by a height of more than 1.
        So we cant have the left side with a height of 2 and the right side with a height of 4>
        This is mainly to prevent a tree from having all of the values on one side which would basically be a linked list not a tree

    [-10,-3,0,5,9]
        0
        /   \
    -10    5
    / \   / \ 
        -3     9
    '''

    class Solution:
        def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(l,r):
            if l > r: 
            return None 
            m = (l+r)//2
            root = TreeNode(nums[m])
            root.left = helper(l, m-1)
            root.right = helper(m+1,r)
            return root
        return helper(0, len(nums)-1)

* 101 IF BALANCED BINARY TREE
    '''
    Given a binary tree, determine if it is height-balanced.
    For this problem, a height-balanced binary tree is defined as:
    a binary tree in which the left and right subtrees of every node differ in height by no more than 1.
    '''

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right

    class Solution:
        def isBalanced(self, root: Optional[TreeNode]) -> bool:
            def helper(node, height)->(int,bool):
                if not node:
                    return (height,True)
                else:
                    left, leftBalanced = helper(node.left,height+1)
                    right, rightBalanced = helper(node.right,height+1)
                    if abs(left - right) > 1 or leftBalanced == False or rightBalanced == False:
                        return (height,False)
                    return (max(left,right),True)
            return helper(root,1)[1]

* 111 EASY MINDEPTH TREE
    '''
        Given a binary tree, find its minimum depth.
        The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
        Note: A leaf is a node with no children. 
    '''

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def minDepth(self, root: Optional[TreeNode]) -> int:
            if not root: return 0
            if not root.left and not root.right:
                return 1
            left = self.minDepth(root.left)
            right = self.minDepth(root.right)
            if left == 0: return right + 1 
            elif right == 0: return left + 1
            else:
                return 1 + min(left, right)

* 112 EASY PATH SUM
    '''
    Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that 
    adding up all the values along the path equals targetSum. A leaf is a node with no children. 
    '''

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
        def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
            if not root:
                return False
            diff = targetSum-root.val
            if not root.left and not root.right:
                return diff == 0
            left = self.hasPathSum(root.left, diff)
            right = self.hasPathSum(root.right, diff)
            return left or right1

* 118 EASY PASCALS TRIANGLE
    '''
        118E
        Given an integer numRows, return the first numRows of Pascal's triangle.
        In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

        Input: numRows = 5                                    Input: numRows = 1
        Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]     Output: [[1]] 
    '''

    class Solution:
        def generate(self, numRows: int) -> List[List[int]]:
            triangle = [[1]]
            for i in range(1,numRows):
                temp = [0]+triangle[-1]+[0]
                row=[]
                for elm in range(len(temp)-1):
                    row.append(temp[elm]+temp[elm+1])
                triangle.append(row)
            return triangle

* 121 EASY BEST TIME TO BUY AND SELL STOCK 
    '''
        You are given an array prices where prices[i] is the price of a given stock on the ith day.
        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0. 
        
        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    '''

    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            profit = 0
            left = 0
            right = 1
            while right < len(prices):
                if prices[left] < prices[right]:
                    profit = max(profit,prices[right] - prices[left])
                else:
                    left = right
                right += 1
            return profit

* 125 EASY VALID PALINDROME 
    '''
        Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
        Input: s = "A man, a plan, a canal: Panama"
        Output: true
        Explanation: "amanaplanacanalpanama" is a palindrome.
    '''
    
    class Solution:
        def isPalindrome(self, s: str) -> bool:
            left = 0
            right = len(s) - 1
            while left < right:
                if s[left].isalnum():
                    if s[right].isalnum():
                        if s[left].upper() == s[right].upper():
                            left += 1
                            right -= 1
                        else:
                            return False
                    else:
                        right -= 1
                else:
                    left += 1
            return True

* 136 EASY SINGLE NUMBER 
    '''
        Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
        You must implement a solution with a linear runtime complexity and use only constant extra space.
        
        Example 1:
        Input: nums = [2,2,1]
        Output: 1
        
        Example 2:
        Input: nums = [4,1,2,1,2]
        Output: 4
    '''
    class Solution:
        def singleNumber(self, nums: List[int]) -> int:
            a = 0
            for i in nums:
                a ^= i
            return a

* 141 EASY LINKED LIST CYCLE 
    '''
        Given head, the head of a linked list, determine if the linked list has a cycle in it.
        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
        Internally, pos is used to denote the index of the node that tail's next pointer is connected to. 
        Note that pos is not passed as a parameter.
        Return true if there is a cycle in the linked list. Otherwise, return false. 
        Input: head = [3,2,0,-4], pos = 1
        Output: true
        Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
    '''
    
    class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
        return False
        slow = head 
        fast = head.next
        while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
        return True

    #Summary
    #1 This is a fast and slow method, the slow will move at a regular pace
    # the fast will move 2x faster than slow 
    #If fast and slow ever equal each other that means their is a cycle

* 144 BINARY TREE PREORDER TRAVERSAL 
    '''
        144 BInary Tree Preorder Traversal
        Given the root of a binary tree, return the preorder traversal of its nodes' values. 
    '''
    class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
        return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right
    #Summary 
    #1 If we reach an empty node return an empty list 
    #2 Split the root into left and right 
    #3 return in the order you want, in this case preorder 
* 160 INTERSECTION OF TWO NODES
    '''
        Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 
        If the two linked lists have no intersection at all, return null.
        For example, the following two linked lists begin to intersect at node c1: 
        a1 -> a2 \ 
                    c1 -> c2 -> c3
        b1 -> b2 /
        return c1

        a1 -> a2 ->
        b1 -> b2 ->
        return None
    '''
    class Solution:
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
            p1 = headA
            p2 = headB
            while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
            return p1

* 167 TWO SUM II INPUT-ARRAY IS SORTER
    '''
        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
        find two numbers such that they add up to a specific target number. 
        Let these two numbers be numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.
        Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.
        The tests are generated such that there is exactly one solution. You may not use the same element twice.
    '''

    class Solution:
        def twoSum(self, numbers: List[int], target: int) -> List[int]:
            l,r = 0, len(numbers)-1
            while l < r:
            if numbers[l]+numbers[r] == target:
                return [l+1,r+1]
            elif numbers[l]+numbers[r] > target:
                r -= 1
            else:
                l += 1

* 168 EXCEL SHEET COLUMN TITLE

    ''' 
        168 Excel Sheet Column Title 
        Given an integer columnNNumber return its corresponding column title as it appears in an Excel sheet.
        Example 1:
        Input: columnNumber = 1
        Output: "A"

        Example 2:
        Input: columnNumber = 28
        Output: "AB"
        
        Example 3:
        Input: columnNumber = 701
        Output: "ZY"
        
        Example 4:
        Input: columnNumber = 2147483647
        Output: "FXSHRXW"
    '''

    class Solution:
        def convertToTitle(self, columnNumber: int) -> str:
            result = ""
            while columnNumber:
            result += chr(ord('A') + (columnNumber-1) % 26)
            columnNumber = (columnNumber-1) // 26
            return result[::-1]

* 169 MAJORITY ELEMENT
    '''
        Given an array nums of size n, return the majority element.
        The majority element is the element that appears more than ⌊n / 2⌋ times. 
        You may assume that the majority element always exists in the array.

        Example 1:
        Input: nums = [3,2,3]
        Output: 3
        
        Example 2:
        Input: nums = [2,2,1,1,1,2,2]
        Output: 2
    '''

    class Solution:
        def majorityElement(self, nums: List[int]) -> int: 
            counter = 0
            elm = None  
            for i in nums:
            if counter == 0:
                elm = i
                counter += 1
            elif elm == i:
                counter += 1
            else:
                counter -= 1
            return elm