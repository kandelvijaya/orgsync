import sys
import os
import subprocess
import config
import datetime


class RSyncPush:

    def sync_file_command(self, file_path):
        remote_path_base = config.remote_server_note_path
        just_file_name = os.path.basename(file_path)
        return ["rsync", file_path, remote_path_base + just_file_name]

    def _perform(self, command):
        subprocess.run(command)

    def sync_file(self, file_path):
        command = self.sync_file_command(file_path)
        self._perform(command)


class GitPush:

    def sync_file(self, file_path):
        curdir = os.path.dirname(file_path)
        subprocess.call(["cd", curdir])
        subprocess.call(["git", "add", file_path])
        curdatetime = str(datetime.datetime.now())
        filename = os.path.basename(file_path)
        commit_msg = "SyncOnSave @" + curdatetime + " @ " + filename
        subprocess.call(["git", "commit", "-m", commit_msg])
        subprocess.call(["git", "push", "origin", "master"])


if __name__ == "__main__":
    if len(sys.argv) == 3:
        strategy = sys.argv[1]
        file_path = sys.argv[2]
        if strategy == "rsync":
            RSyncPush().sync_file(file_path)
        elif strategy == "git":
            GitPush().sync_file(file_path)
