# Face-Human-Bench: A Comprehensive Face and Human Understanding Benchmark for Large Visual Language Models

<p align="center">
    <img src="https://github.com/Face-Human-Bench/face-human-bench/blob/main/pictures/logo.png" width="30%"> <br>
</p>


## Introduction

Faces and humans are crucial elements in social interaction and are widely included in everyday photos and videos. Therefore, a deep understanding of faces and humans will enable multi-modal assistants to achieve improved response quality and broadened application scope. Currently, the multi-modal assistant community lacks a comprehensive and scientific evaluation of face and human understanding abilities. In this paper, we first propose a hierarchical ability taxonomy that includes three levels of abilities. Then, based on this taxonomy, we collect images and annotations from publicly available datasets in the face and human community and build a semi-automatic data pipeline to produce problems for the new benchmark. Finally, the obtained Face-Human-Bench comprises a development set with 1800 problems and a test set with 1800 problems, supporting both English and Chinese. We conduct evaluations over 25 mainstream multi-modal large language models (MLLMs) with our Face-Human-Bench, focusing on the correlation between abilities, the impact of the relative position of targets on performance, and the impact of Chain of Thought (CoT) prompting on performance.
Moreover, inspired by multi-modal agents, we also explore which abilities of MLLMs need to be supplemented by specialist models.

 <img src="https://github.com/Face-Human-Bench/face-human-bench/blob/main/pictures/face_human_bench.png" alt="Image" width="800">


## 💥 News


- **[2025.1.7]** Our dataset is [accessible](https://github.com/Face-Human-Bench/face-human-bench/tree/main/data/Face-Human-Bench).
- **[2025.1.2]** Our paper is accessible at https://arxiv.org/abs/2501.01243.
- **[2024.7.28]** Our project homepage can be accessed at https://face-human-bench.github.io.



## Scores
Leaderboard of MLLMs on Face-Human-Bench(EN)：

<img src="https://github.com/Face-Human-Bench/face-human-bench/blob/main/pictures/leaderboard.png" alt="Image" width="800">

Comparison of different MLLMs on English and Chinese versions of the Face-Human-Bench：

<img src="https://github.com/Face-Human-Bench/face-human-bench/blob/main/pictures/EN-CN.png" alt="Image" width="800">

For more results, please refer to our website or paper.


## Data Acquisition
We comply with all agreements of the original public datasets used and do not involve further copying, publishing, or distributing any portion of the images from these datasets. We will only open-source the [JSON files](https://github.com/Face-Human-Bench/face-human-bench/tree/main/data/Face-Human-Bench) containing our test and development sets.

To help you reproduce the Face-Human-Bench Benchmark, we provide the following guidelines:

1. Download all original images from the relevant public datasets and organize them according to the file tree below.

```
<your_path>/raw_data
├── face
│   ├── CALFW
│   │   ├── calfw
│   │   └── calfw.zip
│   ├── CelebA
│   │   ├── img_align_celeba
│   │   ├── img_celeba
│   │   └── list_attr_celeba.txt
│   ├── CPLFW
│   │   ├── cplfw
│   │   └── cplfw.zip
│   ├── FF+
│   │   └── cropped
│   ├── LFW
│   │   ├── data
│   │   └── pairs.txt
│   ├── MLFW
│   │   ├── aligned
│   │   ├── mask_list.txt
│   │   ├── MLFW.zip
│   │   ├── origin
│   │   └── pairs.txt
│   ├── RAF-DB
│   │   ├── basic
│   │   └── compound
│   ├── SiW-Mv2
│   │   └── cropped
│   ├── SLLFW
│   │   └── pair_SLLFW.txt
│   └── UTKFace
│       ├── cropped
│       ├── part1
│       ├── part2
│       └── part3
└── human
    ├── HICO-DET
    │   ├── anno
    │   ├── HICO-DET
    │   ├── HICO-DET.tar.gz
    │   ├── metafile.yaml
    │   └── README.md
    ├── Market1501
    │   ├── distractors_500k.zip
    │   ├── Market-1501-v15.09.15
    │   └── Market-1501-v15.09.15.zip
    ├── PISC
    │   ├── annotation_image_info.json
    │   ├── domain.json
    │   ├── domain_split
    │   ├── domain_split.zip
    │   ├── image
    │   ├── images-00
    │   ├── images-01
    │   ├── images-02
    │   ├── images-03
    │   ├── occupation.json
    │   ├── relationship.json
    │   ├── relationship_split
    │   ├── relationship_split.zip
    │   └── test
    ├── ShTech
    │   ├── final_partA
    │   ├── final_partA.zip
    │   ├── ShanghaiTech_Crowd_Counting_Dataset
    │   └── ShanghaiTech_Crowd_Counting_Dataset.zip
    ├── SpatialSense
    │   ├── annotations.json
    │   ├── images
    │   ├── images.tar.gz
    │   └── SHA-256.txt
    └── WIDERAttribute
        ├── Image
        ├── Readme.txt
        ├── wider_attribute_annotation.zip
        ├── wider_attribute_image.tgz
        ├── wider_attribute_test.json
        └── wider_attribute_trainval.json
```
   
2. Use the [`prepare_data.py`](https://github.com/Face-Human-Bench/face-human-bench/blob/main/data/prepare_data.py) script to extract test samples from the original images based on the JSON files we provide. Note: You will need to modify the paths in the script to match your local environment. 


## Citation

If you find **Face-Human-Bench** useful for your research and applications, please kindly cite using this BibTeX:

```latex
@article{qin2025facehumanbench,
  title={Face-Human-Bench: A Comprehensive Benchmark of Face and Human Understanding for Multi-modal Assistants},
  author={Qin, Lixiong and Ou, Shilong and Zhang, Miaoxuan and Wei, Jiangning and Zhang, Yuhang and Song, Xiaoshuai and Liu, Yuchen and Xu, Weiran},
  journal={arXiv preprint arXiv:2501.01243},
  year={2025}
}
```

