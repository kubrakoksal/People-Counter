# People-Counter
This project counts people coming in and going out of structures such as building, stores,etc. The project was developed using Raspberry 3B + and Raspian Operating System. <br />
The project uses Google Cloud Vision API to object detection and Sort algorithm to object tracking.

## Object Tracking
The Sort algorithm was used to track the objects. [GitHub Page](https://github.com/abewley/sort/blob/master/sort.py).
###SORT
A simple online and realtime tracking algorithm for 2D multiple object tracking in video sequences. See an example video here.

By Alex Bewley

SORT is a barebones implementation of a visual multiple object tracking framework based on rudimentary data association and state estimation techniques. It is designed for online tracking applications where only past and current frames are available and the method produces object identities on the fly. While this minimalistic tracker doesn't handle occlusion or re-entering objects its purpose is to serve as a baseline and testbed for the development of future trackers.

SORT was initially described in an arXiv tech report. At the time of the initial publication, SORT was ranked the best open source multiple object tracker on the MOT benchmark.

### License
SORT is released under the GPL License (refer to the LICENSE file for details) to promote the open use of the tracker and future improvements. If you require a permissive license contact Alex (alex@bewley.ai).


### Citing Sort
If you find this repo useful in your research, please consider citing:
```
@inproceedings{Bewley2016_sort,
  author={Bewley, Alex and Ge, Zongyuan and Ott, Lionel and Ramos, Fabio and Upcroft, Ben},
  booktitle={2016 IEEE International Conference on Image Processing (ICIP)},
  title={Simple online and realtime tracking},
  year={2016},
  pages={3464-3468},
  keywords={Benchmark testing;Complexity theory;Detectors;Kalman filters;Target tracking;Visualization;Computer Vision;Data Association;Detection;Multiple Object Tracking},
  doi={10.1109/ICIP.2016.7533003}
}
```

### Prerequisites
https://github.com/jjhelmus/berryconda (Installing BerryConda)<br />
Python Libraries<br />
The Vision API Token file to be used in the project should be downloaded as described on the slide. (Token.json)<br />
```
pip install numba
conda install scikit-learn
conda install scikit-image
pip install google.cloud
pip install google.cloud.vision
conda install numpy
conda install pandas
conda install matplotlib
pip install filterpy
```

### Getting Started
Open raspberry pi terminal 
```
git clone https://github.com/kubrakoksal/People-Counter
cd People-Counter
python counter.py
```
