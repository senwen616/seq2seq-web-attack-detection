# Seq2Seq for Network User Abnormal Behavior Detection
This is the implementation of the Seq2Seq model for  Network User Abnormal Behavior Detection. The Seq2Seq model is usually used in Neural Machine Translation. The main goal of this project is to demonstrate the relevance of the NLP approach for web security.


## Model
The step-by-step solution is presented in [seq2seq.ipynb](seq2seq.ipynb) that contains the main stages such as a model initialization, training, validation, prediction and results.

Unfortunately, github ui doesn't correctly visualize cell output with colored malicious parts of requests. So, we suggest to download the notebook or use this [link](https://nbviewer.jupyter.org/github/PositiveTechnologies/seq2seq-web-attack-detection/blob/master/seq2seq.ipynb) for correctly displaying cells outputs.


## Dataset
The dataset contains data with 21991 benign and 1097 anomalous requests.


## Running
Please make sure that you have the same [requirements](requirements.txt) and python 2.7.*

This repository contains environment.yml so it can be dockerized using [jupyter/repo2docker](https://github.com/jupyter/repo2docker). We have already dockerized it for you and you can run this playbook by

```bash
docker run -it  -p 8888:8888 montekki/seq2seq-web-attack-detection:latest  jupyter notebook --ip=0.0.0.0
```

