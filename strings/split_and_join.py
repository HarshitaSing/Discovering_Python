def split_and_join(line):
    # write your code here
    list = line.split(" ")
    joined = "-".join(list)
    return joined

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
    # just using inbuilt functions split() & join() 
