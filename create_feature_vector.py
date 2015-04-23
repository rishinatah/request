import glob
import re
import nltk
from nltk import word_tokenize 
from nltk.util import ngrams
from collections import OrderedDict

count=0

feature_vectors_binary = open('analysis_feature_vectors.txt','w')	########################################
feature_vectors_binary_filename = open('analysis_filename.txt','w')

features_5 = dict()

# emails_labels = dict()
# t = open('Analysis/_a/analysis')
# l = open('Analysis/_a/analysis_label')
# t_read = t.readline()
# l_read = l.readline()
# while t_read:
# 	t_read = t_read.strip()
# 	emails_labels[t_read] = int(l_read.strip())
# 	t_read = t.readline()
# 	l_read = l.readline()

# print emails_labels

# get all lines from trigrams_1_final and set count = 0
features = dict()
features_dict = open('all_training/all_trigrams')
features_dict_line = features_dict.readline()
while features_dict_line:
	features_dict_line = features_dict_line.strip()
	features[features_dict_line] = 0
	features_dict_line = features_dict.readline()

# features_dict = open('0_body_only/trigrams_0_final')
# features_dict_line = features_dict.readline()
# while features_dict_line:
# 	features_dict_line = features_dict_line.strip()
# 	features[features_dict_line] = 0
# 	features_dict_line = features_dict.readline()

# print features
print "Reading all_training"
for filename in glob.glob('all_training/*.txt'):
	# print count

	for f in features:
		features[f] = 0

	# feature_vectors_binary_labels.write(str(emails_labels[filename[13:-4]]))
	# feature_vectors_binary_labels.write('\n')

	count = count + 1
	text = open(filename)
	# print filename
	text_body = text.read()
	text_body = text_body.lower()
	
	# text_body = re.sub(r'\n+', ' ', text_body)
	# text_body = re.sub(r' +', ' ', text_body)
	# # Before any punctuation, add a space
	# text_body = re.sub(r'[.,?!'"()-]', ' [.,?!\'"()-]', text_body)

	# for f in features:
	# 	if text_body.find(f) >= 0: features[f] = features[f] + 1

	text_body = re.sub(r'[\d]+[st|nd|rd|th]', '__NUM__', text_body)
	text_body = re.sub(r'[\d]*[,-:.][\d]+', '__NUM__', text_body)
	text_body = re.sub(r'[\d]+', '__NUM__', text_body)


	token_lower_case=nltk.word_tokenize(text_body.lower())
	trigrams=ngrams(token_lower_case,3)



	for trigram in trigrams:
		trigram = str(trigram)
		if trigram in features:
			features[trigram] = features[trigram] + 1
			# features[trigram] = 1
		if trigram in features_5: features_5[trigram] = features_5[trigram] + 1
		else: features_5[trigram] = 0

	# for f in features:
	# 	if features[f]==0: 
	# 		print f, features[f]	

		# if text_body.find(f) >= 0: features[f] = features[f] + 1 

	string = ''
	for x in features:
		string = string + str(features[x]) + ' '
	# go through dictionary and add each element in one line e.g 0 0 1 2
	string = string + '\n'

	# print string
	# feature_vectors.write(string)	########################################

	# if count == 1: break

# feature_vectors.close()
# print count


# print "Reading 1_body_only"
# for filename in glob.glob('1_body_only/*.txt'):
# 	# print count

# 	for f in features:
# 		features[f] = 0

# 	count = count + 1
# 	text = open(filename)
# 	# print filename
# 	text_body = text.read()
# 	text_body = text_body.lower()	

# 	text_body = re.sub(r'[\d]+[st|nd|rd|th]', '__NUM__', text_body)
# 	text_body = re.sub(r'[\d]*[,-:.][\d]+', '__NUM__', text_body)
# 	text_body = re.sub(r'[\d]+', '__NUM__', text_body)

# 	token_lower_case=nltk.word_tokenize(text_body.lower())
# 	trigrams=ngrams(token_lower_case,3)

# 	for trigram in trigrams:
# 		trigram = str(trigram)
# 		if trigram in features:
# 			# features[trigram] = features[trigram] + 1
# 			features[trigram] = 1
# 		if trigram in features_5: features_5[trigram] = features_5[trigram] + 1
# 		else: features_5[trigram] = 0

# 	string = ''
# 	for x in features:
# 		string = string + str(features[x]) + ' '
# 	# go through dictionary and add each element in one line e.g 0 0 1 2
# 	string = string + '\n'

final_features=dict()

print "Checking freq>5"
for i in features_5:
	if features_5[i]>=0: 	
		final_features[i]=0

### Add more features to dictionary
# Message length - number of characters
# final_features['num_chars']=0
# Message length - number of words
# final_features['num_words']=0
# Number of nonalphanumeric characters
# final_features['num_nonalpha_chars']=0
# Presence/number of question words (who what where when how why which) appearing at beginning of sentence
# final_features['num_question_words']=0
# Presence of question mark at end of sentence
# final_features['question_mark']=0

print "Getting modified vectors"
countf=0
for filename in glob.glob('Analysis/_a/*.txt'):
	# print count
	countf = countf+1
	print countf, filename

	feature_vectors_binary_filename.write(str(filename))
	feature_vectors_binary_filename.write('\n')
	# feature_vectors_binary_labels.write(str(emails_labels[filename[9:-4]]))
	# feature_vectors_binary_labels.write('\n')

	for f in final_features:
		final_features[f] = 0

	count = count + 1
	text = open(filename)
	# print filename
	text_body = text.read()
	# text_body=unicode(text_body)

	# text_body=text_body.encode('ascii',errors='ignore')

	text_body = re.sub(r'[^\x00-\x7F]',' ', text_body)

	text_body = text_body.lower()	

	text_body = re.sub(r'[\d]+[st|nd|rd|th]', '__NUM__', text_body)
	text_body = re.sub(r'[\d]*[,-:.][\d]+', '__NUM__', text_body)
	text_body = re.sub(r'[\d]+', '__NUM__', text_body)


	token_lower_case=nltk.word_tokenize(text_body.lower())
	trigrams=ngrams(token_lower_case,3)

	for trigram in trigrams:
		trigram = str(trigram)
		if trigram in final_features:
			# final_features[trigram] = final_features[trigram] + 1		
			final_features[trigram] = 1

	# Message length - number of characters
	# final_features['num_chars']=len(text_body)

	# Message length - number of words
	# text_body_split = text_body.split()
	# final_features['num_words'] = len(text_body_split)

	# Number of nonalphanumeric characters
	# letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
	# count_nonalpha = 0
	# for c in text_body:
		# if c in letters: count_nonalpha = count_nonalpha - 1
	# count_nonalpha = len(text_body) - count_nonalpha
	# final_features['num_nonalpha_chars']=count_nonalpha/len(text_body_split)

	# Presence/number of question words (who what where when how why which) appearing at beginning of sentence
	# question_words=['could', 'would', 'who','what','where','when','why','how','which','can','may']
	# text_body_split = text_body.split()
	# count_question_words=0
	# for t in text_body_split:
		# if t in question_words: count_question_words = count_question_words + 1
	# final_features['num_question_words']=count_question_words/len(text_body_split)

	# Presence of question mark at end of sentence	
	# final_features['question_mark']=text_body.count('?')/len(text_body.split('\n'))


	string = ''
	for x in final_features:
		string = string + str(final_features[x]) + ' '
	# go through dictionary and add each element in one line e.g 0 0 1 2
	string = string + '\n'

	feature_vectors_binary.write(string)	########################################


