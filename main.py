import time



filename = 'bx-23806_1611131310900_1611191286231_1.gp'


def check_timestamp_validation(fpath):
    check_odd_flag = 0
    last_line = ''
    with open('./' + fpath, 'rb') as f:
        barr = f.readlines()

        # for line in barr:
        #     print(line.strip())
        #     split_time = str(line.strip()).split((','))
        #     print(split_time[1])
        #     before_time_buf =
        #     time.sleep(1)
        #     if
        # print(len(barr))

        for i in range(0, len(barr), 2):
            # print(i)
            try:
                past_split_time = str(barr[i].strip()).split((','))[1]
            except:
                pass
            try:
                # print(i + 2)
                current_split_time = str(barr[i + 2].strip()).split((','))[1]
            except:
                check_odd_flag = 1

            # print(check_odd_flag)
            if check_odd_flag:
                last_line = str(barr[i])

            if past_split_time > current_split_time:
                print(past_split_time, current_split_time)
                print("timestamp error break loop")
                print(str(barr[i + 2]))

                return i + 2

            elif len(last_line) < 10 and check_odd_flag == 1:
                print(fpath)
                print("Timestamp validation check DONE!!!")
                return 1

        print(fpath)
        print("Timestamp validation check DONE!!!")
        return 1


def erase_timestamp_error_line(fpath, line_number):
    file = 'tt.txt'
    with open(fpath, 'r') as my_file:
        file_lines = my_file.readlines()

    print(line_number - 1, line_number + 10)
    print(file_lines[line_number -1], file_lines[line_number + 10])
    first_part = file_lines[:line_number]

    second_part = file_lines[line_number + 10:]

    lines = first_part + second_part
    with open(fpath, 'w') as my_file:
        my_file.writelines(lines)


if __name__ == '__main__':
    check_flag = 1

    while check_flag:
        rtn = check_timestamp_validation(filename)

        if rtn != 1:
            print("Error line = ", rtn)
            erase_timestamp_error_line(filename, rtn)
        else:
            print("This file is No Error")
            check_flag = 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
