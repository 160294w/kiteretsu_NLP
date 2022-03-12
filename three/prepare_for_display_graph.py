#% matplotlib inline
# ↑グラフを表示するためのおまじない
# Colaboratoryで実行する場合はなくても問題ありません

import matplotlib.pyplot as plt
plt.ion()

# X座標
x =  [ 1,  2,  3,  4 , 5,  6]
# Y座標は２種類
y1 = [10, 30, 30, 20, 80, 90]
y2 = [20, 10, 30, 50, 60, 50]

# グラフのフォーマットを指定してプロット
plt.plot(x, y1, marker="o", color = "red", linestyle = "--")
plt.plot(x, y2, marker="x", color = "blue",  linestyle = ":")

plt.show()
