import unittest
import rsyncpush
import config


class RsyncPushTest(unittest.TestCase):

    def test_command_args_is_3(self):
        command = rsyncpush.RSyncPush().sync_file_command("file")
        self.assertEqual(len(command), 3)

    def test_command_args_are_proper(self):
        command = rsyncpush.RSyncPush().sync_file_command("~/that/filename")
        self.assertEqual(command[0], "rsync")
        self.assertEqual(command[1], "~/that/filename")
        self.assertEqual(command[2],
                         config.remote_server_note_path + "filename")
