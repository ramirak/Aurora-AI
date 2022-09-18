import math

def train_test_split(x, y, test_ratio):
    x_train, y_train, x_test, y_test = list(), list(), list(), list()
    train_size = math.floor(len(y) * test_ratio)
    
    for i in range(len(y)):
        if i < train_size:
            x_train.append(x[i])
            y_train.append(y[i])
        else:
            x_test.append(x[i])
            y_test.append(y[i])
            
    return x_train, y_train, x_test, y_test


def k_fold_split(x, y, k, split_num):
    cur_fold_x_train, cur_fold_y_train, cur_fold_x_validation, cur_fold_y_validation = list(), list(), list(), list()
    validation_size = len(y) / k
    
    for i in range(len(y)):
        if  i >= split_num * validation_size and i < (split_num + 1) * validation_size :
            cur_fold_x_validation.append(x[i])
            cur_fold_y_validation.append(y[i])    
        else:
            cur_fold_x_train.append(x[i])
            cur_fold_y_train.append(y[i])
    
    return cur_fold_x_train, cur_fold_y_train, cur_fold_x_validation, cur_fold_y_validation
    
    