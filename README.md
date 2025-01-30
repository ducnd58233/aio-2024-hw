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
conda env create --file=./environment.yml
```

```bash
conda activate aio2024-hw
conda install --yes --file requirements.txt
conda env update -n aio2024-hw --file=./environment.yml

streamlit run <file_name>.py
```