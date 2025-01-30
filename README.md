AIO2024 homework

- export requirements

```bash
pip list --format=freeze > requirements.txt
# conda env export > environment.yml --no-builds
conda env export --from-history > environment.yml --no-builds
```

- start env

```bash
# First using conda
conda remove -n aio2024-hw --all
conda create -n aio2024-hw python=3.12
conda install -n base conda-libmamba-solver
conda env create --file=./environment.yml --solver=libmamba --verbose
```

```bash
conda activate aio2024-hw
conda install --yes --file requirements.txt
conda install -n base conda-libmamba-solver --verbose
conda env update -n aio2024-hw --file=./environment.yml --solver=libmamba --verbose

streamlit run <file_name>.py
```

```bash
# First, create the base environment with core packages
conda create -n aio2024-hw python=3.12
conda activate aio2024-hw

# Install packages in groups to better manage dependencies
# Group 1: Basic scientific packages
conda install matplotlib numpy scikit-learn ipykernel -c conda-forge

# Group 2: NLP packages
conda install nltk spacy -c conda-forge

# Group 3: PyTorch and related packages
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Group 4: Additional ML packages
conda install transformers accelerate bitsandbytes -c conda-forge

# Finally, install the remaining packages
conda install streamlit gdown ultralytics timm -c conda-forge
```
