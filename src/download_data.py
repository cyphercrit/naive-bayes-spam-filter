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

    def download_file(self, file_name: str) -> None:
        save_path = self.raw_directory / file_name
        if save_path.exists():
            return
        
        try:
            with requests.get(self.base_url + file_name, stream=True) as r:
                r.raise_for_status()
                with open(save_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)
        except Exception as e:
            print(f"Encountered exception when trying to download file: {file_name} from {self.base_url}")
            raise e

    def extract_data(self, file_name: str) -> None:
        from_path = self.raw_directory / file_name
        # Sort path by spam/ham and removes .tar.bz2 suffix
        to_path = Path(str(
            self.ham_directory / file_name if "ham" in file_name else self.spam_directory / file_name
        ).removesuffix(".tar.bz2"))

        try:
            with tarfile.open(from_path, "r:bz2") as tar:
                tar.extractall(path=to_path)
        except Exception as e:
            print(f"Encountered exception when trying to extract file: {file_name}")

    def download_data(self) -> None:
        for file_name in self.file_names:
            self.download_file(file_name)
            self.extract_data(file_name)