import scipy.io as sio
M = sio.loadmat('K_in_9.1837_K_out_0.5102.mat', squeeze_me = True)
z = M['z']
print(z[1:10])
