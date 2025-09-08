## Notes

### Ito et al. (2024)

"Mapping Dissolved Oxygen Concentrations by Combining
Shipboard and Argo Observations Using Machine Learning Algorithms."

- I like the inclusion of with/without Argo - is both an interesting question and a good way to showcase the value of the program.
- Ship bottle and CTD data from WOD18.
- Observations binned into 1 deg x 1 deg boxes. Defined on 47 depth levels from 0-1000m (WOD standard). Argo data mapped onto this same grid field. 
- ML _predictand_ is oxygen concentration. ML _predictors_ are absolute salinity, conservative temperature, pressure, potential density, buoyancy frequency, and time/location/month. 
- Both neural network and random forest algorithms are used through Scikit-learn (v. 1.3)
- Random 80%/20% learning/validation data sets. Also used Decadal Group K-folds method for validation (DKCV). 
- In DKCV, final "decade" is actually 15 years, effectively encompassing almost all of the Argo-O2 era. Nice for evaluation of the Argo program. 

## References

Addey, Charles Izuma. 2022. “Using Biogeochemical Argo Floats to
Understand Ocean Carbon and Oxygen Dynamics.” *Nature Reviews Earth &
Environment* 3 (11): 739–39.
<https://doi.org/10.1038/s43017-022-00341-5>.

Cervania, Ahron A., and Roberta C. Hamme. 2024. “Isopycnal Shoaling
Causes Interannual Variability in Oxygen on Isopycnals in the Subarctic
Northeast Pacific.” *Journal of Geophysical Research: Oceans* 129 (7):
e2023JC020414. https://doi.org/<https://doi.org/10.1029/2023JC020414>.

Feucher, Charlène, Esther Portela, Nicolas Kolodziejczyk, and Virginie
Thierry. 2022. “Subpolar Gyre Decadal Variability Explains the Recent
Oxygenation in the Irminger Sea.” *Communications Earth & Environment* 3
(1): 279. <https://doi.org/10.1038/s43247-022-00570-y>.

Gordon, C., K. Fennel, C. Richards, L. K. Shay, and J. K. Brewster.
2020. “Can Ocean Community Production and Respiration Be Determined by
Measuring High-Frequency Oxygen Profiles from Autonomous Floats?”
*Biogeosciences* 17 (15): 4119–34.
<https://doi.org/10.5194/bg-17-4119-2020>.

Gouretski, V., L. Cheng, J. Du, X. Xing, F. Chai, and Z. Tan. 2024. “A
Consistent Ocean Oxygen Profile Dataset with New Quality Control and
Bias Assessment.” *Earth System Science Data* 16 (12): 5503–30.
<https://doi.org/10.5194/essd-16-5503-2024>.

Ito, Takamitsu, Ahron Cervania, Kaylin Cross, Sanika Ainchwar, and Sara
Delawalla. 2024. “Mapping Dissolved Oxygen Concentrations by Combining
Shipboard and Argo Observations Using Machine Learning Algorithms.”
*Journal of Geophysical Research: Machine Learning and Computation* 1
(3): e2024JH000272.
https://doi.org/<https://doi.org/10.1029/2024JH000272>.

Johnson, Kenneth S., and Mariana B. Bif. 2021. “Constraint on Net
Primary Productivity of the Global Ocean by Argo Oxygen Measurements.”
*Nature Geoscience* 14 (10): 769–74.
<https://doi.org/10.1038/s41561-021-00807-z>.

Koelling, J., D. Atamanchuk, J. Karstensen, P. Handmann, and D. W. R.
Wallace. 2022. “Oxygen Export to the Deep Ocean Following Labrador Sea
Water Formation.” *Biogeosciences* 19 (2): 437–54.
<https://doi.org/10.5194/bg-19-437-2022>.

Maurer, Tanya L., Joshua N. Plant, and Kenneth S. Johnson. 2021.
“Delayed-Mode Quality Control of Oxygen, Nitrate, and pH Data on SOCCOM
Biogeochemical Profiling Floats.” *Frontiers in Marine Science* Volume
8 - 2021. <https://doi.org/10.3389/fmars.2021.683207>.

Stoer, Adam C., Yuichiro Takeshita, Tanya Lea Maurer, Charlotte Begouen
Demeaux, Henry C. Bittig, Emmanuel Boss, Hervé Claustre, et al. 2023. “A
Census of Quality-Controlled Biogeochemical-Argo Float Measurements.”
*Frontiers in Marine Science* Volume 10 - 2023.
<https://doi.org/10.3389/fmars.2023.1233289>.

Wu, Yingxu, Dorothee C. E. Bakker, Eric P. Achterberg, Amavi N. Silva,
Daisy D. Pickup, Xiang Li, Sue Hartman, David Stappard, Di Qi, and Toby
Tyrrell. 2022. “Integrated Analysis of Carbon Dioxide and Oxygen
Concentrations as a Quality Control of Ocean Float Data.”
*Communications Earth & Environment* 3 (1): 92.
<https://doi.org/10.1038/s43247-022-00421-w>.
