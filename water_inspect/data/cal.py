"""
fetch中取得数据
进行计算
返回models存入数据库
"""

import numpy as np
import math
import water_inspect.config

history_data = water_inspect.config.result
history_data = [132, 92, 118, 130, 187, 207]
# m = int(input())
# print(type(m))


class GM:
    def __init__(self):    #history_data:your input list,  m:the year you want to perdict
        self.history_data = history_data
        self.n = len(self.history_data)
        self.X0 = np.array(self.history_data)
        # 累加生成
        self.history_data_agg = [sum(self.history_data[0:i + 1]) for i in range(self.n)]
        self.X1 = np.array(self.history_data_agg)

    def mat_cal(self):
        # 计算数据矩阵B和数据向量Y
        n, X0, X1= self.n, self.X0, self.X1
        B = np.zeros([n - 1, 2])
        Y = np.zeros([n - 1, 1])
        for i in range(0, n - 1):
            B[i][0] = -0.5 * (X1[i] + X1[i + 1])
            B[i][1] = 1
            Y[i][0] = X0[i + 1]
        # 计算GM(1,1)微分方程的参数a和u
        A = np.linalg.inv(B.T.dot(B)).dot(B.T).dot(Y)
        self.a = A[0][0]
        self.u = A[1][0]
        # 建立灰色预测模型
        XX0 = np.zeros(n)
        XX0[0] = X0[0]
        for i in range(1, n):
            XX0[i] = (X0[0] - self.u / self.a) * (1 - math.exp(self.a)) * math.exp(-self.a * (i));
        # 模型精度的后验差检验
        e = 0  # 求残差平均值
        for i in range(0, n):
            e += (X0[i] - XX0[i])
        e /= n
        # 求历史数据平均值
        aver = 0;
        for i in range(0, n):
            aver += X0[i]
        aver /= n
        # 求历史数据方差
        s12 = 0;
        for i in range(0, n):
            s12 += (X0[i] - aver) ** 2;
        s12 /= n
        # 求残差方差
        s22 = 0;
        for i in range(0, n):
            s22 += ((X0[i] - XX0[i]) - e) ** 2;
        s22 /= n
        # 求后验差比值
        C = s22 / s12
        # 求小误差概率
        cout = 0
        for i in range(0, n):
            if abs((X0[i] - XX0[i]) - e) < 0.6754 * math.sqrt(s12):
                cout = cout + 1
            else:
                cout = cout
        P = cout / n
        return C, P

    def perdict(self, C, P, m):
        # 预测精度为 一级
        n, X0, u, a = self.n, self.X0, self.u, self.a
        f = np.zeros(m)
        if C < 0.35 and P > 0.95:
            print("1")
            # 请输入需要预测的年数
            for i in range(0, m):
                f[i] = (X0[0] - u / a) * (1 - math.exp(a)) * math.exp(-a * (i + n))
        # 预测精度为 二级
        elif P > 0.80 and C < 0.45:
            print("2")
            # 请输入需要预测的年数
            for i in range(0, m):
                f[i] = (X0[0] - u / a) * (1 - math.exp(a)) * math.exp(-a * (i + n))
        # 预测精度为 三级
        else:
            print("3")
            # 请输入需要预测的年数
            for i in range(0, m):
                f[i] = (X0[0] - u / a) * (1 - math.exp(a)) * math.exp(-a * (i + n))
        return f


# gm = GM()
# Diff, Prb = gm.mat_cal()
#
# res = []
# #to access res's length, must use res.size
# res = gm.perdict(Diff, Prb, 1)
# length = len(res)
#
# for i in range(0, length):
#     print("asdasda%lf "%res[i])