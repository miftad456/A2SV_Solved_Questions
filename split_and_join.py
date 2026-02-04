

def split_and_join(line):
    result  = line.split(" ")
    final = "-".join(result)
    return final

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
