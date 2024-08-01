import time
import numpy as np

#Sin vectorizacion
a = np.array([1,2,3,4])
print(a)

#with vectorization
a = np.random.rand(10000000)
b = np.random.rand(10000000)

tic2 = time.time()

#Scalar version (not really vectorized)
c = 0
for i in range(len(a)):
    c += a[i] + b[i]
toc2 = time.time()

#Vectorized with numpy
c = 0
tic = time.time()
c = np.sum(a + b)
toc = time.time()

print(f"Vectorized numpy version: {str(1000*(toc-tic))} ms")
print(f"Vectorized for version: {str(1000*(toc2-tic2))} ms")
