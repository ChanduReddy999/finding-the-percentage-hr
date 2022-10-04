"""
finding the percentage of marks scored in subjects hackerrank
"""

"""method 1"""

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# average = sum(student_marks[query_name])/len(student_marks[query_name])
# print('%.2f'%average)


"""method 2"""

# n = int(input())
# student_marks = {}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()
# query_marks = student_marks[query_name]
# avg = ((query_marks[0] + query_marks[1] + query_marks[2]) / 3)
# print(f"{avg :.2f}")
"""
3
chandu 90 70 80
akhil 40 50 60
raj 90 50 60
chandu
80.00
"""