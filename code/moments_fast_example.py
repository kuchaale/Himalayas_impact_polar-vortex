from netCDF4 import Dataset
import matplotlib.pyplot as plt
import numpy as np
import vor_fast
import vor_fast_setup
import xarray as xr
import sys

#input variables
plot = False
save2netcdf = True
resolution = 'full'

# Read in NetCDF file with geopotential height values
print('opening')
ncin = xr.open_dataset('zg_daily_CMAM_CMAM30-SD_r1i1p1_19790101-20101231_10hPa.nc')
gph = ncin.zg.values
lons = ncin.lon.values
lats = ncin.lat.values
days = ncin.time.values#[:100]
ncin.close()

# Set up cartesian mapping xypoints and restrict to NH
gph_nh, lats_nh, xypoints = vor_fast_setup.setup(gph,lats,lons,'NH')



# Calculate diagnostics for each day
print('Calculating for resolution: '+resolution)
for iday, day in enumerate(days):
    if iday % 1000 == 0:
        print('Calculating moments for day '+str(iday), day)
    moments = vor_fast.calc_moments(gph_nh[iday,:,:],lats_nh,lons,xypoints,
                                    hemisphere='NH',field_type='GPH',
                                    edge=3.02e4,resolution=resolution)
    if iday == 0:
        ds = xr.Dataset(moments, coords={'time': [day]})
    else:
        temp = xr.Dataset(moments, coords={'time': [day]})
        ds = xr.concat([ds,temp], dim='time')
    

if save2netcdf:
    print('saving')
    ds.to_netcdf('moment_calculation_w_obj-area_CMAM.nc')

# Plot timeseries
if plot:
    print('plotting')
    fig, axes = plt.subplots(nrows=2)
    ds['aspect_ratio'].plot(ax = axes[0])
    ds['aspect_ratio'].where(ds.aspect_ratio >= 2.4).plot(ax = axes[0], color= 'red')
    ds['centroid_latitude'].plot(ax = axes[1])
    ds['centroid_latitude'].where(ds.centroid_latitude < 66).plot(ax = axes[1])
    plt.tight_layout()
    plt.savefig('ar_centroid_full.pdf', bbox_inches = 'tight')

