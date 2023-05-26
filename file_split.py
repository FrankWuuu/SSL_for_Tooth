import os, shutil, random


##################### train and test list split #########
# path = "../Radiographs_maxillomandibular/"
# name_list = os.listdir(path)
# # print(len(name_list))

# name_train_index = random.sample(list(range(0, 1000)), 800)
# name_test_index = [x for x in list(range(0, 1000)) if x not in name_train_index]

# name_train_list = []
# name_test_list = []
# for ind, name in enumerate(name_list):
#     if ind in name_train_index:
#         # print(ind, name)
#         name_train_list.append(name)
#     else:
#         name_test_list.append(name)
#     # print(ind,name)
# print(len(name_train_list))
# print(len(name_test_list))

# # file_train = open('train_name.txt','w')
# # for item in name_train_list:
# #     file_train.write(item+"\n")
# # file_test = open('test_name.txt','w')
# # for item in name_test_list:
# #     file_test.write(item+"\n")
# # name_train_list.sort()
# # name_test_list.sort()

# print(name_train_list)
# print(name_test_list)


##################### train label and unlabel split #########

train_file_path = 'train_name.txt'

# with open(train_file_path) as file:
#     # contents = file.readlines()
#     contents = file.readlines()
#     name_list = []
#     [name_list.append(line.strip()) for line in contents]
#     print(name_list)
#     print(len(name_list))


with open(train_file_path) as name:
    tt = name.read()
    name_list = tt.split("\n")
    # print(name_list)
    # print(len(name_list))

name_label_index = random.sample(list(range(0, 800)), 160)
name_unlabel_index = [x for x in list(range(0, 800)) if x not in name_label_index]

name_label_index.sort()
name_unlabel_index.sort()

# print(name_label_index)
# print(name_unlabel_index)

name_label_list = []
name_unlabel_list = []
for ind, name in enumerate(name_list):
    if ind in name_label_index:
        # print(ind, name)
        name_label_list.append(name)
    else:
        name_unlabel_list.append(name)
    # print(ind,name)
print(len(name_label_list))
print(len(name_unlabel_list))

# file_train = open('label_name.txt','w')
# for item in name_label_list:
#     file_train.write(item+"\n")
# file_test = open('unlabel_name.txt','w')
# for item in name_unlabel_list:
#     file_test.write(item+"\n")
# name_label_list.sort()
# name_unlabel_list.sort()

print(name_label_list)
print(name_unlabel_list)
