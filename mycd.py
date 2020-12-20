def my_cd():
    prompt = input('# mycd ')
    first_dir, second_dir = prompt.split()

    stack = []  # use a stack to store all the file that is in the directory
    # if second directory starts with '/', the result must start with root '/', else we need our first directory
    if second_dir[0] != '/':
        temp1 = first_dir.split('/')
        first_real_dir = [p for p in temp1 if p]
        for path in first_real_dir:
            stack.append(path)

    temp2 = second_dir.split('/')
    second_real_dir = [p for p in temp2 if p]  # handle the situation of multiple '/'
    for directory in second_real_dir:
        if directory not in ['..', '.'] and not directory.isalnum():
            print(second_dir + ': No such file or directory')
            break
        if directory == '..' and stack:
            stack.pop()
        elif directory.isalnum():
            stack.append(directory)
    else:
        print('/' + '/'.join(stack))


if __name__ == '__main__':
    my_cd()
