* 1 EASY TWO SUM
    '''
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        You can return the answer in any order.

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Output: Because nums[0] + nums[1] == 9, we return [0, 1].

        Input: nums = [3,2,4], target = 6
        Output: [1,2]
    ''' 
    class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dix = {} 
        for i in range(len(nums)):
        diff = target-nums[i]
        if diff in dix:
            return [dix[diff],i]
        else:
            dix[nums[i]] = i

* 9 EASY PALINDROME NUMBER 
    '''
        Given an integer x, return true if x is palindrome integer.
        An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not. 
        
        Input: x = 121
        Output: true

        Input: x = -121
        Output: false
        Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

        Input: x = 10
        Output: false
        Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    '''

    class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        s = str(x)
        l,r = 0, len(s)-1
        while l < r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1
        return True

    class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
        return False 
        inverted = 0
        original = x
        while x > 0:
        inverted *= 10
        inverted += (x%10)
        x = x//10
        return inverted == original  

* 13 EASY ROMAN TO INTEGER 
    ''' 
        Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. 

        Input: s = "III"
        Output: 3 

        Input: s = "IX"
        Output: 9

        Input: s = "LVIII"
        Output: 58
        Explanation: L = 50, V= 5, III = 3.
    '''

    class Solution:
    def romanToInt(self, s: str) -> int:
        converter = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = converter[s[0]]
        for i in range(1,len(s)):
        previous = converter[s[i-1]]
        current = converter[s[i]]
        if previous < current:
            result -= previous * 2
        result += current
        return result

* 14 EASY LONGEST PREFIX 
    '''
        Write a function to find the longest common prefix string amongst an array of strings.
        If there is no common prefix, return an empty string "".

        Input: strs = ["flower","flow","flight"]
        Output: "fl"

        Input: strs = ["dog","racecar","car"]
        Output: ""
    '''

    class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
            return res
        res += strs[0][i]
        return res

* 20 VALID PARENTHESES 
    '''
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.

    '''
    class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        dix = {'(':')', '{':'}', '[':']'}
        st = []
        for i in s:
        if i == '(' or i == '{' or i == '[':
            st.append(i)
        elif len(st) == 0 or dix[st[-1]] != i:
            return False 
        else:
            st.pop()
        return len(st) == 0

* 21 MERGE TWO SORTED LINKED LISTS 
    '''
        Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists. 
        
        Input: l1 = [1,2,4], l2 = [1,3,4]   Input: l1 = [], l2 = []   Input: l1 = [], l2 = [0]
        Output: [1,1,2,3,4,4]               Output: []                Output: [0]
    '''
    class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = res = ListNode(0)
        while l1 or l2:
            if not l1:
                res.next = l2
                l2 = l2.next
            elif not l2:
                res.next = l1
                l1 = l1.next
            else:
                if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
                else:
                res.next = l2
                l2 = l2.next
            res = res.next
        return head.next

* 26 EASY REMOVE DUPLICATES FROM SORTED ARRAY 
    ''' 
        Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
        The relative order of the elements should be kept the same.
        Since it is impossible to change the length of the array in some languages, 
        you must instead have the result be placed in the first part of the array nums. 
        More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. 
        It does not matter what you leave beyond the first k elements.
        Return k after placing the final result in the first k slots of nums.
        Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.
    '''

    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            idx = 0
            for i in nums:
            if i != nums[idx]:
                idx += 1
                nums[idx] = i 
            return idx+1

* 28 EASY IMPLEMENT STR
    '''
        Implement strStr().
        Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

        Input: haystack = "hello", needle = "ll"
        Output: 2

        Input: haystack = "aaaaa", needle = "bba"
        Output: -1

        Input: haystack = "", needle = ""
        Output: 0
    ''' 
    class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0: return 0
        if len(needle) > len(haystack): return -1
        for i in range(len(haystack)):
            end = len(needle) + i
            if haystack[i:end] == needle:
            return i
        return -1

* 35 EASY SEARCH INSERT POSITION
    '''
        Given a sorted array of distinct integers and a target value, return the index if the target is found. 
        If not, return the index where it would be if it were inserted in order.
        You must write an algorithm with O(log n) runtime complexity.
        
        Input: nums = [1,3,5,6], target = 5
        Output: 2

        Input: nums = [1,3,5,6], target = 2
        Output: 1

        Input: nums = [1,3,5,6], target = 7
        Output: 4
    '''

    class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
            return m
            elif nums[m] < target:
            l = m+1
            elif nums[m] > target:
            r = m-1
        return l

* 53 MAXIMUM SUBARRAY 
    '''
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
        A subarray is a contiguous part of an array. 

        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.

        Input: nums = [5,4,-1,7,8]
        Output: 23
    '''

    class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        current = nums[0]
        for i in nums[1:]:
        if current+i < i:
            current = i
        else:
            current += i
        largest = max(largest,current)
        return largest

* 66 EASY PLUS ONE 
    '''
        You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
        The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
        Increment the large integer by one and return the resulting array of digits.

        Input: digits = [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
        Incrementing by one gives 123 + 1 = 124.
        Thus, the result should be [1,2,4].
    '''
    
    #No String Conversion
    class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
        if digits[i] + carry > 9:
            digits[i] = 0
            carry = 1
        else:
            digits[i] += carry
            carry = 0
        if carry: 
        return [1]+digits
        return digits

* 67 EASY ADD BINARY 
    '''
        Given two binary strings a and b, return their sum as a binary string.
        Input: a = "11", b = "1"    Input: a = "1010", b = "1011"
        Output: "100"               Output: "10101"
    '''

    #Using a Stack
    class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        result = ''
        carry = 0
        while a or b:
        if a:
            carry += int(a.pop())
        if b:
            carry += int(b.pop())
        result = str(carry%2) + result
        carry //= 2
        if carry:
        return '1' + result
        return result

* 69 EASY SQRT 
    '''
        Given a non-negative integer x, compute and return the square root of x.
        Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
        Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5. 
        
        Input: x = 4  Input: x = 8
        Output: 2     Output: 2
    '''
        
    class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
        return x
        left, right = 2, x
        while left < right:
        mid = (left+right)//2
        if mid*mid == x: return mid
        elif mid*mid > x: right = mid
        elif mid*mid < x: left = mid + 1
        return left - 1

* 70 EASY CLIMBING STAIRS
    '''
        You are climbing a staircase. It takes n steps to reach the top.
        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top? 
        
        Input: n = 2
        Output: 2
        Explanation: There are two ways to climb to the top.
        1. 1 step + 1 step
        2. 2 steps
    '''
    #O(N) Dynamic Programming Memoization
    class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 0, 1
        for i in range(n):
        one, two = two, one+two
        return two

* 83 REMOVE DUPLICATE SORTED LL
    '''
        Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
        1->1->2->3->3 = 1->2->3
    '''
    class Solution:
        def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            if curr:
            while curr.next:
                if curr.val == curr.next.val:
                curr.next = curr.next.next
                else:
                curr = curr.next
            return head

* 88 EASY MERGE SORTED ARRAY
    '''
        You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
        representing the number of elements in nums1 and nums2 respectively.
        Merge nums1 and nums2 into a single array sorted in non-decreasing order.
        The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
        To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
        and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
    '''
    class Solution:
    def merge(self, nums1, m, nums2, n):
        while m > 0 and n > 0:
        if nums1[m-1] >= nums2[n-1]:
            nums1[m + n - 1] = nums1[m-1]
            m-=1
        else:
            nums1[m + n - 1] = nums2[n-1]
            n-=1
        while n > 0:
        nums1[m+n-1] = nums2[n-1]
        n-=1

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

* 171 EXCEL SHEET COLUMN NUMBER
    '''
        Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
        Example 1:
        Input: columnTitle = "A"
        Output: 1

        Example 2:
        Input: columnTitle = "AB"
        Output: 28

        Example 3:
        Input: columnTitle = "ZY"
        Output: 701

        Example 4:
        Input: columnTitle = "FXSHRXW"
        Output: 2147483647
    '''

    class Solution:
        def titleToNumber(self, columnTitle: str) -> int:
            result = 0
            for i in columnTitle:
            result = 1 + (result*26) + (ord(i)-65) % 26
            return resul

* 190 REVERSE BITS
    '''
        Reverse bits of a given 32 bits unsigned integer. 
        Input: n = 00000010100101000001111010011100
        Output:    964176192 (00111001011110000010100101000000)
    '''
    class Solution:
        def reverseBits(self, n: int) -> int:
            res = 0
            for i in range(32):
            bit = (n >> i) & 1
            res = res | bit << (31-i)
            return res

* 191 NUMBER OF 1 BITS 
    ''' 
        Write a function that takes an unsigned integer and returns the number of '1' bits it has
        Input: n = 00000000000000000000000000001011
        Output: 3

        Input: n = 11111111111111111111111111111101
        Output: 31
    ''' 
    class Solution:
        def hammingWeight(self, n: int) -> int:
            count = 0
            for i in range(32):
                bit = (n >> i) & 1
                if bit == 1:
                    count += 1
            return count
* 226 INVERT BINARY TREE
    '''
        Given the root of a binary tree, invert the tree, and return its root.
        
        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]
        
        Input: root = [2,1,3]
        Output: [2,3,1]
    '''

    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
    class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    #Summary 
    #1 Use python swap short hand to swap the left side and the right side 
    #2 Return the original root but now the tree is inverted

* 202 HAPPY NUMBER 
    '''
        Write an algorithm to determine if a number n is happy.
        A happy number is a number defined by the following process:
        Starting with any positive integer, replace the number by the sum of the squares of its digits.
        Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
        Those numbers for which this process ends in 1 are happy.
        Return true if n is a happy number, and false if not.
        
        Input: n = 19
        Output: true
        Explanation:
        12 + 92 = 82
        82 + 22 = 68
        62 + 82 = 100
        12 + 02 + 02 = 1
    '''
    class Solution:
        def isHappy(self, n: int) -> bool:
            slow = self.squareSum(n)
            fast = self.squareSum(self.squareSum(n))
            while slow!=fast and fast!= 1:
            slow = self.squareSum(slow)
            fast = self.squareSum(self.squareSum(fast))
            return fast == 1
        def squareSum(self, n: int) -> int:
            res = 0
            while n:
            res += (n%10)**2
            n = n//10
            return res

* 203 REMOVE LINKED LIST ELEMENTS
    '''
        Given the head of a linked list and an integer val, 
        remove all the nodes of the linked list that has Node.val == val, and return the new head.

        Example 1:
        Input: head = [1,2,6,3,4,5,6], val = 6
        Output: [1,2,3,4,5]
        
        Example 2:
        Input: head = [], val = 1
        Output: []
        
        Example 3:
        Input: head = [7,7,7,7], val = 7
        Output: []
    '''
    # Definition for singly-linked list.
    # class ListNode:
    #     def __init__(self, val=0, next=None):
    #         self.val = val
    #         self.next = next
    class Solution:
        def removeElements(self, head, val):
            dummy_head = ListNode(-1)
            dummy_head.next = head
            head = dummy_head
            current = head
            
            while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next                    
            return head.next

* 205 ISOMORPHIC STRINGS
    '''
        Given two strings s and t, determine if they are isomorphic.
        Two strings s and t are isomorphic if the characters in s can be replaced to get t.
        All occurrences of a character must be replaced with another character while preserving the order of characters. 
        No two characters may map to the same character, but a character may map to itself.
        
        Example 1:
        Input: s = "egg", t = "add"
        Output: true
        
        Example 2:
        Input: s = "foo", t = "bar"
        Output: false
        
        Example 3:
        Input: s = "paper", t = "title"
        Output: true
    '''
    class Solution:
        def isIsomorphic(self, s: str, t: str) -> bool:
            m1, m2 = [0]*256, [0]*256
            for i in range(len(s)):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            m1[ord(s[i])] = i+1
            m2[ord(t[i])] = i+1
            return True

* 206 REVERSE LINKED LIST
    '''
        Given the head of a singly linked list, reverse the list, and return the reversed list.
    '''
    class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
        temp = current.next 
        current.next = prev 
        prev = current 
        current = temp
        return prev

* 217 CONTAINS DUPLICATE
    '''
        Given an integer array nums, return true if any value appears at least twice in the array, 
        and return false if every element is distinct.
    '''
    class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

* 226 INVERT BINARY TREE
    '''
        226 INVERT BINARY TREE 
        Given the root of a binary tree, invert the tree, and return its root.
        
        Input: root = [4,2,7,1,3,6,9]
        Output: [4,7,2,9,6,3,1]
        
        Input: root = [2,1,3]
        Output: [2,3,1]
    '''
    class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

* 228 SUMMARY RANGES
    '''
        You are given a sorted unique integer array nums.
        Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
        That is, each element of nums is covered by exactly one of the ranges, 
        and there is no integer x such that x is in one of the ranges but not in nums.
        
        Each range [a,b] in the list should be output as:
            "a->b" if a != b
            "a" if a == b
    '''
    
    class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        for num in nums:
        if not result or result[-1][-1]+1 != num:
            result.append([num])
        else:
            result[-1].append(num)
        return [str(i[0]) + "->" + str(i[-1]) if len(i) > 1 else str(i[0]) for i in result]

* 231 POWER OF TWO
    '''
        Given an integer n, return true if it is a power of two. Otherwise, return false.
        An integer n is a power of two, if there exists an integer x such that n == 2^x.
    '''

    class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return not n&n-1 if n else False

* 232 IMPLEMENT QUEUE USING STACKS

'''
  Implement a first in first out (FIFO) queue using only two stacks. 
  The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
  Implement the MyQueue class:
  void push(int x) Pushes element x to the back of the queue.
  int pop() Removes the element from the front of the queue and returns it.
  int peek() Returns the element at the front of the queue.
  boolean empty() Returns true if the queue is empty, false otherwise.
'''
class MyQueue:
  def __init__(self):
    self.new = []
    self.old = []

  def push(self, x: int) -> None:
    self.new.append(x)

  def pop(self) -> int:
    if not self.old:
      while self.new:
        self.old.append(self.new.pop())
    return self.old.pop()

  def peek(self) -> int:
    if not self.old:
      while self.new:
        self.old.append(self.new.pop())
    return self.old[-1]

  def empty(self) -> bool:
    return (len(self.new) + len(self.old)) == 0

* 234 PALINDROME LINKED LIST
    '''
        Given the head of a singly linked list, return true if it is a palindrome.
        Input: head = [1,2,2,1]   Input: head = [1,2]
        Output: true              Output: true
    ''' 

    class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid, end = head, head 
        #Find mid point
        while end and end.next:
        mid = mid.next 
        end = end.next.next 
        #Reverse right side of the LL
        prev = None
        while mid:
        temp = mid.next
        mid.next = prev 
        prev = mid
        mid = temp
        #Compare left and right sides
        left, right = head, prev
        while right: 
        if left.val != right.val:
            return False
        left, right = left.next, right.next
        return True

* 235 LOWEST COMMON ANCESTOR OF A BINARY SEARCH TREE
'''
  Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
  According to the definition of LCA on Wikipedia: 
  “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
  (where we allow a node to be a descendant of itself).”
'''

class Solution:
  def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if p.val > root.val and q.val > root.val:
      return self.lowestCommonAncestor(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
      return self.lowestCommonAncestor(root.left, p, q)
    else:
      return root 

* 237 DELETE NODE IN A LINKED LIST

'''
  Write a function to delete a node in a singly-linked list. 
  You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
  It is guaranteed that the node to be deleted is not a tail node in the list.
'''

class Solution:
  def deleteNode(self, node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    node.val = node.next.val 
    node.next = node.next.next

* 258 ADD DIGITS
    '''
        Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
        Input: n = 38 
        Output: 2
        Explanation: 3+8->11 1+1->2
    '''

    class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0
        return num % 9 or 9

* 263 UGLY NUMBER 
'''
  An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
  Given an integer n, return true if n is an ugly number.
  
  Input: n = 6
  Output: true
  Explanation: 6 = 2 × 3
'''
class Solution:
  def isUgly(self, n: int) -> bool:
    for p in [2, 3, 5]:
      while (n % p == 0) and (0 < n):
        n /= p
    return n == 1

* 268 MISSING NUMBER 
    '''
        Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    '''
    class Solution:
        def missingNumber(self, nums: List[int]) -> int:
            return len(nums)*(len(nums)+1)//2 - sum(nums)

* 278 FIRST BAD VERSION 
    '''
        You are a product manager and currently leading a team to develop a new product. 
        Unfortunately, the latest version of your product fails the quality check. 
        Since each version is developed based on the previous version, all the versions after a bad version are also bad.
        Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
        You are given an API bool isBadVersion(version) which returns whether version is bad. 
        Implement a function to find the first bad version. You should minimize the number of calls to the API.
    '''
    class Solution:
        def firstBadVersion(self, n):
            l, r = 0, n
            while l < r:
            mid = (l+r)//2      
            if isBadVersion(mid):
                r = mid
            else:
                l = mid + 1
            return l

* 278 MOVE ZEROS 
    '''
        Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
        Note that you must do this in-place without making a copy of the array. 
    '''
    class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        zero = 0
        for i in range(len(nums)):
        if nums[zero] == 0 and nums[i] != 0:
            nums[zero], nums[i] = nums[i], nums[zero]
        if nums[zero] != 0:
            zero +=1

* 290 WORD PATTERN 
    '''
        Given a pattern and a string s, find if s follows the same pattern.
        Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
        Input: pattern = "abba", s = "dog cat cat dog"
        Output: true

        Input: pattern = "abba", s = "dog cat cat fish"
        Output: false
    '''
    class Solution:
        def wordPattern(self, pattern: str, s: str) -> bool:
            words = s.split(" ")
            if len(words) != len(pattern): return False
            return len(set(zip(pattern,words))) == len(set(words)) == len(set(pattern))

* 303 RANGE SUM QUERY 
    '''
        Given an integer array nums, handle multiple queries of the following type:
            Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
        Implement the NumArray class:
            NumArray(int[] nums) Initializes the object with the integer array nums.
            int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
            (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
    '''
    class NumArray:
        def __init__(self, nums: List[int]):
            self.range = [0]+list(accumulate(nums))

        def sumRange(self, left: int, right: int) -> int:
            return self.range[right+1] - self.range[left]

* 326 POWER OF THREE 
    '''
        Given an integer n, return true if it is a power of three. Otherwise, return false.
        An integer n is a power of three, if there exists an integer x such that n == 3x. 

        Input: n = 27   Input: n = 0    Input: n = 45
        Output: true    Output: false   Output: false
    '''

    class Solution:
        def isPowerOfThree(self, n: int) -> bool:
            p = 0
            while 3**p < n:
            p += 1
            return 3**p == n

    class Solution:
        def isPowerOfThree(self, n: int) -> bool:
            max = 3**19
            return n > 0 and max%n == 0

* 338 EASY COUNTING BITS 
    '''
        Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), 
        ans[i] is the number of 1's in the binary representation of i.
    '''
    class Solution:
        def countBits(self, n: int) -> List[int]:
            dp = [0]
            offset = 1
            for i in range(1,n+1):
            if offset * 2 == i:
                offset = i 
            dp.append(1+dp[i-offset])
            return dp

* 342 EASY POWER OF FOUR 
    '''
        Given an integer n, return true if it is a power of four. Otherwise, return false.
        An integer n is a power of four, if there exists an integer x such that n == 4x.
        Input: n = 16   Input: n = 5    Input: n = -123
        Output: true    Output: false   Output: false
    '''

    #Mathematical
    class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n>0 and log(n,4).is_integer()

    #Brute Force
    class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n>1:
        n = n/4
        return n == 1

* 344 EASY REVERSE STRING 
    '''
        Write a function that reverses a string. The input string is given as an array of characters s. 
        Input: s = ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
    '''

    class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1
        while l < r:
        s[l], s[r] = s[r], s[l]
        l, r = l+1, r-1

* 345 REVERSE VOWELS OF STRING
    '''
        Given a string s, reverse only all the vowels in the string and return it.
        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

        Input: s = "hello"  Input: s = "leetcode"
        Output: "holle"     Output: "leotcede"
    '''
    class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        s = list(s)
        vowels = set('aeiouAEIOU')
        while l < r:
        if s[l] in vowels and s[r] in vowels:
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        elif s[l] in vowels:
            r-=1
        elif s[r] in vowels:
            l+=1
        else:
            l, r = l+1, r-1
        return ''.join(s)