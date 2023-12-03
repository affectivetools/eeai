# Information about the public annotations of Affection

The publicly available annotations of Affection are comprised by essentially three assets: 
1. `emotion clicks`: the dominant emotion of an annotator observing an image
2. `explanations`: text that justifies why each annotator had the specific emotional reaction
3. `names` information of the image data we used in our studies

These are shared in two **csv** files, which you can download once you sign our terms of use [here](https://affective-explanations.org/#dataset):

| Filename | Description |
| --- | --- |
|language/version_0/**affection_raw_public_version_0.csv**| The **raw** Affection data from Amazon Mech. Turk|
|language/version_0/**affection_preprocessed_public_version_0.csv**| The data after we clean them and **preprocess** them|

Both files contain **526,749 lines** each corresponding to a unique annotation of Affection.

--------------------------------------

### A. Details for affection\__raw_\_public\_version\_0.csv:

It contains 5 columns with the following data:

| Column | Description |
| --- | --- |
| workerid  | Unique anonymized identifier corresponding to each individual annotator|
| utterance | The **raw** text of the explanation the annotator submitted |
| emotion   | The underlying emotion he indicated (one out of nine options)|
| dataset   | String indicating which image dataset the underlying image was taken from (one of five options) |
|           | E.g., ``coco_affective`` implies an image from [COCO](https://cocodataset.org/), please see the naming convention used [here](#image-datasets-naming-conventions)|
| image_name| The string identifier of the image, **exactly** as found in each corresponding dataset|

### B. Details for affection\__preprocessed_\_public\_version\_0.csv:

This file is a copy of the `raw` version above, with the additional five columns:
| Column | Description |
| --- | --- |
|utterance_spelled| The text of the explanation after we apply manual and automatic spell-checking,|
| |or very rarely (less than 0.01%) rewrite parts of the raw explanation upon further communication with the annotator. |
| |This text is lowercased and puctuation marks have been removed.|
|tokens| Simple, white-space-based, tokenization  of the spelled utterance |
|tokens_len| Cardinality of the resulting tokens.|
|tokens_encoded| Integer representation of the tokens based on the vocabulary we used (shared with the public .csv files above).|
||Using this vocabulary has the advantage of being able to directly reuse our trained models,|
||or in your (new) studies apply the same mapping to rare words to the \<UNK\> symbol. |
|split|	one of {train/test/val} to indicate which set the annotation belongs |
||this is what we followed when we trained all **our** neurals nets (e.g., speakers)|

Of course, in your study you can use your own tokenizers etc. The above meta-data are only meant to help you if you want to repeat _exactly_ our experimental protocols.


--------------------------------------

### Image datasets: Naming Conventions 
The five image datasets we have used in our study to aggregate and annotate a total of 85k images, along with their respective papers are the following:

| Commonly Used Name | Dataset Name as used in Affection | \| Images \| | Link-to-Paper|
|------------------------------| --- | :---:  | :---: |
| COCO               | coco_affective               | 22,766 (out of 123,287) |[arXiv](https://arxiv.org/abs/1405.0312) |
| Visual Genome      | visual_genome_affective      | 16,634 (out of 108,249) | [arXiv](https://arxiv.org/abs/1602.07332) |
| FlickR30k          | flickr30k_affective          | 13,196 (out of 31,783)  |[arXiv](https://arxiv.org/abs/1505.04870) |
| -                  | you_aaai_affective           | 21,808 (out of 23,185)  |[arXiv](https://arxiv.org/abs/1605.02677) |
| -                  | emotional_machines_affective | 10,603 (out of 10,767)  |[arXiv](https://arxiv.org/abs/1705.07543) |
|||**85,007** images|


The second column above shows the five names we have used internally to refer to the different image datasets we used for our studies. These names cover the five options of the column ```dataset``` of the above mentioned .csv files that capture all Affection's annotations.

To link an image to its annotations in Affection you need to further consult the column named `image_name` of the the above .csv files. This column indicates the <b>filenames</b> of the images we annotated; maintaining the <u>**same**</u> names as those in the public versions of these datasets. For instance, ```coco_affective```, ```COCO_train2014_000000206192.jpg``` corresponds to <a href="https://cocodataset.org/#explore?id=206192"> this </a> image from the <a href="https://cocodataset.org/">COCO</a> dataset. Note that the name ```COCO_train2014_000000206192.jpg``` is exactly the same to the name you will get for this image if you download the COCO dataset. <b>The same is true for all the image_name strings in our shared .csv files</b>


**Notice**: The five image datasets we used _have overlaps_ (duplicate images) among each other; and even duplicates among themselves. We removed such duplicates when building Affection. In the table above we give in parenthesis, "(out of N)", the original number of images these datasets had. When we take this overlaps into account we have covered **entirely** the `you_aaai_affective` and `emotional_machines_affective` datasets.
