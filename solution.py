import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


chat_id = 485082255 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool: 
    t_stat, p_val = ttest_ind(x, y)
    
    return p_val < 0.09
