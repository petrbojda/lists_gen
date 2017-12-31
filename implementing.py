#!/usr/bin/env python

import data_containers as dc
import logging
import logging.config
import numpy as np


def main(config_data):
    if config_data["log_config_filename"]:
        cfg_logfile_path = config_data["log_config_filename"]
        logging.config.fileConfig(cfg_logfile_path)
        # create logger
        logger = logging.getLogger(__name__)
        # logfile_level = config_data["log_level"]
        # level_of_logging = getattr(logging,logfile_level.upper())
        # logging.basicConfig(filename=logfile_path,level=level_of_logging)
        logger.info('Started the test_implementing')
    # Load Data from .csv file
    if config_data["radar_datafile"]:
        radar_data_path = config_data["radar_datafile"]
        radar_csv_header = config_data["radar_csv_header"].split(',')
        radar_point_parameters = config_data["radar_detection_parameters"].split(',')
        logger.debug(90*'=')
        logger.debug("Radar CSV header from cnf file: %s", radar_csv_header)
        logger.debug("Parameters of the RADAR point class: %s", radar_point_parameters)
        radar_detections = dc.DataList()
        radar_detections.append_data_from_csv(filename=radar_data_path, csv_header=radar_csv_header)

    if config_data["dgps_datafile"]:
        dgps_data_path = config_data["dgps_datafile"]
        dgps_csv_header = config_data["dgps_csv_header"].split(',')
        dgps_point_parameters = config_data["DGPS_reference_parameters"].split(',')
        logger.debug(90 * '=')
        logger.debug("DGPS CSV header from cnf file: %s", dgps_csv_header)
        logger.debug("Parameters of the DGPS point class: %s", dgps_point_parameters)
        dgps_references = dc.DataList()
        dgps_references.append_data_from_csv(filename=dgps_data_path, csv_header=dgps_csv_header)
    else:
        logging.debug("filtering: lst_det is empty.")


if __name__ == "__main__":
    config_data = dc.cnf_file_read("./setup.cnf")
    if config_data:
        main(config_data)
