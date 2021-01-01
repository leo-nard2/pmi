1. Experimental environment:
	pycharm
	keras 2.2.4
	tensorflow 1.13.1
2. Data sources:
	2.1 metabolite database: HMDB
	2.2 protein database: UniProt
	2.3 protein-protein interaction database: String
	2.4 protein metabolite interaction (PMI) database: http://easybioai.com/PMIDB
3. Experiment
	3.1 data acquisition
		① Download the PMI data set from pmidb
		② Find four metabolites in HMDB and download their SDF files
		③ Find the protein in the data set in UniProt and download its file
		④ Obtain protein-protein interaction data set from string
	3.2 workflow
		① Human-related PMIs were selected from PMI-DB. 
		② 30 proteins corresponding to PMIs can not be found in UniProt, so these 30 proteins-related PMIs were deleted. Finally, 14120 PMIs were obtained, including 3859 true PMIs, 10261 false PMIs. 
		Feature extraction:
		③The 1d2d structure and chemical fingerprint of the metabolites were calculated by PaDEL-Descriptor as the features of metabolites. (2325 dimensional feature)
		④ Obtain protein-protein interaction from String database and construct PPI network. The adjacency matrix of PPI network is the feature of all proteins. (6354 dimensional feature )
		⑤ Combine features of metabolites and proteins to obtain the features of PMIs (14120 * 8679)
		(this data link is: https://pan.baidu.com/s/1DRTwANVW3VQiGjUfRU8SyA , extraction code: e614)
		⑥ PCA was implemented to reduce the dimension of PMI features. Finally, 99% of the information is retained and the dimension of new feature is 14120 * 3390 (see the code: PCA.py ).
	3.3 comparison experiment
		Identification of PMIs:
		DNN, SVM, MLP and RF are used to identify PMIs.(10-cross validation). The source code of DNN is DNN.ipynd.
		