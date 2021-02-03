import pandas as pd
from models.Trading import TechnicalAnalysis
from models.CoinbaseProAPI import PublicAPI

api = PublicAPI()
data = api.getHistoricalData('BTC-GBP', 3600)

ta = TechnicalAnalysis(data)
ta.addAll()
#ta.addChangePct()
#ta.addCMA()
#ta.addSMA(20)
#ta.addSMA(50)
#ta.addSMA(200)
#ta.addEMA(12)
#ta.addEMA(26)
#ta.addRSI(14)
#ta.addMACD()
#ta.addOBV()
#ta.addEMABuySignals()
#ta.addMACDBuySignals()

print (ta.getDataFrame())
print (ta.getDataFrame().dtypes)
print (ta.supportResistanceLevels())
print (ta.seasonalARIMAModelFittedValues())