import matplotlib.pyplot as plt

input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.style.use('seaborn-v0_8')       # 图形样式
fig, ax = plt.subplots()

ax.plot(input_values,squares,linewidth=3)                #绘制的线条粗细
ax.set_title('Square Numbers',fontsize=24)
ax.set_xlabel('Value',fontsize=15)
ax.set_ylabel('Square of value',fontsize=15)
ax.tick_params(labelsize =14)
plt.show()
