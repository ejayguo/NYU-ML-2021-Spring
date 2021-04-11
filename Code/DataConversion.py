import numpy as np
from scipy import stats

def ConvertContinuousToBinary(array_data, height_bt, type_root):
#     print(array_data)
    N = len(array_data)
    mean_data = np.mean(array_data)
    median_data = np.median(array_data)
    min_data = np.amin(array_data)
    max_data = np.amax(array_data)
        
    ## Temporarily only accept non-negative values
    if(min_data < 0):
        return None
    
    value_root = mean_data
    if(type_root == "mean"):
        value_root = mean_data
    elif(type_root == "median"):
        value_root = median_data
        
    array_bin_data = np.empty((N,height_bt))
    
    for i_n in range(0, N):
        data = array_data[i_n]
        value_check = value_root
        bin_data = np.empty((1,height_bt))
        
        for i_height in range(0, height_bt):
            bin_i = None
            
            if(data <= value_check):
                bin_i = 0
                value_check = value_check - value_check/2
            else:
                bin_i = 1
                value_check = value_check + value_check/2
                
            bin_data[0,i_height] = bin_i
                    
#         print(array_bin_data)
        array_bin_data[i_n] = bin_data
        

#     print(array_bin_data)
    return array_bin_data

def ConvertContinuousToDiscreteK(array_data, num_bins):
    N = len(array_data)
    
    k_statistic, k_edges, array_K_data = stats.binned_statistic(array_data, array_data, bins = num_bins)

    return array_K_data