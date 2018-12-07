import os, sys

def exec_packet_child():
    os.execv('mtr-packet', ('',))
    # os._exit(0)


r, w = os.pipe()


def open_pipe():
    # fork child/subprocess
    chpid = os.fork()
    if chpid == 0:
        # pipes
        os.dup2(r, sys.stdin.fileno())
        os.dup2(w, sys.stdout.fileno())
        exec_packet_child()
    else:
        print('error creating fork child')


# alternative using NewType from typing to define custom types like pid_t
#
class packet_command_pipe_t:
    def __init__(self, pid: int, rpipe: int, wpipe: int, reply_buffer: str, reply_buffer_used: int):
        self.pid = pid
        self.rpipe = rpipe
        self.wpipe = wpipe
        self.reply_buffer = reply_buffer
        self.reply_buffer_used = reply_buffer_used

open_pipe()