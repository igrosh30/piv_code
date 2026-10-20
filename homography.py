#load mat files scipy.io
import scipy.io
import numpy as np 

''''
.load returns a dict where the keys are each columns on the file 
values are already the numpy arrays

dict with keys: 'U1', 'V1', 'U2', 'V2', 'img1', 'img2'

we choose img1- dest img2- source -> we are computing H_{12}
'''

data = scipy.io.loadmat("homography_data.mat")

u1 = data['U1']
v1 = data['V1']
u2 = data['U2']
v2 = data['V2']

src = np.column_stack([u2,v2])
dst = np.column_stack([u1,v1])

#need to initialize A outisde! A is 61x9 matrix! 
A = np.zeros((u1.size *2,9))
'''check waht we have so far
print(src)
print(dst)
print(A)
'''

for i in range(u1.size):
    xs,ys= src[i]
    xd,yd= dst[i]
    A[2*i]      = [xs,ys,1,0,0,0,-xd*xs,-xd*ys,-xd]
    A[2*i +1]   = [0,0,0,xs,ys,1,-yd*xs,-yd*ys,-yd]


_, _, Vt = np.linalg.svd(A)
h = Vt[-1]
H = h.reshape(3, 3)


print("H =")
print(H / H[2, 2])
