import unittest
import rsyncer
import config


class MyTest(unittest.TestCase):

    def test_command_args_is_3(self):
        command = rsyncer.RSync().sync_file_command("file")
        self.assertEqual(len(command), 3)

    def test_command_args_is_calling_local_server(self):
        command = rsyncer.RSync().sync_file_command("~/that/filename")
        self.assertEqual(command[0], "rsync")
        self.assertEqual(command[1], "~/that/filename")
        self.assertEqual(command[2],
                         config.remote_server_note_path + "filename")
