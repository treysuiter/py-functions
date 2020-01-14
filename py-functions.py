# running_kids = ["Pam", "Sam", "Andrea", "Will"]
# swinging_kids = ["Marybeth", "Jenna", "Kevin", "Courtney"]
# sliding_kids = ["Mike", "Jack", "Jennifer", "Earl"]
# hiding_kids = ["Henry", "Heather", "Hayley", "Hugh"]

# def run(kidArray):
#     for kid in kidArray:
#         print(f"{kid} ran like a fool!")

# run(running_kids)

# def swing(kidArray):
#     for kid in kidArray:
#         print(f"{kid} is swinging!")

# swing(swinging_kids)

# def slide(kidArray):
#     for kid in kidArray:
#         print(f"{kid} is going down the slide!")

# slide(sliding_kids)

# def hide(kidArray):
#     for kid in kidArray:
#         print(f"{kid} is hiding")

# hide(hiding_kids)

def chickenMonkey():
    
    for number in range(1, 101):
        isChickenMonkey = False
        print(number)
        if number % 5 == 0 and number % 7 == 0:
            print(f"{number} is Chicken Monkey!")
            isChickenMonkey = True
        if isChickenMonkey == False:
            if number % 5 == 0:
                print(f"{number} is chicken")
            if number % 7 == 0:
                print(f"{number} is monkey")

chickenMonkey()