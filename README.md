# Evasion Attacks Against ML-based Malware Detectors

## Project Description

The aim of this project is to explore evasion attacks against machine learning-based malware detectors.

## Project structure
- data/ Contains a subset of benign and malicious executables that will be used for testing purposes. 
- src/ Contains the code of the project.
  - architectures/ Contains the architectures for MalConv and Aloha networks. MalConv takes as input the bytes of the executable while ALOHA takes as input a set of features, i.e. EMBER features.
    - end2end/ Contains the MalConv architecture implementation in PyTorch.
    - expert_features/ Contains the ALOHA network implementation in PyTorch.
  - checkpoints/ Contains the checkpoints/model weights for the MalConv, Aloha and LightGBM models.
  - datasets/ Contains the code to build a PyTorch dataset for training MalConv.
