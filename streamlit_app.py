import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split
import streamlit as st
import pickle
import os
import graphviz

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
	def __init__(self, feature=None, trashold=None, left=None, right=None, value=None):
		self.feature= feature
		self.trashold = treshold
		self.left= left
		self.right = right
		self.value = value

with open("tree.pkl", "rb") as f:
	tree = pickle.load(f)
error = pd.read_csv("error.csv")

def build_graph(root):
	graph = []
	def traverse(node, node_id=0):
		nonlocal graph
		if node is None:
			return

		if node.value is not None:
			graph.append(f'{node_id} [label = "predict: {node.value}"]')
			return
		graph.append(f'{node_id} [label="X[{node.feature}]>={node.trashold:.3f}"];')

		for child, child_id, label in [(node.left, 2*node_id+1, "True"), (node.right, 2*node_id+2, "False")]:
			if child:
				graph.append(f'{node_id}-> {child_id} [label="{label}"];')
				traverse(child, child_id)

	traverse(root)
	return """digraph Tree{\n graph [rankdir=TB, dpi=150, nodesep=0.1, ranksep=0.1, fontsize=5, size="", pad=0.2]; node [fontsize=2 width=0.2, height=0.1, margin=0 fixedsize=false]; edge [fontsize=2 arrowsize=0.1];""" + "\n".join(graph) + "}"

graph = graphviz.Source(build_graph(tree))
svg = graph.pipe(format="svg", engine="dot")
st.components.v1.html(
f'''
<div style="width:100%; height:800px; overflow:auto;">
<div style="width:max-content; height: max-content;">
{svg}
</div>
''',
height = 820,
scrolling =True
)

st.download_button(label="Download tree", data = svg, file_name=f"decisiontree.svg", mime="image/svg+xml")

