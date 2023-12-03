"""
Basic utilities to load/visualize data of the Visual Genome paper: https://arxiv.org/abs/1602.07332
"""

import json
import pandas as pd
import os.path as osp
from PIL import Image


def visual_genome_image_name_to_local_image_file(x, local_prefix_dir):
    img_name = osp.basename(x)
    possibility_1 = osp.join(local_prefix_dir, 'VG_100K', img_name)
    if osp.exists(possibility_1):
        return possibility_1    
    return osp.join(local_prefix_dir, 'VG_100K_2', img_name)


def show_vg_image(image_id, top_vg_img_dir):
    vg_sub_folder_1 = 'VG_100K'
    vg_sub_folder_2 = 'VG_100K_2'
    try:
        return Image.open(osp.join(top_vg_img_dir, vg_sub_folder_1, str(image_id) + '.jpg'))
    except:
        return Image.open(osp.join(top_vg_img_dir, vg_sub_folder_2, str(image_id) + '.jpg'))


def extract_vg_phrase_of_largest_region_per_image(vg_region_desc_file, min_tokens=5):
    with open(vg_region_desc_file) as fin:
        region_descriptions = json.load(fin)

    raw_data = []
    for r in region_descriptions:
        raw_data.extend(r['regions'])

    regions_df = pd.DataFrame(raw_data)
    regions_df = regions_df.assign(area=regions_df.width * regions_df.height)
    print(f'Using {len(regions_df)} regions across {len(regions_df.image_id.unique())} images')

    if min_tokens != None:
        tokens_len = regions_df['phrase'].apply(lambda x: len(x.split()))
        regions_df = regions_df[tokens_len >= min_tokens]
        regions_df.reset_index(inplace=True, drop=True)

    # Find largest area-wise caption of each image
    sub_df = regions_df.iloc[regions_df.groupby('image_id')['area'].idxmax()]
    sub_df.reset_index(inplace=True, drop=True)
    return sub_df
