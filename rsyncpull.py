import sys
import os
import subprocess
import config


class RsyncPull:

    def sync_file(self, filepath):
        command = self.rsync_pull_command(filepath)
        self._perform(command)

    def rsync_pull_command(self, filepath):
        filename = os.path.basename(filepath)
        return ["rsync", config.remote_server_note_path + filename, filepath]

    # This approach doesnot care if the rsync didnt find a file
    # in remote location. It justs does the work.
    def _perform(self, command):
        subprocess.run(command)


class GitPull:

    def sync_file(self, filepath):
        '''from the immediate directory of the filename, stash
        any changes and pull from notes branch'''
        curdir = os.path.dirname(filepath)
        subprocess.run(["cd", curdir])
        git_stash_return = subprocess.run(["git", "stash"])
        if git_stash_return.returncode == 0:
            subprocess.run(["git", "pull", "origin", "master"])


if __name__ == "__main__":
    if len(sys.argv) == 3:
        strategy = str(sys.argv[1])
        filepath = str(sys.argv[2])
        if strategy == "rsync":
            RsyncPull().sync_file(filepath)
        elif strategy == "git":
            GitPull().sync_file(filepath)
