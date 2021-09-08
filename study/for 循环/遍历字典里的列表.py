students = [
    {"name": "小刘"},
    {"name": "小王"}
]

find_name = "小刘"

for stu_dict in students:

    print(stu_dict)
    if stu_dict["name"] == find_name:
        print("找到了")
        break
else:
    print("没有找到")








