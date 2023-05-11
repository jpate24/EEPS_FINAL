import numpy as np
import get_image_data
from pylandsat import Scene
import rasterio as rio
import tifffile
import earthpy.plot as ep
import matplotlib.pyplot as plt

def downscale_image(image, new_dimensions):
    # Get current dimensions
    current_rows, current_cols, num_bands = image.shape

    # Calculate scaling factors
    scale_rows = current_rows // new_dimensions[0]
    scale_cols = current_cols // new_dimensions[1]

    # Check if new dimensions are zero
    if scale_rows == 0 or scale_cols == 0:
        raise ValueError("New dimensions result in zero scaling factor")

    # Calculate new dimensions after downscaling
    new_rows = current_rows // scale_rows
    new_cols = current_cols // scale_cols

    # Downscale the image
    downsampled_image = image[:new_rows*scale_rows, :new_cols*scale_cols, :]
    downsampled_image = downsampled_image.reshape(new_rows, scale_rows, new_cols, scale_cols, num_bands)
    downsampled_image = np.mean(downsampled_image, axis=(1, 3)) 

    return downsampled_image