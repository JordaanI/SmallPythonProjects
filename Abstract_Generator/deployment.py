import pandas as pd
import numpy as np
import random
from flask import Flask
from tensorflow.keras.models import load_model

def lookup(param):
    if type(param) is np.int64 or int:
        return word_index[param]
    elif type(param) is str:
        return word_lexicon[param]
    else:
        print('Parameter not accepted.')

model_dir = r'D:/PythonProjects/AbstractGenerator/deployment/models/'
model_name = 'Main_model'
model = load_model(f'{model_dir}{model_name}.h5')

X_test = np.loadtxt('D:/PythonProjects/AbstractGenerator/deployment/data/X_test.txt')
word_lexicon = pd.read_csv('D:/PythonProjects/AbstractGenerator/deployment/data/word_lexicon.csv')
word_index = pd.read_csv('D:/PythonProjects/AbstractGenerator/deployment/data/word_index.csv')
word_lexicon = dict(word_lexicon.drop(['Unnamed: 0'],axis=1).values)
word_index = dict(word_index.drop(['Unnamed: 0'],axis=1).values)

app = Flask(__name__)

@app.route('/')
def generate_sequence():    
    training_length = 35
    seq = list(random.choice(X_test))
    diversity=1

    seed_idx = 0
    end_idx = training_length

    seed = list(seq[seed_idx:end_idx])
    original_sequence = [word_index[i] for i in seed]
    generated = seed[:] + ['#']


    actual = generated[:] + seq[end_idx:end_idx + training_length]

    for i in range(training_length):
        preds = model.predict(np.array(seed).reshape(1, -1))[0].astype(
            np.float64)
        preds = np.log(preds) / diversity
        exp_preds = np.exp(preds)
        preds = exp_preds / sum(exp_preds)
        probas = np.random.multinomial(1, preds, 1)[0]
        next_idx = np.argmax(probas)
        seed = seed[1:] + [next_idx]
        generated.append(next_idx)

    SEED = ' '.join(original_sequence)
    AI = ' '.join([lookup(i) for i in generated[36:]])
    REAL = ' '.join([lookup(i) for i in actual[36:]])
    return 'Seeded sequence: ' + SEED + '\n Actual sequence:' + REAL + '\n Generated squence:' + AI 


if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=True)