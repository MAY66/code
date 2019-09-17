from string import punctuation
import os
import sys, getopt


def countFileWords(filename):
def processLine(line,wordCounts):

        line = replaceLine(line)
        words = line.split()
        for word in words:
            if word in wordCounts:
                wordCounts[word]+=1
            else:
                wordCounts[word]=1
                
    def replaceLine(line):
        for ch in '\r .,"' :
            line = line.replace(ch,' ')
        return line
  
    def main():
        infile=open(filename,'r')
        count=100
        words=[]
        data=[]
    
        wordCounts={}
        for line in infile:
            processLine(line.lower(), wordCounts)#这里line.lower()的作用是将大写替换成小写，方便统计词频
        pairs = list(wordCounts.items())
      
        print("total : %d\n"% len(pairs))
    
        items = [[x,y]for (y,x)in pairs]
        items.sort()
       
        for i in range(len(items) - 1,  -1 , -1):
            print(items[i][1] + "\t" + str(items[i][0]))
            data.append(items[i][0])
            words.append(items[i][1])
        infile.close()
 
    if __name__ == '__main__':
        main()
        
def countFileWords(inputfile):

    import functools
    
    def readFile(file_name):
        y = []
        with open(file_name, 'r',encoding="utf-8") as f:
            x=f.readlines()
        for line in x:
            y.extend(line.split())
        word_list2 = []

        for word in y:
            # last character of each word
            word1 = word

            # use a list of punctuation marks
            while True:
                lastchar = word1[-1:]
                if lastchar in [",", ".", "!", "?", ";", '"',"-","*","%"]:
                    word2 = word1.rstrip(lastchar)
                    word1 = word2
                else:
                    word2 = word1
                    break

            while True:
                firstchar = word2[0:]
                if firstchar in [",", ".", "!", "?", ";", '"',"-","*","%"]:
                    word3 = word2.lstrip(firstchar)
                    word2 = word3
                else:
                    word3 = word2
                    break
                    # build a wordList of lower case modified words
            word_list2.append(word3)
          
        #统计词频
        tf = {}
        for word in word_list2:
            word = word.lower()
                # print(word)
            word = ''.join(word.split())
            if word in tf:
                tf[word] += 1
            else:
                tf[word] = 1
        return tf

    def get_counts(words):
        tf = {}
        for word in words:
            word = word.lower()
            # print(word)
            word = ''.join(word.split())
            if word in tf:
                tf[word] += 1
            else:
                tf[word] = 1

    def merge2(dic1, dic2):
        from collections import Counter
        counts = Counter(dic1) + Counter(dic2)
        return counts
    
    #获得前n个最热词和词频
    def top_counts(word_list,n=10):
        value_key_pairs = sorted([(count, tz) for tz, count in word_list.items()],reverse=True)
        return value_key_pairs[:n]
        # print(value_key_pairs[:n])

    if __name__ == '__main__':

        file_list = [inputfile]
        cc=map(readFile,file_list)
        word_list = functools.reduce(merge2,cc)
        top_counts=top_counts(word_list)
        # print(top_counts)
        print("total : %d\n"% len(word_list))
        for word in top_counts[0:10]:
            print("{0:10}{1}".format(word[1], word[0]))
              
def getFileName(folderName):
	path = os.listdir(os.getcwd())
	folderList = []
	for p in path:
		if os.path.isdir(p):
			folderList.append(p)

	textFolder = folderName
	fileNameList = []
	for folder in folderList:
		if textFolder == folder:
			path1= os.listdir(folder)#该文件夹下所有文件建成列表
			for i in path1:
				if os.path.splitext(i)[1] == '.txt':
					fileNameList.append(os.path.splitext(i)[0])
	
	#print(fileNameList)
	for filenames in fileNameList:
		#filename = input()
		#if filename == filenames:
		print(filenames)
		countFileWords(filenames + ".txt") 
		print("----")
def countWordsFrequency(text):
	for ch in '\r .,"':
		text = text.replace(ch,' ')
	list1 = text.replace('\n',' ').lower().split()
	list2 = list(set(list1) ) 
	print("total  " + str(len(list2)))
	print("\n")
	dir1 = {} 
	for str1 in list1:
		if str1 != ' ':
			if str1 in dir1.keys():
				dir1[str1] = dir1[str1] + 1
			else:
				dir1[str1] = 1
	dir2 = sorted((dir1).items(),key = lambda x:x[1],reverse = True) # 按照频数排序
	if (len(dir2) > 30):
		count = 10
	else:
		count = len(dir2)
	for x in range(0,count):
		print('%-10s %-10s' % (dir2[x][0],dir2[x][1]))
            
def main(argv):
	if sys.argv[1] == '-h':
		#print(sys.argv[1])
		print ('test.py -i -s filename.txt')
		sys.exit()
	elif sys.argv[1]=="-s":
		if(len(sys.argv)==3):
			#print(sys.argv)
			countFileWords(sys.argv[2])
		else:
			#print(sys.argv)
			redirect_words = sys.stdin.read()
			#print(redirect_words)
			countWordsFrequency(redirect_words)
			#print(redirect_words)
			#print("lalala")	
	elif str(os.path.exists(sys.argv[1]))=='True':
		#print(sys.argv[1])
		getFileName(sys.argv[1])
	else:
		inputfile=sys.argv[1]+'.txt'
		#print(inputfile)
		countFileWords(inputfile)
if __name__ == "__main__":
	main(sys.argv[1:])
