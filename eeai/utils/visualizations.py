"""
Originally created at 2/23/21, for Python 3.x
"""

import os.path as osp
import numpy as np

from PIL import Image
from IPython.display import display

from ..in_out.datasets.various import wikiart_file_name_to_style_and_painting


def show_image_caption_at_loc(df, loc=None, img_column='Input.image_url',
                              utter_column='original_utterance', worker_column=None, dataset=None,
                              print_meta=True, top_img_dir=None, derive_img_location=False):
    """
    :param df:
    :param loc: int, index of row in df. if None random int will be generated.
    :param top_img_dir:
    :param img_column:
    :param utter_column:
    :param dataset:
    :return:
    """

    if loc is None:
        loc = np.random.randint(len(df))
        
    if worker_column is not None:        
        w_id = df.loc[loc][worker_column]
        if print_meta:        
            print(w_id, end='\t')

    if print_meta:
        utterance = df.loc[loc][utter_column]
        print(utterance)

    if print_meta:
        emotion = df.loc[loc]['emotion']
        print(emotion)

    if not derive_img_location:
        return Image.open(df.loc[loc][img_column])

    if derive_img_location:
        if dataset is None:
            dataset = df.loc[loc]['dataset']

        if dataset[-len('_affective'):] == '_affective':
            dataset = dataset[:-len('_affective')]   # convenience e.g., coco_affective => coco

        if dataset == 'mixed':        
            x = df.loc[loc][img_column]        
            if 'COCO' in x:
                dataset = 'coco'
            elif 'emotion_recognition_AAAI_16' in x:
                dataset = 'yang'
            elif 'Flickr30k' in x:
                dataset = 'flickr30k'
            elif 'Emotional_Machines' in x:
                dataset = 'emotional_machines'
            else:
                assert False

        default_img_dir = dict()
        default_img_dir['yang'] = '/home/optas/DATA/Images/Emotion_Recognition_AAAI_2016/Flickr'
        default_img_dir['coco'] = '/home/optas/DATA/Images/COCO/2014'
        default_img_dir['wikiArt'] = '/home/optas/DATA/Images/Wiki-Art/rescaled_max_size_to_600px_same_aspect_ratio'
        default_img_dir['flickr30k'] = '/home/optas/DATA/Images/Flickr30k/flickr30k_images'
        default_img_dir['emotional_machines'] = '/home/optas/DATA/Images/Emotional_Machines/raw'
        default_img_dir['visual_genome'] = '/data/Visual_Genome/Images'

        if top_img_dir is None:
            top_img_dir = default_img_dir[dataset]
            
        if dataset == 'yang':
            image_name = osp.basename(df.loc[loc][img_column])        
            emo = image_name.split('_')[0]
            im_local_file = osp.join(top_img_dir, emo, image_name)
            return Image.open(im_local_file)

        if dataset == 'coco':
            image_name = osp.basename(df.loc[loc][img_column])
            if 'train' in image_name:
                im_local_file = osp.join(top_img_dir, 'train2014', image_name)
            else:
                im_local_file = osp.join(top_img_dir, 'val2014', image_name)
            return Image.open(im_local_file)

        if dataset == 'visual_genome':
            image_name = osp.basename(df.loc[loc][img_column])
            im_local_file = osp.join(top_img_dir, 'VG_100K', image_name)
            if not osp.exists(im_local_file):
                im_local_file = osp.join(top_img_dir, 'VG_100K_2', image_name)
            return Image.open(im_local_file)

        if dataset in ['pixabay', 'unsplash', 'flickr30k', 'emotional_machines']:
            im_local_file = osp.join(top_img_dir, osp.basename(df.loc[loc][img_column]))
            return Image.open(im_local_file)

        if 'wikiArt' in dataset:
            art_style, painting = wikiart_file_name_to_style_and_painting(df.loc[loc][img_column])
            im_local_file = osp.join(top_img_dir, art_style, painting + '.jpg')
            return Image.open(im_local_file)

    
def show_random_captions(df):
    if 'image_file' not in df.columns:
        raise NotImplementedError()

    random_image = df.image_file.sample(1).iloc[0]
    ndf = df[df.image_file == random_image]
    display(Image.open(random_image))
    for _, row in ndf.iterrows():
        print(row['emotion'].capitalize(), row['utterance'])
        
        
def stack_images_horizontally(file_names, save_file=None):
    ''' Opens the images corresponding to file_names and
    creates a new image stacking them horizontally.
    '''
    images = list(map(Image.open, file_names))
    widths, heights = list(zip(*(i.size for i in images)))
    total_width = sum(widths)
    max_height = max(heights)
    new_im = Image.new('RGBA', (total_width, max_height))

    x_offset = 0
    for im in images:
        new_im.paste(im, (x_offset, 0))
        x_offset += im.size[0]
    if save_file is not None:
        new_im.save(save_file)
    return new_im