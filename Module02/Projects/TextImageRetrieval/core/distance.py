from core.cfg import np

def absolute_difference(query, data):
    """
        Calculate Absolute Difference between query image (only 1 image) with all image in Database
        * query image shape : (h, w, 3)
        * database: (axis_batch_size, h, w, 3)
        * Return sum of difference of 3 channel (RGB channel) for each image (batch_size = 1)
    """
    axis_batch_size = tuple(range(1,len(data.shape)))
    return np.sum(np.abs(data - query), axis=axis_batch_size)

def mean_square_difference(query, data):
   """
        Calculate Mean Square Difference between query image (only 1 image) with all image in Database
        * query image shape : (h, w, 3)
        * database: (axis_batch_size, h, w, 3)
        * Return sum of difference of 3 channel (RGB channel) for each image (batch_size = 1)
    """
   axis_batch_size = tuple(range(1,len(data.shape)))
   return np.mean((data - query)**2, axis=axis_batch_size)

def cosine_similarity(query, data):
    """
        Calculate Cosine Similarity between query image (only 1 image) with all image in Database
        * query image shape : (h, w, 3)
        * database: (axis_batch_size, h, w, 3)
        * Return sum of Cosine Similarity of 3 channel (RGB channel) for each image (batch_size = 1)
    """
    axis_batch_size = tuple(range(1,len(data.shape)))
    query_norm = np.sqrt(np.sum(query**2))
    data_norm = np.sqrt(np.sum(data**2, axis=axis_batch_size))
    return np.sum(data * query, axis=axis_batch_size) / (query_norm*data_norm + np.finfo(float).eps)

def correlation_coefficient(query, data):
    """
        Calculate Cosine Similarity between query image (only 1 image) with all image in Database
        * query image shape : (h, w, 3)
        * database: (axis_batch_size, h, w, 3)
        * Return sum of Correlation Coefficient of 3 channel (RGB channel) for each image (batch_size = 1)
    """
    axis_batch_size = tuple(range(1,len(data.shape)))
    query_mean = query - np.mean(query)
    data_mean = data - np.mean(data, axis=axis_batch_size, keepdims=True)

    query_norm = np.sqrt(np.sum(query_mean**2))
    data_norm = np.sqrt(np.sum(data_mean**2, axis=axis_batch_size)) 
    return np.sum(data_mean * query_mean, axis=axis_batch_size) / (query_norm*data_norm + np.finfo(float).eps)