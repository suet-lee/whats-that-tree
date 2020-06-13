# What's that tree: a tree classification app built with fast.ai

A homework from the fast.ai deep learning course v3.
See the jupyter notebook used for classification [here](https://github.com/suet-lee/fastai/blob/master/TreeClassifier.ipynb).

## Requirements
- python3
- Flask==1.1.2
- fastai==1.0.61

## Setup
- You will need to create an .env file with a secret key for the Flask application. You can generate a key with:  
`python -c 'import os; print(os.urandom(16))'`
- You will need to create a `tmp` folder in the root_directory, this is where uploaded images will be temporarily stored (and later deleted)
- If you wish to use logging, you will need an `app.log` file in the root directory
- The `app.log` file and `tmp` folder need write permissions:  
`sudo chown www-data:www-data app.log`  
`sudo chown -R www-data:www-data tmp`

For more detail on how to deploy a flask app on server see [here]().

## TODO
- Add user feedback option for incorrect classification (can be used for further training)
- Add classification based on flower, leaf, seeds etc.
