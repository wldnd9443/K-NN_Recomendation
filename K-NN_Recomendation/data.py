import numpy as np
import pandas as pd
import json
from sklearn.metrics.pairwise import cosine_similarity
NO_LIST = 10

class StampDataset(object):

    def __init__(self):
        self.table1 = pd.read_excel('stamp.xlsx',0)
        self.table2 = pd.read_excel('stamp.xlsx',1)

    def get_random_stamp(self):
        return self.table1.iloc[np.random.randint(self.table1.shape[0])]

    def get_recommend_stamp(self, form_data, single_result = False):
        user_data = json.loads([key for key in form_data.keys()][0])
#        user_data = form_data
        Da = 0
        for i in range(self.table2.shape[0]):
            if self.table2.type.iloc[i]=='float':
                Da += 1
            else:
                Da += np.sum(~self.table2.iloc[i].isnull())-3

        Na = self.table1.shape[0]
        mat_a = np.zeros((Na,Da))
        idx = 0

        for i in range(self.table2.shape[0]):
            item = self.table2.iloc[i]
            question = item.question
            dtype = item.type

            if dtype == 'float':
                mat_a[:,idx] = self.table1[question]
                idx += 1

            else:
                D = np.sum(~self.table2.iloc[i].isnull())-3
                mat_tmp = np.zeros((Na,D))
                ans = self.table1[question]
                for j in range(len(ans)):
                    mat_tmp[j,ans[j]-1] = 1
                    mat_a[:,idx:idx+D] = mat_tmp
                idx += D

        mat = np.zeros((1,Da))

        idx = 0
        for i in range(self.table2.shape[0]):
            item = self.table2.iloc[i]
            question = item.question
            dtype = item.type

            if dtype == 'float':
                mat[:,idx] = user_data[question]
                idx += 1

            else:
                D = np.sum(~self.table2.iloc[i].isnull())-3
                mat_tmp = np.zeros((1,D))
                ans = user_data[question]
                mat_tmp[0,ans-1] = 1
                mat[0,idx:idx+D] = mat_tmp
                idx += D

#        from sklearn.manifold import TSNE
#        import matplotlib.pyplot as plt
#        y = TSNE(n_components=2).fit_transform(mat_a)

#        idx_tgt = np.arange(12)
#        idx_else = np.arange(12,56)
#        plt.plot(y[idx_tgt,0],y[idx_tgt,1],'.r')
#        plt.plot(y[idx_else,0],y[idx_else,1],'.b')
#        plt.show()

#        import pdb
#        pdb.set_trace()




#        import matplotlib.pyplot as plt
#        plt.imshow(mat_a)
#        plt.show()
#        distance = np.sqrt(((mat_a-mat)**2).sum(1))
#
#        if single_result == True:
#            return self.table1.iloc[np.argmin(distance)]
#        else:
#            return self.table1.iloc[np.argsort(distance)[:NO_LIST]]
        cs = cosine_similarity(mat, mat_a)
        if single_result == True:
            return self.table1.iloc[np.argmax(cs)]
        else:
            return self.table1.iloc[np.argsort(cs,reverse=True)[:NO_LIST]]


if __name__ == '__main__':
    item = {}
    item['age'] = 2
    item['tti'] = 4
    item['religion'] = 3
    item['intensity'] = 1
    item['constellation'] = 4
    item['design'] = 1
    item['price'] = 3
    item['letter'] = 2
    item['matter'] = 1
    item['western'] = 1
    item['gender'] = 2

    #item = {str(item):''}

    sd = StampDataset()
    sd.get_recommend_stamp(item, single_result = True)
    import pdb
    pdb.set_trace()
    #import pdb
    #pdb.set_trace()
    #import pandas as pd
    #table1 = pd.read_excel('stamp.xlsx',0)
    #table2 = pd.read_excel('stamp.xlsx',1)

    #import pdb
    #pdb.set_trace()
