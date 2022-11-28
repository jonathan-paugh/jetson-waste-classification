import os
from os.path import exists, isfile
from configs.transfer import config as config_transfer


JETSON_FILE = '.jetson'
IS_JETSON = exists(JETSON_FILE) and isfile(JETSON_FILE)

DATASET_TRAIN_PATH = 'dataset/train'
DATASET_TEST_PATH = 'dataset/test'
OUTPUT_PATH = 'dist'

SEED = 0
VALIDATION_SPLIT = 0.2

MODEL_FEATURE_EXTRACTOR, IMAGE_SIZE = config_transfer(size=299)
MODEL_EARLY_STOPPING_PATIENCE = 5  # stop after x consecutive epochs with no improvement
MODEL_NUM_EPOCHS = 50
MODEL_FINE_TUNING = True
MODEL_FINE_TUNING_NUM_EPOCHS = 50
MODEL_FINE_TUNING_LEARNING_RATE = 1e-5         # defaults to 1e-4
MODEL_FINE_TUNING_BATCH_NORM_MOMENTUM = 0.997  # defaults to 0.99
MODEL_DROPOUT_RATE = 0.3
MODEL_WORKERS = os.cpu_count() | 1
MODEL_BATCH_SIZE = 2 ** (3 if IS_JETSON else 5)
LOADER_BATCH_SIZE = 2 ** (3 if IS_JETSON else 5)
