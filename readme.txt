1. Experimental environment:
	notebook
	pycharm
	keras 2.2.4
	tensorflow 1.13.1
2. Data sources:
	2.1 metabolite database: HMDB
	2.2 protein database: UniProt
	2.3 protein metabolite interaction (PMI) database: http://easybioai.com/PMIDB
3. Experiment
	3.1 data acquisition
		① Download the PMI data set from pmidb
		② Find four metabolites in HMDB and download their SDF files
		③ Find the protein in the data set in UniProt and download its file
		④ Obtaining protein-protein interaction data set from string
	3.2 data preprocessing
		① In PMI data set, the data labeled "human" is reserved, others are deleted, and the data is divided into positive and negative sets by "true" and "false" labels.
		② If a certain line of protein information in the data set cannot be found in UniProt, delete this line, a total of 30 lines will be deleted, and the remaining 14120 lines will be deleted. Positive set 3859 lines, negative set 10261 lines
		③The 1d2d structure and chemical fingerprint of the metabolites were calculated by PaDEL-Descriptor,They are regarded as metabolite characteristics, and each metabolite is characterized by 2325 dimensions
		④ Blast was used to calculate the similarity between each protein and other proteins, and the similarity score between each protein and other proteins was obtained. As a protein feature, each protein feature has 6354 dimensions
		⑤ Combined with the positive and negative sets, the protein and metabolite related features mentioned in each line were spliced to obtain the feature matrix, with the specification of 14120 * 8679
		(this data link is: https://pan.baidu.com/s/1DRTwANVW3VQiGjUfRU8SyA , extraction code: e614)
		⑥ PCA dimension reduction of the feature matrix is carried out, and 99% features are reserved for the feature matrix. The new feature matrix specification is 14120 * 3390 (see the code: PCA.py )
	3.3 comparative experiment
		① Carry out 10 cross validation on the above characteristic matrix (see the code: DNN.ipynd )
		② DNN, SVM, MLP and RF are used for training prediction, and the results are obtained