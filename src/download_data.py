import tarfile
from pathlib import Path

import requests


class DownloadData:
    def __init__(self, file_names: str, base_url: str) -> None:
        self.file_names = file_names
        self.base_url = base_url

        # Initialize raw data directory
        self.raw_directory = Path("./data/raw/")
        self.raw_directory.mkdir(parents=True, exist_ok=True)

        # Initialize ham data directory
        self.ham_directory = Path("./data/ham/")
        self.ham_directory.mkdir(parents=True, exist_ok=True)

        # Initialize spam data directory
        self.spam_directory = Path("./data/spam/")
        self.spam_directory.mkdir(parents=True, exist_ok=True)

    def download_data(self, file_name: str, base_url: str) -> None:
        save_path = self.raw_directory + file_name
        if Path(save_path).exists():
            return
        
        try:
            with requests.get(base_url+file_name) as r:
                r.raise_for_status()
                with open(save_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
        except Exception as e:
            print(f"Encountered exception when trying to download file: {file_name} from {base_url}")
            raise e

    def extract_data(self, file_name: str) -> None:
        pass

    def download_data(self):
        for file_name in self.file_names:
            self.download_data(file_name)
            self.extract_data(file_name)