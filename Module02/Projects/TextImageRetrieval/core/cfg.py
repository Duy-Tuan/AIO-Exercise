import os 
import chromadb
from tqdm import tqdm
from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import argparse
import json
import time

from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
embedding_function = OpenCLIPEmbeddingFunction()

ROOT = 'data'
CLASS_NAME = sorted(list(os.listdir(f'{ROOT}/train')))
COLLECTION_PATH = 'database'
  
root_img_path = f"{ROOT}/train/"
query_path = f"{ROOT}/test/Orange_easy/0_100.jpg"
image_size = (640, 640)

HNSW_SPACE = "hnsw:space"

if __name__ == "__main__":
    print("Nothing")