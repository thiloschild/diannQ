from pathlib import PureWindowsPath, PurePosixPath
import subprocess
import tomli
import tomlkit
from rq import get_current_job


def process_auto_job(raw_data, fasta_type):

    job = get_current_job()
    task_id = job.id

    config = {
    "version": "1.8.1",
    "raw_folders_or_files": "",
    "fasta_files": "",
    }

    config["raw_folders_or_files"].append(raw_data)
    config["fasta_files"].append(fasta_type)


    with open(f"tasks/auto_{task_id}.toml", "w") as outfile: 
        tomlkit.dump(config, outfile)
    
    subprocess.run(f"snakemake -call auto/diann/{config['version']}/{task_id}", shell=True)




def process_user_job(args: list):
    """
    create a task.toml and start the snakemake pipeline for user jobs
    """

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

    with open(f"tasks/user_{task_id}.toml", "w") as outfile: 
        tomlkit.dump(config, outfile)

    print("Config created...starting Snakemake pipeline")

    #subprocess.run(f"snakemake -call diann/{config['version']}/user/{task_id}", shell=True)
    subprocess.run(f"snakemake -call user/diann/{config['version']}/{task_id}", shell=True)
