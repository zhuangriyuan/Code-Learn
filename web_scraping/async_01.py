# 异步爬虫
# 多线程，多进程
# 线程池:包含多个线程或进程

import time
from multiprocessing.dummy import Pool


def get_page(str):
    print("downloading: " + str)
    time.sleep(2)
    print("done")


list = ["a", "b", "c", "d"]

# 实例化一个线程池对象
pool = Pool(4)
# 将列表中每一个元素传递给get_page进行处理
pool.map(get_page, list)
