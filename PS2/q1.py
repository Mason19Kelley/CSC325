#Let T be an ordered tree with more than one node. Is it possible that the
#preorder traversal of T visits the nodes in the same order as the postorder
#traversal of T? If so, give an example; otherwise, explain why this cannot
#occur. Likewise, is it possible that the preorder traversal of T visits the
#nodes in the reverse order of the postorder traversal of T? If so, give an
#example; otherwise, explain why this cannot occur.

''' 
No, with preorder traversal the root is visited first followed by the left childed followed by the right.
While with post order traversal the left child is visited first then the right chold followed by the root.
This means that the root will be visited last in the postorder traversal while the root will be visited
first in the preorder traversal. 

Yes, if the tree only has two nodes it is possible for the preorder traversal to be the reverse of the 
postorder traversal. Preorder would be root followed by child and postorder would be child followed by root
'''
