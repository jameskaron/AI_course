# coding=UTF-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
import random


def gen_data():
    line_list = []
    for line in range(0, 100):
        row_list = []
        for row in range(0, 2):
            exam = random.randint(0, 100)
            row_list.append(exam)
        admitted = random.randint(0, 1)
        row_list.append(admitted)
        line_list.append(row_list)
    rl = pd.DataFrame(line_list)
    print(rl.shape)
    path = 'data' + os.sep + 'LogiReg_data.csv'
    rl.to_csv(path, index=False, sep=',')


def init_data():
    path = 'data' + os.sep + 'LogiReg_data.csv'
    pdData = pd.read_csv(path, header=None, names=['Exam 1', 'Exam 2', 'Admitted'])
    return pdData


def logi_reg():
    pdData = init_data()
    print(pdData.head())
    print(pdData.shape)

    positive = pdData[pdData['Admitted'] == 1]
    negative = pdData[pdData['Admitted'] == 0]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(positive['Exam 1'], positive['Exam 2'], s=30, c='b', marker='o', label='Admitted')
    ax.scatter(negative['Exam 1'], negative['Exam 2'], s=30, c='r', marker='x', label='Not Admitted')
    ax.legend()
    ax.set_xlabel('Exam 1 Score')
    ax.set_ylabel('Exam 2 Score')
    plt.show()


def sigmod(z):
    # print('sigmod: ', 1/(1 + np.exp(-z)))  # [0.5]
    return 1/(1 + np.exp(-z))


def draw_sigmod():
    nums = np.arange(-10, 10, step=1)
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(nums, sigmod(nums), 'r')
    plt.show()


def model(x, theta):
    # print('np.dot(x, theta.T): ', np.dot(x, theta.T))  # [0]
    return sigmod(np.dot(x, theta.T))  # [0.5]


# X是数据, y是标签, theta是参数
def cost(X, y, theta):
    left = np.multiply(-y, np.log(model(X, theta)))
    right = np.multiply(1-y, np.log(1 - model(X, theta)))
    return np.sum(left - right) / len(X)


# 平均损失
def cost_process():
    pdData = init_data()
    pdData.insert(0, 'Ones', 1)
    # orig_data = pdData.as_matrix()
    orig_data = pdData.values
    cols = orig_data.shape[1]
    X = orig_data[:, 0:cols-1]
    y = orig_data[:, cols-1:cols]
    theta = np.zeros([1, 3])
    print(X[:5])
    print(y[:5])
    print(theta)
    # print(X.shape, y.shape, theta.shape)
    print (cost(X, y, theta))


def gradient(X, y, theta):
    grad = np.zeros(theta.shape)  # [0 0 0 ]占位
    # print ('grad: ', grad)
    error = (model(X, theta) - y).ravel()
    print ('error: ', error)
    for j in range(len(theta.ravel())):
        term = np.multiply(error, X[:, j])
        print ('theta' + str(j) + ',term: ' + str(term))
        grad[0, j] = np.sum(term)/len(X)
        print ('theta' + str(j) + ',grad[]: ' + str(grad[0, j]))
    return grad


# 梯度下降
def grad_process():
    pdData = init_data()
    pdData.insert(0, 'Ones', 1)
    orig_data = pdData.values
    cols = orig_data.shape[1]
    X = orig_data[:, 0:cols - 1]
    y = orig_data[:, cols - 1:cols]
    theta = np.zeros([1, 3])
    grad_value = gradient(X, y, theta)
    print(grad_value)


# 以迭代次数停止
STOP_ITER = 0
# 迭代前和迭代后的差异值(损失之变化)
STOP_COST = 1
# 以梯度变化停止
STOP_GRAD = 2


def stop_criterion(type, value, threshold):
    # 设定三种不同的停止策略
    if type == STOP_ITER:
        return value > threshold
    if type == STOP_COST:
        return abs(value[-1] - value[-2]) < threshold
    if type == STOP_GRAD:
        return np.linalg.norm(value) < threshold

# 洗牌
def shuff_data(data):
    
# gen_data()
# logi_reg()
# draw()
# cost_process()
grad_process()