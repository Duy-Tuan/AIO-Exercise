import sys
sys.path.append('./core/')

from cfg import COLLECTION_PATH, root_img_path
from cfg import os ,tqdm, np, Image, json
from cfg import embedding_function
from cfg import HNSW_SPACE
from utilies import get_files_path


files_path = get_files_path(path=root_img_path)

def get_single_image_embedding(image : np.ndarray):
    embedding = embedding_function._encode_image(image=image)
    return np.array(embedding)

def add_embedding(files_path):
    ids = []
    embeddings = []
    mapping_paths = {}
    
    for id_filepath, filepath in tqdm(enumerate(files_path)):
        ids.append(f'id_{id_filepath}')
        image = Image.open(filepath)
        # Convert Image to nparray
        image = np.array(image)
        embedding = get_single_image_embedding(image=image)
        embeddings.append(embedding.tolist())
        mapping_paths[f'id_{id_filepath}'] = filepath

    return embeddings,ids, mapping_paths

def __save_collection(embeddings,ids, mapping_paths, save_path):
    print('start saving ')
    """
        Save collection
        * save collection.metadata
        * save features embeddings
        * save ids
    """
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    embeddings_path = os.path.join(save_path, 'embeddings.npy')
    np.save(embeddings_path, embeddings)

    ids_path = os.path.join(save_path, 'ids.json')
    with open(ids_path, 'w') as ids_file:
        json.dump(ids, ids_file)

    files_path = os.path.join(save_path, 'mapping_paths.json')
    with open(files_path, 'w') as path_file:
        json.dump(mapping_paths, path_file)

def load_collection(client,collection_name,metadata,load_path):
    """
        Collection loading: Return Collection
        * Collection Building
        * Features embeddings loading
        * ids loading
        * mapping_paths loading
    """
    
    # Load the ids from the .json file
    ids_path = os.path.join(load_path, 'ids.json')
    with open(ids_path, 'r') as ids_file:
        ids = json.load(ids_file)

    # Load the paths from the .json file
    mapping_paths = os.path.join(load_path, 'mapping_paths.json')
    with open(mapping_paths, 'r') as paths_file:
        mapping = json.load(paths_file)

    # Load the embeddings from the .npy file
    embeddings_path = os.path.join(load_path, 'embeddings.npy')
    embeddings = np.load(embeddings_path, allow_pickle=True)

    # Get or create the collection in ChromaDB
    #collection = client.get_or_create_collection(name=collection_name)
    collection = client.get_or_create_collection( name = collection_name,
                                                        metadata={HNSW_SPACE: metadata})
    # Add the embeddings and ids back to the collection
    collection.add(
        embeddings=embeddings.tolist(), 
        ids = ids)

    return collection, mapping

def main():
    print('>>>>>>>>>>>>>>>>>>>  Save ...')
    
    embeddings, ids, mapping_paths = add_embedding(files_path)
    __save_collection(embeddings,ids, mapping_paths, os.path.join(COLLECTION_PATH))
    
    print('>>>>>>>>>>>>>>>>>>> Finished ...')

if __name__ == "__main__":
    main() 