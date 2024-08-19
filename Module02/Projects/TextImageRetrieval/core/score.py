from cfg import os, CLASS_NAME

from core.distance import absolute_difference
from core.distance import mean_square_difference
from core.distance import cosine_similarity
from core.distance import correlation_coefficient
from core.utilies import read_image_from_path, folder_to_images

def get_l1_score(root_img_path, query_path, size, top_k = 5):
    """
        Return top_k (number of image) have minimum l1 score 
        * l1_score = l1{query image ,(all of image in all of folder)}
    """
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) 

            rates = absolute_difference(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))

    ls_path_score.sort(key=lambda x: x[1], reverse=False)
    print(ls_path_score[:top_k])

    return query, ls_path_score[:top_k]

def get_l2_score(root_img_path, query_path, size, top_k = 5):
    """
        Return top_k (number of image) have minimum l2 score 
        * l2_score = l2{query image ,(all of image in all of folder)}
    """
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) 

            rates = mean_square_difference(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))

    ls_path_score.sort(key=lambda x: x[1], reverse=False)
    print(ls_path_score[:top_k])
    return query, ls_path_score[:top_k]

def get_cosine_similarity_score(root_img_path, query_path, size, top_k = 5):
    """
        Return top_k (number of image) have minimum cosine similarity score 
        * cosine_similarity_score = cosine_similarity{query image ,(all of image in all of folder)}
    """
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) 

            rates = cosine_similarity(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))

    ls_path_score.sort(key=lambda x: x[1], reverse=True)
    print(ls_path_score[:top_k])
    
    return query, ls_path_score[:top_k]


def get_correlation_coefficient_score(root_img_path, query_path, size, top_k = 5):
    """
        Return top_k (number of image) have minimum correlation coefficient score 
        * coefficient scor = cosine_similarity{query image ,(all of image in all of folder)}
    """
    query = read_image_from_path(query_path, size)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) 

            rates = correlation_coefficient(query, images_np)
            ls_path_score.extend(list(zip(images_path, rates)))

    ls_path_score.sort(key=lambda x: x[1], reverse=True) 
    print(ls_path_score[:top_k])

    return query, ls_path_score[:top_k]