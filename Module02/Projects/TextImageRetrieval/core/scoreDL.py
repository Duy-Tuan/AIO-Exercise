from cfg import np, os
from cfg import embedding_function
from cfg import CLASS_NAME

from core.distance import absolute_difference
from core.distance import mean_square_difference
from core.distance import cosine_similarity
from core.distance import correlation_coefficient
from core.utilies import read_image_from_path, folder_to_images

def get_single_image_embedding(image : np.ndarray):
    embedding = embedding_function._encode_image(image=image)
    return np.array(embedding)

def get_l1_score(root_img_path, query_path, size, top_k = 5):
    """
        Return top_k (number of image) have minimum l1 score 
        * l1_score = l1{query image's feature ,(all of image's feature in all of folder)}
    """
    query = read_image_from_path(query_path, size)
    query_embedding = get_single_image_embedding(query)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) 

            embedding_list = []
            for idx_img in range(images_np.shape[0]):
                embedding = get_single_image_embedding(images_np[idx_img].astype(np.uint8))
                embedding_list.append(embedding)

            rates = absolute_difference(query_embedding, np.stack(embedding_list))
            ls_path_score.extend(list(zip(images_path, rates)))

    ls_path_score.sort(key=lambda x: x[1] , reverse = False )
    return query, ls_path_score[:top_k]

def get_l2_score(root_img_path, query_path, size):
    """
        Return top_k (number of image) have minimum l2 score 
        * l2_score = l2{query image's feature ,(all of image's feature in all of folder)}
    """
    query = read_image_from_path(query_path, size)
    query_embedding = get_single_image_embedding(query)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) 

            embedding_list = []
            for idx_img in range(images_np.shape[0]):
                embedding = get_single_image_embedding(images_np[idx_img].astype(np.uint8))
                embedding_list.append(embedding)
                rates = mean_square_difference(query_embedding, np.stack(embedding_list))
                ls_path_score.extend(list(zip(images_path, rates)))
    ls_path_score.sort(key = lambda x : x[1], reverse= False)
    return query, ls_path_score


def get_cosine_similarity_score(root_img_path, query_path, size):
    """
        Return top_k (number of image) have minimum cosine similarity score 
        * cosine_similarity_score = cosine_similarity{query image's feature ,(all of image's feature in all of folder)}
    """
    query = read_image_from_path(query_path, size)
    query_embedding = get_single_image_embedding(query)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) 

            embedding_list = []
            for idx_img in range(images_np.shape[0]):
                embedding = get_single_image_embedding(images_np[idx_img].astype(np.uint8))
                embedding_list.append(embedding)
                rates = cosine_similarity(query_embedding, np.stack(embedding_list))
                ls_path_score.extend(list(zip(images_path, rates)))

    ls_path_score.sort(key = lambda x: x[1], reverse = True)
    return query, ls_path_score

def get_correlation_coefficient_score(root_img_path, query_path, size):
    """
        Return top_k (number of image) have minimum correlation coefficient score 
        * correlation_coefficient_score = correlation_coefficient{query image's feature ,(all of image's feature in all of folder)}
    """
    query = read_image_from_path(query_path, size)
    query_embedding = get_single_image_embedding(query)
    ls_path_score = []
    for folder in os.listdir(root_img_path):
        if folder in CLASS_NAME:
            path = root_img_path + folder
            images_np, images_path = folder_to_images(path, size) 
            embedding_list = []

            for idx_img in range(images_np.shape[0]):
                embedding = get_single_image_embedding(images_np[idx_img].astype(np.uint8))
                embedding_list.append(embedding)
                rates = correlation_coefficient(query_embedding, np.stack(embedding_list))
                ls_path_score.extend(list(zip(images_path, rates)))
    return query, ls_path_score