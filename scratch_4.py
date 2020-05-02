import matplotlib.pyplot as plt
ax = plt.subplot(111)
ax.bar(range(1,6), a.values())
for label, x, y in zip(a.keys(), range(1,6), a.values()):
    plt.annotate(
        label,
        xy=(x, y), xytext=(10,10),
        textcoords='offset points', ha='right', va='bottom',
        bbox=dict(boxstyle='round,pad=0.5', alpha=0),
        fontname='Segoe UI Emoji',
        fontsize=20)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_xticks([])
plt.show()