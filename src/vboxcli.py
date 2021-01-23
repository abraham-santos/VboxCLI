"""
VirtualBox CLI for Python.

This program is a simple command line for VirtualBox. You can run commands
to create, delete, start and stop VMs.

This is under development
"""

import sys

prompt = "vboxcli> "


def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filename = sys.argv[2]

    if action == 'createvm':
        vmname = sys.argv[2]
        ostype = sys.argv[3]
        print("VM " + vmname + " created successfully.")
    elif action == 'deletevm':
        vmname = sys.argv[2]
        print("VM " + vmname + " deleted successfully.")
    elif action == 'startvm':
        vmname = sys.argv[2]
        print("VM " + vmname + " started successfully.")
    elif action == 'stopvm':
        vmname = sys.argv[2]
        print("VM " + vmname + " stopped successfully.")


if __name__ == '__main__':
    main()