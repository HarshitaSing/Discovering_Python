import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    # so I got to know about textwrap library from stackoverflow. 
    #Instead of checking discussion I wanted to explore the options for wrapping the text.
