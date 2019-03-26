import subprocess
import shlex


def isNoInternetConnected():
    """
    1 for not connected
    0 for connected
    """
    cp = subprocess.run(["ping", "-c", "5", "1.1.1.1"], capture_output=True)
    return cp.returncode


def runCommands(cmds, **args):
    """
    cmds is like
    [
        ['ls','-l'],
        ['echo','$PATH']
    ]
    """
    rs = []
    for cmd in cmds:
        r = subprocess.run(cmd, capture_output=True, **args)
        rs.append(r)
    return rs


def RUN(cmdstrs, **args):
    """
    cmdstrs : list[str]
    """
    cmds = [shlex.split(cmd) for cmd in cmdstrs]
    return runCommands(cmds, **args)


def startTrain(cmds):
    for cmd in cmds:
        tmp = subprocess.run(cmd)
        if tmp.returncode != 0:
            break
