"""
VirtualBox CLI for Python.

This program is a simple command line for VirtualBox. You can run commands
to create, delete, start and stop VMs.

This is under development

TO DO:
1. Adding functionality to list VMs
2. Refactoring import calls for each method
3. Improving createVM method
4. Testing CI
5.
"""

import sys

def createVM(vmname, ostype):
    from vboxapi import VirtualBoxManager
    mgr = VirtualBoxManager(None, None)
    vbox = mgr.getVirtualBox()
    name = vmname
    vboxConstants = mgr.constants
    mach = vbox.createMachine("", name, [], ostype, "") # ubuntu_64
    mach.memorySize = 2048
    # hdd = vbox.createMedium("vdi", "", vboxConstants.constants.AccessMode_ReadWrite, vboxConstants.constants.DeviceType_HardDisk)
    mach.saveSettings()
    print("created machine with UUID", mach.id)
    vbox.registerMachine(mach)


def deleteVM(vmname):
    from vboxapi import VirtualBoxManager
    mgr = VirtualBoxManager(None, None)
    vbox = mgr.getVirtualBox()
    name = vmname
    vboxConstants = mgr.constants
    mach = vbox.findMachine(name)
    uuid = mach.id
    print("removing machine ", mach.name, "with UUID", uuid)
    # cmdClosedVm(ctx, mach, detachVmDevice, ["ALL"])
    disks = mach.unregister(vboxConstants.CleanupMode_Full)
    progress = mach.deleteConfig(disks)


def startVM(vmname):
    from vboxapi import VirtualBoxManager
    mgr = VirtualBoxManager(None, None)
    vbox = mgr.getVirtualBox()
    name = vmname
    mach = vbox.findMachine(name)
    session = mgr.getSessionObject(vbox)
    progress = mach.launchVMProcess(session, "gui", [])
    progress.waitForCompletion(-1)
    mgr.closeMachineSession(session)


def stopVM(vmname):
    from vboxapi import VirtualBoxManager
    mgr = VirtualBoxManager(None, None)
    vbox = mgr.getVirtualBox()
    name = vmname
    mach = vbox.findMachine(name)
    session = mgr.getSessionObject(vbox)
    vboxConstants = mgr.constants
    mach.lockMachine(session, vboxConstants.LockType_Shared)
    console = session.console
    console.powerDown()
    session.unlockMachine()
    # mgr.closeMachineSession(session)


def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filename = sys.argv[2]

    if action == 'createvm':
        vmname = sys.argv[2]
        ostype = sys.argv[3]
        createVM(vmname, ostype)
        print("VM " + vmname + " was created successfully.")
    elif action == 'deletevm':
        vmname = sys.argv[2]
        deleteVM(vmname)
        print("VM " + vmname + " was deleted successfully.")
    elif action == 'startvm':
        vmname = sys.argv[2]
        startVM(vmname)
        print("VM " + vmname + " was started successfully.")
    elif action == 'stopvm':
        vmname = sys.argv[2]
        print("VM " + vmname + " was stopped successfully.")
        stopVM(vmname)


if __name__ == '__main__':
    main()