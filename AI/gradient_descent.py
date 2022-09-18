import numpy as np 

def gradient_descent(f, x , y , w, learning_rate, obj_tol, param_tol,max_iter):
    fw , gw = f(w,x,y)
    for z in range(max_iter): 
        wOld = w.copy()
        fwO = fw        
        for i in range(len(w)):
            w[i] = w[i] - learning_rate * gw[i]             
        fw, gw = f(w,x,y)
        if abs(fw - fwO) < obj_tol or np.linalg.norm(np.array(w) - np.array(wOld)) < param_tol:
            break    
    return 1, w 
