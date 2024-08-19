#!/usr/bin/python3
"""
0-main
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        # Instead of printing the subscriber count, print "OK" or "0"
        if number_of_subscribers(sys.argv[1]) > 0:
            print("OK")
        else:
            print("0")
