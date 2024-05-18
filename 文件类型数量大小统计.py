import os

def get_directory_input():
    while True:
        lj = input('请输入要统计的目录名：')
        if os.path.exists(lj):
            return lj
        else:
            print('指定的目录不存在，请重新输入。')

lj = get_directory_input()

wjzd = {}
wjsize = {}
l1 = []
l2 = []
l3 = []
dic1 = {}

for dirpath, dirnames, filenames in os.walk(lj):
    dir_list = os.listdir(dirpath)
    for dir1 in dir_list:
        dir_split = os.path.splitext(dir1)
        l1.append(dir_split[1].lower())  # 添加后缀名（转换为小写）
        l2.append(dir_split[0])  # 添加文件名
        path = os.path.join(dirpath, dir1)
        size = os.path.getsize(path)
        houzui = dir_split[1].strip().lower()  # 去掉重复的后缀名（转换为小写）
        l3.append((houzui, size))

    s11 = set(l1)
    for s1 in s11:
        count = l1.count(s1)
        wjzd[s1] = count

    n = 0
    l4 = []
    for m in s11:
        dic1[m] = n
        n += 1
        l4.append(0)


    for houzui, size in l3:
        l4[dic1[houzui]] += size

    lv = list(dic1.keys())
    for v in range(len(lv)):
        wjsize[lv[v]] = l4[v]

lb = list(wjzd.items())
lb.sort()
lb2 = list(wjsize.items())
lb2.sort()

total_mb = 0
for i in range(len(lb)):
    print("文件类型{}；文件数{}；文件大小{:.2f}MB".format(lb[i][0], lb[i][1], lb2[i][1] / pow(1024, 2)))
    total_mb += lb2[i][1]

total_gb = total_mb / pow(1024, 3)
print(f'文件总大小为{total_gb}GB')
# (这个改进后的代码增加了用户输入的验证，确保了目录存在，同时对文件扩展名进行
# 了小写转换，以确保统计时的一致性。此外，它还使用了pow()函数来提高代码的可
# 读性，并将最终的总大小转换为GB单位。)