def marker(data):
	queue = []

	for item,c in enumerate(data):
		queue.append(c)

		if len(queue) > 4:
			queue.pop(0)

		if len(set(queue)) == 4:
			return item+1


def main():
	f=open('input.txt','r')

	inp = f.read().strip()

	mark = marker(inp)
	print(mark)







if __name__ == '__main__':
	main()