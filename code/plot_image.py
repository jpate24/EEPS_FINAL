import rasterio as rio
import matplotlib.pyplot as plt
from pylandsat import Scene
import earthpy as et
import earthpy.spatial as es
import earthpy.plot as ep
import glob as glob
import os

def plot_bands(scene):
    landsat_path = []
    for file in scene._available_files():
        if file.endswith('.TIF'):
            file_path = 'toydata/' + scene.product_id + '/' + file
            rio.open(file_path)
            landsat_path.append(file_path)
    
    landsat_path.sort()
    array_stack, meta_data = es.stack(landsat_path, nodata=-9999)#0?
    titles = scene.available_bands()
    titles.append("quality")
    ep.plot_bands(array_stack, title=titles)