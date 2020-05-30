import numpy as np
class NMF():
    def __init__(self, k=10, tol=1e-3,max_iter=200,fill=3):
        self.k=k #行列分解幅
        self.tol=tol #収束の基準(誤差の減少率)
        self.max_iter=max_iter  #重み更新の最大回数
        self.fill=fill #値なし要素の保管値
        self.error = 10000000000 #誤差
        self.ex_error = 100000000000 #1ステップ前の誤差


    def fit(self, aX):
        if (max(aX.shape[0], aX.shape[1]) < self.k):
            print("size k error")
            exit()
        # Q,Pは学習する行列(初期値は乱数)
        self.X = np.copy(aX)
        self.W = np.random.rand(self.k, self.X.shape[0])
        self.H = np.random.rand(self.k, self.X.shape[1])

        for i in range(self.max_iter):
            # self.__loglikelihood()
            self.__error()
            # 二乗誤差出力
            print("step:" + str(i) + " 損失誤差減少率:" + str(1- (self.error / self.ex_error)))
            # 誤差の減少率がself.tol以下になったら収束とみなす
            if (abs(1- (self.error/self.ex_error)) < self.tol):
                print("収束，"+"二乗誤差:"+str(self.error))
                return np.dot(self.W.T, self.H)
            self.__update()

            self.ex_error = self.error

        print("iter終了，"+"二乗誤差:"+str(self.error))
        return np.dot(self.W.T, self.H)

    # 誤差計算(値が入っている場所のみ)
    def __error(self):
        tTemp = self.X - np.dot(self.W.T, self.H)
        tTemp[np.isnan(tTemp)] = 0
        self.error =np.linalg.norm(tTemp,'fro')**2
        return self.error

    # 重み更新
    def __update(self):
        tTemp = self.X
        tTemp[np.isnan(tTemp)] = self.fill
        for k in range(self.k):
            tXHt = np.dot(tTemp, self.H.T)
            for i in range(self.W.shape[1]):
                tWtHHt = np.dot(np.dot(self.W.T, self.H), self.H.T)
                self.W[k, i] = self.W[k, i] * (tXHt[i, k] / tWtHHt[i, k])
                    
            tWtX = np.dot(self.W, tTemp)
            for u in range(self.H.shape[1]):
                tWWtH = np.dot(np.dot(self.W,self.W.T), self.H)
                self.H[k, u] = self.H[k, u] *(tWtX[k, u] / tWWtH[k, u])            