def marker(data,marker_size):
	queue = []

	for item,c in enumerate(data):
		queue.append(c)

		if len(queue) > marker_size:
			queue.pop(0)

		if len(set(queue)) == marker_size:
			return item+1


def main():
	f=open('input.txt','r')

	inp = f.read().strip()

	mark = marker(inp,14)
	print(mark)







if __name__ == '__main__':
	main()