#!/usr/bin/python3
import sys


def read_map_output(file):
    for line in file:
        yield line.strip().split('\t')


def category_reducer():
    current_video_id = None
    current_sum = 0
    current_count = 0

    for video_id, average, count in read_map_output(sys.stdin):

        if not current_video_id:
            current_video_id = video_id

        if current_video_id != video_id:
            output = "{}\t{}\t{}".format(current_video_id, (current_sum/current_count), current_count)

            print(output)

            current_video_id = video_id
            current_sum = 0
            current_count = 0

        current_count = current_count + float(count)
        current_sum = current_sum + (float(count) * float(average))

    if not current_video_id:
        output = "{}\t{}\t{}".format(current_video_id, (current_sum/current_count), current_count)
        print(output)


if __name__ == "__main__":
    category_reducer()
