FROM jupyter/scipy-notebook
RUN pip install numpy matplotlib geopandas mapclassify seaborn 
COPY datasets /datasets