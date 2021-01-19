from skimage.feature import hog

new_size = (150,150)

def preprocessing(img):
    img = img.resize(new_size)

    hog_features = hog(img,
                    orientations=8,
                    pixels_per_cell=(5, 5),
                    cells_per_block=(1, 1),
                    block_norm='L2')

    hog_features = hog_features.reshape(1, -1)

    return hog_features