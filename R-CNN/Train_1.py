import os
import numpy as np
from SelectiveSearch import SelectiveSearch

#Designation of paths
Dataset_path = "C:\\Pascal VOC 2012\\VOC_train_val2012\\VOCdevkit\\VOC2012"
IMAGE_FOLDER = "JPEGImages"
PROPOSAL_FOLDER = "Proposals"

#How many proposals should come out
Max_rects = 2000

#Searching regional proposals
ProposalGather= SelectiveSearch(min_area=9)
for img_dir, _, img_files in os.walk(os.path.join(Dataset_path, IMAGE_FOLDER)):
    for img_file in img_files:
        np.save(
                os.path.join(Dataset_path, PROPOSAL_FOLDER, img_file.split(".")[0]+".npy"),
                ProposalGather.execute(os.path.join(img_dir,img_file), Max_rects))