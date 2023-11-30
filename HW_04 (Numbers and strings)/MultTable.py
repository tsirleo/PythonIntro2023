from math import ceil


def print_sep_line(max_line_length):
    print('=' * max_line_length)


def count_num_cols(num, max_line_length):
    col_width = len(str(num)) * 2 + len(str(num * num)) + len(".*.") + len(".=.")
    _row_length = 0
    _num_of_cols = 0

    while _row_length <= max_line_length:
        if _row_length + col_width <= max_line_length:
            _num_of_cols += 1
            _row_length += (col_width + len(".|."))
        else:
            break

    return _num_of_cols


def init_section(_num_of_cols, max_num):
    return [['' for _ in range(_num_of_cols)] for _ in range(max_num)]


def make_section(section, start, end, max_number):
    for num in range(1, max_number + 1):
        col = 0
        for j in range(start, end + 1):
            section[num - 1][col] = f"{j:.>{len(str(max_number))}}.*.{num:.<{len(str(max_number))}}.=.{j * num:.<{len(str(max_number * max_number))}}"
            col += 1

    return section


def print_section(section):
    for row in section:
        print(".|.".join(row))


def print_table(max_num, max_length):
    num_of_cols = count_num_cols(max_num, max_length)
    num_of_sections = ceil(max_num / num_of_cols)
    rem_cols_to_print = max_num
    start = 1
    end = num_of_cols

    print_sep_line(max_length)
    for sec_num in range(num_of_sections):
        start = (sec_num * num_of_cols) + 1
        end = (sec_num * num_of_cols) + num_of_cols if rem_cols_to_print >= num_of_cols else max_num
        section = init_section(num_of_cols, max_num) if rem_cols_to_print >= num_of_cols else init_section(rem_cols_to_print, max_num)
        print_section(make_section(section, start, end, max_num))
        print_sep_line(max_length)
        rem_cols_to_print -= num_of_cols


N, M = map(int, input().split(','))
print_table(N, M)
