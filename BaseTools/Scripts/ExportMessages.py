#!/usr/bin/env python3
## @File
#
# Copyright (c) 2023, Qualcomm Innovation Center, Inc. All rights reserved.<BR>
#
# SPDX-License-Identifier: BSD-2-Clause-Patent
#
# Convert a downloaded message archive mbox from groups.io to
# a directory tree with messages in individual files grouped
# per month.
#
# This script is terribly hard-coded, but then it is intended
# to be a one-shot operation for migrating to github PR code
# review.
#
# Script expects uncompressed 'messages.mbox' in working
# directory and builds the hierarchy under 'out/'.
#

import mailbox
import os
import urllib
from collections import defaultdict
from datetime import datetime

def write_out(filename, buffer, timestamp):
    try:
        with open(filename, 'xb') as f:
            f.write(buffer)
    except FileExistsError:
        print("File '%s' exists, aborting!" % filename)
        exit(1)

    try:
        os.utime(filename, times=(timestamp, timestamp))
    except:
        print("Failed to set timestamps for '%s'" % filename)
        exit(2)


if __name__ == '__main__':
    year = defaultdict(lambda: defaultdict(int, defaultdict(int)))

    prevyear = 0
    prevmonth = 0

    for message in mailbox.mbox('messages.mbox'):
        subject = message['subject']
        datestring = message.get_from().split(maxsplit=1)[1]

        try:
            datetime = datetime.strptime(datestring, '%a %b %d %H:%M:%S %Y')
        except ValueError:
            print("Invalid date string: %s" % datestring)
            exit(1)

        if datetime.month != prevmonth or datetime.year != prevyear:
            dirname = "out" + "/" + str(datetime.year) + "/" + str(datetime.month)
            if not os.path.exists(dirname):
                print("creating '%s'" % dirname)
                os.makedirs(dirname)
            else:
                print("entering '%s'" % dirname)

        prevmonth = datetime.month
        prevyear = datetime.year

        message_id = message['Message-ID'].strip()   # outlook.com pollutes Message-ID with line breaks
        filename = dirname + "/" + urllib.parse.quote(message_id, safe='')
        write_out(filename, message.as_bytes(), datetime.timestamp())

        # Count number of messages per month
        year[datetime.year][datetime.month] += 1

    for key in sorted(year.keys()):
        print("%s" % key)
        for month in sorted(year[key].keys()):
            print("%s: %s" % (month, year[key][month]))
