import AI.cost_functions
from AI.data_split import train_test_split , k_fold_split
from AI.gradient_descent import gradient_descent
import csv, json, os


config_file_name = "Data/ai.conf"
## First make sure to load the config file
file = None
if os.path.isfile(config_file_name):
    file = open(config_file_name, "r")
else:
    print("No config file found")
    exit(-1)
config = json.load(file)


def prep_data():
    with open(config["data_path"], newline='') as f:
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


def train(x_train, y_train, x_test, y_test):
    log_reg = AI.cost_functions.log_reg_penalty
    x, w = gradient_descent(log_reg,x_train,y_train,[1,1,1,1], config["learning_rate"], config["obj_tol"], config["param_tol"], config["max_iter"])
    scan(x_test, y_test, w)


def scan(x_test, y_test, w):
    preditctions = AI.cost_functions.predict_log_reg(x_test,y_test,w, config["classify_threshold"])
    y_pred = [pred[0] for pred in preditctions]
    count = 0
    right = 0
    for i in y_pred:
        #print("Case " + str(count) + ": Prediction: " + str(i) + ", Real value: " + str(y_test[count][0])) 
        if str(i) == str(y_test[count][0]):
            right+=1
        count+=1
    print("Malware identification success: % " + str((right / count) * 100))


def init():
    allData = prep_data()
    feature_indexes = [1,2,3,4]
    x = get_features(allData, feature_indexes)
    y = get_features(allData, [1001])
    x_train, y_train, x_test, y_test = train_test_split(x, y, config["test_ratio"])
    train(x_train, y_train, x_test, y_test)

#    new_data,y = shuffle(new_data,y)

init()
    

