# Trie a retrieval data structure

class tnode:
	def __init__(self):
		self.children=[None]*26 # each for one alphabet
		self.iseow=False        # check for end of word
		
class trie:
	def __init__(self):
		self.root=self.get_node()
		
	def get_node(self):
		return tnode()
		
	def char_index(self,c):     # to find the index of a character
		return ord(c)-ord('a')
		
	def insert(self,word):
		cur=self.root
		length=len(word)
		for l in range(length):
			index=self.char_index(word[l])
			if not cur.children[index]:
				cur.children[index]=self.get_node()
			cur=cur.children[index]
		cur.iseow=True
		
	def search(self,word):
		cur=self.root
		length=len(word)
		for i in range(length):
			index=self.char_index(word[i])
			if not cur.children[index]:
				return False
			cur=cur.children[index]
		return cur!=None and cur.iseow
		
if __name__=='__main__':
	t=trie()
	k=['boss','hello','money','whassup']
	for i in k:
		t.insert(i)
	for i in ['india','boss','code','money']:
		print(t.search(i))
