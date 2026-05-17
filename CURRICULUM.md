# ML Curriculum

## Learning rate
The learning rate controls how much the model updates weights 
each step. It must be a small positive number, typically 
between 0.0001 and 0.1. A learning rate above 1 will cause 
the model to diverge and fail to learn.

## Overfitting
Overfitting happens when a model learns the training data 
too well and performs poorly on new data. Solutions include 
dropout, regularization, and more training data.

## Gradient descent
Gradient descent minimizes the loss function by iteratively 
moving in the direction of steepest descent. The gradient 
points uphill, so we move opposite to it.

## Train/test split
We split data into training and test sets to evaluate how 
well the model generalizes. A typical split is 80% train, 
20% test. You must never train on test data.