
import pandas as pd

def colour_dtype(val):
    a= 3
    b= 3.0
    c= 'str'

    int_types = type(a)
    float_types = type(b)
    object_types = type(c)
    if type(val) == int_types:
        return 'background-color: red'
    elif type(val) == float_types:
        return 'background-color: green'
    else:
        return 'background-color: orange'
    
def get_mem_usage(obj):
    col_num = obj.shape[1]
    mean_usage_bytes = obj.memory_usage(deep=True).mean()
    sum_usage_bytes = obj.memory_usage(deep=True).sum()
    mean_usage_mb = mean_usage_bytes/1024**2
    sum_usage_mb = sum_usage_bytes/1024**2
    print("Average memory usage for {} column(s): {:03.2f} MB".format(col_num, mean_usage_mb))
    print("Total memory usage for {} column(s): {:03.2f} MB".format(col_num, sum_usage_mb))