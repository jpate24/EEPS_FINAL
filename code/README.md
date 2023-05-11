Thank you so much for taking the time to view my project :)

The main code directory contains only scripts used in the project. There are two main categories: cliamte analysis and image analysis.

Climate analysis files:

    analyze_climate_data.R 
    - graphs the climate (SWH and SST) data
 
    preprocess_NSIDC_data.R
    - processes and graphs ice cover data

    get_climate_data.py
    - uses CDS API to get climate data

    preprocess_climate_data.py
    - preprocesses SWH and SST data

Landsat analysis files:

    downsample.py
    - downsamples an image, helper method

    get_image_data/get_image_data_db:
    - retreives images 

    preprocess_image_data.py
    - executes preprocessing techniques - main'ish file

    plot_image.py
    - plots a band or scene

The figure files hold some of the generated figurs in no particualr order

The data file holds the datasets involved in their raw form

The code in this project is influenced by packages pylandsat and earthpy
