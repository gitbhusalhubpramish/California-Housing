import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
import pickle
import os

path = kagglehub.dataset_download("camnugent/california-housing-prices", "housing.csv")

df = pd.read_csv(path)

x,y = df[["median_income", "total_rooms", "housing_median_age"]], df["median_house_value"]

xtrain, xtest, ytriain, ytest = train_test_split(x,y,test_size=0.2, random_state=42)

st.write('''## Data(set)''')
st.write('''This project uses [California Housing] dataset in kaggle. The dataset has house data and it's prize. our work is to predict it's prize''')
st.write('''- Total rows(data)''', len(df))
st.write('''- Median house value(output) range''', f"${min(y)} - ${max(y)}")
st.write('''- Training sampe''', len(xtrain))
st.write('''- Testing sample''', len(xtest))

st.write('''## Algorithm''')
st.write('''This uses decision tree to predict output. Decision tree is like a tree where it compares a feature with a trashold on and on untill it reach to the leaf(prediction point)''')

st.write('''## Model''')
st.write('''The visulization of the tree looks like this''')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "tree.pkl")

class Node:
	def __init__(self, feature=None, treshold=None, left=None, right=None, value=None):
		self.feature= featrue
		self.treshold = treshold
		self.left= left
		self.right = right
		self.value = value

with open("tree.pkl", "rb") as f:
	forest = pickle.load(f)
error = pd.read_csv("error.csv")
