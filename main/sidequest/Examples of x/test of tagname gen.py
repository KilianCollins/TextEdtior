import random

#
# tag_name = "t" + str(random.randint(0, 50))
#
# print(tag_name)
sample_list = []
for i in range(0,100):
    tag_name_current = "t" + str(random.randint(0, 50))
    tag_name_previous = tag_name_current
    tag_name = "t" + str(random.randint(0, 50)) if tag_name_previous != tag_name_current else "t" + str(random.randint(50,990))
    sample_list.append(tag_name)

print(sample_list)




# print(tag_name)



