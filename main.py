def rewrite_file(file1, file2, file3):
    with open('1.txt', 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
    with open('2.txt', 'r', encoding=' utf-8') as f2:
        file2 = f2.readlines()
    with open('3.txt', 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
    with open("new_file.txt", 'w', encoding='utf-8') as f_new:
        if len(file1) < len(file2) and len(file1) < len(file3):
            f_new.write('1.txt' + '\n')
            f_new.write(str(len(file1)) + '\n')
            f_new.writelines(file1)
        elif len(file2) < len(file1) and len(file2) < len(file3):
            f_new.write('2.txt' + '\n')
            f_new.write(str(len(file2)) + '\n')
            f_new.writelines(file2)
        elif len(file3) < len(file1) and len(file3) < len(file2):
            f_new.write('3.txt' + '\n')
            f_new.write(str(len(file3)) + '\n')
            f_new.writelines(file3)
        if len(file1) < len(file2) and len(file2) < len(file3) or len(file2) > len(file3) and len(file2) < len(file1):
            f_new.write('2.txt' + '\n')
            f_new.write(str(len(file2)) + '\n')
            f_new.writelines(file2)
        elif len(file1) > len(file2) and len(file1) < len(file3) or len(file1) < len(file2) and len(file1) > len(file3):
            f_new.write('1.txt' + '\n')
            f_new.write(str(len(file1)) + '\n')
            f_new.writelines(file1)
        elif len(file3) > len(file1) and len(file3) < len(file2) or len(file3) < len(file1) and len(file3) > len(file2):
            f_new.write('3.txt' + '\n')
            f_new.write(str(len(file3)) + '\n')
            f_new.writelines(file3)
        if len(file1) > len(file2) and len(file1) > len(file3):
            f_new.write('1.txt' + '\n')
            f_new.write(str(len(file1)) + '\n')
            f_new.writelines(file1)
        elif len(file2) > len(file1) and len(file2) > len(file3):
            f_new.write('2.txt' + '\n')
            f_new.write(str(len(file2)) + '\n')
            f_new.writelines(file2)
        elif len(file3) > len(file1) and len(file3) > len(file2):
            f_new.write('3.txt' + '\n')
            f_new.write(str(len(file3)) + '\n')
            f_new.writelines(file3)
    return


hello = rewrite_file('1.txt', '2.txt', '3.txt')
