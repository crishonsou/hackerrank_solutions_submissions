import sys


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        line = string[i : i + k]
        new = ''
        for i in line:
            if i not in new:
                new = new + i
        print(new)





if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
    
    
