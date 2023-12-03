Below we make the following assumptions about the <u>**Directory Structure**</u> of the **Image Datasets** for **our** code to work _as is_. 

Feel free to adapt the code as needed to work with your directory structures.

-------------------------
1. **for the COCO dataset** ( https://cocodataset.org/ ) our top_directory looks like this:
    
    <top_COCO_directory>/2014/{train2014, val2014}/{*.jpg}
    
    \# _i.e., we used images from the 2014 COCO version that are in the train/val sets (later versions of COCO also contain all these images)_     

-------------------------

2. **for Visual Genome** ( https://arxiv.org/abs/1602.07332 )

    <top_Visual_Genome_directory>/{VG_100K, VG_100K_2}/{*.jpg}
    
    \# _Visual Genome's photos were split by the authors into those two: 100K and 100K_2 subfolders_

-------------------------
3. **for Flickr30k** ( https://arxiv.org/abs/1505.04870 )

    <top_Flickr30k_directory>/{*.jpg}
    
    \# _in the original dataset, they listed 31,783 images here_
-------------------------

4. **for Emotional_Machines** ( https://arxiv.org/abs/1705.07543 )
    
    <top_Emotional_Machines_directory>/{*.jpg}
    
    \# _in the original dataset, they listed 10,767 images here_
-------------------------

5. for the paper of **You et al.** ( https://arxiv.org/abs/1605.02677 )
    
    <top_You_et_al_directory>/<emotion_category>/{*.jpg}
    
    \# _In the original release, the authors cover eight emotion categories and share 23,185 images._\
    \# _They do so under corresponding sub-folders such as awe, amusement, etc., and the final image files look like this:_\
    \# _<top\_You\_et\_al_directory>/amusement/amusement\_0000.jpg_
- - - - - - 
