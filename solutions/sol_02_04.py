import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2*np.pi, 2*np.pi, 10)
delta_x = x[1] - x[0]

y = np.sin(x)
dy_dx_analyt = np.cos(x)
dy_dx_num = np.full_like(y, np.nan) # creates an array of the same size as y and fills it with NaNs
dy_dx_num[1:] = (y[1:] - y[:-1])/delta_x
dy_dx_num[0] = (y[1] - y[0]) / delta_x

plt.plot(x, y, label="func")
plt.plot(x, dy_dx_analyt, label="dy/dx analyt")
plt.plot(x, dy_dx_num, label="dy/dx numerical")

plt.legend()
plt.grid()