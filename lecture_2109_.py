# -*- coding: utf-8 -*-
"""Lecture_2109**.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LX1ZQzMi2HE4w2zKivtFEN-HkXBMP5px
"""

#data sample 1
x = 7 # feature of sample 1
y = 3 # label of sample 1

# yp = w*x
# L = (yp -y)^2

#gradient Descent
# 1, w 초기화
# 2. dL/dw
#       L = (w*x-y)^2
#   dL/dw = 2(w*x-y)x
#   dL/dw = 2(w*7-3)7 : gradient
# 3. w = w - d*dL/dw

w = 1.5
d = 0.001 # learning rate

for i in range(10):
    dL = 2*(w*7-3)*7 # gradient dL/dw
    w = w - d * dL
    Loss = (w*x-y)**2
    print(i, "w ", w)
    print(i, "L ", Loss)
    print(i, "dL/dw ", dL)

import numpy as np

A = np.random.rand(4, 3)
print(A.shape)
print(A)

#A * B = C
B = np.random.rand(3, 2)
print(B.shape)
print(B)

C = np.matmul(A, B)
print(C.shape)
print(C)



### 실습과제 01
import numpy as np

#A = np.array([ [7], [5]])
#print(A.shape)
#print(A)
#print()

X1 = np.empty((0,3), int)
X1 = np.append(X1, np.array([[1, 2, 3]]), axis=0)
X1 = np.append(X1, np.array([[4, 5, 6]]), axis=0)
X1 = np.append(X1, np.array([[7, 8, 9]]), axis=0)
print(X1.shape)
print(X1)
print()

w = np.random.rand(3, 2)
print(w.shape)
print(w)
print()

Yp = np.matmul(X1, w)
print(Yp.shape)
print(Yp)


# X1 -> np.matmul(X1, W) -> Yp
#data
# 1 2 3
# 4 5 6
# 7 8 9

# X1 = ? -> np.array
# W의 shape? -> np.random.rand
# Yp의 shape? -> np.matmul

### 실습과제 02

# X1 -> X2 -> X3 -> Yp
# X2 = np.matmul(X1, W1)
# X3 = np.matmul(X2, W2)
# Yp = np.matmul(X3, W3)
# W1.shape?, W2. shape?, W3.shape?
# Mean 평균 squared 제곱 error/loss 계산 : MSE를 말하는 것 가트댜
## Loss 값을 계산하는 함수를 만들거라..

## W는 랜덤으로 만들고, 행렬을 어떻게 잘 지정 하느냐가 문제다.
## Yp는 정해져 있음


import numpy as np

X1 = np.empty((0,3), int)
X1 = np.append(X1, np.array([[1, 2, 3]]), axis=0)
X1 = np.append(X1, np.array([[4, 5, 6]]), axis=0)
X1 = np.append(X1, np.array([[7, 8, 9]]), axis=0)

W1 = np.random.rand(3, 1)
W2 = np.random.rand(1, 2)
W3 = np.random.rand(2, 3)

print(W1.shape)
print(W1)
print()

print(W2.shape)
print(W2)
print()

print(W3.shape)
print(W3)
print()

X2 = np.matmul(X1, W1)
X3 = np.matmul(X2, W2)
Yp = np.matmul(X3, W3)

print(X2.shape)
print(X2)
print()
print(X3.shape)
print(X3)
print()
print(Yp.shape)
print(Yp)
print()

mse = np.square(np.subtract(X1, Yp)).mean()
print(mse)

# X1-> X2 -> X3-> Yp
# X2 = np.matmul(X1,W1)
# X3 = np.matmul(X2,W2)
# Yp = np.matmul(X3,W3)
# W1.shape?, W2.shape?, W3.shape?
# Mean 평균 squared 제곱 error/loss 계산

(RaXCa)x(RbXCb) = (RcXCc)
Ra = Rc
Cb = Cc
Ca = Rb

# Ca = Cc 는 옳지 않음

# 1 2 3
# 4 5 6
# 7 8 9
# feature, label은 뭐가 되는지 다시한 번 생각해보아라

