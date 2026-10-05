import numpy as np
import matplotlib.pyplot as plt

print("===== 1.6.1 그래프 =====")
x = np.arange(0, 6, 0.1) # 0~6까지 0.1 간격으로 생성
y = np.sin(x)

plt.plot(x, y)
plt.show()

print("===== 1.6.2 pyplot 기능 =====")
# 데이터 준비
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# 그래프 그리기
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x") # x축 이름
plt.ylabel("y") # y축 이름
plt.title('sin & cos') # 제목
plt.legend()
plt.show()

print("===== 1.6.3 이미지 표시 =====")
import os
from matplotlib.image import imread

# img = imread('test.png') <- 경로 못 찾아서 수정
img = imread(os.path.join(os.path.dirname(__file__), 'test.jpg')) # 이 .py 파일과 같은 폴더 기준

plt.imshow(img)
plt.show()