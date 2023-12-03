import os.path as osp
import warnings
import pandas as pd
from typing import Dict

from .you_aaai16 import you_file_path_to_local_image_file
from .coco import coco_image_name_to_local_image_file
from .visual_genome import visual_genome_image_name_to_local_image_file


def link_image_files_to_dataframe(dataframe: pd.DataFrame, top_img_dirs: Dict[str, str]) -> None:
    """Find the full filepaths of images referenced in Affection on the local hard drive and add them as corresponding entries in the column
    of the input dataframe, titled `image_file`.

    Args:
        dataframe (pd.DataFrame): Dataframe with `image_name` and `dataset` columns carrying publicly-shared annotations of Affection.
        top_img_dirs (Dict[str, str]): A dictionary pointing for each image-dataset we used in Affection (e.g., COCO) to its top-directory in 
            your hard drive. See https://github.com/optas/eeai/blob/master/eeai/docs/Affection_Images.md for the assumed directory structure.
    Returns:
        Nothing, operation alters input dataframe inplace.
    """
    dataset_name_to_loader = dict()
    dataset_name_to_loader['you_aaai_affective'] = you_file_path_to_local_image_file
    dataset_name_to_loader['coco_affective'] = coco_image_name_to_local_image_file
    dataset_name_to_loader['visual_genome_affective'] = visual_genome_image_name_to_local_image_file
        
    def basic_image_name_to_image_file(x, top_image_dir):  # default linker
        return osp.join(top_image_dir, x)
    
    dataframe['image_file'] = None
    
    for dataset in dataframe['dataset'].unique():
        loader = dataset_name_to_loader.get(dataset, basic_image_name_to_image_file)
        top_img_dir = top_img_dirs[dataset]
        
        mask = dataframe['dataset'] == dataset
        dataframe.loc[mask, 'image_file'] = dataframe['image_name'][mask].apply(lambda x: loader(x, top_img_dir))
        
    assert all(~dataframe.image_file.isna())
    
    if not all(dataframe.image_file.apply(osp.exists)):
        warnings.warn('There exist image files that were not found in the hard drive.')    