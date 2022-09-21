import os, glob
from AI.classify import init_classification, predict_file
from Inpsect.autopsy import get_dlls, pe_load


def init():
    weights_file = "Data/weights.txt"
    if os.path.isfile('Imgs/logo'):
        with open('Imgs/logo', 'r') as f:
            print(f.read())
        feature_indexes = [67,14,1,7,157,160,183]
        w = None
        choice = "-1"
        while choice == "-1":
            print("(1) Start computation")
            print("(2) Scan a file or path")
            choice = input("\n > ")
            if choice == "1":
                w = init_classification(feature_indexes)
                with open(weights_file, 'w+') as f:
                    f.write(str(w))
            elif choice == "2": 
                if os.path.isfile(weights_file):
                    with open(weights_file, 'r') as f:
                        w = f.read()
                        w = w[1:-1].split(',')
                        path = input("\nEnter file or path to scan\n > ")
                        if os.path.isfile(path):
                            scan(path, w, feature_indexes)
                        else:
                            scan_path(path + "/", w, feature_indexes)
            choice = "-1"


def scan_path(path, w, feature_indexes):
    for filename in glob.iglob(path + "**", recursive=True):
        if os.path.isfile(filename):
            if scan(filename , w, feature_indexes):
                print("Possible identified malware:\n" + filename)

       

def scan(filename ,w, feature_indexes):
    features = []
    features_file = "Data/features"  
    if os.path.isfile(features_file):  
        with open(features_file) as f:
            features = f.read().split(",")
        if os.path.isfile(features_file):
            pe = pe_load(filename)
            if pe:
                dlls = get_dlls(pe,True)
                if dlls == None:
                    return
                func_list = dlls[1][0]
                file_features = [ 0 for i in range(1002)]
                for f in func_list:
                    if f in features:
                        file_features[features.index(f)] = 1  
                return predict_file(file_features, feature_indexes, w)

init()