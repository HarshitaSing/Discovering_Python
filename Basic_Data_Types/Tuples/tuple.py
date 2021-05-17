if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    var = hash(t)
    print (var)
    
    
  '''
  At first I thought just using () would do the job but NO
  Used the inbuilt tuple() function. 
  Just 1 line to add & it passes the testcases.
  '''
