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
<!-- 
Comment this since github sanitize this style tag
<style>
    table {
        width: 85%;
        margin: 4% auto;
    }
    table th {
        text-align: center;
    }
    table th:first-child {
        width: 5%;
    }
    table th:nth-child(2) {
        width: 5%;
    }
    table th:nth-child(3) {
        width: 30%;
    }
    table th:nth-child(4) {
        width: 60%;
    }
</style> 
-->

### [Module 1: Towards AI and Data Science](./module-1)
|Date|ID|Topic|Note|
|---|---|---|---|
|01/06/2024|[M01EX01](./module-1/01_06_2024_M01EX01)|Basic Python|Python syntax|
|08/06/2024|[M01EX02](./module-1/08_06_2024_M01EX02)|Data Structure|Data Structure with Python|
|15/06/2024|[M01EX03](./module-1/15_06_2024_M01EX03)|OOP|OOP with Python|
|22/06/2024|[M01EX04](./module-1/22_06_2024_M01EX04)|Streamlit|Streamlit project|

### [Module 2: Calculus and Linear Algegra, and theirs Applications to AI](./module-2)
|Date|ID|Topic|Note|
|---|---|---|---|
|06/07/2024|[M02EX01](./module-2/06_07_2024_M02EX01)|Numpy|Numpy syntax|
|13/07/2024|[M02EX02](./module-2/13_07_2024_M02EX02)|Vector|How to calculate matrix inverse, eigen values and eigen vectors|
|20/07/2024|[M02EX03](./module-2/20_07_2024_M02EX03)|Probability|Naive Bayes Classifier|
|27/07/2024|[M02EX04](./module-2/27_07_2024_M02EX04)|Statistics||

### [Module 3: Probability&Statistics and Optimization, and theirs Applications to AI](./module-3)
|Date|ID|Topic|Note|
|---|---|---|---|
|17/08/2024|[M03EX01](./module-3/17_08_2024_M03EX01)|Data Analysis with Pandas|Pandas syntax|
|24/08/2024|[M03EX02](./module-3/24_08_2024_M03EX02)|K-Nearest Neighbors and K-Means Clustering|How to implement from scratch K-Nearest Neighbors and K-Means Clustering|
|31/08/2024|[M03EX03](./module-3/31_08_2024_M03EX03)|Decision Tree|How to implement Decision Tree|
|08/09/2024|[M03EX04](./module-3/08_09_2024_M03EX04)|Ensemble Learning|Using library to for Decision Tree, Random Forest, AdaBoost and Gradient Boosting applied to Regression|
|13/09/2024|[M03EX05](./module-3/13_09_2024_M03EX05)|XGBoost|How to implement XGBoost from scratch and using library XGBoost|

### [Module 4: Machine Learning and Data Science](./module-4)
|Date|ID|Topic|Note|
|---|---|---|---|
|28/09/2024|[M04W01](./module-4/28_09_2024_M04W01)|Linear Regression|How to implement Linear Regression from scratch with Numpy|
|05/10/2024|[M04W02](./module-4/05_10_2024_M04W02)|Linear Regression|How to implement Linear Regression with vectorization using stochastic gradient descent, m samples (mini-batch gradient descent), N samples (batch gradient descent) in numpy|
|12/10/2024|[M04W03](./module-4/12_10_2024_M04W03)|Genetic Algorithm|How to implement Genetic Algorithm|

### [Module 5: Steps to Deep Learning (Using Numpy and PyTorch)](./module-5)
|Date|ID|Topic|Note|
|---|---|---|---|
|26/10/2024|[M05EX01](./module-5/26_10_2024_M05EX01)|Logistic Regression|How to implement Logistic Regression from scratch|

### [Module 6: Deep Learning for Different Data (Using PyTorch)](./module-6)
|Date|ID|Topic|Note|
|---|---|---|---|


### [Module 7: Deep Learning Applications for Images](./module-7)
|Date|ID|Topic|Note|
|---|---|---|---|


### [Module 8: Deep Learning Applications for Text](./module-8)
|Date|ID|Topic|Note|
|---|---|---|---|


### [Module 9: Generative Models](./module-9)
|Date|ID|Topic|Note|
|---|---|---|---|


### [Module 10: Advanced Deep Learning and LLMs](./module-10)
|Date|ID|Topic|Note|
|---|---|---|---|

