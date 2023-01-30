# Guidelines for the Action Spotting challenge

The 3rd [Action Spotting Challenge]() and the 1st [Ball Action Spotting Challenge]() will be held at the 
official [CVSports Workshop](https://vap.aau.dk/cvsports/) at CVPR 2023! 
Subscribe (watch) the repo to receive the latest info regarding timeline and prizes!


SoccerNet-v2 is a large-scale dataset build upon SoccerNet that benchmarks the tasks of action spotting, camera shot segmentation / boundary detection and replay grounding. 
SoccerNet-v2 is composed of 300k manual annotations, span 500 complete soccer games from six main European leagues, covering three seasons from 2014 to 2017 and a total duration of 764 hours.

We propose the SoccerNet challenge to encourage the development of state-of-the-art algorithm for Generic Soccer Video Understanding.
 - **Action Spotting**: Spot the actions on a complete video of soccer game among 17 classes.
 - **Ball Action Spotting**: Spot the actions related to the ball on a complete video of soccer game among 2 classes.

We provide an [evaluation server]() for anyone competing in the SoccerNet challenge. 
This evaluation server handles predictions for the open **test** set and the segregated **challenge** set.

Winners will be announced at CVSports Workshop at CVPR 2023. 
Prizes will be announced soon, stay tuned!


## Who can participate / How to participate?

 - Any individual can participate to the challenge, except the organizers.
 - The participants are recommended to form a team to participate.
 - Each team can have one or more members. 
 - An individual/team can compete on both task.
 - An individual associated with multiple teams (for a given task) or a team with multiple accounts will be disqualified.
 - On both task, a particpant can only use the video stream as input (visual and/or audio).
 - To help the participants, we provide pre-extracted ResNet-152 visual features at 2fps.
 - A particpant is allowed to extract its own visual/audio features with any pre-trained model.

## How to win / What is the prize?

 - For each task, the winner is the individual/team who reach the highest performance on the **challenge** set.
 - The metrics taken into consideration are the **tight Average-mAP for Action Spotting** and the **mAP@1 for Ball Action Spotting**.
 - The deadline to submit your results is May 30th 2023 at 11.59 pm Pacific Time.
 - In order to be eligible for the prize, we require the individual/team to provide a short report describing the details of the methodology (CVPR format, max 2 pages).



## Important dates

Note that these dates are tentative and subject to changes if necessary.

 - **February 6:** Open evaluation server on the (Open) Test set.
 - **February 15:** Open evaluation server on the (Seggregated) Challenge set.
 - **May 30:** Close evaluation server.
 - **June 6:** Deadline for submitting the report.
 - **June TBD:** A full-day workshop at CVPR 2023.

For any further doubt or concern, please raise an issue in that repository, or contact us directly on [Discord](https://discord.gg/SM8uHj9mkP).
