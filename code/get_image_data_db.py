
from datetime import datetime
import numpy as np
from shapely.geometry import Point
from pylandsat import Catalog, Product
from pylandsat.database import sync_catalog, sync_wrs

sync_catalog()
sync_wrs()

catalog = Catalog()

begin = datetime(1979, 1, 1)
end = datetime(2021, 12, 31)

MSS_path_list = [76,77,78,79,80,81,82,83,84,85,86]
path_list_11 = [65,66,67,68]
path_list_10 = [69,70,71,72,73,74,75,76,77,78,79,80]
path_list_9 = [81,82]

for path in MSS_path_list:
    # Results are returned as a list
    scenes = catalog.search(
        begin=begin,
        end=end,
        sensors=['LM01', 'LM02','LM03'],
        path = path,
        row=10,
        maxcloud=20
    )
    for scene in scenes:
        # Get the product ID of the first scene
        product_id = scene.get("product_id")

        # Download the scene
        product = Product(product_id)
        product.download(out_dir='~/Documents/EEPS 1720/code/data/MSS')

for path in path_list_9:
    # Results are returned as a list
    scenes = catalog.search(
        begin=begin,
        end=end,
        sensors=['LT04', 'LT05','LE07', 'LC08'],
        path = path,
        row=9,
        maxcloud=80,
        tiers='T1'
    )
    for scene in scenes:
        product_id = scene.get("product_id")
        product = Product(product_id)
        product.download(out_dir='data/ROW_9')

for path in path_list_10:
    # Results are returned as a list
    scenes = catalog.search(
        begin=begin,
        end=end,
        sensors=['LT04', 'LT05','LE07', 'LC08'],
        path = path,
        row=10,
        maxcloud=80,
        tiers='T1'
    )
    for scene in scenes:
        product_id = scene.get("product_id")
        product = Product(product_id)
        product.download(out_dir='data/ROW_10')

for path in path_list_11:
    # Results are returned as a list
    scenes = catalog.search(
        begin=begin,
        end=end,
        sensors=['LT04', 'LT05','LE07', 'LC08'],
        path = path,
        row=11,
        maxcloud=80,
        tiers='T1'
    )
    for scene in scenes:
        product_id = scene.get("product_id")
        product = Product(product_id)
        product.download(out_dir='data/ROW_11')


