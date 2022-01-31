# Programming Challenge: Given a binary search tree T, write a Python function that returns an AVL tree with
# the same node values.
# Use the following binary search tree node class:
class tree_node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.value)


# In other words, you can freely use p.value, p.left, and p.right for a node p in your function to access the value,
# left child, and right child of p.
# If there is more than one answer, your function can return any of them.
# Example:
# 1
#    2
#       3
#          4
# is balanced into
#
# 2
#
# 1  3
#       4

# Hint: you can first do some preprocessing and then use the same approach as we did in class programming challenge.
# first we will find the inorder of the tree then convert that to a balanced bst
def inorder(root, arr=[]):
	if root == None:
		return
	else:
		inorder(root.left, arr)
		arr.append(root.value)
		inorder(root.right, arr)


def in2avl(arr):
	if len(arr) > 0:
		mindex = (len(arr)-1) // 2

		return tree_node(arr[mindex], in2avl(arr[0:mindex]), in2avl(arr[mindex + 1:len(arr)]))


if __name__ == "__main__":
	arr = []
	head = tree_node(1, None, tree_node(2, None, tree_node(3, None, tree_node(4))))
	inorder(head, arr)
	print(arr)
	head2 = in2avl(arr)
	print(head2)
	print(head2.left)
	print(head2.right)
	print(head2.right.right)
