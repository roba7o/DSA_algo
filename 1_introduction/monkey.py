import random
import string

def string_generator(string_length):
    alpha = string.ascii_lowercase + " "
    #print(alpha)
    res = ""
    for r in range(string_length):
        res = res + alpha[random.randrange(len(alpha))]
    return res

def string_score(target, attempt):
    num_same = 0
    for i in range(len(target)):
        if target[i] == attempt[i]:
            num_same += 1
    return num_same / len(target)

if __name__ == "__main__":
    goal_string = "lets choose a random string"
    generated_string = string_generator(len(goal_string))
    
    best = 0 
    while string_score(goal_string,generated_string) < 1:
        generated_string = string_generator(len(goal_string))
        print(generated_string)

                                    