import yaml
import os
from train.test import test

config = yaml.safe_load(open('/content/DS203/config.yml'))
mode = config['mode']
os.environ["CUDA_VISIBLE_DEVICES"] = str(config['aspect_' + mode + '_model'][config['aspect_' + mode + '_model']['type']]['gpu'])
test(config)