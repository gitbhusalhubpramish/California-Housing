# California housing with decision tree

In this project I have applied Decision tree fro mscratch in [California Housing](https://www.kaggle.com/datasets/camnugent/california-housing-prices) dataset in kaggle from it's notebook, trained it, stored the parameter and showed the preview in streamlit app. This markdown is just the preview of the project and how I made this. I have given more details in m [notes](https://github.com/gitbhusalhubpramish/ml-notes/tree/main/0.004%20decision-tree) about decision tree.

<img src="visual.jpg"/>

This is what the losses(mse) of model in different depth looks like. I have rendered this in the [preview](https://california-housing-decision-tree.streamlit.app/)

## Small intro to Decision Tree

Decision Tree is a supervised meachine learning algorithm where it splits data using a treshold on and on untill it reach to leaf(prediction). It is usually classification model but I've made this regression and used MSE to calculate loss.

## Feature

This project was made by me to understand Decision tree form scratch so it has decision tree applied from scratch - trained in kaggle notebooks and preview in streamlit app. But also:

- Decision Tree from scratch
- GPU Parellized processing
- decision tree visulization
- trained in kaggle environment

## Tech-Stack

This project uses python liberies used for datascience - Visulization, calculation and data manipulation. I've used:

- Numpy for calculation
- Streamlit and graphviz for data visulization and preview
- cupy for GPU bashed parellel processing
- Pandas for data manipulation
- sk-learn for datasplit

## Work-flow

The workflow of the project is divided into 2 catogary:

## Kaggle side(training):

First I'd train the trees in data by building algorithm from scratch in kaggle jupiter notebook. The flow looks like this:

- **Data fetch:** First data is initilized from the kaggle dataset to training environment.
- **Data Split:** Here the data is splited into 2(4) parts for training and testing for each with x and y.
- **Impurity/best split:** The impurity is calculated in each possible treshold through MSE using this formula then select the purist data(with higest split score):

$$
split score = \frac{n_left}{n_total} MSE(left) + frac{n_right}{n_total} MSE(right)
$$

- **repeat:** repeat the split(score)/impurity untill you reach to the max depth or no split possible - simplly return the mean of the data in leaf.
- **Build tree:** Each repitation build a node and branches of tree we store feature, treshold, left and right node for spliting nodes while value for leaf and store that.
- **running/testing:** we simpilly run the testing data from build tree.
- **Export:** Since training model in streamlit server is expencive and requires gpu so we train model in kaggle environment and export model in `"tree.pkl"` and error in `"error.csv"`.

### Streamlit side(Preview):

After training we show the preview of the model in streamlit app. The flow looks like this:

- **Fetch data:** Here we fetch data from kaggle dataset and initilze the trained parameter.
- **Visulization:** This app visulizes the tree using `graphviz` and plots the loss of the model in different depth.

*Most of the training stuff is done in kaggle side streamlit is just he preview*


