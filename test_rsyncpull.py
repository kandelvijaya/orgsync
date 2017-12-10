import unittest
import rsyncpull
import config


class RsyncPullTest(unittest.TestCase):

    def test_rsync_pull_command_has_3_components(self):
        command = rsyncpull.RsyncPull().rsync_pull_command("~/this.org")
        self.assertEqual(len(command), 3)

    def test_rsync_pull_command_has_proper_components(self):
        filepath = "~/filename.org"
        command = rsyncpull.RsyncPull().rsync_pull_command(filepath)
        self.assertEqual(command[0], "rsync")
        self.assertEqual(command[1],
                         config.remote_server_note_path + "filename.org")
        self.assertEqual(command[2], filepath)
