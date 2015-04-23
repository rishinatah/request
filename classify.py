import numpy as np
from sklearn.svm import SVC
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.feature_selection import chi2
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest

train = open('training_vectors_stratified_all.txt')
label = open('training_labels_stratified_all.txt')

# test = open('test_vectors_stratified_binary_5.txt')
# label_test = open('test_labels_stratified_binary_5.txt')

test = open('analysis_feature_vectors.txt')
# label_test = open('test_labels_stratified_all.txt')

# train = open('training_vectors.txt')
# label = open('training_labels.txt')

# train = open('random_file.txt')
# label = open('random_file_label.txt')

X=[]
Y=[]
X_test=[]
Y_test=[]

print "Getting training vectors"
train_count = 0
x_train = train.readline()
while x_train:	
	train_count = train_count+1
	x_train_split = x_train.split()
	x_new = []
	for x in x_train_split:
		x_new.append(int(x))
	# print x_new
	X.append(x_new)
	x_train = train.readline()

# print X

print "Getting training labels"
label_count = 0
y_label = label.readline()
while y_label:	
	label_count = label_count+1	
	y_label=int(y_label)
	Y.append(y_label)	
	y_label = label.readline()

# print Y

# chi2score = chi2(X,Y)[0]
# print len(chi2score)

# chi2score = sorted(chi2score)
# plt.plot(chi2score)
# plt.show()

ch2 = SelectKBest(chi2, k=1500)
X=ch2.fit_transform(X, Y)
# print X

print "Getting test vectors"
test_count = 0
x_test = test.readline()
while x_test:	
	test_count = test_count+1
	x_test_split = x_test.split()
	x_new = []
	for x in x_test_split:
		x_new.append(int(x))
	X_test.append(x_new)
	x_test = test.readline()

# print "Getting test labels"
# label_test_count = 0
# y_label_test = label_test.readline()
# while y_label_test:	
# 	label_test_count = label_test_count+1	
# 	y_label_test=int(y_label_test)
# 	Y_test.append(y_label_test)	
# 	y_label_test = label_test.readline()

# X = np.array(X)
# y = np.array(Y)

# X_test = np.array(X_test)
# Y_test = np.array(Y_test)

print "Training"
clf = svm.SVC(kernel='rbf',C=100000,gamma=0.001).fit(X, Y)

# clf = KNeighborsClassifier(n_neighbors=13).fit(X, y)
# clf = RandomForestClassifier(n_estimators=1000).fit(X, y)

# clf = svm.SVC(kernel='rbf',C=10000,gamma=0.0001).fit(X, y) - 5 freq, 48%
# clf = svm.SVC(kernel='rbf',C=10000000,gamma=0.01).fit(X, y) - 10 freq, 32%

# clf = svm.SVC(kernel='rbf',C=10000,gamma=0.0001).fit(X, y) - binary all, 12%
# clf = svm.SVC(kernel='rbf',C=100000000,gamma=0.0001).fit(X, y) - binary 5 or 10 freq, 62%

# clf = svm.SVC(kernel='rbf',C=100000000,gamma=0.0001).fit(X, y)  - binary 5 freq stratified, 64.7059%
# clf = RandomForestClassifier(n_estimators=10).fit(X, y) - binary 5 freq stratified, 66.67% * acc = 64.7059 for all other values of n
# clf = svm.SVC(kernel='rbf',C=100000,gamma=0.001).fit(X, y) - binary 5 freq stratified, 64.7059% * most common accuracy
# clf = KNeighborsClassifier(n_neighbors=20).fit(X, y) - binary 5 freq stratified, 66.67% * works well only for dev, not train.

print "Predicting"
X_test = ch2.transform(X_test)
# Y_test = ch2.transform(Y_test)

# s = clf.score(X_test,Y_test)
s = clf.predict(X_test)
# f1 = f1_score(Y_test, s, average='micro')

preds = open('analysis_preds.txt','w')
for s1 in s:
	preds.write(str(s1))
	preds.write('\n')
preds.close()
# print s
# print f1

# ([[],[],[]])

# X = np.array([[0,0,0],[0,1,0],[1,1,1]])
# y = np.array([0, 0, 1])

# clf = svm.SVC(kernel='rbf',C=1,gamma=1).fit(X, y)
# s = clf.score([[1,1,1],[0,0,0]],[0,1])
# s = clf.score([[1,1,1],[0,0,0]],[0,1])
# s = clf.predict([[1,1,1],[0,0,0]])