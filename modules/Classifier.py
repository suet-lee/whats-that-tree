from fastai.vision import *

def get_class(idx):
    types = [
        'alder tree',
        'ash tree',
        'beech tree',
        'birch tree',
        'cedar tree',
        'chestnut tree',
        'elm tree',
        'lime tree',
        'maple tree',
        'oak tree',
        'scots pine tree',
        'white poplar tree',
        'spruce tree',
        'willow tree'
    ]
    return types[idx]

def classify(file):
    learn = load_learner(".", 'export.pkl')
    pred_class,pred_idx,outputs = learn.predict(file.read())
    print(pred_class)
    return pred_class
