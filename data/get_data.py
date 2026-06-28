from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

# Authenticate
api = KaggleApi()
api.authenticate()
data_download_path = "downloads"


# Create data directory
Path(data_download_path).mkdir(exist_ok=True)

# Download and unzip competition files
api.competition_download_files(
    competition="GiveMeSomeCredit",
    path="downloads",
    quiet=False
)

# Unzip the downloaded archive
import zipfile

zip_path = f"{data_download_path}" + "/GiveMeSomeCredit.zip"

with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(data_download_path)

print("Download complete!")