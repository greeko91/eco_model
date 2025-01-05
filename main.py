import pandas as pd
#import netCDF4
import nctoolkit as nc
from multiprocessing import freeze_support, Process


def worker():
    nc_name = 'dutch_harbor_1_mhw_2006.nc'
    ds = nc.open_data(nc_name)
    print(ds)
    df = ds.to_dataframe()
    print(df)
    


if __name__ == "__main__":
    freeze_support()
    p = Process(target=worker)
    p.start()
    p.join()

