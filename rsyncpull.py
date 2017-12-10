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


if __name__ == "__main__":
    filepath = str(sys.argv[1])
    RsyncPull().sync_file(filepath)
