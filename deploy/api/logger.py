import os
import sys
import logging
from logging.handlers import RotatingFileHandler

# Define log format
logging_format = "[%(asctime)s - %(levelname)s - %(module)s:%(lineno)d] %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

# Create log directory
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Set up log file path
log_filepath = os.path.join(log_dir, "app.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_format,
    datefmt=date_format,
    handlers=[
        RotatingFileHandler(log_filepath, maxBytes=10*1024*1024, backupCount=5),  # Rotating file handler
        logging.StreamHandler(sys.stdout)
    ]
)

# Create logger instance
logger = logging.getLogger("Logger")