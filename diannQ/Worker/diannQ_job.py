from pathlib import PureWindowsPath, PurePosixPath
import subprocess
import tomli
import tomlkit
from rq import get_current_job


def process_job(args):


    job = get_current_job()
    task_id = job.id

    args_str = " ".join(str(element) for element in args)
    # print(args_str)


    config = {
    "version": "1.8.1",
    "raw_folders_or_files": [],
    "fasta_files":[],
    "args": ""
}

    # create config.json
    for i, arg in enumerate(args):

        if arg == "--f":
            file = args[i+1].rstrip()
            posix = str(PurePosixPath(PureWindowsPath(file)))
            name = f"data/{posix.split('/')[-1]}"
            
            config["raw_folders_or_files"].append(name)

            

        if arg == "--fasta":
            file = args[i+1]
            posix = str(PurePosixPath(PureWindowsPath(file)))
            name = f"fasta/{posix.split('/')[-1]}"
            
            config["fasta_files"].append(name)
        
        if arg == "--version":
            config["version"] = str(args[i+1])
        


    args_str = " ".join(str(element) for element in args)
    config["args"] = args_str

    print(config)

    with open(f"{task_id}.toml", "w") as outfile: 
        tomlkit.dump(config, outfile)

    print("Config created...starting Snakemake pipeline")

    #subprocess.run(f"snakemake -call diann/{config['version']}/user/{task_id}", shell=True)
    subprocess.run(f"snakemake -call user/diann/{config['version']}/{task_id}", shell=True)
