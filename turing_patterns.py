#Simulated Turing Patterns via the Gray-Scott Model: Spots, Stripes 
### Interactive simulation of the PDEs ∂u/∂t = D_u ∇²u − uv² + F(1−u) and ∂v/∂t = D_v ∇²v + uv² − (F+k)v
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

N = 300
Du, Dv, F, k = 0.16, 0.08, 0.060, 0.062   # try Feed=0.035, kill=0.065 for spots

u = np.ones((N, N))
v = np.zeros((N, N))

# seed with a few random squares
for i in range(15):
    x, y = np.random.randint(50, N-50, 2)
    u[x-10:x+10, y-10:y+10] = 0.5
    v[x-10:x+10, y-10:y+10] = 0.25

def update(_):
    global u, v
    for i in range(20):  # multiple steps per frame
        Lu = np.roll(u, 1, 0) + np.roll(u, -1, 0) + np.roll(u, 1, 1) + np.roll(u, -1, 1) - 4*u
        Lv = np.roll(v, 1, 0) + np.roll(v, -1, 0) + np.roll(v, 1, 1) + np.roll(v, -1, 1) - 4*v
        uvv = u * v * v
        u += Du * Lu - uvv + F * (1 - u)
        v += Dv * Lv + uvv - (F + k) * v
    im.set_array(u + v)
    return [im]

fig, ax = plt.subplots()
im = ax.imshow(u + v, cmap='magma', animated=True)
ax.axis('off')
anim = FuncAnimation(fig, update, frames=10000, interval=50, blit=True)
plt.show()