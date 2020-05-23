# People-Counter
This project counts people coming in and going out of structures such as building, stores,etc. The project was developed using Raspberry 3B + and Raspian Operating System. The project uses Google Cloud Vision API to object detection. 


### Prerequisites
https://github.com/jjhelmus/berryconda (Installing BerryConda)\n
Python Libraries\n
The Vision API Token file to be used in the project should be downloaded as described on the slide. (Token.json)
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
