#!/usr/bin/env python

import sys
import os
import re
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from matplotlib.dates import DateFormatter
import pylab
from datetime import datetime
from tabulate import tabulate


#os.chdir('g:/cygwin64/home/argon/conversantexercise')


def parseDataMontoya():
        montoya_file = "data.Montoya.txt"
        if not os.path.isfile(montoya_file):
                sys.exit(1)

        dcI_dates, dcI_values, dcI_dc, dcI_record = [],[],[],[]
        dcS_dates, dcS_values, dcS_dc, dcS_record = [],[],[],[]
        dcA_dates, dcA_values, dcA_dc, dcA_record = [],[],[],[]
        lines = []
        # Parse thru each line
        with open(montoya_file) as mf:
                lines = mf.readlines()
                lines.pop(0)
        mf.close()
        
        # Find each item per data center and append its respective list
        for line in lines:
                items = re.split(r'\t+', line.strip())
                dt = datetime.fromtimestamp(float(items[1]))
                
                if line.find('dc=I') != -1:
                        dcI_record.append(items)
                        dcI_dates.append(dt)
                        dcI_values.append(items[2])
                        dcI_dc.append(items[3])
                        continue
                elif line.find('dc=S') != -1:
                        dcS_record.append(items)
                        dcS_dates.append(dt)
                        dcS_values.append(items[2])
                        dcS_dc.append(items[3])
                        continue
                elif line.find('dc=A') != -1:
                        dcA_record.append(items)
                        dcA_dates.append(dt)
                        dcA_values.append(items[2])
                        dcA_dc.append(items[3])
                        continue

        #dataCenters = sorted(set(all_record_datacenter))
        # Create plot figures for all 3 Data Centers
        f_dcI = plt.figure()
        f_dcS = plt.figure()
        f_dcA = plt.figure()
        datefmt = DateFormatter('%m-%d-%y %H:%M')
        Icvrted_dates = date2num(dcI_dates)
        Scvrted_dates = date2num(dcS_dates)
        Acvrted_dates = date2num(dcA_dates)
        

        # Data Center I
        Iax = f_dcI.add_subplot(111)
        Iax.xaxis.set_major_formatter(datefmt)
        Iax.xaxis.set_label_text('Time')
        Iax.yaxis.set_label_text('Value Points')
        Iax.title.set_text('RTB Request data points from Data Center I')
        Iax.plot_date(Icvrted_dates, dcI_values, label="Data Center I", color="red",marker="x",markersize=10)

        # Data Center S
        Sax = f_dcS.add_subplot(111)
        Sax.xaxis.set_major_formatter(datefmt)
        Sax.xaxis.set_label_text('Time')
        Sax.yaxis.set_label_text('Value Points')
        Sax.title.set_text('RTB Request data points from Data Center S')
        Sax.plot_date(Scvrted_dates, dcS_values, label="Data Center S", color="blue",marker="o",markersize=10)
        
        # Data Center A
        Aax = f_dcA.add_subplot(111)
        Aax.xaxis.set_major_formatter(datefmt)
        Aax.xaxis.set_label_text('Time')
        Aax.yaxis.set_label_text('Value Points')
        Aax.title.set_text('RTB Request data points from Data Center A')
        Aax.plot_date(Acvrted_dates, dcA_values, label="Data Center A", color="black",marker="*",markersize=10)

        
        plt.show()
        
        return
        


def main():
        parseDataMontoya()
       
        
if __name__ == "__main__":
        main()
