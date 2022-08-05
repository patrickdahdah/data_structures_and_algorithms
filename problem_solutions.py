
import collections


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    required = {}
    for i in range(len(nums)):
        if target - nums[i] in required:
            return [required[target - nums[i]], i]
        else:
            required[nums[i]] = i


input_list = [2, 8, 12, 15]

print(twoSum(input_list, 20))


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode):
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
