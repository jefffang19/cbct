import model.model as model
import model.fit as fit
import utils.load_dicom as load_dicom
import numpy as np
from cv2 import cv2
import os


def inference(path):

    # define window level and window width
    WL = 0
    WW = 1000

    # init model
    net = model.get_model(os.path.join(
        path, 'weights/save_model_unet_resnet152.pth'))

    # read dicom img
    slices = load_dicom.read_dicom(os.path.join(path, 'input'))

    # fit model
    pred = fit.fit(net, slices[0])

    # save the results to output/
    s = ((slices[0] + WW/2) / WW * 255).astype(np.uint8)
    pr = ((pred - np.min(pred)) / (np.max(pred) -
                                   np.min(pred)) * 255).astype(np.uint8)

    cv2.imwrite(os.path.join(path, 'output/ori.jpg'), s)
    cv2.imwrite(os.path.join(path, 'output/proc.jpg'), pr)

    print('result saved!')


if __name__ == '__main__':
    path = '../..'

    inference(path)
