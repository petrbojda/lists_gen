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
        logger.info('Configuration file: %s',cfg_logfile_path)
    # Load Data from .csv file
    if config_data["radar_datafile"]:
        radar_data_path = config_data["radar_datafile"]

        radar_csv_header = config_data["radar_csv_header"].split(',')
        radar_point_attributes = config_data["radar_detection_attributes"].split(',')
        logger.info(' ')
        logger.info('RADAR Data')
        logger.info(90*'=')
        logger.info('RADAR data file: %s', radar_data_path)
        logger.info("Radar CSV header from cnf file: %s", radar_csv_header)
        logger.info("Attributes of the RADAR point class: %s", radar_point_attributes)
        radar_detections = dc.DataList(data_point_attributes=radar_point_attributes)
        logger.info("List of radar detections created: %s", radar_detections)
        radar_detections.append_data_from_csv(filename=radar_data_path, csv_header=radar_csv_header)
        logger.info("List of radar detections filled with: %s", radar_detections)
    else:
        logging.warning("filtering: List of radar detections is not created, datapath to RADAR data in csv file does not exists.")

    if config_data["dgps_datafile"]:
        dgps_data_path = config_data["dgps_datafile"]
        logger.info('DGPS data file: %s', dgps_data_path)
        dgps_csv_header = config_data["dgps_csv_header"].split(',')
        dgps_point_attributes = config_data["DGPS_reference_attributes"].split(',')
        logger.info(' ')
        logger.info('DGPS Reference Data')
        logger.info(90 * '=')
        logger.info("DGPS CSV header from cnf file: %s", dgps_csv_header)
        logger.info("Attributes of the DGPS point class: %s", dgps_point_attributes)
        dgps_references = dc.DataList()
        logger.info("List of dgps references created: %s", dgps_references)
        dgps_references.append_data_from_csv(filename=dgps_data_path, csv_header=dgps_csv_header)
        logger.info("List of dgps references filled with: %s", dgps_references)
    else:
        logging.warning("filtering: List of dgps references is not created, datapath to DGPS data in csv file does not exists.")


if __name__ == "__main__":
    config_data = dc.cnf_file_read("./setup.cnf")
    if config_data:
        main(config_data)
