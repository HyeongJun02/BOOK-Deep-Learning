# %% [3.3.1] 다차원 배열
import numpy as np

print("=== 1차원 ===")
A = np.array([1, 2, 3, 4])
print(A)
print(np.ndim(A))   # 1         : 1차원 배열이다
print(A.shape)      # (4,)      : 1차원, 4원소
print(A.shape[0])   # 4         : 0번째 차원의 크기 (원소 개수)

print()
print("=== 2차원 ===")
B = np.array([[1, 2], [3, 4], [5, 6]])
print(B)
print(np.ndim(B))   # 2         : 2차원 배열이다
print(B.shape)      # (3, 2)    : 2차원, 3원소 x 2원소
print(B.shape[0])   # 3         : 0번째 차원의 크기 (원소 개수)

# %% [3.3.2] 곱
import numpy as np

A = np.array([[1,2,3], [4,5,6]])
print(f"A의 형상: {A.shape}")   # 2 x 3
B = np.array([[1,2], [3,4], [5,6]])
print(f"B의 형상: {B.shape}")   # 3 x 2

np.dot(A, B)

# %% [3.3.3] 신경망에서의 행렬 곱
import numpy as np

# TODO: 82쪽부터 이어서