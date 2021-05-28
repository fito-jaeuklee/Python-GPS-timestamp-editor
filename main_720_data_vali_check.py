from tkinter import filedialog
import os
import glob

all_file_path_glob = glob.glob('/Users/jaeuklee/workspace/timestamp_validation_check/TNT-0521/*.csv')
print(all_file_path_glob)

# all_file_path_glob = filedialog.askopenfilename()
# print(all_file_path_glob)

# file_name = file_path.split('/')
# print(file_name[5][:-4])
# file_name = file_name[5][:-4]

prefix_dummy_gps_data = '$GPRMC'
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


def secs_10_600_data_augmentation_fixed_data(filtered_data_list, filename):
    with open('./' + filename + '_result.txt', 'a') as f1:
        for m in range(0, len(filtered_data_list)):
            # split_data_w_dummy = split_data[0] + ',' + split_data[1] + ',' + dummy_gps_data
            augmentation_data = prefix_dummy_gps_data + filtered_data_list[m] + dummy_gps_data
            f1.write(augmentation_data + os.linesep)


def open_intersect_filtered_file_write_gps_left_data(filtered_data_list, filename):
    with open('./' + filename + '_result.txt', 'a') as f1:
        for m in range(0, len(filtered_data_list)):
            split_data = filtered_data_list[m].split(',')
            split_data_w_dummy = split_data[0] + ',' + split_data[1] + ',' + dummy_gps_data
            f1.write(split_data_w_dummy + os.linesep)


def final_data_size_10_secs_backup(file_path):
    current_data = []
    past_data = []
    save_filtered_data = []

    print(file_path)
    first_past_data_flag = 0
    cnt_big_bracket = 0
    bracket_line_number_list = []

    with open(file_path, 'rb') as f:
        barr = f.readlines()

    print(len(barr))

    for k in range(0, len(barr)):
        line_data = barr[k].decode('utf-8')
        print(line_data)
        print(len(line_data))
        # print(line_data[0])
        # print(line_data[1])
        # print(line_data[2])
        # print(line_data[3])

        if len(line_data) > 1 and line_data[0] == '[':
            print("here")
            bracket_line_number_list.append(k)
            cnt_big_bracket += 1
    print(bracket_line_number_list)
#len(bracket_line_number_list
    for i in range(0, len(bracket_line_number_list)):
        # print(i)
        for z in range(i * 110, i * 110 + 110):
            # print(barr[z])
            # print(z)
            filterd_barr = barr[z].decode('utf-8')
            filterd_barr = filterd_barr[filterd_barr.find(','):]
            # print(filterd_barr)

            if z < 10:
                past_data.append(filterd_barr[0:11])
                past_data.append(filterd_barr[11:22])
                past_data.append(filterd_barr[22:33])
                past_data.append(filterd_barr[33:44])
                past_data.append(filterd_barr[44:55])
            else:
                current_data.append(filterd_barr[0:11])
                current_data.append(filterd_barr[11:22])
                current_data.append(filterd_barr[22:33])
                current_data.append(filterd_barr[33:44])
                current_data.append(filterd_barr[44:55])

        p1 = set(past_data)
        c1 = set(current_data)

        t1 = p1 | c1
        t1 = list(t1)
        t1.sort()


    save_filtered_data.extend(t1)
    past_data = []
    current_data = []
    data_chunk_size_cnt = 0
    t1 = []

    del save_filtered_data[0]
    del save_filtered_data[0]
    print("TOTAL: ", save_filtered_data, len(save_filtered_data))



    return save_filtered_data


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

    for z in range(0, int(len(barr) / 30 / 4)):
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


# The broken cell.
# Sort time flow from reversed time seq.

# print(all_file_path_glob)
# for buf in all_file_path_glob:
# print(buf)
# save_filtered_720_data = data_size_720_filter(buf)
# save_filtered_240_data = data_size_240_filter(file_path)

# file_name = buf.split('/')
# print(file_name[6][:-4])
# file_name = file_name[6][:-4]
# open_intersect_filtered_file_write_gps_left_data(save_filtered_720_data, file_name)
# file_name = all_file_path_glob


print(all_file_path_glob)
for buf in all_file_path_glob:
    save_filtered_secs10_600_data = final_data_size_10_secs_backup(buf)

    file_name = buf.split('/')
    print(file_name[6][:-4])
    file_name = file_name[6][:-4]
    secs_10_600_data_augmentation_fixed_data(save_filtered_secs10_600_data, file_name)
