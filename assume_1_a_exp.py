import numpy as np
import matplotlib.pyplot as plt
import random

# 定义参数
num_workers = 10
num_routines = 10
num_variants = 10
num_stages = 10

# 初始化矩阵Z
Z = np.random.randint(1, 7, size=(num_workers, num_routines * num_variants))
indices = np.random.choice(num_workers * num_routines * num_variants, int(num_workers * num_routines * num_variants * 0.1), replace=False)
Z.ravel()[indices] = np.random.randint(6, 11, size=int(num_workers * num_routines * num_variants * 0.1))

# 初始化变化函数参数
change_prob = [0.7, 0.3]  # 大于5的值替换的新值的概率分布
change_range = [5, 10]  # 大于5的值替换的新值的范围


# 选择数值函数
stage_mem = np.full((num_stages, num_workers), -1, dtype=int)
def select_value(worker_index, stage, is_transparent):
    if is_transparent:
        top_10_percent = int(num_routines * num_variants * 0.1)
        sorted_indices = np.argsort(Z[:, worker_index])
        available_indices = sorted_indices[-top_10_percent:]
        # 检查可用索引是否与stage_mem中的索引重复
        while True:
            selected_index = np.random.choice(available_indices)
            if selected_index not in stage_mem[stage]:
                break
        stage_mem[stage][worker_index] = selected_index
        return selected_index

    else:
        choiced = np.random.choice(range(num_routines))
        # 检查可用索引是否与stage_mem中的索引重复
        while choiced in stage_mem[stage][1:num_workers]:
            choiced = np.random.choice(range(num_routines))
        stage_mem[stage][worker_index] = choiced
        return choiced

def refresh_Z(Z):
    # 重置矩阵Z为[1, 10]的随机整数
    Z[:] = np.random.randint(1, 11, size=Z.shape)

    # 选择大于5和小于5的值的索引
    indices_greater_than_5 = np.where(Z > 5)
    indices_less_than_5 = np.where(Z < 5)

    # 替换大于5的值为新的随机值
    new_values_greater_than_5 = np.random.choice([np.random.randint(1, 6), np.random.randint(6, 11)], size=len(indices_greater_than_5[0]), p=[0.6, 0.4])
    Z[indices_greater_than_5] = new_values_greater_than_5

    # 替换小于5的值为新的[1, 10]的随机整数
    Z[indices_less_than_5] = np.random.randint(1, 11, size=len(indices_less_than_5[0]))


# 初始化存储变量
worker_scores = np.zeros((num_workers, num_stages))
platform_scores = np.zeros(num_stages)

# 进行实验
for stage in range(num_stages):
    # 生成随机的工作人员执行顺序
    worker_order = list(range(num_workers))
    random.shuffle(worker_order)
    # 按随机顺序执行select_value函数
    for worker_index in worker_order:
        is_transparent = np.random.rand() < 0.8  # 80%的概率为透明，20%的概率为非透明
        worker_scores[worker_index][stage] = select_value(worker_index, stage, is_transparent)

    if stage < num_stages - 1:
        refresh_Z(Z)
    # 计算平台得分
    platform_scores[stage] = np.sum(worker_scores[:, stage])

# 绘制每个劳动者得分变化图
for worker_index in range(num_workers):
    plt.plot(range(num_stages), worker_scores[worker_index, :], label=f"Worker {worker_index}")
plt.xlabel("Stage")
plt.ylabel("Score")
plt.title("Individual Worker Scores")
plt.legend()
plt.show()

# 绘制平台得分变化图
plt.plot(range(num_stages), platform_scores)
plt.xlabel("Stage")
plt.ylabel("Score")
plt.title("Platform Scores")
plt.show()