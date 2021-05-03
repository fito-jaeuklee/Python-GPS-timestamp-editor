from tkinter import filedialog
import os
import glob


all_file_path_glob = glob.glob('/Users/jaeuklee/Downloads/tnt_20210303/*.csv')
print(all_file_path_glob)

# file_path = filedialog.askopenfilename()
# print(file_path)
# file_name = file_path.split('/')
# print(file_name[5][:-4])
# file_name = file_name[5][:-4]

dummy_gps_data = 'A,3724.51225,N,12641.82677,E,4.097,211.51,110420,,,A*63'

# current_data = []
# past_data = []
# save_filtered_data = []
#
# data_chunk_size_cnt = 0
# first_data_in_come_flag = 0
# total_save_cnt = 0
# cnt_big_bracket = 0
# bracket_line_number_list = []


def open_intersect_filtered_file_write_gps_left_data(filtered_data_list, filename):
    with open('./' + filename + '_result.txt', 'a') as f1:
        for m in range(0, len(filtered_data_list)):
            split_data = filtered_data_list[m].split(',')
            split_data_w_dummy = split_data[0] + ',' + split_data[1] + ',' + dummy_gps_data
            f1.write(split_data_w_dummy + os.linesep)


def data_size_720_filter(file_path):
    current_data = []
    past_data = []
    save_filtered_data = []

    data_chunk_size_cnt = 0
    cnt_big_bracket = 0
    bracket_line_number_list = []

    with open(file_path, 'rb') as f:
        barr = f.readlines()

    print(len(barr))

    for k in range(0, len(barr)):
        line_data = barr[k].decode('utf-8')
        if line_data[0] == '[':
            bracket_line_number_list.append(k)
            cnt_big_bracket += 1

    for z in range(0, int(len(barr)/30/4)):
        for i in range(4 * z, 4 * z + 2):
            cnt_big_bracket = i
            # print("cnt big", cnt_big_bracket)
            for j in range(0, 30):
                line_data = barr[cnt_big_bracket * 30 + j].decode('utf-8')

                # print(line_data)
                line_data = line_data[line_data.find('$'):]

                if data_chunk_size_cnt < 30:
                    # print("ju1")
                    past_data.append(line_data)
                    data_chunk_size_cnt += 1
                elif data_chunk_size_cnt == 29:
                    # print("ju2")
                    data_chunk_size_cnt = 0
                else:
                    # print("ju3")
                    current_data.append(line_data)

            # print("past -----------=", past_data, len(past_data))
            # print("current -----------=", current_data, len(current_data))

            p1 = set(past_data)
            c1 = set(current_data)

            # print("")

            t1 = p1 | c1
            t1 = list(t1)
            t1.sort()

            # print("t1 -------------", list(t1), len(list(t1)))

            # print("")
        save_filtered_data.extend(t1)
        past_data = []
        current_data = []
        data_chunk_size_cnt = 0
        t1 = []

    print("TOTAL: ", save_filtered_data, len(save_filtered_data))

    return save_filtered_data


def data_size_240_filter(file_path):
    print("")
    save_240_data = []

    with open(file_path, 'rb') as f:
        barr = f.readlines()
    for i in range(0, len(barr)):
        line_data = barr[i].decode('utf-8')

        # print(line_data)
        line_data = line_data[line_data.find('$'):]
        save_240_data.append(line_data)
    # print(save_240_data)

    return save_240_data


for buf in all_file_path_glob:
    print(buf)
    save_filtered_720_data = data_size_720_filter(buf)
    # save_filtered_240_data = data_size_240_filter(file_path)

    file_name = buf.split('/')
    print(file_name[5][:-4])
    file_name = file_name[5][:-4]
    open_intersect_filtered_file_write_gps_left_data(save_filtered_720_data, file_name)
