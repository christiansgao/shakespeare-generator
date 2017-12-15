import tensorflow as tf
from tensorflow.contrib import layers
from tensorflow.contrib import rnn  # rnn stuff temporarily in contrib, moving back to code in TF 1.1
import os
import time
import math
import numpy as np
import my_txtutils as util

###Model Params###

tf.set_random_seed(0)

text_dir = "shakespeare/*.txt"

traning_text, validation_text,