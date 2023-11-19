import matplotlib.pyplot as plt
from assume_1_b_exp import num_workers, num_stages

from assume_1_a_exp import run as run1a
from assume_1_b_exp import run as run1b

def draw1():
    worker_scores_1a, platform_scores_1a = run1a()
    worker_scores_1b, platform_scores_1b = run1b()

    fig = plt.figure(dpi=1000)

    # 添加第一个子图
    ax1 = fig.add_subplot(2, 2, 1)
    for worker_index in range(num_workers):
        ax1.plot(range(num_stages), worker_scores_1a[worker_index, :], label=f"Worker {worker_index}")
    ax1.set_xlabel("Stage")
    ax1.set_ylabel("Score")
    ax1.set_title("Individual Worker Scores")
    ax1.legend()

    # 添加第二个子图
    ax2 = fig.add_subplot(2, 2, 2)
    ax2.plot(range(num_stages), platform_scores_1a)
    ax2.set_xlabel("Stage")
    ax2.set_ylabel("Score")
    ax2.set_title("Platform Scores")

    # 添加第一个子图
    ax3 = fig.add_subplot(2, 2, 3)
    for worker_index in range(num_workers):
        ax3.plot(range(num_stages), worker_scores_1b[worker_index, :], label=f"Worker {worker_index}")
    ax3.set_xlabel("Stage")
    ax3.set_ylabel("Score")
    ax3.set_title("Individual Worker Scores")
    ax3.legend()

    # 添加第二个子图
    ax4 = fig.add_subplot(2, 2, 4)
    ax4.plot(range(num_stages), platform_scores_1b)
    ax4.set_xlabel("Stage")
    ax4.set_ylabel("Score")
    ax4.set_title("Platform Scores")

    # 调整子图之间的间距
    fig.tight_layout()

    # 显示图形
    plt.show()

def draw2():
    worker_scores_1a, platform_scores_1a = run1a()
    worker_scores_1b, platform_scores_1b = run1b()

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

    # 添加第一个子图
    for worker_index in range(num_workers):
        ax1.plot(range(num_stages), worker_scores_1a[worker_index, :], label=f"Worker {worker_index}")
    ax1.set_xlabel("Stage")
    ax1.set_ylabel("Score")
    ax1.set_title("Individual Worker Scores")
    ax1.legend()

    # 添加第二个子图
    ax2.plot(range(num_stages), platform_scores_1a)
    ax2.set_xlabel("Stage")
    ax2.set_ylabel("Score")
    ax2.set_title("Platform Scores")

    # 添加第一个子图
    for worker_index in range(num_workers):
        ax1.plot(range(num_stages), worker_scores_1b[worker_index, :], label=f"Worker {worker_index}")
    ax1.set_xlabel("Stage")
    ax1.set_ylabel("Score")
    ax1.set_title("Individual Worker Scores")
    ax1.legend()

    # 添加第二个子图
    ax2.plot(range(num_stages), platform_scores_1b)
    ax2.set_xlabel("Stage")
    ax2.set_ylabel("Score")
    ax2.set_title("Platform Scores")

    # 调整子图之间的间距
    fig.tight_layout()

    # 显示图形
    plt.show()


if __name__ == '__main__':
    draw2()