#!/usr/bin/env python

import data_containers as dc
import numpy as np


def main(config_data):

    # Load Data from .csv file
    if config_data["radar_datafile"]:
        radar_data_path = config_data["radar_datafile"]
        radar_csv_header = config_data["radar_csv_header"].split(',')
        radar_point_parameters = config_data["radar_detection_parameters"].split(',')
        print(90*'=')
        print("Radar CSV header from cnf file:", radar_csv_header)
        print("Parameters of the RADAR point class:", radar_point_parameters)
        radar_detections = dc.DataList()
        radar_detections.append_data_from_csv(filename=radar_data_path, csv_header=radar_csv_header)

    if config_data["dgps_datafile"]:
        dgps_data_path = config_data["dgps_datafile"]
        dgps_csv_header = config_data["dgps_csv_header"].split(',')
        dgps_point_parameters = config_data["DGPS_reference_parameters"].split(',')
        print(90 * '=')
        print("DGPS CSV header from cnf file:", dgps_csv_header)
        print("Parameters of the DGPS point class:", dgps_point_parameters)
        dgps_references = dc.DataList()
        dgps_references.append_data_from_csv(filename=dgps_data_path, csv_header=dgps_csv_header)


    else:
        print("filtering: lst_det is empty.")




if __name__ == "__main__":
    config_data = dc.cnf_file_read("./setup.cnf")
    if config_data:
        main(config_data)
