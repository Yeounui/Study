import numpy as np
import cv2


class SelectiveSearch:
    def __init__(self, min_area=25):
        self.min_area = min_area
        # Set ss_object = OpenCV selective search object instance
        self.ss_object = cv2.ximgproc.segmentation.createSelectiveSearchSegmentation()

    def execute(self, img_path, max_rects):
        """
        Performs Selective Search on a given image, returning a list of proposed
        regions.
        Input(s):
        -image: numpy array representing an image
        -max_rects: the maximum number of rectangles to return
        -min_area: the min_area a proposed region can be
        Output(s):
        -accepted_rects: list of region proposals (rects)
        """

        print("Initiate selective search - {}".format(img_path))

        # Set the base image of the object
        image = cv2.imread(img_path)
        self.ss_object.setBaseImage(image)

        # Switch to fast but low recall Selective Search method
        self.ss_object.switchToSelectiveSearchFast()

        # run selective search segmentation on image set as Base
        print("Selective searching...")
        rects = self.ss_object.process()  # one rect: x1, y1, w, h

        # filtering out results only sufficiently large regions
        # keep only the first max_rects number of regions
        print("Manipulating rects...")
        rects = rects[:max_rects]
        #[np.greater(rects[:, 2] * rects[:, 3], self.min_area)]
        print(rects.shape)

        #transform format to  y1, x1, y2, x2
        y1= rects[:, 1]
        x1= rects[:, 0]
        y2= rects[:, 3]+rects[:, 1]
        x2= rects[:, 2]+rects[:, 0]

        result = np.concatenate([y1[:, np.newaxis], x1[:, np.newaxis], y2[:, np.newaxis], x2[:, np.newaxis]], axis=1)

        # and returning
        print("Selective search finished.")
        return result