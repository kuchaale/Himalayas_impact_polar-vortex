import cdstoolbox as ct

   
@ct.application(title='Calculate composite mean')
@ct.output.download()
def download_application():
    variable = 'total_column_ozone'
    
    data_ls = []
    year_ls = [1981, 1982, 1982, 1982, 1983, 1983, 1984, 1984, 1984, 1985, 1985,
       1986, 1988, 1988, 1988, 1989, 1990, 1991, 1993, 1994, 1994, 1995,
       1996, 1996, 1998, 1998, 1999, 2000, 2001, 2002, 2002, 2003, 2003,
       2005, 2006, 2006, 2006, 2007, 2008, 2008, 2009, 2009, 2010]
    month_ls = [ 2,  1,  2, 12,  2,  3,  2,  3, 12,  1,  2,  1,  1,  2,  3,  2,  1,
        2,  4,  1,  2, 12,  1,  3,  1,  3,  3,  2,  1,  2, 12,  2,  3,  1,
        1,  1,  2,  1,  1, 12,  1,  2,  2]
    day_ls = [21, 21, 20,  8, 14, 11,  1, 13, 19, 10, 24, 30, 21, 11, 20, 14, 16,
       15,  3, 11, 17, 11, 21, 14, 15, 13, 16, 21, 24,  6,  6,  8,  3, 31,
        3, 30, 20,  2, 21, 18, 22, 21, 13]
    time_ls = [f'{i:02d}:00' for i in range(1,24)]
    for year, month, day in zip(year_ls, month_ls, day_ls):
        data_may_08 = ct.catalogue.retrieve(
            'reanalysis-era5-single-levels',
            {
                'variable': variable,
                'product_type': 'reanalysis',
                'year': [
                   str(year)
                ],
                'month': [
                    f'{month:02d}'
                ],
                'day': [
                    f'{day:02d}'
                ],
                'time': time_ls,
            }
        )
        data_ls.append(data_may_08)    

    data = ct.cube.concat(data_ls,  dim='time')
    return data