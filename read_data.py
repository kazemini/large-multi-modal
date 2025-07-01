import numpy as np
import os
from torch.utils.data import Dataset
from constants import Constants
from PIL import Image

## Get Path of .txt file path,label like: 75219.jpg 101
## returns array of tuples in (path, label)
def load_split_file(file_path):
    with open(file_path,'r') as f:
        samples = np.array(
            [(path,int(label)) for path, label in (line.strip().split() for line in f)],
            dtype= object
        )
    return samples


def load_labels(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    labels = []
    ids = []
    for line in lines:
        id_str, label = line.strip().split(maxsplit=1)
        id = int(id_str)
        ids.append(id)
        labels.append(label)
    return ids, labels


class CustomImageDataset(Dataset):
    def __init__(self,image2class_path,transform=None):
        
        self.data_list = load_split_file(image2class_path)
        self.root_dir = Constants.IMG_ROOT    
        self.transform = transform

    def __len__(self):
        return len(self.data_list)
    
    def __getitem__(self, idx):
        path, label = self.data_list[idx]
        image_path= os.path.join(self.root_dir,path)
        image= Image.open(image_path)

        if self.transform:
            image = self.transform(image)

        return image, label

