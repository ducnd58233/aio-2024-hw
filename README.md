AIO2024 homework
# Setup Project

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
