# %% [3.2.2] 계단 함수 구현
import numpy as np

def step_function1(x):
    if x > 0:
        return 1
    else:
        return 0

def step_function2(x):
    y = x > 0
    return y.astype(int)

print(step_function2(np.array([-1.0, 1.0, 2.0])))

# %% [3.2.3] 계단 함수의 그래프
import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    return np.array(x > 0, dtype=int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1) # y축의 범위 지정
plt.show()

# %% [3.2.4] 시그모이드 함수 구현하기
import numpy as np
import matplotlib.pylab as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-1.0, 1.0, 2.0])
print(sigmoid(x))

x = np.arange(-5.0, 5.0, 0.1)
y = sigmoid(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

# %% [3.2.7] ReLU (Recified Linear Unit) 함수
# x (x > 0)
# 0 (x <= 0)
def relu(x):
    return np.maximum(0, x)