import matplotlib.pyplot as plt
import matplotlib

# 日本語フォント（例: ヒラギノ角ゴ ProN）
matplotlib.rcParams['font.family'] = 'Hiragino Sans'

plt.tick_params(labelbottom=False,
                labelleft=False,
                labelright=False,
                labeltop=False)

plt.tick_params(bottom=False,
                left=False,
                right=False,
                top=False)

plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['left'].set_visible(False)

plt.gca().spines['bottom'].set_linewidth(1.5)

plt.gca().spines['bottom'].set_position(('data',0))
