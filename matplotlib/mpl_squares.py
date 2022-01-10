import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)
ax.set_title('平方数', fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)
plt.rcParams['font.sans-serif'] = ['SimHei']

plt.show()
