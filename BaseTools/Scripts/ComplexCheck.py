## @file
#  Scores complexity of functions within files modified by a given commit,
#  or in a specified file in the filesystem.
#
#  Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.<BR>
#
#  SPDX-License-Identifier: BSD-2-Clause-Patent
#
"""Module analyzing complexity of code in specified file or commit."""

import argparse
import os.path
import sys

import git_helpers

try:
    from lizard import FileAnalyzer, get_extensions
    from lizard_ext.lizardcognitive import LizardExtension as Cognitive
except ImportError:
    print('Unable to load "lizard" module - please install and try again.')
    sys.exit(1)

CHECKFILES = ['.c', '.h', '.py', '.rs']

def get_source_buf (args, repo, filepath):
    """Return a buffer of source code to analyze, based on command line."""
    if args.file:
        try:
            f = open(filepath, encoding='utf-8')
            with f:
                buf = f.read()
        except OSError:
            print('File not found!')
            sys.exit(1)

    else:
        buf = git_helpers.read_git_file(repo, args.commit, filepath)

    return buf

def analyze_source_buf (buf, filename):
    """Analyze a source buffer using lizard with the Cognitive extension.

    Return a dictionary of results.
    """
    result = FileAnalyzer(get_extensions([Cognitive()])).analyze_source_code(filename, buf)

    functions = result.function_list
    if functions:
        # Functions with CogC value of 0 don't have 'cognitive_complexity'
        # entry,add one here to simplify consumers.
        for function in functions:
            f=function.__dict__

            if not 'cognitive_complexity' in f:
                f['cognitive_complexity'] = 0

    return result

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser(
        description='Checks code complexity changes caused by a given commit')
    PARSER.add_argument('commit',
                        action="store",
                        help='git revision to examine (default: read from filesystem)',
                        nargs='?',
                        default='HEAD')
    PARSER.add_argument('-f', '--file',
                        nargs='?',
                        help='File to examine')

    ARGS = PARSER.parse_args()

    REPO = git_helpers.locate_repo()
    if ARGS.file:
        FILES=[ARGS.file]
    else:
        FILES = git_helpers.get_modified_files(REPO, ARGS.commit)

    for FILE in FILES:
        if not os.path.splitext(FILE)[1] in CHECKFILES:
            print('Skipping "' + FILE + '" (analysis for file type not enabled)')
            continue

        print(FILE)

        source_buf = get_source_buf (ARGS, REPO, FILE)

        ANALYSIS = analyze_source_buf(source_buf, FILE)

        if not ANALYSIS.function_list:
            print('  no functions found!')
            continue

        print(' CycC  CogC  Lines  Tokens  Name')
        FUNCTIONS = ANALYSIS.function_list
        for FUNCTION in FUNCTIONS:
            funcinfo=FUNCTION.__dict__

            print(f" {funcinfo['cyclomatic_complexity']:>4}",
                  f" {funcinfo['cognitive_complexity']:>4}",
                  f" {funcinfo['nloc']:>5}",
                  f" {funcinfo['token_count']:>6}",
                  f" {funcinfo['name']:<}")
