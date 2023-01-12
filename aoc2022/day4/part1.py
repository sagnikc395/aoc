
def main():
	with open('test.txt','r') as f:
		p=[line.strip() for line in f]

	print(p)
	


	
if __name__=='__main__':
	main()


