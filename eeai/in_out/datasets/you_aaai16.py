"""
Originally created at 4/6/21, for Python 3.x

Load data published with (AAAI-2016) paper: https://arxiv.org/abs/1605.02677
"""

import os.path as osp
from ..basics import files_in_subdirs

def you_file_path_to_local_image_file(x, local_prefix_dir):
    img_name = osp.basename(x)
    emotion = img_name.split('_')[0]   # image_name's format is = <emotion>_<name>.jpg
    return osp.join(local_prefix_dir, emotion, img_name)


def load_image_files_of_yang_aaai16(img_top_dir):
    emotions = ['amusement', 'anger', 'awe', 'contentment', 'disgust', 'excitement', 'fear', 'sadness']

    all_img_files = []
    for emo in emotions:
        emo_top_img_dir = osp.join(img_top_dir, emo)
        emo_img_files = [f for f in files_in_subdirs(emo_top_img_dir, '.jpg$')]
        assert all([emo in osp.basename(f) for f in emo_img_files])
        all_img_files += emo_img_files

    assert len(set(all_img_files)) == len(all_img_files), 'unique names'
    print('{} image files were found.'.format(len(all_img_files)))
    return all_img_files