import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	col=len(a[0])
	row=len(a)
	shape=col * row
	a= np.array(a)
	if shape == new_shape[0] * new_shape[1]:
		reshaped_matrix = a.reshape(new_shape)
		return reshaped_matrix
	else:
		return []