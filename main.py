import pandas as pd
#import netCDF4
import nctoolkit as nc

if __name__ == "__main__":
    nc_name = 'dutch_harbor_1_mhw_2006.nc'

    ds = nc.open_data(nc_name)

#print(ds)

#df = ds.to_dataframe()

#print(df)