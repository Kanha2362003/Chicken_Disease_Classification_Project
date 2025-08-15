import os
import urllib.request as request
import zipfile
from CNNClassifier import logger
from CNNClassifier.utils.common import get_size
from CNNClassifier.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config




    def download_file(self):

        file_path = Path(self.config.local_data_file)
        min_valid_size_kb = 50  # adjust depending on expected dataset size

        if not file_path.exists() or file_path.stat().st_size < min_valid_size_kb * 1024:
            if file_path.exists():
                logger.info(f"File exists but is too small ({file_path.stat().st_size // 1024} KB), re-downloading...")
                os.remove(file_path)

            filename, headers = request.urlretrieve(
            url=self.config.source_URL,
            filename=str(file_path)
                 )
            logger.info(f"{filename} downloaded successfully with info:\n{headers}")
        else:
            logger.info(f"File already exists of size: {file_path.stat().st_size // 1024} KB")
  



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """ 

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file,'r') as zip_ref:
            zip_ref.extractall(unzip_path)


