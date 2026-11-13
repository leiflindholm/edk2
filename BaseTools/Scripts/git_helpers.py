## @file
#  Shared git helper functions between scripts in this directory
#
#  Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.<BR>
#
#  SPDX-License-Identifier: BSD-2-Clause-Patent
#

import sys

try:
    import git
except ImportError:
    print('Unable to load "gitpython" module - please install and try again.')
    sys.exit(1)

def locate_repo():
    """Opens a Repo object for the current tree, searching upwards in the directory hierarchy."""
    try:
        repo = git.Repo(path='.', search_parent_directories=True)
    except (git.InvalidGitRepositoryError, git.NoSuchPathError):
        print("It doesn't look like we're inside a git repository - aborting.")
        sys.exit(2)
    return repo
