# AIO2024 homework
## Table of contents:
- [Setup Project](#setup-project)
- [Content](#content)
    - [Module 1: Towards AI and Data Science](#module-1-towards-ai-and-data-science)
    - [Module 2: Calculus and Linear Algegra, and theirs Applications to AI](#module-2-calculus-and-linear-algegra-and-theirs-applications-to-ai)
    - [Module 3: Probability&Statistics and Optimization, and theirs Applications to AI](#module-3-probability-statistics-and-optimization-and-theirs-applications-to-ai)
    - [Module 4: Machine Learning and Data Science](#module-4-machine-learning-and-data-science)
    - [Module 5: Steps to Deep Learning (Using Numpy and PyTorch)](./module-5)
    - [Module 6: Deep Learning for Different Data (Using PyTorch)](./module-6)
    - [Module 7: Deep Learning Applications for Images](./module-7)
    - [Module 8: Deep Learning Applications for Text](./module-8)
    - [Module 9: Generative Models](./module-9)
    - [Module 10: Advanced Deep Learning and LLMs](./module-10)
    
## Setup Project

- Remove environment (if already created)

```
conda env remove -n aio2024-hw -y
```

- Create environment (if not already created)

```
conda create -n aio2024-hw python=3.12
conda activate aio2024-hw
pip install setuptools
pip install poetry
```

- Activate conda environment

```
conda activate aio2024-hw
```

- Install dependencies

```
poetry install --no-root
```

- Install pre-commit hooks

```
poetry run pre-commit install
```

- Run pre-commit hooks

```
poetry run pre-commit run --all-files
```

## Content


### [Module 1: Towards AI and Data Science](./module-1)

### [Module 2: Calculus and Linear Algegra, and theirs Applications to AI](./module-2)

### [Module 3: Probability&Statistics and Optimization, and theirs Applications to AI](./module-3)
<div align="center" width="100%">

|Date|ID|Topic|Note|
|---|---|---|---|
|17/08/2024|[M03EX01](./module-3/17_08_2024_M03EX01)|Data Analysis with Pandas|Pandas syntax|
|24/08/2024|[M03EX02](./module-3/24_08_2024_M03EX02)|K-Nearest Neighbors and K-Means Clustering|How to implement from scratch K-Nearest Neighbors and K-Means Clustering|
|31/08/2024|[M03EX03](./module-3/31_08_2024_M03EX03)|Decision Tree|How to implement Decision Tree|
|08/09/2024|[M03EX04](./module-3/08_09_2024_M03EX04)|Ensemble Learning|Using library to for Decision Tree, Random Forest, AdaBoost and Gradient Boosting applied to Regression|
|13/09/2024|[M03EX05](./module-3/13_09_2024_M03EX05)|XGBoost|How to implement XGBoost from scratch and using library XGBoost|


</div>

### [Module 4: Machine Learning and Data Science](./module-4)

|Date|ID|Topic|Note|
|---|---|---|---|
|09/10/2024|[M04W01](./module-4/09_10_2024_M04W01)|Linear Regression|How to implement Linear Regression from scratch|

### [Module 5: Steps to Deep Learning (Using Numpy and PyTorch)](./module-5)

### [Module 6: Deep Learning for Different Data (Using PyTorch)](./module-6)

### [Module 7: Deep Learning Applications for Images](./module-7)

### [Module 8: Deep Learning Applications for Text](./module-8)

### [Module 9: Generative Models](./module-9)

### [Module 10: Advanced Deep Learning and LLMs](./module-10)
