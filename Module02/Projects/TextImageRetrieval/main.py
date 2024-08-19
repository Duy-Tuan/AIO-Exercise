from core.utilies import plot_results
import core.score as score
import core.scoreDL as scoreDL

from core.cfg import root_img_path, query_path, image_size, argparse
pretrained_true = 'pretrained: True'
pretrained_false= 'pretrained: False'

def __query_l1 (args):
    """
        Return l1 score 
    """
    if args.pretrained == 'True':
        print(pretrained_true)
        _, ls_path_score = scoreDL.get_l1_score(root_img_path, query_path, image_size)
    else:
        print(pretrained_false)
        _, ls_path_score = score.get_l1_score(root_img_path, query_path, image_size)

    plot_results(query_path, ls_path_score, reverse=False)

def __query_l2(args):
    """
        Return l2 score 
    """
    if args.pretrained == 'True':
        print(pretrained_true)
        _, ls_path_score = scoreDL.get_l2_score(root_img_path, query_path, image_size)
    else:
        print(pretrained_false)
        _, ls_path_score = score.get_l2_score(root_img_path, query_path, image_size)
    plot_results(query_path, ls_path_score, reverse=False)


def __query_cosine(args):
    """
        Return cosine similarity score 
    """
    if args.pretrained == 'True':
        print(pretrained_true)
        _, ls_path_score = scoreDL.get_cosine_similarity_score(root_img_path, query_path, image_size)
    else:
        print(pretrained_false)
        _, ls_path_score = score.get_cosine_similarity_score(root_img_path, query_path, image_size)
    plot_results(query_path, ls_path_score, reverse=True)


def __query_coeff(args):
    """
        Return correlation coefficient
    """
    if args.pretrained == 'True':
        print(pretrained_true)
        _, ls_path_score = scoreDL.get_correlation_coefficient_score(root_img_path, query_path, image_size)
    else:
        print(pretrained_false)
        _, ls_path_score = score.get_correlation_coefficient_score(root_img_path, query_path, image_size)
    plot_results(query_path, ls_path_score, reverse=True)
    

def main():
    parser = argparse.ArgumentParser(description="The different of programer")
    
    parser.add_argument('-m', type = str, choices=['l1', 'l2', 'cosine', 'coeff'], required=True, default='l1',
                        help="Select score: l1, l2, cosine, hoặc coeff.")
    
    parser.add_argument('-pretrained',  type = str, choices=['False', 'True'],  required=True, default='False',
                        help="Extract Model: True or False")

    args = parser.parse_args()
    if args.m == 'l1':
        print('metric: l1')
        __query_l1(args)

    elif args.m == 'l2':
        print('metric: l2')
        __query_l2(args)

    elif args.m == 'cosine':
        print('metric: cosine')
        __query_cosine(args)

    elif args.m == 'coeff':
        print('metric: coeff')
        __query_coeff(args)

if __name__ == "__main__":
    main()