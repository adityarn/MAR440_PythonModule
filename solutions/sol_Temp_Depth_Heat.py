depths = -np.arange(1, 1000, 1)
T = 20*np.exp(-(-depths/1e2))
plt.plot(T, depths)

Cp = 3980

Q = 1035 * Cp * (T + 273.15)
plt.plot(Q, depths)

Q.sum()