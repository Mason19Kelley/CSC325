
# from __future__ import print_function
 
class Node(object):
	def __init__(self):
		self.edges = {} # edges (or forward links)
		self.link = None # suffix link (backward links)
		self.len = 0 # the length of the node
 
class Eertree(object):
	# initializes base roots of 0 and -1 before adding the palindrome character nodes to the graph
	def __init__(self):
		self.nodes = []
		# two initial root nodes
		self.root_odd = Node() #odd length root node, or node -1
		self.root_even = Node() #even length root node, or node 0
 
		# Initialize empty tree
		self.root_odd.link = self.root_even.link = self.root_odd;
		self.root_odd.len = -1
		self.root_even.len = 0
		self.S = [0] # accumulated input string, T=S[1..i]
		self.maxSufT = self.root_even # maximum suffix of tree T



	def get_max_suffix_pal(self, startNode, a):
		# We traverse the suffix-palindromes of T in the order of decreasing length.
		# For each palindrome we read its length k and compare T[i-k] against a
		# until we get an equality or arrive at the -1 node.
		u = startNode
		i = len(self.S)
		k = u.len
		while id(u) != id(self.root_odd) and self.S[i - k - 1] != a:
			assert id(u) != id(u.link) #Prevent infinte loop
			u = u.link
			k = u.len
 
		return u
 
	def add(self, a):
 
		# We need to find the maximum suffix-palindrome P of Ta
		# Start by finding maximum suffix-palindrome Q of T.
		# To do this, we traverse the suffix-palindromes of T
		# in the order of decreasing length, starting with maxSuf(T)
		Q = self.get_max_suffix_pal(self.maxSufT, a)
 
		# We check Q to see whether it has an outgoing edge labeled by a.
		createANewNode = not a in Q.edges
 
		if createANewNode:
			# We create the node P of length Q+2
			P = Node()
			self.nodes.append(P)
			P.len = Q.len + 2
			if P.len == 1:
				# if P = a, create the suffix link (P,0)
				P.link = self.root_even
			else:
				# It remains to create the suffix link from P if |P|>1. Just
				# continue traversing suffix-palindromes of T starting with the suffix 
				# link of Q.
				P.link = self.get_max_suffix_pal(Q.link, a).edges[a]
 
			# create the edge (Q,P)
			Q.edges[a] = P
 
		#P becomes the new maxSufT
		self.maxSufT = Q.edges[a]
 
		#Store accumulated input string
		self.S.append(a)
 
		return createANewNode
 
	def get_sub_palindromes(self, nd, nodesToHere, charsToHere, result):
		#Each node represents a palindrome, which can be reconstructed
		#by the path from the root node to each non-root node.
 
		#Traverse all edges, since they represent other palindromes
		for lnkName in nd.edges:
			nd2 = nd.edges[lnkName] #The lnkName is the character used for this edge
			self.get_sub_palindromes(nd2, nodesToHere+[nd2], charsToHere+[lnkName], result)
 
		#Reconstruct based on charsToHere characters.
		if id(nd) != id(self.root_odd) and id(nd) != id(self.root_even): #Don't print for root nodes
			tmp = "".join(charsToHere)
			if id(nodesToHere[0]) == id(self.root_even): #Even string
				assembled = tmp[::-1] + tmp
			else: #Odd string
				assembled = tmp[::-1] + tmp[1:]
			result.append(assembled)



if __name__ == "__main__":
	palindrome = "eertree"
	eertree = Eertree()
	for char in palindrome:
		eertree.add(char)
 	# prints nodes in the graph excluding the root nodes
	print ("Number of sub-palindromes:", len(eertree.nodes))
 
	#Traverse tree to find sub-palindromes
	result = []

	eertree.get_sub_palindromes(eertree.root_odd, [eertree.root_odd], [], result) #Odd length words
	eertree.get_sub_palindromes(eertree.root_even, [eertree.root_even], [], result) #Even length words
	print ("Sub-palindromes:", result)