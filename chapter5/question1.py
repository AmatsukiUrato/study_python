from chapter5.module import print_result

print("1")

all_color = ("red", "blue", "yellow", "green")
color_number = {1: "red", 2: "blue", 3: "yellow", 4: "green"}


def pick_color(number):
    if color_number.get(number) in all_color:
        return color_number.get(number)
    print("2")

print("3")

if __name__ == "__main__":
    print("main")
    color_name = pick_color(1)
    print(color_name)

    collected_color = []
    for key in color_number:
        if color_name[1] in color_number[key]:
            collected_color.append(color_number[key])

    print_result(collected_color)

print("4")
