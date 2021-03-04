import sys


def read_series(filename):
    try:
        f = open(filename, mode='rt', encoding='utf-8')
        # series = []
        # for line in f:
        #     a = int(line.strip())
        #     series.append(a)
        return [int(line.strip()) for line in f]
    finally:
        f.close()
    # return series


def read_series_with(filename):
    """Use python built in context-manager function to handle close()"""
    with open(filename, mode='rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]


def main(filename):
    series = read_series(filename)
    print(series)


# File like objects and duck typing into file like reading:

def words_per_line(flo):
    """Counts line lengths for file like objects.

    usage:
    import corepy.file_reader
    with open('wasteland.txt', mode='rt', encoding='utf-8') as real_file:
       wpl = corepy.file_reader.words_per_line(real_file)

    from urllib.request import urlopen
    with urlopen('http://sixty-north.com/c/t.txt') as web_file:
        wpl = ...

    Args:
        flo: file like object

    Returns:

    """
    return [len(line.split()) for line in flo.readlines()]

