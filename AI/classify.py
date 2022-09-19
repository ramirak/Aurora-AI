from .data_split import train_test_split , k_fold_split
from .gradient_descent import gradient_descent
import csv, json, os
from . import cost_functions
import numpy as np 


config_file_name = "./Data/ai.conf"
## First make sure to load the config file
file = None
if os.path.isfile(config_file_name):
    file = open(config_file_name, "r")
else:
    print("No config file found")
    exit(-1)
config = json.load(file)
allData = []

def prep_data():
    with open("./Data/" + config["data_file"], newline='') as f:
        reader = csv.reader(f)
        return list(reader)


def get_features(allData,indexes):
    chosen_data = []
    for row in allData:
        new_row = []
        for i in indexes:
            new_row.append(row[i])
        chosen_data.append(new_row)
    return chosen_data


def k_split(x,y,k):
    for i in range(k):
        print("\n -------------------Fold number" + str(i) + "------------------- \n")
        train(*k_fold_split(x,y,k,i))


def train(x_train, y_train, x_test, y_test, initial_weights):
    log_reg = cost_functions.log_reg_penalty
    x, w = gradient_descent(log_reg,x_train,y_train, initial_weights, config["learning_rate"], config["obj_tol"], config["param_tol"], config["max_iter"])
    return scan(x_test, y_test, w)


def scan(x_test, y_test, w):
    preditctions = cost_functions.predict_log_reg(x_test,y_test,w, config["classify_threshold"])
    y_pred = [pred[0] for pred in preditctions]
    count = 0
    right = 0
    for i in y_pred:
        if str(i) == str(y_test[count][0]):
            right+=1
        count+=1
    print("Malware identification success: % " + str((right / count) * 100))
    return w


def init_classification(feature_indexes):
    allData = prep_data()
    x = get_features(allData, feature_indexes)
    y = get_features(allData, [1001])
    x_train, y_train, x_test, y_test = train_test_split(x, y, config["test_ratio"])
    initial_weights = [ 1 for i in range(len(feature_indexes))]
    return train(x_train, y_train, x_test, y_test, initial_weights)


def predict_file(x, indexes, w):
    x = [x]
    x = get_features(x, indexes)
    w=np.array(w,dtype=float)
    x=np.array(x,dtype=float)
    preditctions = cost_functions.predict_log_reg(x,x,w, config["classify_threshold"])
    y_pred = [pred[0] for pred in preditctions]
    get_classify_result(y_pred)


def get_classify_result(prediction):
    print("-----------------------------")
    if(prediction[0] == 0):
        print("No malware was found")
    else:
        print("Possible identified malware")
    print("-----------------------------")