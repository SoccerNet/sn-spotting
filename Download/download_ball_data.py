import os
import zipfile
import argparse
import SoccerNet
from SoccerNet.Downloader import SoccerNetDownloader

parser = argparse.ArgumentParser(
    description='Prepare data for ball pass and drive action spotting.')

parser.add_argument('--dataset_dir', type=str,
                    help="Path for dataset directory ")
parser.add_argument('--password_videos', type=str,
                    help="Password to videos from the NDA")
args = parser.parse_args()

list_splits = ["train", "valid", "test", "challenge"]

# Download zipped folder per split
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory=args.dataset_dir)
mySoccerNetDownloader.downloadDataTask(task="spotting-ball-2024",
                                       split=list_splits,
                                       password=args.password_videos)
# Extract files from zipped folders
for split in list_splits:
    print(f"Unzipping {split}.zip ...")
    subtask_data_dir = os.path.join(args.dataset_dir, "spotting-ball-2023")
    zip_filename = os.path.join(subtask_data_dir, f"{split}.zip")
    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        zip_ref.extractall(subtask_data_dir)
    print(f"... done unzipping {split}.zip")


    print(f"Remove {split}.zip ...")
    if os.path.exists(zip_filename):
        os.remove(zip_filename)
    else:
        print("The file does not exist")
    print(f"... {split}.zip has been removed")
