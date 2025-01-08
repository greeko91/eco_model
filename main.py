import netCDF4 as nc
    
nc_name = 'dutch_harbor_1_mhw_2006.nc'
ds = nc.Dataset(nc_name, 'r')

print(ds.variables)

# Долгота shape = (3060, )
lat = ds.variables['lat'][:]
# Ширина shape = (4680, )
lon = ds.variables['lon'][:]
# Размер волны в точке на Земле shape = (3060, 4680)
Band1 = ds.variables['Band1'][:]

