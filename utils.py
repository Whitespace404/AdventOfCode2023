def get_raw_input(file_name):
    with open(file_name) as f:
        return f.read()


def get_lines_input(file_name):
    with open(file_name) as f:
        return [line.rstrip("\n") for line in f.readlines()]


def get_numbers_input(file_name):
    with open(file_name) as f:
        return [int(line.rstrip("\n")) for line in f.readlines()]


def get_delim_input(file_name, delim):
    with open(file_name) as f:
        return f.read().split(delim)
