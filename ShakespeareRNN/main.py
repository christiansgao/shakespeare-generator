import rnn
import numpy as np
import utils

from preprocessing import Preprocessing as Preprocessing

### Main ###
filepath = './Resources/shakespeare_test.txt';
vocabulary_size = 20
hidden_dim = 12

# Preprocessing
preprocess = Preprocessing();
x_train, y_train = preprocess.create_tokens(vocabulary_size, filepath)
print("Done Preprocessing")

# Forward Prop with initial values
np.random.seed(10)
model_rnn = rnn.RNNNumpy(preprocess = preprocess,word_dim=vocabulary_size, hidden_dim=hidden_dim)
prediction = model_rnn.predict(x=x_train[0])

o, s = model_rnn.forward_propagation(x_train[0])

print "prediction: " + str(prediction)
print "o shape: " + str(o.shape)
print "s.shape: " + str(s.shape)

# Testing loss
print "Expected Loss for random predictions: %f" % np.log(vocabulary_size)
print "Actual loss: %f" % model_rnn.calculate_loss(x_train[:1000], y_train[:1000])

#Training
model_rnn.train_with_sgd(x_train=x_train, y_train=y_train, nepoch = 2000)
outfile = "./models/model_1"
utils.save_model(outfile, model_rnn)
model_rnn = utils.load_model(outfile)
#Prediction
print "Predictions: "
model_rnn.generate_shakespeare()