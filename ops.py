import os


def run_backup(filename):
    os.system(f"tar -cvf backup.tar {filename}")


def read_log(log_name):
    with open(f"/var/logs/{log_name}") as f:
        return f.read()
