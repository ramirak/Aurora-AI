import numpy as np 
import math

def sigmoid(x):
    return 1/(1+np.exp(-x))


def log_reg_penalty(w, x, y):
    w=np.array(w,dtype=float)
    x=np.array(x,dtype=float)
    y=np.array(y,dtype=float)

    cost,gradient = 0 , 0 ;
    for i in range(len(y)):
        for j in range(len(w)):
            gradient += np.multiply(sigmoid(np.dot(np.transpose(w),x[i])) - y[i], x[i])
        cost += y[i] * np.log(sigmoid(np.dot(np.transpose(w),x[i]))) + (1-y[i])*np.log(1-sigmoid(np.dot(np.transpose(w),x[i])))      
    cost = cost / -len(y)
    gradient = gradient / len(y)
    return cost, gradient

    
def predict_log_reg(x_test,y_test, learned_w, threshold):
    x_test=np.array(x_test,dtype=float)
    y_test=np.array(y_test,dtype=float)
    learned_w=np.array(learned_w,dtype=float)
    
    predictions = []
    preds = []
    for i in range(len(y_test)):
        wx = 0
        for j in range(len(learned_w)):
            wx += learned_w[j] * x_test[i][j]
        predictions.append([sigmoid(wx),y_test[i]])   
        preds.append(sigmoid(wx))
    return [[math.floor(predictions[i][0]),predictions[i][1]] if predictions[i][0] < threshold else [math.ceil(predictions[i][0]),predictions[i][1]]  for i in range(len(y_test))]
    