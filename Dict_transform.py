# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 16:05:56 2018

@author: Administrator
"""
"""
#create a dict transform function : one_key:mulity_values to one_values:one_key(repeated) ; 
#one_key:one_value(repeated) to one_key:mulity_values
#one_key:mulity_values to one_values:one_key(repeated)
例如：
Dict_onebyone结果：
{'name': ['jing', 'ming'], 'str': '你好', 'surname': ['han', 'li']}
转换为：
{'han': 'surname',
 'jing': 'name',
 'li': 'surname',
 'ming': 'name',
 '你好': 'str'}
Dict_onebymul结果为反向转换。
"""

def Dict_onebyone(dict_0):
    d = {}
    for k,v in dict_0.items():
        if type(v) is str:
            dict_0[k] = [v]
            d[v]=k
        else:
            for vv in v:
                d[vv]=k
    return d
    
#one_key:one_value(repeated) to one_key:mulity_values
def Dict_onebymul(dict_0):
    d = {}
    for v,k in dict_0.items():
        if k not in d:
            d[k] = v
        else :
            d[k] =[d[k]]
            d[k].append(v)
    return d

