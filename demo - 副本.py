import h5py
import numpy as np
f = h5py.File('./bpnn2.h5','r')
#遍历文件中的一级组
for group in f.keys():
    print(group)
    #根据一级组名获得其下面的组
    group_read = f[group]
    #遍历该一级组下面的子组
    for subgroup in group_read.keys():
        print(subgroup)
        #根据一级组和二级组名获取其下面的dataset
        dset_read = f[group+'/'+subgroup]
        #遍历该子组下所有的dataset
        for dset in dset_read.keys():
            #获取dataset数据
            dset1 = f[group+'/'+subgroup+'/'+dset]
            print(dset1.name)
            data = np.array(dset1)
            print(data.shape)
            # x = data[...,0]
            # y = data[...,1]

# with h5py.File('./bpnn2.h5',"r") as f:
#     for key in f.keys():
# # print(f[key], key, f[key].name, f[key].value) # 因为这里有group对象它是没有value属性的,故会异常。另外字符串读出来是字节流，需要解码成字符串。
#         print(f[key], key, f[key].name)
# f = h5py.File('./bpnn2.h5',"r")
# for key in f.keys():
#     print(f[key].name)
#     print(f[key].data)
#     # print(f[key].value)