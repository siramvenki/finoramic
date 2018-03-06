# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers'
    @staticmethod
    
    def pathSum( A, B):
        result=[]
        temp=[]
        if A is None :
            return 
        
        def paths(node,B,result,temp):
            if node is None:
                return 0
            cval=node.val
            temp.append(cval)
            if(node.left is None and node.right is None):
                if(B-cval==0):
                    result.append(list(temp))
            paths(node.left,B-node.val,result,temp)
            paths(node.right,B-node.val,result,temp)
            temp.pop()
        paths(A,B,result,temp)
        return result
    
