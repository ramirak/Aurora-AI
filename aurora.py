import os
from AI.classify import init_classification, predict_file
from Inpsect.autopsy import get_dlls, pe_load


def init():
    if os.path.isfile('Imgs/logo'):
        with open('Imgs/logo', 'r') as f:
            print(f.read())
        input("\nPress enter to start\n > ")
        feature_indexes = [67,14,1,7,157,160,183]
        w = init_classification(feature_indexes)
        scan(w, feature_indexes)


def scan(w, feature_indexes):
    features = []    
    with open("Data/features") as f:
        features = f.read().split(",")
    pe = pe_load("browser.dll")
    if pe:
        func_list = get_dlls(pe,True)[1][0]
        file_features = [ 0 for i in range(1002)]
        for f in func_list:
            if f in features:
                file_features[features.index(f)] = 1  
        predict_file(file_features, feature_indexes, w)

init()