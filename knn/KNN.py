
#coding=utf-8
from numpy import *
import operator
#测试样本	6.3,3.3,6.0,2.5,Iris-virginica
def filere():
	filename = 'UCI-Iris.txt' # txt文件和当前脚本在同一目录下，所以不用写具体路径

	trains = []
	labels = []
	tset = []
	with open(filename, 'r') as file_to_read:
		while True:
			lines = file_to_read.readline() # 整行读取数据
			if not lines:
				break
				pass
			#ta1,ta2,ta3,ta4,tlabels = [float(i) for i in lines.split(',',5)] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
			ta1,ta2,ta3,ta4,tlabels = [i for i in lines.split(',',5)]

			'''
			a1.append(float(ta1))  # 添加新读取的数据
			a2.append(float(ta2))
			a3.append(float(ta3))
			a4.append(float(ta4))
			'''

			trains.append([float(ta1),float(ta2),float(ta3),float(ta4)])
			labels.append(tlabels)
			pass
		group = array(trains) # 将数据从list类型转换为array类型。
		tests = [6.3,3.3,6.0,2.5]
		return  group,labels,tests

'''
def createDataSet():
    group = array([[1.0, 0.9], [1.0, 1.0], [0.1, 0.2], [0.0, 0.1]])
    labels = ['A','A','B','B']
    return group,labels
'''

def knn(trains,label,tests,k):
	
	tsize=trains.shape[0]
	tnum=(tile(tests,(tsize,1))-trains) ** 2
	dist=tnum.sum(axis=1) ** 0.5

	distsort=dist.argsort()
	count={}

	for i in range(k):
		tclass=label[distsort[i]]
		count[tclass]=count.get(tclass,0)+1

	return max(count)	



def main():
    #group,labels = createDataSet()

    group,labels,tests = filere()

    t = knn(group,labels,tests,3)
    print (t)
    
if __name__=='__main__':
    main()