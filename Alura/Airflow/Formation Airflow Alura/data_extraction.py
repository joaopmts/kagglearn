import os
from os.path import join
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

date_start = datetime.today()
date_end = date_start + timedelta(days=7)

date_start = date_start.strftime('%Y-%m-%d')
date_end = date_end.strftime('%Y-%m-%d')

city = 'Boston'
key = 'FBJUV2HJ6PEUHB3J8DB9GZPC8'


URL = join('https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/',
 f'{city}/{date_start}/{date_end}?unitGroup=metric&include=days&key={key}&contentType=csv')

data = pd.read_csv(URL)
print(data.head())

base_dir    = Path(r'C:\Users\JOAO PC\Documents\VSCode\kagglearn\Alura\Airflow\Formation Airflow Alura')

folder_path = base_dir / f'semana{date_start}'
folder_path.mkdir(parents=True, exist_ok=True)

data.to_csv(os.path.join(folder_path,'dados_brutos.csv'))
data[['datetime', 'tempmin', 'temp', 'tempmax']].to_csv(os.path.join(folder_path,'temperaturas.csv'))
data[['datetime', 'description', 'icon']].to_csv(os.path.join(folder_path,'condicoes.csv'))
