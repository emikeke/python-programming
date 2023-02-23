total_num_of_students = int(input("How mant students on the course?"))
group_size = int(input("Desired group size?"))

groups_formed = 0
if total_num_of_students % group_size == 0:
    groups_formed = total_num_of_students//group_size
else:
    groups_formed = total_num_of_students//group_size + 1

print("Number of groups formed:", groups_formed)