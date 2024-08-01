import time
import numpy as np

# Generar arrays grandes
a = np.random.rand(10000000)
b = np.random.rand(10000000)

# Medir tiempo para la versión no vectorizada
tic = time.time()

# Versión no vectorizada
c = 0
for i in range(len(a)):
    c += a[i] - b[i]

toc = time.time()

# Medir tiempo para la versión vectorizada
tic2 = time.time()

# Versión vectorizada
c = np.sum(a - b)

toc2 = time.time()

print(f"Non-vectorized version: {str(1000*(toc-tic))} ms")
print(f"Vectorized numpy version: {str(1000*(toc2-tic2))} ms")
