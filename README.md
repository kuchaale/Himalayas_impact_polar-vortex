[![Python 3.7](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-369/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# On the impact of the Himalayas on the polar vortex
**A. Kuchar, P. Sacha, R. Eichinger, Ch. Jacobi, P. Pisoft, and H. Rieder**

Submitted to [?](?).

Code used to process and visualise the model and other data outputs in order to reproduce figures in the manuscript.
Model data are available [here](http://climate-modelling.canada.ca/climatemodeldata/cmam/output/CMAM/CMAM30-SD/index.shtml). All datasets already preprocessed can be found [here](?).

Notebooks for each individual figure as well as for two data tables are in the [`code/` directory](code), while the figures themselves are in the [`plots/` directory](plots).

### Figures
|  #  | Figure                                                                                                                                                                                                    | Notebook                                                                              | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  1 | [Composites documenting vortex morphology](plots/PVmoments_lagA_composite_20days_poster.pdf)                                                                              | [moment_calculation_distribution_in_CMAM30-sd_composites.ipynb](code/moment_calculation_distribution_in_CMAM30-sd_composites.ipynb)                       |   [uref_calculation_CMAM.ipynb](code/uref_calculation_CMAM.ipynb), [uref_ration_validation.ipynb](code/uref_ration_validation.ipynb), [moments_fast_example.py](code/moments_fast_example.py), [vor_fast_setup.py](https://github.com/wseviour/vortex-moments/blob/master/vor_fast_setup.py), [vor_fast.py](https://github.com/wseviour/vortex-moments/blob/master/vor_fast.py)                                                                                                                               |
|  2 | [Composite anomalies of NAM](plots/NAM_lagA_composite_HIonly_FDR.pdf)                                                      | [NAM_lagA.ipynb](code/NAM_lagA.ipynb)                 |                                                                                                                           |
|  3 | [Conditional probabilities that NAM is less or equal -1](plots/NAM_lagA_probability_10hPa_CI.pdf)                | [NAM_lagA.ipynb](code/NAM_lagA.ipynb)|                                                                                              |
|  4 | [Composites of anomalies documenting evolution total column ozone for CMAM](plots/TO3_anomalies_lagA_FDR.pdf) | [toz_anomalies_CMAM.ipynb](code/toz_anomalies_CMAM.ipynb)                     |       [composite_example_ERA5.py](code/composite_example_ERA5.py)                                                                                                                     |
|  5 | [Effective_diffusivity composite at 450 K](plots/effective_diffusivity_HI-composite@450K_pv_FDR-xcontour.pdf)                                                                                      | [effective_diffusivity_HI_composite-pv-xcontour.ipynb](code/effective_diffusivity_HI_composite-pv-xcontour.ipynb)                           |                 [xcontour_isoentropic_CMAM-script.py](code/xcontour_isoentropic_CMAM-script.py)                                                                                                       |
|  6 | [Composite anomalies of Eliassen-Palm flux](plots/EPflux-analysis_Himalayas_anomalies_20days_zm_wEPFDsignificancetropopause_DJFonly_pvalue005_lags0357_FDR.pdf)                                               | [GRL_reproduce_Fig1_Himalayas_lagA.ipynb](code/GRL_reproduce_Fig1_Himalayas_lagA.ipynb)                     |                                                                        |
|  7 | [Composite anomalies of refractive index and zonally averaged OGWD](plots/OGWDzm+refr_lagA_composite_CI_daily.pdf)                                                  | [OGWD+refr_index_himalayas_composite_lagA.ipynb](code/OGWD+refr_index_himalayas_composite_lagA.ipynb)               |   [refraction_index_calc.py](code/refraction_index_calc.py)                                                                                                                        |


#### Supplementary figures
|  #  | Figure                                                                                                                                                                                                    | Notebook                                                                              | Dependencies                                                                                                                                                             |
|:---:|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  S1 | [Explained variance of NAM time series.](plots/NAM_explained_variance.pdf)                                               | [NAM_CMAM_variance.ipynb](code/NAM_CMAM_variance.ipynb)                     | |
|  S2 | [Residual circulation and ozone anomalies composite](plots/vmro3+RC_percentages_all_20days_zm_wabsolutevaluesandtropopause_DJFonly_HIonly.pdf)                                               | [chap3_vykreslovani_dizertace_new-DJFonly-tropo-strato-meso.ipynb](code/chap3_vykreslovani_dizertace_new-DJFonly-tropo-strato-meso.ipynb)                     | |
| S3 | Composites in absolute values documenting total column ozone in [CMAM](plots/TO3_CMAM30-SD_himalayas_composite_verif_fig.pdf), [MERRA2](plots/TO3_MERRA2_himalayas_composite_verif_fig.pdf), and [ERA5](plots/TO3_ERA5_himalayas_composite_verif_fig.pdf)                                                                             | [total_ozone_MERRA2_opendap_vs_CMAM30SD.ipynb](code/rtotal_ozone_MERRA2_opendap_vs_CMAM30SD.ipynb)                       |                                          [composite_example_ERA5.py](code/composite_example_ERA5.py)                                                                                          |
|  S4 | [Age of air anomalies](plots/stmeanage@7000Pa_anomalies_allwclim_20days_PlateCarree_DJFonly+HIonly.pdf)                                                                              | [bootstrap_statistical_significance@height-visualization-contourswithclimatology.ipynb](code/bootstrap_statistical_significance@height-visualization-contourswithclimatology.ipynb)                       |                                                                                                                                    |
|  Html | [interactive file showing Empirical distribution function of interpeak timescales](plots/ecdf_interpeak_times.html)                                                                              | [interpeak_times_analysis.ipynb](code/interpeak_times_analysis.ipynb)                       |                                                                                                                                    |
                                                  



    
    
### Auxiliar notebooks:
- [Plumb_flux_analysis_Himalayas.ipynb](code/Plumb_flux_analysis_Himalayas.ipynb) + ?
- [refractive_index_lagA.ipynb](code/refractive_index_lagA.ipynb)
- [VMFC_ERA5_composite.ipynb](code/VMFC_ERA5_composite.ipynb)
- [predictability_wavenumbers.ipynb](code/predictability_wavenumbers.ipynb)
- [EPFD_vs_OGWD_correlation.ipynb](code/EPFD_vs_OGWD_correlation.ipynb)
- [OGWD_trendanalysis_CCMI-SD.ipynb](code/OGWD_trendanalysis_CCMI-SD.ipynb)
- [influx_figure_using_composites.ipynb](code/influx_figure_using_composites.ipynb)
- [EPFD_lagA_again.ipynb](code/EPFD_lagA_again.ipynb)
- [geoapps_vs_xcontour.ipynb](code/geoapps_vs_xcontour.ipynb)
- [xcontour_isoentropic_CMAM.ipynb](code/xcontour_isoentropic_CMAM.ipynb)
- [OGWD_himalayas_composite_lagA.ipynb](code/OGWD_himalayas_composite_lagA.ipynb)
- [vmrh2o_composite.ipynb](code/vmrh2o_composite.ipynb)
