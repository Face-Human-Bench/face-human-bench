# Face-Human-Bench: A Comprehensive Face and Human Understanding Benchmark for Large Visual Language Models

<p align="center">
    <img src="https://github.com/Face-Human-Bench/face-human-bench/blob/main/pictures/logo.png" width="30%"> <br>
</p>


## Introduction

Faces and humans are crucial elements in social interaction and are widely included in everyday photos and videos. Therefore, a deep understanding of faces and humans will enable multi-modal assistants to achieve improved response quality and broadened application scope. Currently, the multi-modal assistant community lacks a comprehensive and scientific evaluation of face and human understanding abilities. In this paper, we first propose a hierarchical ability taxonomy that includes three levels of abilities. Then, based on this taxonomy, we collect images and annotations from publicly available datasets in the face and human community and build a semi-automatic data pipeline to produce problems for the new benchmark. Finally, the obtained Face-Human-Bench comprises a development set with 900 problems and a test set with 1800 problems, supporting both English and Chinese. We conduct evaluations over 25 mainstream multi-modal large language models (MLLMs) with our Face-Human-Bench, focusing on the correlation between abilities, the impact of the relative position of targets on performance, and the impact of Chain of Thought (CoT) prompting on performance.
Moreover, inspired by multi-modal agents, we also explore which abilities of MLLMs need to be supplemented by specialist models.

 <img src="https://github.com/Face-Human-Bench/face-human-bench/blob/main/pictures/face_human_bench.png" alt="Image" width="800">


## 💥 News
- **[2024.7.28]** Our project homepage can be accessed at https://face-human-bench.github.io.

## Scores
Leaderboard of MLLMs on Face-Human-Bench(EN)：

<img src="https://github.com/Face-Human-Bench/face-human-bench/blob/main/pictures/leaderboard.png" alt="Image" width="800">

Comparison of different MLLMs on English and Chinese versions of the Face-Human-Bench：

<img src="https://github.com/Face-Human-Bench/face-human-bench/blob/main/pictures/EN-CN.png" alt="Image" width="800">

For more results, please refer to our website or paper.

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

