# from datetime import datetime
import datetime
from psx import stocks, tickers


def stocks_data(symbols, start, end):
    
    # tickers = tickers()
    data = stocks(symbols, start=start, end=end)
    documents = data.to_dict(orient='records')
    # to csv
    file_path = "data_PSX.csv"
    data.to_csv(file_path)
    return file_path

symbols = ['SILK', 'PACE','KEL', 'WTL', 'BOP','PIAA', 'FABL', 'PAEL', 'AIRLINK', 'TOMCL', 'NBPXD', 'LOADS',
           'AGLNCPS', 'SGPL', 'FPRM', 'PIM', 'SAIF', 'LOADS', 'SMCPL', 'DAAG', 'THCCL', 'BELADEF',
           'HIRATDEF', 'FIBLM', 'TRSM', 'GFIL', 'RUBYDEF', 'BNL', 'NETSOL', 'TRG', 'AGL', 'HCL','PIBTL', 'FFL', 'FCCL','BOP','SNGP', 'GHNI', 'TELE', 'GAL', 'WAVES', 'HBLXD', 'SEARL', 'CSIL', 'SNBL', 'KOSM', 'FFC', 'OCTOPUS', 'JSBL', 'LOTCHEM', 'HUBC', 'PACE', 'EFERTXD', 'TPLP', 'ASC', 'HCAR', 'AKBL', 'AVNXDXB', 'LPL', 'HUMNL', 'POWER', 'DCL', 'RPL', 'HTL', 'PAKRIXD', 'GATM', 'NCPL', 'NPL', 'ASL', 'PSO', 'BAFL', 'KAPCO', 'SILK', 'ILP', 'FLYNG', 'WAVESAPP', 'ATRL', 'SAZEWXD', 'HIRATDEF', 'CPHL', 'AGHA', 'MEBLX']

print(len(symbols), " len of symbols")
data = stocks(symbols, start=datetime.date(2024, 5, 1), end=datetime.date.today())
print(type(data),"nature of data")
print(data,"data")
documents = data.to_dict(orient='records')

# to csv
data.to_csv("data_PSX.csv")