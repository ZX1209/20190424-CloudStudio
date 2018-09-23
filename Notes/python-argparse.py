import argparse

#
cmd_atgs_list = " add ".split()

# setup
parser = argparse.ArgumentParser()
parser.add_argument("echo")
parser.add_argument("--maybe")
# type choices action default...

# args parser
# default is sys.arg
args = parser.parse_args(cmd_atgs_list)

# handle
if args.echo:
    print(args.echo)