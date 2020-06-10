from fastai.vision import *
import pathlib

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

def classify(img):
    path = pathlib.Path(__file__).parent.absolute()
    learn = load_learner(path, 'export.pkl')
    pred_class,pred_idx,outputs = learn.predict(img)
    print(pred_class)
    return pred_class
