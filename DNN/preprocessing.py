import numpy as np
import pandas as pd
import awkward as ak
import seaborn as sns
import matplotlib.pyplot as plt
import myModule

def dfMaker(inputset,features)
	for process in inputset:
		columns = features
		if process == 'Signal':
			y = np.ones(len(inputset['{0}'.format(process)]['MET_pt']))
			evt = nEventDict['Signal']
			xsec = xsecDict['Signal']
		else:
			y = np.zeros(len(inputset['{0}'.format(process)]['MET_pt']))
			evt = nEventDict[process]
			xsec = xsecDict[process]

		data = {'y':y,'Event':evt,'xsec':xsec}
		df = pd.DataFrame(data)

		for column in columns:
			df[column] = ak.to_pandas(inputset['{0}'.format(process)][column])

		lista = df.value.tolist()
		output += lista
	return output


## MC Load

filepath = "./"

mclist = [
        'Signal',
        'tt_1l',
        'tt_2l',
        'ttV'
]

mc = myModule.npyLoader(filepath, mclist)

## Arrange MC

Set = {
	'Signal' : mc[0],
	'tt_1l' : mc[1],
	'tt_2l' : mc[2],
	'ttV' : mc[3]
}

lumi = 3000000

nEventDict = {
	'Signal' : 100000,
	'tt_1l' : 1321415,
	'tt_2l' : 1563214,
	'ttV' : 1531534
}

xsecDict = {
	'Signal' : 0.0023465
	'tt_1l' : 211.5
	'tt_2l' : 40.288
	'ttV' : 0.1523
}

features = []

for d in Set['Signal'].keys():
	features.append(d)

print(features)

df = dfMaker(inputset,features)

col = ['y','Event','xsec']
cols = col + features


df = pd.DataFrame(df,columns=cols)

pd.set_option("display.max_colwidth",200)

df['weight'] = (df['xsec'] * lumi) / df['Event']

sigY = df[df['y'] == 1]['weight'].sum(axis=0, skipna = False)
bkgY = df[df['y'] == 0]['weight'].sum(axis=0, skipna = False)

sf = sigY/bkgY

target = []

for y in df['y']:
        if y == 1:
                target.append(1)
        else:
                target.append(sf)

df['SF'] = target

sigN = len(df['weight'][df['y'] == 1])
bkgN - df['weight'][df['y'] == 0].sum()

SF = sigN/bigN
print("Signal : {0}, BKG : {1}, SF : {2}".format(sigN,bkgN,SF)

df['weight'][df['y'] == 1] = 1
df['weight'][df['y'] == 0] = df['weight'][df['y'] == 0] * SF

df_weight = df['weight']

df = df.drop(['weight','SF'],axis=1)

df['weight'] = df_weight

print(df)

df_shuf = sklearn.utils.shuffle(df)

df_shuf.to_hdf('binary.h5',key = 'df',mode='w')

