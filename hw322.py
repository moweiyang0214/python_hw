# 可以用collections模块中的Counter()函数方便地统计词频
import collections
import copy
s="我 是 一个 测试 句子 ， 大家 赶快 来 统计 我 吧 ， 大家 赶快 来 统计 我 吧，大家 赶快 来 统计 我 吧 ， 重要 事情 说 三遍 ！"
s_list = s.split()
s_list_backup = copy.deepcopy(s_list)
print(s_list_backup)
[s_list.remove(item) for item in s_list_backup if item in '，。！“”']
print(collections.Counter(s_list))

# 用字典解决统计词频
s_dict = {}
for item in s_list:
    if item.strip() not in "，。！“”":
        if item not in s_dict:
            s_dict[item] = 1
        else:
            s_dict[item] += 1
print(s_dict)