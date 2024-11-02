import sys
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt


def visualize_nifti_slice(filepath, slice_index=50):
    # Load the NIFTI file
    nifti_img = nib.load(filepath)
    data = nifti_img.get_fdata()

    # Get the desired slice
    data_slice = data[:, :, slice_index]

    # Visualize the slice
    plt.imshow(data_slice.T, cmap="gray", origin="lower")
    plt.title(f'Slice {slice_index}')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ipython main_surface.py <path_to_nifti_file>")
        sys.exit(1)

    filepath = sys.argv[1]
    visualize_nifti_slice(filepath)