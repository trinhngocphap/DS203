import yaml
from data_process.data_process import data_process

config = yaml.safe_load(open('/content/MAMS-for-ABSA/config.yml'))

data_process(config)