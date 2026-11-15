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

    print(anlysis.__dict__)

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

        A_ANALYSIS =  analyze_source_buf(reference_source_buf, FILE)
        B_ANALYSIS = analyze_source_buf(current_source_buf, FILE)

        if not A_ANALYSIS or not B_ANALYSIS:
            sys.exit(1)

        a_files = get_analyzed_files(A_ANALYSIS)
        b_files = get_analyzed_files(B_ANALYSIS)

    print(ANALYSIS.__dict__['filename'] + '@' + ARGS.commit, ANALYSIS.__dict__['nloc'])
    for FUNCTION in ANALYSIS.__dict__['function_list']:
        DATA=FUNCTION.__dict__
        print(DATA['name'], DATA['cyclomatic_complexity'], DATA['token_count'])

    print('==============')

    sys.exit(0)

    if ANALYSIS.nloc > REFANALYSIS.nloc:
        print('Got worse!')
