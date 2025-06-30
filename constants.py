import os

class Constants:
    ## PATHs ##
    DATASET_ROOT = '../ip102_v1.1/'
    IMG_ROOT = os.path.join(DATASET_ROOT, "images")
    TRAIN_PATH = os.path.join(DATASET_ROOT, "train.txt")
    VAL_PATH = os.path.join(DATASET_ROOT, "val.txt")
    TEST_PATH = os.path.join(DATASET_ROOT, "test.txt")