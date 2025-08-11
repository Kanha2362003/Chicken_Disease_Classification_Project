import sys
import os

# Add src/ to path so Python can find CNNClassifier without installing
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from CNNClassifier import logger

logger.info("This is a test log message from CNNClassifier")
logger.warning("This is a warning log message")
logger.error("This is an error log message")
