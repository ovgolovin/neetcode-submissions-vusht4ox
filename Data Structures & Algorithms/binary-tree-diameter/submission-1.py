from dataclasses import dataclass, field

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

@dataclass
class Result:
    height: int = None

@dataclass
class Job:
    node: TreeNode
    result: Result = field(default_factory=Result)
    left_result: Result = field(default_factory=Result)
    right_result: Result = field(default_factory=Result)


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        job = Job(root)
        stack = []
        max_diam = 0
        while job or stack:
            if job:
                stack.append(job)
                if job.node:
                    par = job
                    job = Job(job.node.left)
                    par.left_result = job.result
                else:
                    job = None
            else:
                peek = stack[-1]
                if peek.node is None:
                    stack.pop()
                    peek.result.height = 0
                elif peek.right_result.height is None:
                    job = Job(peek.node.right)
                    peek.right_result = job.result
                else:
                    stack.pop()
                    peek.result.height = max(peek.left_result.height, peek.right_result.height) + 1
                    max_diam = max(max_diam, peek.left_result.height + peek.right_result.height)
        return max_diam


        