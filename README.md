# SoccerNet - Action Spotting

Welcome to the SoccerNet Development Kit for the Action Spotting Task and Challenge. This kit is meant as a help to get started working with the soccernet data and the proposed task. More information about the dataset can be found on our [official website](https://www.soccer-net.org/).

SoccerNet Action Spotting is part of the SoccerNet-v2 dataset, which is an extension of SoccerNet-v1 with new and challenging tasks including
action spotting, camera shot segmentation with boundary detection, and a novel replay grounding task.

__[New]__ In 2023, we introduce a novel spotting challenge on ball events including drive and passes. Those events are much more dense and require a higher level of spotting precision. The density of those events, as well as the subtle underlying movement of the ball and players, make this new task even more challenging. For this new challenge, you only have access to 7 annotated games, so you may want to take a look at different training paradigms such as transfer learning, unsupervised learning or semi-supervised learning. Remember that you still have access to the 500 videos from soccernet to help you.

<p align="center"><img src="Images/GraphicalAbstract-SoccerNet-V2-1.png" width="640"></p>

The Action Spotting dataset consists of 500 complete soccer games including:
 - Full untrimmed broadcast videos in both low and high resolution.
 - Pre-computed features such as ResNET-152.
 - Annotations of actions among 17 classes (Labels-v2.json).

 The new Ball Action Spotting dataset consists of 7 complete soccer games including:
 - Full untrimmed broadcast videos in both low and high resolution.
 - Annotations of actions among 2 classes (Labels-ball.json).

Participate in our upcoming Challenges during the [CVPR 2023 International Challenge at the CVSports Workshop](https://vap.aau.dk/cvsports/)! All details are provided on our [evaluation server](https://eval.ai/web/challenges/challenge-page/1949/overview) for the Action Spotting task, and on another [evaluation server](https://eval.ai/web/challenges/challenge-page/1950/overview) for the ball action spotting task, or on the [main soccernet page](https://www.soccer-net.org/).

The participation deadline is fixed at the 30th of May 2023.
The official rules and guidelines are available on [ChallengeRules.md](ChallengeRules.md).

<a href="https://youtu.be/tA9E1hkiyB0">
<p align="center"><img src="Images/Thumbnail.png" width="720"></p>
</a>

### 2023 Action Spotting Challenge leaderboard

<p><table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Team</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Average-mAP (tight)</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Shown only (tight)</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Unshown only (tight)</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Average-mAP (loose)</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Shown only (loose)</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Unshown only (loose)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">SDU_VSISLAB</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">71.31</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">76.29</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">54.09</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">78.56</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">81.67</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">69.13</td>
    </tr>
    <tr>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">mt_player</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">71.1</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">77.22</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">58.5</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">78.79</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">82.02</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">77.62</td>
    </tr>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">ASTRA  (ASBY193)</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">70.1</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">75.0</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">57.98</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">79.21</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">81.69</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">75.36</td>
    </tr>
    <tr>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">team_ws_action</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">69.17</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">75.18</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">59.12</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">76.95</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">80.39</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">75.92</td>
    </tr>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">CEA LVA</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">68.38</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">74.79</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">47.68</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">73.98</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">78.57</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">61.75</td>
    </tr>
    <tr>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">Baseline (Yahoo)</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">68.33</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">73.22</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">60.88</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">78.06</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">80.58</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">78.32</td>
    </tr>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">DVP</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">66.95</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">74.68</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">53.81</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">73.61</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">79.15</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">67.38</td>
    </tr>
    <tr>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">JAMY2  (AF_GRU)</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">51.97</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">58.05</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">44.29</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">63.12</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">65.98</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">61.66</td>
    </tr>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">tyru  (GRU_CALF)</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">51.38</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">57.5</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">41.82</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">62.88</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">66.3</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">56.57</td>
    </tr>
    <tr>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">JAMY  (LocPoint)</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">45.83</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">49.68</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">45.71</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">61.8</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">64.23</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">63.48</td>
    </tr>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">test_YYQ</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">12.73</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">14.13</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">11.21</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">54.21</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">58.75</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">48.55</td>
    </tr>
  </tbody>
</table></p>

### 2022 Action Spotting Challenge leaderboard

<table border="0" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>Team</th>
      <th>tight Avg-mAP (challenge)</th>
      <th>tight Avg-mAP visible (challenge)</th>
      <th>tight Avg-mAP unshown (challenge)</th>
      <th>Avg-mAP (challenge)</th>
      <th>Avg-mAP visible (challenge)</th>
      <th>Avg-mAP unshown (challenge)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Yahoo Research</td>
      <td>67.81</td>
      <td>72.84</td>
      <td>60.17</td>
      <td>78.05</td>
      <td>80.61</td>
      <td>78.05</td>
    </tr>
    <tr>
      <td>PTS</td>
      <td>66.73</td>
      <td>74.84</td>
      <td>53.21</td>
      <td>73.62</td>
      <td>79.16</td>
      <td>67.42</td>
    </tr>
    <tr>
      <td>AS&amp;RG</td>
      <td>64.88</td>
      <td>70.31</td>
      <td>53.03</td>
      <td>72.83</td>
      <td>76.08</td>
      <td>72.35</td>
    </tr>
    <tr>
      <td>mt_sdu_action</td>
      <td>62.26</td>
      <td>67.48</td>
      <td>45.04</td>
      <td>69.86</td>
      <td>73.81</td>
      <td>59.15</td>
    </tr>
    <tr>
      <td>Rkrystal</td>
      <td>61.84</td>
      <td>67.39</td>
      <td>48.71</td>
      <td>74.75</td>
      <td>78.29</td>
      <td>69.02</td>
    </tr>
    <tr>
      <td>arturxe</td>
      <td>60.56</td>
      <td>65.75</td>
      <td>53.00</td>
      <td>71.72</td>
      <td>75.15</td>
      <td>69.91</td>
    </tr>
    <tr>
      <td>cihe</td>
      <td>59.97</td>
      <td>64.51</td>
      <td>53.80</td>
      <td>72.95</td>
      <td>76.29</td>
      <td>71.95</td>
    </tr>
    <tr>
      <td>GUC</td>
      <td>58.71</td>
      <td>63.70</td>
      <td>51.86</td>
      <td>70.49</td>
      <td>73.46</td>
      <td>70.11</td>
    </tr>
    <tr>
      <td>abcdefg</td>
      <td>56.07</td>
      <td>62.97</td>
      <td>46.51</td>
      <td>67.88</td>
      <td>72.54</td>
      <td>66.37</td>
    </tr>
    <tr>
      <td>intro-and inter</td>
      <td>53.97</td>
      <td>60.04</td>
      <td>47.52</td>
      <td>67.75</td>
      <td>71.16</td>
      <td>70.12</td>
    </tr>
    <tr>
      <td>memory</td>
      <td>53.03</td>
      <td>57.94</td>
      <td>43.16</td>
      <td>67.15</td>
      <td>69.20</td>
      <td>68.28</td>
    </tr>
    <tr>
      <td>stargazer</td>
      <td>52.04</td>
      <td>60.18</td>
      <td>32.06</td>
      <td>60.86</td>
      <td>66.64</td>
      <td>48.46</td>
    </tr>
    <tr>
      <td>heaven</td>
      <td>51.85</td>
      <td>59.85</td>
      <td>31.62</td>
      <td>60.88</td>
      <td>66.67</td>
      <td>48.45</td>
    </tr>
    <tr>
      <td>lczazu</td>
      <td>49.56</td>
      <td>56.82</td>
      <td>31.60</td>
      <td>60.86</td>
      <td>66.56</td>
      <td>48.51</td>
    </tr>
    <tr>
      <td>Baseline*</td>
      <td>49.56*</td>
      <td>54.42</td>
      <td>45.42</td>
      <td>74.84</td>
      <td>78.58</td>
      <td>71.52</td>
    </tr>
    <tr>
      <td>zqing</td>
      <td>47.54</td>
      <td>51.75</td>
      <td>41.65</td>
      <td>66.66</td>
      <td>69.06</td>
      <td>67.17</td>
    </tr>
    <tr>
      <td>welkin</td>
      <td>42.74</td>
      <td>49.91</td>
      <td>20.67</td>
      <td>50.90</td>
      <td>56.48</td>
      <td>35.38</td>
    </tr>
    <tr>
      <td>DUT</td>
      <td>40.65</td>
      <td>43.87</td>
      <td>43.10</td>
      <td>68.40</td>
      <td>71.68</td>
      <td>68.53</td>
    </tr>
    <tr>
      <td>sshinde5</td>
      <td>36.71</td>
      <td>39.33</td>
      <td>21.26</td>
      <td>51.36</td>
      <td>55.29</td>
      <td>35.34</td>
    </tr>
    <tr>
      <td>SIT</td>
      <td>21.60</td>
      <td>26.55</td>
      <td>16.83</td>
      <td>29.92</td>
      <td>34.92</td>
      <td>25.22</td>
    </tr>
  </tbody>
</table>
Check out our paper on the [SoccerNet 2022 Challenge Results](https://arxiv.org/abs/2210.02365) published at the ACMM Workshop.

### 2021 Action Spotting Challenge leaderboard

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

### Published Action Spotting research benchmark

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


### 2023 Ball Action Spotting Challenge leaderboard

<p><table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Team</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">mAP@1</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">mAP@2</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">mAP@3</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">mAP@4</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">mAP@5</th>
      <th style = "background-color: #FFFFFF;font-family: Century Gothic, sans-serif;font-size: medium;color: #305496;text-align: left;border-bottom: 2px solid #305496;padding: 0px 20px 0px 0px;width: auto">Average-mAP (tight)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">Ruslan Baikulov</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">86.47</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">87.98</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">88.28</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">88.18</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">87.95</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">87.91</td>
    </tr>
    <tr>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">FDL@ZLab</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.39</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">85.19</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">85.81</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">86.0</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">86.19</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">85.45</td>
    </tr>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">BASIK</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">82.06</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.39</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.86</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">84.04</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.91</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.57</td>
    </tr>
    <tr>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">FC Pixel Nets</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">81.89</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.22</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.97</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.85</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">84.02</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.5</td>
    </tr>
    <tr>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">play</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">79.74</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">82.58</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">84.06</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">84.49</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">84.34</td>
      <td style = "background-color: #D9E1F2;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">83.29</td>
    </tr>
    <tr>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">Baseline (PTS)</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">62.72</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">69.24</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">72.57</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">74.29</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">74.8</td>
      <td style = "background-color: white; color: black;font-family: Century Gothic, sans-serif;font-size: medium;text-align: left;padding: 0px 20px 0px 0px;width: auto">71.21</td>
    </tr>
  </tbody>
</table></p>

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

The easiest way to download and prepare the data is to use the following python code.

```
python Download/download_ball_data.py --dataset_dir path/to/SoccerNet --password_videos "password_received_from_NDA"
```

Alternatively, you may use the same pip package as for SoccerNet-v2.

The following code will download the videos and annotations (except annotations on the challenge set) in separated zip files.

```
from SoccerNet.Downloader import SoccerNetDownloader as SNdl
mySNdl = SNdl(LocalDirectory="path/to/SoccerNet")
mySNdl.downloadDataTask(task="spotting-ball-2023", split=["train", "valid", "test", "challenge"], password=<PW_FROM_NDA>)
```

Note that you may have to extract and merge the zip files yourself if you choose the second option.

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
- [Dense Video Captioning](https://github.com/SoccerNet/sn-caption)
- [Jersey Number Recognition](https://github.com/SoccerNet/sn-jersey)

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


