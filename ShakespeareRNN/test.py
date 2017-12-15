import rnn
import numpy as np


#Check if gradients ARE correct
grad_check_vocab_size = 100
np.random.seed(10)
model = rnn.RNNNumpy(grad_check_vocab_size, 10, bptt_truncate=1000)
model.gradient_check([0,1,2,3], [1,2,3,4])

