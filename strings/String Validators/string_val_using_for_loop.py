# python 3.x

if __name__ == '__main__':
    str = input()
    set_ = ("isalnum", "isalpha","isdigit", "islower", "isupper")
    for test in set_:
        print (any(eval("c." + test + "()") for c in str))
        
  # most important function - any() & eval()
  # eval() will calculate the function for each character in the string
  # any() will give the o/p as true if any of the character in the whole string matches the test functions
