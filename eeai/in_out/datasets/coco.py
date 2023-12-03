"""
Originally created at 4/6/21, for Python 3.x
"""

import os.path as osp


def coco_image_name_to_local_image_file(x, local_prefix_dir, year='2014'):
    img_name = osp.basename(x)
    if 'train' in img_name:
        split_subdir = f'train{year}'
    else:
        split_subdir = f'val{year}'
    return osp.join(local_prefix_dir, split_subdir, img_name)