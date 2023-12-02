import string
import random

if __name__ == "__main__":
    s1 = string.ascii_uppercase
    
    s2 = string.ascii_lowercase
    
    s3 = string.digits
    
    s4 = string.punctuation
    
    len = int(input("Enter password length\n")) #Todo1: Handle Gibberish
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    # random.shuffle(s)
    # print(s)
    print("Your password is: ")
    print("".join(random.sample(s, len)))
    # print("".join(s[0:plen]))