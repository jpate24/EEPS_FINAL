import numpy as np
import rasterio as rio
import matplotlib.pyplot as plt
from pylandsat import Scene
from osgeo import gdal
import os
from pylandsat import preprocessing
import earthpy.mask as em
import earthpy.plot as ep
import earthpy.spatial as es

import get_image_data
import plot_image 
import tifffile
import downsample
import write_out

scene_list = get_image_data.get_data()



# Access band data
for scene in scene_list:
    
    plot_image.plot_bands(scene)

    print(scene.available_bands())
    print(scene.product_id)
    print(scene.sensor)
    print(scene.date)
    print(scene.mtl['IMAGE_ATTRIBUTES']['CLOUD_COVER_LAND'])

    if scene.mtl['PRODUCT_METADATA']['SENSOR_ID'] == 'MSS':
        nir = scene.nir2.read(1)
    else: 
        nir = scene.nir.read(1)
    
    red = scene.red.read(1)
    green = scene.green.read(1)

    print(nir.shape)

    # Use reflectance values instead of DN
    '''
    if scene == scene_sens2 or scene == scene_sens1 or scene == scene_sens3:
        nir_gain, nir_bias = scene.nir2._gain_bias()
    else: 
        nir_gain, nir_bias = scene.nir._gain_bias()
    
    red_gain, red_bias = scene.red._gain_bias()
    green_gain, green_bias = scene.green._gain_bias()

    sun_elev_angle = scene.mtl['IMAGE_ATTRIBUTES']['SUN_ELEVATION']

    nir = preprocessing.to_reflectance(nir, nir_gain, nir_bias, sun_elevation_angle=sun_elev_angle)
    red = preprocessing.to_reflectance(red, red_gain, red_bias, sun_elevation_angle=sun_elev_angle)
    green = preprocessing.to_reflectance(green, green_gain, green_bias, sun_elevation_angle=sun_elev_angle)

    # Save file to disk
    
    if scene == scene_sens2 or scene == scene_sens1 or scene == scene_sens3:
        with rio.open(str(scene.product_id + '_reflected.TIF' ), 'w', **scene.nir2.profile) as dst:
            dst.write(nir, 1)
    else:
        with rio.open(str(scene.product_id + '_reflectedNIR.TIF' ), 'w', **scene.nir.profile) as dst:
            dst.write(nir, 1)

    with rio.open(str(scene.product_id + '_reflectedR.TIF' ), 'w', **scene.red.profile) as dst:
            dst.write(red, 1)

    with rio.open(str(scene.product_id + '_reflectedG.TIF' ), 'w', **scene.green.profile) as dst:
            dst.write(green, 1)
'''
    path = str(scene.product_id + '/')
    nir_name = str(path+ scene.product_id + '_nirtoa.TIF')
    red_name = str(path + scene.product_id + '_redtoa.TIF')
    green_name = str(path + scene.product_id + '_greentoa.TIF')

    if scene.mtl['PRODUCT_METADATA']['SENSOR_ID'] == 'MSS':  
        nir_toa = scene.nir2.to_reflectance()
    else: 
        nir_toa = scene.nir.to_reflectance()

    green_toa = scene.green.to_reflectance()
    red_toa = scene.red.to_reflectance()

    ep.plot_bands(np.array([nir,red,green]), title = ['nir original','red original','green original'])
    plt.show()
    ep.plot_bands(np.array([nir_toa,red_toa,green_toa]), title = ['nir TOA','red TOA','green TOA'])
    plt.show()
   

    #create cloud masks
    mask = np.where(red > .18, 1, 0)

    nir_name = str(path+ scene.product_id + '_nircloud.TIF')
    red_name = str(path + scene.product_id + '_redcloud.TIF')
    green_name = str(path + scene.product_id + '_greencloud.TIF')

    nir_cloudmask = em.mask_pixels(nir, mask, vals=[1])
    red_cloudmask = em.mask_pixels(red, mask)
    green_cloudmask = em.mask_pixels(green, mask)

    ep.plot_bands(np.array([nir_cloudmask,red_cloudmask,green_cloudmask]), title = ['nir cloudmask','red cloudmask','green cloudmask'])
    plt.show()
    
    #create terrain shadow masks
    
    nir_name = str(path+ scene.product_id + '_nirshadow.TIF')
    red_name = str(path + scene.product_id + '_redshadow.TIF')
    green_name = str(path + scene.product_id + '_greenshadow.TIF')

    sun_angle = scene.mtl['IMAGE_ATTRIBUTES']['SUN_ELEVATION']
    azimuth = scene.mtl['IMAGE_ATTRIBUTES']['SUN_AZIMUTH']
    nir_shade = es.hillshade(nir, azimuth, sun_angle)
    red_shade = es.hillshade(red, azimuth, sun_angle)
    green_shade = es.hillshade(green, azimuth, sun_angle)

    ep.plot_bands(np.array([nir_shade,red_shade,green_shade]), title = ['nir shade','red shade','green shade'])
    plt.show()

    output_name = str(scene.product_id + '_multibanded.TIF')
    nir_name = str(scene.product_id + '_nir.TIF')
    red_name = str(scene.product_id + '_red.TIF')
    green_name = str(scene.product_id + '_green.TIF')
    
    all_bands = np.stack((nir,red,green), axis=2)
    
    tifffile.imwrite(output_name, all_bands)

    if scene.mtl['PRODUCT_METADATA']['SENSOR_ID'] != 'MSS':
        row = all_bands.shape[0] // 2  # Fixed incorrect shape index
        col = all_bands.shape[1] // 2  # Fixed incorrect shape index
        print(row)
        print(col)
        downsampled = downsample.downscale_image(all_bands, (row, col))
        print(downsample.shape)
        tifffile.imwrite(output_name, downsampled)  # Used tifffile to save the downscaled image
    else: 
        tifffile.imwrite(output_name, all_bands)


        
