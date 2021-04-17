
from sklearn.datasets import load_digits    #we're importing the hand-written digits dataset from sklearn
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from src.pca import pca

digits = load_digits() 
X = digits.data 
y = digits.target

X = pca(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35)

mlp = MLPClassifier(hidden_layer_sizes=(15,), activation='logistic', alpha=1e-4,
                    solver='sgd', tol=1e-4, random_state=1,
                    learning_rate_init=.1, verbose=True)

def test(X_train,y_train,X_test):
  mlp.fit(X_train,y_train)
  y_pred = mlp.predict(X_test)
  return y_pred

y_pred = test(X_train,y_train,X_test)
print("Accuracy:")
print(accuracy_score(y_test, y_pred))
print("\nAccuracy in percentage:")
print(accuracy_score(y_test, y_pred)*100)