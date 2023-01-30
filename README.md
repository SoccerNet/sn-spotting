# SoccerNet - Action Spotting

Welcome to the SoccerNet Development Kit for the Action Spotting Task and Challenge. This kit is meant as a help to get started working with the soccernet data and the proposed task. More information about the dataset can be found on our [official website](https://www.soccer-net.org/).

SoccerNet Action Spotting is part of the SoccerNet-v2 dataset, which is an extension of SoccerNet-v1 with new and challenging tasks including
action spotting, camera shot segmentation with boundary detection, and a novel replay grounding task.

__[News]__ For the 2023, we introduce a novel spotting challenge on ball events including drive and passes. Those events are much more dense and require a higher level of spotting precision. The density of those events, as well as the subtle underlying movement of the ball and players, make this new task even more challenging. For this new challenge, you only have access to 7 annotated games, so you may want to take a look at different training paradigms such as transfer learning, unsupervised learning or semi-supervised learning. Remember that you still have access to the 500 videos from soccernet to help you.


<p align="center"><img src="Images/GraphicalAbstract-SoccerNet-V2-1.png" width="640"></p>

The Action Spotting dataset consists of 500 complete soccer games including:
 - Full untrimmed broadcast videos in both low and high resolution.
 - Pre-computed features such as ResNET-152.
 - Annotations of actions among 17 classes (Labels-v2.json).

 The new Ball Action Spotting dataset consists of 7 complete soccer games including:
 - Full untrimmed broadcast videos in both low and high resolution.
 - Annotations of actions among 2 classes (Labels-ball.json).

Participate in our upcoming Challenges during the [CVPR 2023 International Challenge at the CVSports Workshop](https://vap.aau.dk/cvsports/)! All details will be available on the [challenge website](https://eval.ai/web/challenges/challenge-page/1536/overview), or on the [main soccernet page](https://www.soccer-net.org/).

The participation deadline is fixed at the 30th of May 2023.
The official rules and guidelines are available on [ChallengeRules.md](ChallengeRules.md).

<a href="https://youtu.be/tA9E1hkiyB0">
<p align="center"><img src="Images/Thumbnail.png" width="720"></p>
</a>

### 2022 Challenge leaderboard

The leaderboard will soon be provided here. In the meantime, please check out our paper on the [SoccerNet 2022 Challenge Results](https://arxiv.org/abs/2210.02365) published at the ACMM Workshop.

### 2021 Challenge leaderboard

This table summarizes the current performances on the 2021 Action Spotting Challenge. 
For the leaderboard on the 2022 challenge, please visit EvalAI [test](https://eval.ai/web/challenges/challenge-page/761/leaderboard/2072) and [challenge](https://eval.ai/web/challenges/challenge-page/761/leaderboard/2074) leaderboards.

| Model     | tight Avg-mAP (challenge)  | Avg-mAP (challenge) | tight Avg-mAP (test)  | Avg-mAP (test) |
| ----------| -------- | -------- | -------- | -------- |
|[Baidu Research](https://arxiv.org/pdf/2106.14447.pdf)| 49.56% | 74.84% | 47.05% | 73.77% |
|[OPPO]()| 46.17% | 64.73% | NA | NA |
|[NetVLAD++ with Baidu features](https://arxiv.org/pdf/2106.14447.pdf)| 43.99% | 74.63% | NA | NA |
|[AImageLab-RMS](https://arxiv.org/abs/2102.07624)| 27.69% | 60.92% | 28.83% | 63.49% |
|[IdealCat]()| 26.47% | 54.24% | NA | NA |
|[CALF-calibration](https://arxiv.org/abs/2104.09333)| 15.83% | 46.39% | NA | 46.80% |
|[CALF](https://openaccess.thecvf.com/content_CVPR_2020/papers/Cioppa_A_Context-Aware_Loss_Function_for_Action_Spotting_in_Soccer_Videos_CVPR_2020_paper.pdf)| 15.33% | 42.22% | 14.10% | 41,61% |
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

## How to download the dataset

### SoccerNet-v2 Action Spotting

A [SoccerNet pip package](https://pypi.org/project/SoccerNet/) to easily download the data and the annotations is available. 

To install the pip package simply run:

<code>pip install SoccerNet</code>

Then use the API to downlaod the data of interest:

```
from SoccerNet.Downloader import SoccerNetDownloader
mySoccerNetDownloader = SoccerNetDownloader(LocalDirectory="/path/to/SoccerNet")
mySoccerNetDownloader.downloadGames(files=["Labels-v2.json"], split=["train","valid","test"])
```

If you want to download the videos, you will need to fill a NDA to get the password.

```
mySoccerNetDownloader.password = input("Password for videos?:\n")
mySoccerNetDownloader.downloadGames(files=["1_224p.mkv", "2_224p.mkv"], split=["train","valid","test","challenge"])
mySoccerNetDownloader.downloadGames(files=["1_720p.mkv", "2_720p.mkv", "video.ini"], split=["train","valid","test","challenge"])
```
We provide several features including ResNET (used for our [benchmarks](Benchmarks)), and last year's winners features from [Baidu Research](https://arxiv.org/pdf/2106.14447.pdf). Check out our [pip package](https://pypi.org/project/SoccerNet/) documentation for more features.
```
mySoccerNetDownloader.downloadGames(files=["1_ResNET_TF2_PCA512.npy", "2_ResNET_TF2_PCA512.npy"], split=["train","valid","test","challenge"])
mySoccerNetDownloader.downloadGames(files=["1_baidu_soccer_embeddings.npy", "2_baidu_soccer_embeddings.npy"], split=["train","valid","test","challenge"])
```


### SoccerNet Ball Action Spotting

You may use the same pip package as for SoccerNet-v2.
Information and data coming soon.


## How to extract video features 

As it was one of the most requested features on SoccerNet-V1, this repository provides functions to automatically extract the ResNet-152 features and compute the PCA on your own broadcast videos. These functions allow you to test pre-trained action spotting, camera segmentation or replay grounding models on your own games.

The functions to extract the video features can be found in the [Features](Features) folder.

<p align="center"><img src="Images/Videos_and_features.png" width="720"></p>

## Benchmark Implementations

### SoccerNet-v2 Action Spotting

This repository contains several [benchmarks](Benchmarks) for action spotting, which are presented in the [SoccerNet-V2 paper](https://arxiv.org/pdf/2011.13367.pdf), or subsequent papers. You can use these codes to build upon our methods and improve the performances.

### SoccerNet Ball Action Spotting

The benchmark to beat this year is the [E2E-spot](https://arxiv.org/abs/2207.10213) method published at ECCV 2022 by J. Hong et. al trained with default parameters and 25fps videos. This method arrived second in the 2022 Action Spotting Challenge The code will be updated on their [github repository](https://github.com/jhong93/spot) for anyone to reproduce the baseline results and improve on them.

## Evaluation

This repository and the pip package provide evaluation functions for the proposed tasks based on predictions saved in the JSON format. See the [Evaluation](Evaluation) folder of this repository for more details.

## Visualizations

Finally, this repository provides the [Annotation tool](Annotation) used to annotate the actions. This tool can be used to visualize the information. Please follow the instruction in the dedicated folder for more details.

## Our other Challenges

Check out our other challenges related to SoccerNet!
- [Action Spotting](https://github.com/SoccerNet/sn-spotting)
- [Replay Grounding](https://github.com/SoccerNet/sn-grounding)
- [Calibration](https://github.com/SoccerNet/sn-calibration)
- [Re-Identification](https://github.com/SoccerNet/sn-reid)
- [Tracking](https://github.com/SoccerNet/sn-tracking)

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

For further information about the chalklenge check out the paper and supplementary material:
https://arxiv.org/abs/2210.02365

Please cite our work if you use the SoccerNet dataset:
```bibtex
@inproceedings{Giancola_2022,
	doi = {10.1145/3552437.3558545},
	url = {https://doi.org/10.1145%2F3552437.3558545},
	year = 2022,
	month = {oct},
	publisher = {{ACM}},
	author = {Silvio Giancola and Anthony Cioppa and Adrien Deli{\`{e}}ge and Floriane Magera and Vladimir Somers and Le Kang and Xin Zhou and Olivier Barnich and Christophe De Vleeschouwer and Alexandre Alahi and Bernard Ghanem and Marc Van Droogenbroeck and Abdulrahman Darwish and Adrien Maglo and Albert Clap{\'{e}}s and Andreas Luyts and Andrei Boiarov and Artur Xarles and Astrid Orcesi and Avijit Shah and Baoyu Fan and Bharath Comandur and Chen Chen and Chen Zhang and Chen Zhao and Chengzhi Lin and Cheuk-Yiu Chan and Chun Chuen Hui and Dengjie Li and Fan Yang and Fan Liang and Fang Da and Feng Yan and Fufu Yu and Guanshuo Wang and H. Anthony Chan and He Zhu and Hongwei Kan and Jiaming Chu and Jianming Hu and Jianyang Gu and Jin Chen and Jo{\~{a}}o V. B. Soares and Jonas Theiner and Jorge De Corte and Jos{\'{e}} Henrique Brito and Jun Zhang and Junjie Li and Junwei Liang and Leqi Shen and Lin Ma and Lingchi Chen and Miguel Santos Marques and Mike Azatov and Nikita Kasatkin and Ning Wang and Qiong Jia and Quoc Cuong Pham and Ralph Ewerth and Ran Song and Rengang Li and Rikke Gade and Ruben Debien and Runze Zhang and Sangrok Lee and Sergio Escalera and Shan Jiang and Shigeyuki Odashima and Shimin Chen and Shoichi Masui and Shouhong Ding and Sin-wai Chan and Siyu Chen and Tallal El-Shabrawy and Tao He and Thomas B. Moeslund and Wan-Chi Siu and Wei Zhang and Wei Li and Xiangwei Wang and Xiao Tan and Xiaochuan Li and Xiaolin Wei and Xiaoqing Ye and Xing Liu and Xinying Wang and Yandong Guo and Yaqian Zhao and Yi Yu and Yingying Li and Yue He and Yujie Zhong and Zhenhua Guo and Zhiheng Li},
	title = {{SoccerNet} 2022 Challenges Results},
	booktitle = {Proceedings of the 5th International {ACM} Workshop on Multimedia Content Analysis in Sports}
}
```


