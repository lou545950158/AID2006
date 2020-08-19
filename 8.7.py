"""
    基础算法：
        1. 变量交换
              a,b=b,a
        2. 计算极值
             max_value = list01[0]
             for i in range(1,len(list01)):
                if max_value  < list01[i]:
                    max_value = list01[i]
            print(max_value)
        3. 排序
"""
# 降序：大 --> 小
# 核心思想：每个元素之间进行比较
#  规律：用第一个元素与后面元素依次比较，发现更大则交换.
#       用第二个元素与后面元素依次比较，发现更大则交换.
#       用第...个元素与后面元素依次比较，发现更大则交换.
# 步骤：取数据/作比较/发现更大就交换


def compare(list_target):#传入列表地址，函数内修改元素，所以不用通过返回值，函数外也可以得到数据结果
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    return list_target

list01 = [43, 2, 45, 65, 76, 8, 9]
result=compare(list01)
print(list01)

# 升序：小 --> 大