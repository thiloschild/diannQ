from pathlib import PureWindowsPath, PurePosixPath
import os
import shutil
import subprocess


def process_job(args):

    new_args = args

    print("++++++++++++++++++++++++++++++")
    print("GOT THIS REQUEST:")
    print("++++++++++++++++++++++++++++++")

    print(args)

    args_str = " ".join(str(element) for element in args)
    print(args_str)

    print("++++++++++++++++++++++++++++++")
    print("COPYING ALL NECESSARY FILES")
    print("++++++++++++++++++++++++++++++")

    # translate paths
    for i, arg in enumerate(args):
        if arg == "--f":
            file = args[i+1].rstrip()
            print("rawfile: " + file)
            posix = str(PurePosixPath(PureWindowsPath(file)))
            name = posix.split("/")[-1]
            path = "/mnt/ms/new/user" + posix.split("\\")[1]
            print("This Path was found: " + path)
            print("Does is exist: " + str(os.path.exists(path)))
            if not os.path.exists(path):
                break
            dest = "/home/devel/diann_data/"+name
            if not os.path.exists(dest):
                shutil.copytree(path, dest)
                os.sync()
            new_args[i+1] = dest

        if arg == "--fasta":
            file = args[i+1]
            posix = str(PurePosixPath(PureWindowsPath(file)))
            name = posix.split("/")[-1]
            path = "/mnt/ms/new/user" + posix.split("\\")[1]
            print("This Path was found: " + path)
            print("Does is exist: " + str(os.path.exists(path)))
            dest = "/home/devel/diann_data/"+name
            if not os.path.exists(dest):
                shutil.copy2(path, dest)
                os.sync()
            new_args[i+1] = dest
        if arg == "--out":
            file = args[i+1]
            posix = str(PurePosixPath(PureWindowsPath(file)))
            name = posix.split("/")[-1]
            path = "/mnt/ms/new/user" + posix.split("\\")[1]
            # print(path, os.path.exists(path))
            dest = "/home/devel/diann_data/"+name
            print("Set output path: " + dest)
            new_args[i+1] = dest
        if arg == "--out-lib":
            file = args[i+1]
            posix = str(PurePosixPath(PureWindowsPath(file)))
            name = posix.split("/")[-1]
            path = "/mnt/ms/new/user" + posix.split("\\")[1]
            # print(path, os.path.exists(path))
            dest = "/home/devel/diann_data/"+name
            print("Set output path: " + dest)
            new_args[i+1] = dest


    print("++++++++++++++++++++++++++++++")
    print("NEW DIANN ARGUMENTS")
    print("++++++++++++++++++++++++++++++")

    args_str = " ".join(str(element) for element in new_args)
    print(args_str)
    print("++++++++++++++++++++++++++++++")
    print("STARTING DIANN COMPUTATION")
    print("++++++++++++++++++++++++++++++")
    # subprocess.run(["/usr/diann/1.8.1/diann-1.8.1", args_str])
