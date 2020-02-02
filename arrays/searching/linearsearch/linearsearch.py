def search_element(arr, k):
	for index, value in enumerate(arr):
		if value==k:
			print(index)



arr = [1, 2, 3, 4, 5, 10]
k = 10
search_element(arr, 10)