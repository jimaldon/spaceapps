"""Download a NEOSAT survey from ftp."""


# Imports.
import os
import logging
import sys
import io
import argparse
from os.path import join, basename
from ftplib import FTP
from utils import setup_logging


# Logging.
logger = logging.getLogger(__name__)
log_file = '{}.log'.format(os.path.basename(sys.argv[0]))
setup_logging(log_path=log_file, print_level='INFO', logger=logger)


# Args.
def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Args')
    parser.add_argument('--out_dir', default='_out', type=str, help='output folder')
    args = parser.parse_args()

    return args


FTP_ASC_CSA = "ftp.asc-csa.gc.ca"
NEOSAT_SUBDIR = "users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO"


def main(args):
    survey = "2018/345/TOI138/FINE_POINT"
    logger.info('Fetching {} survey'.format(survey))
    os.makedirs(args.out_dir, exist_ok=True)
    
    ftp = FTP(FTP_ASC_CSA)
    ftp.login()

    ftp.cwd(NEOSAT_SUBDIR)
    files = ftp.nlst()

    ftp.cwd(survey)
    files = ftp.nlst()
    num_files = len(files)
    for i, f in enumerate(files):
        logger.info('Saved {}/{} files'.format(i + 1, num_files))
        ftp.retrbinary("RETR " + f, open(join(args.out_dir, f), 'wb').write)


if __name__ == '__main__':
	args = parse_args()
	main(args)
