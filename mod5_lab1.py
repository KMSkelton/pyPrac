with open("./land_time_forgot.txt", "r") as land_time_forgot:
  txt_list = land_time_forgot.readlines()

line_counter = 0;

for char in txt_list:
    if char == "\n":
        line_counter += 1

one_third = int(line_counter/3)
two_thirds = one_third * 2

middle_third_lines = txt_list[one_third: two_thirds+1]
print(middle_third_lines)

print(f"There are {line_counter} lines in this file.")
print(f"There are {one_third} lines in the middle-third of this file.")

print(middle_third_lines[0])
print(middle_third_lines[-1])

with open("thirds_lines.txt", "w") as f:
    text_thirds = middle_third_lines[0] + middle_third_lines[-1]
    f.write(text_thirds)


# # Chunkadunk
# with open("./land_time_forgot.txt", "r") as land_time_forgot:
#     txt_list_all = land_time_forgot.readlines()
#     # without a hint, readlines reads all the characters in all the lines
# with open("./land_time_forgot.txt", "r") as land_time_forgot:
#     txt_list_200 = land_time_forgot.readlines(200)
#     # with a hint of 200 this stops after 200 characters
# with open("./land_time_forgot.txt", "r") as land_time_forgot:
#     txt_list_2000 = land_time_forgot.readlines(2000)
#     # with a hint of 2000 this stops after 2000 characters
#
# print("text list all: ", txt_list_all)
# print("text list 200: ", txt_list_200)
# print("text list 2000: ", txt_list_2000)