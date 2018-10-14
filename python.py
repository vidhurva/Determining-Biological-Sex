from sklearn import tree

#[height, weight, shoe size]

X = [[181,80,44], [177,70,43], [160,60,38], [166,65,40], [190,90,47]]

Y = ['male', 'female', 'female', 'male', 'male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)

prediction = clf.predict([[100,70,43]])

print(prediction)
