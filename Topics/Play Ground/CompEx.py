# text = ["function", "is", "a", "synonym", "of", "occupation"]
# new_list = [x for x in text if x.endswith("tion")]
# print(new_list)
#
# old_list = [8, 13, -7, 4, -9, 2, 10]
# only_positive = [x if x >= 0 else 0 for x in old_list]
# print(only_positive)
l = list(input())

l_ = [int(x) for x in l]

print(l_)

