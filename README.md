# SoccerNet - Action Spotting

Welcome to the SoccerNet Development Kit for the Action Spotting Task and Challenge. This kit is meant as a help to get started working with the soccernet data and the proposed task. More information about the dataset can be found on our [official website](https://soccer-net.org/).

SoccerNet Action Spotting is part of the SoccerNet-v2 dataset, which is an extension of SoccerNet-v1 with new and challenging tasks including
action spotting, camera shot segmentation with boundary detection, and a novel replay grounding task.

<p align="center"><img src="Images/GraphicalAbstract-SoccerNet-V2-1.png" width="640"></p>

The Action Spotting dataset consists of 500 complete soccer games including:
 - Full untrimmed broadcast videos in both low and high resolution.
 - Pre-computed features such as ResNET-152.
 - Annotations of actions among 17 classes (Labels-v2.json).

Participate in our upcoming Challenge in the [CVPR 2022 International Challenge on Activity Recognition Workshop](http://activity-net.org/challenges/2021/index.html) and try to win 500$ sponsored by [SportRadar](https://www.sportradar.com/)! All details can be found on the [challenge website](), or on the [main page](https://soccer-net.org/).

The participation deadline is fixed at the 30th of May 2022.
The official rules and guidelines are available on [ChallengeRules.md](ChallengeRules.md).

<a href="https://youtu.be/T8Qc39FcQ7A">
<p align="center"><img src="Images/Miniature.png" width="720"></p>
</a>

### 2021 Challenge leaderboard

This table summarizes the current performances on the 2021 challenge. 
For the leaderboard on the 2022 challenge, please visit EvalAI [test](https://eval.ai/web/challenges/challenge-page/761/leaderboard/2072) and [challenge](https://eval.ai/web/challenges/challenge-page/761/leaderboard/2074) leaderboards.

| Model     | tight Avg-mAP (challenge)  | Avg-mAP (challenge) | tight Avg-mAP (test)  | Avg-mAP (test) |
| ----------| -------- | -------- | -------- | -------- |
|[Baidu Research](https://arxiv.org/pdf/2106.14447.pdf)| 49.56% | 74.84% | 47.05% | 73.77% |
|[OPPO]()| 46.17% | 64.73% | NA | NA |
|[NetVLAD++ with Baidu features](https://arxiv.org/pdf/2106.14447.pdf)| 43.99% | 74.63% | NA | NA |
|[AImageLab-RMS](https://arxiv.org/abs/2102.07624)| 27.69% | 60.92% | 28.83% | 63.49% |
|[IdealCat]()| 26.47% | 54.24% | NA | NA |
|[CALF-calibration](https://arxiv.org/abs/2104.09333)| 15.83% | 46.39% | NA | 46.80% |
|[CALF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Cioppa_A_Context-Aware_Loss_Function_for_Action_Spotting_in_Soccer_Videos_CVPR_2020_paper.pdf)| 15.33% | 42.22% | NA | NA |
|[NetVLAD++](https://arxiv.org/pdf/2104.06779.pdf)| 9.91% | 52.54% | 11.51% | 53.40% |
|[straw]()| 7.39% | 51.65% | 5.92% | 49.78% |
|[NetVLAD](https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w34/Giancola_SoccerNet_A_Scalable_CVPR_2018_paper.pdf)| 4.31% | 30.74% | 4.20% | 31.37% |

### Published research benchmark

This table summarizes the current performances of published methods only.  Last update January 2022.

| Model     | tight Avg-mAP (challenge)  | Avg-mAP (challenge) | tight Avg-mAP (test)  | Avg-mAP (test) |
| ----------| -------- | -------- | -------- | -------- |
|[Baidu Research](https://arxiv.org/pdf/2106.14447.pdf)| 49.56% | 74.84% | 47.05% | 73.77% |
|[NetVLAD++ with Baidu features](https://arxiv.org/pdf/2106.14447.pdf)| 43.99% | 74.63% | NA | NA |
|[AImageLab-RMS](https://arxiv.org/abs/2102.07624)| 27.69% | 60.92% | 28.83% | 63.49% |
|[CALF-calibration](https://arxiv.org/abs/2104.09333)| 15.83% | 46.39% | NA | 46.80% |
|[CALF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Cioppa_A_Context-Aware_Loss_Function_for_Action_Spotting_in_Soccer_Videos_CVPR_2020_paper.pdf)| 15.33% | 42.22% | NA | NA |
|[NetVLAD++](https://arxiv.org/pdf/2104.06779.pdf)| 9,91% | 52.54% | 11.51% | 53.40% |
|[NetVLAD](https://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w34/Giancola_SoccerNet_A_Scalable_CVPR_2018_paper.pdf)| 4.31% | 30.74% | 4.20% | 31.37% |
|[AudioVid](https://openaccess.thecvf.com/content_CVPRW_2020/html/w53/Vanderplaetse_Improved_Soccer_Action_Spotting_Using_Both_Audio_and_Video_Streams_CVPRW_2020_paper.html)| NA | NA | NA | 39.9% |
|[MaxPool](http://openaccess.thecvf.com/content_cvpr_2018_workshops/papers/w34/Giancola_SoccerNet_A_Scalable_CVPR_2018_paper.pdf)| NA | NA | NA | 18.6% |

## How to download SoccerNet-v2 

A [SoccerNet pip package](https://pypi.org/project/SoccerNet/) to easily download the data and the annotations is available. 

To install the pip package simply run:

<code>pip install SoccerNet</code>

Please follow the instructions provided in the [Download](Download) folder of this repository. Do also mind that signing an Non-Disclosure agreement (NDA) is required to access the LQ and HQ videos: [NDA](https://docs.google.com/forms/d/e/1FAIpQLSfYFqjZNm4IgwGnyJXDPk2Ko_lZcbVtYX73w5lf6din5nxfmA/viewform).

## How to extract video features 

As it was one of the most requested features on SoccerNet-V1, this repository provides functions to automatically extract the ResNet-152 features and compute the PCA on your own broadcast videos. These functions allow you to test pre-trained action spotting, camera segmentation or replay grounding models on your own games.

The functions to extract the video features can be found in the [Features](Features) folder.

<p align="center"><img src="Images/Videos_and_features.png" width="720"></p>

## Benchmark Implementations

This repository contains several [benchmarks](Benchmarks) for action spotting, which are presented in the [SoccerNet-V2 paper](https://arxiv.org/pdf/2011.13367.pdf), or subsequent papers. You can use these codes to build upon our methods and improve the performances.


## Evaluation

This repository and the pip package provide evaluation functions for the proposed tasks based on predictions saved in the JSON format. See the [Evaluation](Evaluation) folder of this repository for more details.

## Visualizations

Finally, this repository provides the [Annotation tool](Annotation) used to annotate the actions. This tool can be used to visualize the information. Please follow the instruction in the dedicated folder for more details.

## Citation

For further information check out the paper and supplementary material:
https://openaccess.thecvf.com/content/CVPR2021W/CVSports/papers/Deliege_SoccerNet-v2_A_Dataset_and_Benchmarks_for_Holistic_Understanding_of_Broadcast_CVPRW_2021_paper.pdf

Please cite our work if you use our dataset:
```bibtex
@InProceedings{Deliège2020SoccerNetv2,
      title={SoccerNet-v2 : A Dataset and Benchmarks for Holistic Understanding of Broadcast Soccer Videos}, 
      author={Adrien Deliège and Anthony Cioppa and Silvio Giancola and Meisam J. Seikavandi and Jacob V. Dueholm and Kamal Nasrollahi and Bernard Ghanem and Thomas B. Moeslund and Marc Van Droogenbroeck},
      year={2021},
      booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR) Workshops},
      month = {June},
}
```
