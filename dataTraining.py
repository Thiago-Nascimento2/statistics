import numpy as np


class DataTraining:
    def __init__(self, df):
       self.df = df

    def treatself):

        self.df.where(self.df is None).drop()

        array = np.asarray(self.df)
        #for i in range(array.shape[0]):
        #    for j in range(array.shape[1]):
        #        if array[i][j] is None:

        #print(f'df shape => {self.df.shape}')
        #self.print_data()


    def print_data(self):
        array = np.asarray(self.df)
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                print(array[i][j], end=' ')
            print()

    def test(self):
        df = self.df.dropna()
        print(df)



