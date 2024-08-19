import sys
sys.path.append('./core/')
from cfg import Image, np , os, plt,mpimg, CLASS_NAME
   
def get_files_path(path):
    files_path = []
    for label in CLASS_NAME:
        label_path = path + "/" + label
        filenames = os.listdir(label_path)
        for filename in filenames:
            filepath = label_path + '/' + filename
            files_path.append(filepath)
    return files_path
   
                                    
def read_image_from_path(path, size):
    im = Image.open(path).convert('RGB').resize(size)
    return np.array(im)

def folder_to_images(folder, size):
    """
        Return all of Image's information:
        * image's path: numpy array
        * image data: numpy array shape (num image, h, w, 3)
    """
    list_dir = [folder + '/'+ name for name in os.listdir(folder)]
    images_np = np.zeros(shape=(len(list_dir), *size, 3))
    images_path = []
    for i, path in enumerate(list_dir):
        images_np[i] = read_image_from_path(path, size)
        images_path.append(path)
        
    images_path = np.array(images_path)
    return images_np, images_path


def plot_results(query_path, results, reverse=False):
    """
    Plots the query image along with the top N results.
    
    Parameters:
    - query_path: Path to the query image.
    - results: A list of tuples, where each tuple contains the image path and the label.
    - reverse: If True, reverse the order of the results.
    """
    if reverse:
        results = results[::-1]
    
    n_results = len(results)
    
    # Define the number of rows and columns based on the number of images
    n_cols = 5                                          # Set the maximum number of columns
    n_rows = 1 + (n_results // n_cols)                  # +1 for the query image

    _, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 3, n_rows * 3))
    
    # Plot the query image
    query_img = mpimg.imread(query_path)
    axes[0, 0].imshow(query_img)
    axes[0, 0].axis('off')
    axes[0, 0].set_title(f"Query Image: {query_path.split('/')[-1]}")

    # Plot the results
    for i, (img_path, label) in enumerate(results):
        row = (i + 1) // n_cols
        col = (i + 1) % n_cols
        img = mpimg.imread(img_path)
        axes[row, col].imshow(img)
        axes[row, col].axis('off')
        axes[row, col].set_title(f"Top {i + 1}: {label}")
    
    for i in range(n_results + 1, n_rows * n_cols):
        row = i // n_cols
        col = i % n_cols
        axes[row, col].axis('off')
    
    plt.tight_layout()
    plt.show()
    
def plot_chromadb_results(query_path, mapping_paths, results):
    """
        Plot query image and results
    """
    query_image = Image.open(query_path)
    
    mapping_paths_results = []
    for id in results['ids'][0]  :
        mapping_paths_results.append(mapping_paths[id])

    # Calculate number of Columns and number of Rows
    n_results = len(mapping_paths_results)
    grid_size = int(np.ceil(np.sqrt(n_results + 1)))  # Adding 1 for query image

    plt.figure(figsize=(grid_size * 5, grid_size * 5))
    plt.subplot(grid_size, grid_size, 1)
    plt.imshow(query_image)
    plt.title("Query Image")
    plt.axis('off')

    # Results Ploting
    for i, result_file in enumerate(mapping_paths_results):
        plt.subplot(grid_size, grid_size, i + 2)
        result_image = Image.open(result_file)
        plt.imshow(result_image)
        plt.title(f"Result {i + 1}")
        plt.axis('off')
    plt.show()