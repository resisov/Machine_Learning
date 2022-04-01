#!/bin/python3
import numpy as np

def npyReader(directory,tuplelist,variable): ##(arr_like, arr_like, str)
	count = 0
	outputlist = []
	for f in tuplelist:
		outputlist.append(np.array(np.load(""+ directory +"/"+ str(f) +"_nTuple.npy",allow_pickle=True)[()][''+ variable +'']))
		count+=1
	outputlist = np.array(outputlist)
	return outputlist

def npyLoader(directory, tuplelist)
	outputlist = []
	for f in tuplelist:
		outputlist.append(np.load(""+ directory +"/"+ str(f) +"_nTuple.npy",allow_pickle=True)[()]
	outputlist = np.array(outputlist)
	return outputlist

def npyMoreobj(directory,tuplelist,variable,idx):
	outputlist = []
	for f in tuplelist:
		outputlist.append(np.array(np.load(""+ directory +"/"+ str(f) +"_nTuple.npy",allow_pickle=True)[()][''+ variable +''][:,idx]))
	outputlist = np.array(outputlist)
	return outputlist

def concatArray(tuplelist,start,stop):
	out = np.concatenate((tuplelist[start:stop]))
	return out



def mcNormalizer(tuplelist,genevtlist,xseclist,lumi):
	normed_set = []
	for i in range(len(tuplelist)):
		normed_set.append(np.ones(tuplelist[i].shape)*xseclist[i]*lumi/genevtlist[i])
	return normed_set

def mcReweight(tuplelist,sflist):
	output = []
	for i in range(len(tuplelist)):
		output.append(tuplelist[i]*sflist[i])
		print(tuplelist[i])
		print(sflist[i])
		print(output[i])
	return output

def setEdge(start,stop,step):
	edge = np.arange(start,stop+(step/2.),step)
	return edge

def setCenter(start,stop,step):
	center = np.arange(start+(step/2.),stop+(step),step)
	return center



