import graphlab

Class DocumentRet:
	
	def __init__(path):
	_self.data = graphlab.SFrame(path)

	def documentRetrieve():
		print(_self.data())
		obama = people[people['name'] == 'Digby Morrell']
		print (obama['text'])	

	def main():
		documentRetrieve()

	if __name__ == "__main__":
		main()
