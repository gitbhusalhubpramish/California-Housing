import kagglehub
import pandas as pd
from sklearn.model_selection import train_test_split

path = kagglehub.dataset_download("/camnugent/california-housing-prices", "housing.csv")

df = pd.read_csv(path)

x,y = df[["mdeian_income", "total_rooms", "housing_median_age"]], df["median_house_value"]

xtrain, xtest, ytriain, ytest = train_test_split(x,y,test_size=0.2, random_state=42)

