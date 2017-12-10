import sys
import os
import subprocess
import config


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


if __name__ == "__main__":
    file_path = sys.argv[1]
    RSyncPush().sync_file(file_path)
