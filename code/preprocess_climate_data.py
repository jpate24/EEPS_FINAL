import metview as mv
import pandas as pd
import numpy as np
import csv

filename = "../Data/climate_data/download.grib"
if mv.exist(filename):
    wd = mv.read(filename)
else:
    wd = mv.gallery.load_dataset(filename)
print(wd)
print(len(wd))

attributes = ['sst', 'swh']

for attr in attributes: 

    attribute = wd.select(shortName=attr)
    attribute_dates = mv.valid_date(attribute)
    
    attr_list = [mv.average(v) for v in attribute]
    attr_date_list = [ date.year for date in attribute_dates]
    print(len(attr_date_list))
    print(attr_date_list)
    
    attr_avgs = ((pd.Series(attr_list)).interpolate()).tolist()

    out = str(attr + '_averages.csv')
    fields = ['Value', 'Year']
    with open(out, 'w+') as f:
        write = csv.writer(f)
        write.writerow(fields)
        write.writerows(zip(attr_avgs, attr_date_list))
