
def write_data(df,loc):
    df.to_csv(loc+'.csv',index=False)