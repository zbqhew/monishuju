import numpy as np

# 设置参数
mean = 61.2
std_deviation = 17
min_value = 41
max_value = 87
num_samples = 602

# 生成符合正态分布的数据
data = np.random.normal(mean, std_deviation, num_samples)

# 限制数据在最小值和最大值之间
data = np.clip(data, min_value, max_value)

# 由于数据可能是小数，我们需要将数据转换为整数
data = np.round(data).astype(int)

# 输出数据
print(data)
