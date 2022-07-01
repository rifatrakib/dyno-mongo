# dyno-mongo

This repository contains some ipython notebooks where complex MongoDB aggregation pipelines are built dynamically and queried, and in some cases stored locally. The `utils.py` script contains some commonly used functions and classes. To use the notebooks as standalone, copy those functions and classes from the `utils.py` and put them after the import in any notebook. Remember to remove the import statement where a notebook imports from to that file! To get started install all the necessary modules from `requirements.txt` by using `pip install -r requirements.txt`

## Description of pipelines

What the pipelines included in this repository does are explained below in a few words:

#### 1. Complex grouping:

This pipeline shows consecutive group queries in the query pipeline to generate count of documents grouped by a broader field and sum of a numerical field grouped by another dependent field of the former.

#### 2. Dependency builder

This pipeline is created dynamically to fetch a graph structured dependency data prepared using raw computational power of MongoDB aggregation framework.
