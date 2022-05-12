import xarray as xr
import glob
from aostools.climate import ComputeRefractiveIndex


cesta = '/mnt/4data/CMAM/0A.daily/'
ta_list = sorted(glob.glob(cesta+'ta/ta_6hrPlev_CMAM_CMAM30-SD_r1i1p1_*-*18.nc'))
ua_list = sorted(glob.glob(cesta+'ua/ua_6hrPlev_CMAM_CMAM30-SD_r1i1p1_*-*18.nc'))
Earth_radius = 6.378e+6

for i,(ta_file, ua_file) in enumerate(zip(ta_list[:], ua_list[:])):
    print(ta_file, ua_file)
    suffix = ta_file[len(cesta)+5:]
    print(suffix)
    ds_ta = xr.open_dataset(ta_file)
    ds_ua = xr.open_dataset(ua_file)
    
    if i==0:
        lat = ds_ta.lat.values
        pres = ds_ta.plev.values/100.
    
    uz = ds_ua.ua.mean(['lon'])#
    Tz = ds_ta.ta.mean(['lon'])
        
    n_k_ls = []
    for k in range(1,4):
        n_k = ComputeRefractiveIndex(lat,pres,uz,Tz,k)
        n_k_ls.append(n_k)

    n_k_xa = xr.concat(n_k_ls, dim='wavenumber')
    n_k_xa['wavenumber'] = range(1,4)
    
    n_k_xa.name = 'refr_index'
    outfile = '{0}refr_index/refr_index{1}'.format(cesta, suffix)
    print(outfile)
    n_k_xa.to_netcdf(outfile)

