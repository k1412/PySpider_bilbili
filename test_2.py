import pandas as pd 



for vmid in range(1,100):
    vmid_list = pd.Series(vmid)       #保存vmid
    vmid_list.to_csv('vmid_list.csv',mode='a',index=False,header= False)


