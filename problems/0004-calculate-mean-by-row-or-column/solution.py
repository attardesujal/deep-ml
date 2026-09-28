import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

	def row_mean(matrix):
		means=np.mean(matrix, axis=1)
		return means
	
	def col_mean(matrix):
		means=np.mean(matrix, axis=0)
		return means

	if mode == 'row':
		means=row_mean(matrix)
	else:
		means=col_mean(matrix)

	return means