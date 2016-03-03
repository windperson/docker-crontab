import subprocess


def gen_run_sh_job(command):
    """
    Create APScheduler compatible job function for it to schedule to run.
    :param command: the shell command to execute
    :return: parameter less function
    """
    def run_sh():
        out = subprocess.run(args=[command], universal_newlines=True, stdout=subprocess.PIPE, shell=True)
        print(out.stdout.splitlines())
        pass

    return run_sh
