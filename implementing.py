#!/usr/bin/env python

import data_containers as dc
import numpy as np


def main(config_data):

    # Load Data from .csv file
    if config_data["datafile"]:
        data_path = config_data["datafile"]
        csv_header_01 = config_data["csv_header"].split(',')
        print(type(csv_header_01))
        print("CSV header from cnf file:",csv_header_01)

        lst_det = dc.DataList()
        lst_det.append_data_from_csv(filename=data_path,csv_header=csv_header_01)

        # print("filtering: MCCs start at: ", lst_det.get_min_mcc(),
        #       "and end at: ", lst_det.get_max_mcc())
        # print("filtering: The lst_det keys:",lst_det[0].keys())
        #
        # print("filtering: No filtering applied yet.")
        # print("filtering: MCCs start at: ", lst_det.get_min_mcc(),
        #           "and end at: ", lst_det.get_max_mcc())
        # print("mcc",lst_det.get_array_mcc())
        # print("x",lst_det.get_array_x())
        # print("y",lst_det.get_array_y())
        # print("rho",lst_det.get_array_rho())
        # print("theta",lst_det.get_array_theta_deg())
        # print("rvel",lst_det.get_array_rvel())
    else:
        print("filtering: lst_det is empty.")




if __name__ == "__main__":
    config_data = dc.cnf_file_read("./setup.cnf")
    if config_data:
        main(config_data)
