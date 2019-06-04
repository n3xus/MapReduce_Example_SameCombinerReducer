#!/usr/bin/python3

import sys


def category_mapper():
    """ Maps videos to category
    Input format: video_id \t category \t trending_date \t views \t country
    Output format: category \t video_id \t country
    """
    for line in sys.stdin:
        # Clean input and split it
        parts = line.strip().split(",")

        # Check that the line is of the correct format
        # If line is malformed, we ignore the line and continue to the next line
        if len(parts) != 12:
            continue

        video_id = parts[0]
        likes = parts[6]

        if video_id == "video_id":  # Skipping Header
            continue

        print("{}\t{}\t{}".format(video_id, likes, 1))


if __name__ == "__main__":
    category_mapper()
