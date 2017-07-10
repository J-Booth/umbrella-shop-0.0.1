# =============================================================================
# Author: Joshua Peter Booth
# Purpose: Umbrella Shop (GUI)
# File name: _log.py
# From: 12/06/2017 - 30/06/2017
# =============================================================================
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.propagate = False
log_format = '%(asctime)s - %(levelname)s - %(funcName)s - %(message)s - ' \
             'Line: %(lineno)d'
formatter = logging.Formatter(log_format)

fh = logging.FileHandler('log_file.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

