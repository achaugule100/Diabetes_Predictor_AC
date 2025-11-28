import pandas as pd
import util as utilities
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', None)

print("\n-----\n")

df = pd.read_csv("./2split.csv")
#print(df.head())



def label_encode_health(days):
	if days == 0:
		return "None"
	elif 1 <= days <= 5:
		return "Mild"
	elif 6 <= days <= 15:
		return "Moderate"
	elif 16 <= days <= 29:
		return "Severe"
	elif days >= 30:
		return "Chronic"

df['PhysHlth_Bucket'] = df['PhysHlth'].apply(label_encode_health)
df['MentHlth_Bucket'] = df['MentHlth'].apply(label_encode_health)

#print(df.head())
#print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

df = utilities.labelEncoder(df, ['PhysHlth_Bucket', 'MentHlth_Bucket'])

#print(df.head())

df= df.drop("MentHlth", axis=1)
df =df.drop("PhysHlth", axis=1)
print(df.head())

########## SCALING THE BMI ###############
from sklearn.preprocessing import MinMaxScaler

# instance of the MinMaxScaler
sc = MinMaxScaler()

# fit the scaler to the data
sc.fit(df)

# transform the data using the scaler
data_scaled = sc.transform(df)
#df = pd.DataFrame(data_scaled)
index=df.index
df = pd.DataFrame(
		data_scaled,
		columns=[
				'Diabetes_binary', 'HighBP', 'HighChol', 'BMI', 'Smoker', 'Stroke',
				'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
				'HvyAlcoholConsump', 'GenHlth', 'DiffWalk', 'Sex', 'Age', 'Income',
				'PhysHlth_Bucket', 'MentHlth_Bucket'
		],
		index=df.index
)


#

print(df.head())

#######################################


from sklearn.model_selection import train_test_split
X = df.drop("Diabetes_binary", axis=1)
y = df["Diabetes_binary"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.10,  random_state = 0)

from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators=100, class_weight = 'balanced', max_depth=7)
forest = forest.fit(X_train, y_train)

#preds = forest.predict_proba(X_test)
#print(preds)
preds = forest.predict(X_test)
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix, recall_score, f1_score
test_acc = accuracy_score(y_test, preds)
print("Accuracy Score: " + str(test_acc))

test_pre = precision_score(y_test, preds)
print("Precision Score: " + str(test_pre))

test_recall = recall_score(y_test, preds)
print("Recall Score: " + str(test_recall))

test_f1 = f1_score(y_test, preds)
print("F1 Score: " + str(test_f1))

cm = confusion_matrix( y_test, preds, labels = [1,0])
print("The confusion matrix of the tree is: ")
print(cm)

#Test the model with the training data set and prints accuracy score
train_predictions = forest.predict(X_train)
train_acc = accuracy_score(y_train, train_predictions)
print("The accuracy with the training data set of the Decision Tree is: " + str(train_acc))

'''from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

for x in range(0, 5):
	plot_tree(forest.estimators_[x], feature_names=X.columns, filled=True)
	plt.show()
	'''


### Correlation Matrix ########

import seaborn as sns
import matplotlib.pyplot as plt

#data = df.drop("Diabetes_binary", axis=1)
data = df
corr = data.corr()

plt.figure(figsize=(11,9))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="Spectral")
plt.title("Correlation Matrix")
plt.show()


################################


### Feature Importance Graph #####

importance = forest.feature_importances_

#print(importance)
plt.figure(figsize=(11, 6)) 
plt.barh(range(X.shape[1]), importance)
plt.yticks(range(X.shape[1]), X.columns, rotation=0)
plt.title("Feature Importance")
plt.show()

