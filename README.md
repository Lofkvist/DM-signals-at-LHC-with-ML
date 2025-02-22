# Dark Matter Signals at the LHC using Machine Learning


<p align='center'>
  <a href="https://github.com/EdwardGlockner/DM-signals-at-LHC-with-ML/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=EdwardGlockner/DM-signals-at-LHC-with-ML" />
  </a>
</p>
  
  
<p align='center'>
  <a href="https://instagram.com/alexandresanlim">
    <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" />        
  </a>&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/alexandresanlim/">
    <img src="https://img.shields.io/badge/Shell_Script-121011?style=for-the-badge&logo=gnu-bash&logoColor=white" />
  </a>&nbsp;&nbsp;
  <a href="https://www.linkedin.com/in/alexandresanlim/">
    <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  </a>&nbsp;&nbsp;
  <a href="https://instagram.com/alexandresanlim">
    <img src="https://img.shields.io/badge/Keras-FF0000?style=for-the-badge&logo=keras&logoColor=white" />        
  </a>&nbsp;&nbsp;
</p>

## About the Project
This is a project by Edward Glöckner, Max Andersson and Carl Löfkvist. It was supervised by Stefano Moretti, Prashant Singh, Rikard Enberg, Harri Waltari at Uppsala University. The project investigates the role deep learning can have in the discovery of new physics.

The project can be divided into two sub-projects, where the first is simulating proton-proton collisions generating data, and the second is analyzing the data using deep learning techniques. 

<!-- Table of Contents -->
## Table of Contents
  - [Introduction](#introduction)
    * [Goals](#goals)
    * [Event Generation](#event-generation)
    * [Deep Learning](#deep-learning)
  - [Paper](#paper)

  - [Prerequisites](#prerequisites)
  - [Run Locally](#run-locally)
    * [Data generation](#data-generation)
    * [Deep learning](#deep-learning)

  - [Contact](#contact)
  - [Links](#links)
  - [License](#license)

---
## Introduction
The search for evidence of a dark matter particle is one of the hottest topics is physics today. As high energy physics experiments at the Large Hadron Collider (LHC) at CERN is yet to produce fruitful results in this pursuit, some have resorted to Monte Carlo simulation tools to gain further knowledge in the area. In such programs, high energy physics can be conducted on new models and paradigms that extends the standard model using sophisticated and sound tools. In this project, the production of so a called dark matter candidate particle from high energy proton-proton collisions are investigated using such tools. The tool of choice for this project is *[MadGraph](https://nloaccess.in2p3.fr/tools/MG5/index)*

The complementary program *[MadAnalysis](https://launchpad.net/madanalysis5)* enables the generation of histograms of relevant quantities from the files generated by *MadGraph*. These histograms constitutes the training data for the deep learning model.

### Goals
The *goal* of this project is to develop a deep learning model that can, to a satisfactory degree of accuracy, determine whether a proton-proton collision resulted in the production of a dark matter candidate particle. If true, the model outputs a prediction of the mass of the dark matter candidate particle. Both the classification and mass regression models are realized using a Convolutional Neural Newtwork (CNN) and a Bayesian CNN

### Event Generation
In context of the LHC, an *event* is the collision of two particles at high energy, and the aftermath that follows. MadGraph enables the generation and manipulation of events, calculation of *[cross sections](https://en.wikipedia.org/wiki/Cross_section_(physics))* and sophisticated analyzing of event files with MadAnalysis. Using these programs, histograms of quantities such as Missing Transverse Energy (MET), Transverse Momentum (PT), [Pseudorapidity](https://en.wikipedia.org/wiki/Pseudorapidity) ($\eta$) can be obtained. From these a deep learning model can be trained.


### Deep Learning
<!--- What is Deep Learning compared to regualar machine learning -->
<!--- What is the model(s) trying to predict? Mass and type of model -->
<!--- Architecture? CNN (mention general structure of layers), and bCNN
<!--- Possible tell what accuracy the model obtained? -->

## Paper
TBA

---

<!-- Prerequisites -->
## Prerequisites

 
<!-- Run Locally -->
## Run Locally

Start by cloning the repository

```bash
  git clone https://github.com/EdwardGlockner/DM-signals-at-LHC-with-ML.git
```

Below are tutorials for both the data generation part in MadGraph, and also the deep learning part in Python.

### Data generation

### Deep learning

Go to the project directory

```bash
  cd my-project
```

Install the necessary libraries by running the `install.py`. The python version for which the libraries will be installed for can be modified through the -v flag, which is set to none by default.

```bash
  python install.py -v <python-version>
```

---
<!-- Contact -->
## Contact
Max Andersson - [@linkedin](https://www.linkedin.com/in/maxandersson314/)  
Edward Glöckner - [@linkedin](https://www.linkedin.com/in/edwardglockner/)  
Carl Löfkvist - [@linkedin](https://www.linkedin.com/in/carl-löfkvist-208371225/)

<!-- Links -->
## Links

Here are some helpful links:

<!-- License -->
## License

```
MIT License

Copyright (c) 2023 Max Andersson, Edward Glöckner, Carl Löfkvist

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```




