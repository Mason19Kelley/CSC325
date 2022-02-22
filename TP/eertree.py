
class Node(object):
    # Node Constructor
    def __init__(self):
        self.edges = {} # forward links
        self.link = None # suffix link
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
        self.S = [0] # list that stores all chars in eertree
        self.maxSufT = self.root_even # maximum suffix of tree T, initially 0



    def get_max_suffix_pal(self, startNode, a):
        node = startNode
        i = len(self.S)
        k = node.len
        # navigate through the graph until we reach the node or -1
        while id(node) != id(self.root_odd) and self.S[i - k - 1] != a:
            node = node.link
            k = node.len
        return node
 
    def add(self, a):
        # Start by finding maximum suffix-palindrome Q of T.
        Q = self.get_max_suffix_pal(self.maxSufT, a)
        # We check Q to see whether or not it has an edge to a
        NewNode = not a in Q.edges

        if NewNode:
            # create the new node
            P = Node()
            self.nodes.append(P)
            P.len = Q.len + 2
            if P.len == 1:
                # if the length of the new node is 1, we must connect it's backwards link to 0
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
 
        return NewNode
 
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
