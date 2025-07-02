import os

class Constants:
    ## PATHs ##
    DATASET_ROOT = './ip102_v1.1/'
    IMG_ROOT = os.path.join(DATASET_ROOT, "images")
    TRAIN_PATH = os.path.join(DATASET_ROOT, "train.txt")
    VAL_PATH = os.path.join(DATASET_ROOT, "val.txt")
    TEST_PATH = os.path.join(DATASET_ROOT, "test.txt")
    ID_CLASSES_PATH = os.path.join('./', "classes.txt")
    PROMPT_GEMINI = os.path.join('./', "prompt_gemini.txt")
    PROMPT_GPT = os.path.join('./', "prompt_gpt.txt")
    PROMPT_MOAH = os.path.join('./', "simple prompt.txt")
    BATCH_SIZE = 16
    SHUFFLE = True