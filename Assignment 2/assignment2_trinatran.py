
def handedness():
    score = 0
    hand = input("Which	hand do	you	usually	use when writing?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when drawing?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when throwing?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when using scissors?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when using a toothbrush?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when using a knife (without a fork)?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when using a spoon?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when using a broom (upper hand)?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when striking a match?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when opening a box (holding the lid)?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when holding a computer mouse?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when using a key to unlock a door?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when holding a hammer?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when holding a brush or comb?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    hand = input("Which	hand do	you	usually	use when holding a cup while drinking?")
    if hand == "left":
        score -= 10
    else:
        score += 10
    if 30 <= score <=160:
        return "Right Handed"
    if -160 <= score <= -30:
        return "Left Handed"
    if -29 <= score <= 29:
        return "Ambidextrous"

# import random
# def get_random(low, high, num_type):
#     random_number = random.randint(0, 101)
