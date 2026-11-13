## @file
#  Shared git helper functions between scripts in this directory
#
#  Copyright (c) Qualcomm Technologies, Inc. and/or its subsidiaries.<BR>
#
#  SPDX-License-Identifier: BSD-2-Clause-Patent
#

import io
import sys

try:
    import git
except ImportError:
    print('Unable to load "gitpython" module - please install and try again.')
    sys.exit(1)

def get_modified_files(repo, refspec):
    """Returns a list of the files modified by the commit specified in 'refspec'."""
    commit = repo.commit(refspec)
    return commit.stats.files

def locate_repo():
    """Opens a Repo object for the current tree, searching upwards in the directory hierarchy."""
    try:
        repo = git.Repo(path='.', search_parent_directories=True)
    except (git.InvalidGitRepositoryError, git.NoSuchPathError):
        print("It doesn't look like we're inside a git repository - aborting.")
        sys.exit(2)
    return repo

def read_git_file (repo, refspec, filename):
    """Read a file from repo at a given refspec"""
    commit = repo.commit(refspec)

    file_object = commit.tree[filename]

    with io.BytesIO(file_object.data_stream.read()) as f:
        source_bytes = f.read().decode('utf-8')
        return source_bytes
