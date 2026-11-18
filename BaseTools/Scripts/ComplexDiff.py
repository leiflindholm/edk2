## @file
#  Compares file complexity across git commits
#
#  Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.<BR>
#
#  SPDX-License-Identifier: BSD-2-Clause-Patent
#
"""Module comparing function complexity ."""

import argparse
import io
import sys

import git_helpers

from ComplexCheck import analyze_source_buf

def get_analyzed_files(analysis):
    files = []

    print(analysis.__dict__)

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description='Retrieves information on who to cc for review on a given commit')
    PARSER.add_argument('refcommit',
                        action="store",
                        help='git revision to compare with',
                        nargs='?')
    PARSER.add_argument('commit',
                        action="store",
                        help='git revision to examine (default: HEAD)',
                        nargs='?',
                        default='HEAD')
    PARSER.add_argument('-f', '--file',
                        help='File to diff')

    ARGS = PARSER.parse_args()
    if not ARGS.refcommit:
        sys.exit(1)

    REPO = git_helpers.locate_repo()
    if not REPO.is_ancestor(ARGS.refcommit, ARGS.commit):
        print('WARNING:', ARGS.refcommit, 'is not an ancestor of', ARGS.commit)

    if ARGS.file:
        B_FILES = [ARGS.file]
    else:
        B_FILES = git_helpers.get_modified_files(REPO, ARGS.commit)

    for FILE in B_FILES:
        print(FILE, ARGS.refcommit, ARGS.commit)

        a_source_buf = git_helpers.read_git_file(REPO, ARGS.refcommit, FILE)
        b_source_buf = git_helpers.read_git_file(REPO, ARGS.commit, FILE)

        if a_source_buf:
            a_functions = analyze_source_buf(a_source_buf, FILE)

        b_functions = analyze_source_buf(b_source_buf, FILE)

        if a_source_buf and a_functions:
            a_files = get_analyzed_files(a_functions)

        b_files = get_analyzed_files(b_functions)

        for b_file in b_files:
            path = b_file['filename']
            if a_source_buf:
                for a_file in a_files:
                    if a_file['filename'] == path:
                        print('{} in both')
                    else:
                        print('{} only in b')
