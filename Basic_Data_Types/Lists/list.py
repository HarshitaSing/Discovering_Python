if __name__ == '__main__':
    N = int(input())
    L = []
    for _ in range(N):
        #splitting the input using default parameter - space like -> [insert, 5, 10]
        s = input().split()
        #storing the first string (e.g. "insert")
        cmd = s[0]
        #stroring all rest of the characters
        args = s[1:]
        if cmd !="print":
            cmd += "("+ ",".join(args) +")"
            eval("L."+cmd)
        else:
            print (L)

    '''
    Tried this code in Python 3.x using input() function
    Same can be achieved using raw_input() function in Python2.x
    '''
    
