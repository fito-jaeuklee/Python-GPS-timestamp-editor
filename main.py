import time
import glob
import os

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

    npz_file_path = glob.glob\
        (os.path.join('/Users/jaeuklee/workspace/timestamp_validation_check', "*.gp"))

    for a in range(0, len(npz_file_path)):
        npz_file_path_list = npz_file_path[a].split('/')
        npz_file_path_len = len(npz_file_path_list)
        # print(npz_file_path_list[npz_file_path_len - 1])
        npz_file_name = npz_file_path_list[npz_file_path_len - 1]
        print(npz_file_name)

        rtn = check_timestamp_validation(npz_file_name)
        print(npz_file_name, rtn)

        # while check_flag:
        #     rtn = check_timestamp_validation(npz_file_name)
        #
        #     if rtn != 1:
        #         print("Error line = ", rtn)
        #         # erase_timestamp_error_line(filename, rtn)
        #     else:
        #         print("This file is No Error")
        #         check_flag = 0

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
