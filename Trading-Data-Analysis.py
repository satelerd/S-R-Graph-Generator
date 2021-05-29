import requests
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


# ---------------------------------


#  COLECTA DE DATOS

apiKey = "W4Z9JQF3906F4B25"

# Idealmente cambiar esto a api de yahoo
# Datos del valor actual de la crypto
def dataActual(crypto):
    cryptoData = {}
    cer = (requests.get(f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={crypto.upper()}&to_currency=USD&apikey={apiKey}").json())["Realtime Currency Exchange Rate"]

    precioActual = cer["5. Exchange Rate"]
    tiempo = cer["6. Last Refreshed"]

    cryptoData.update({
        "precio actual": precioActual,
        "tiempo": tiempo,
    })

    return cryptoData

# Datos del valor en un rango de tiempo (OHLC)
# https://rapidapi.com/finance.yahoo.api/api/yahoo-finance-low-latency link de la "documentacion"
def dataDiario(crypto, intervalo, rango):
    url = f"https://yahoo-finance-low-latency.p.rapidapi.com/v8/finance/chart/{crypto.upper()}"
    querystring = {"interval":{intervalo},"range":{rango},"events":"div,split"}
    headers = {
        'x-rapidapi-key': "4393e819bamsh268b084ca3a4710p1d2e61jsn787c57e571f9",
        'x-rapidapi-host': "yahoo-finance-low-latency.p.rapidapi.com"
    }

    daily = (requests.request("GET", url, headers=headers, params=querystring).json())["chart"]["result"][0]["indicators"]["quote"][0]

    dias = {}
    diaActual = len(daily["open"])
    for i in range(diaActual):
        dias.update({
            f"dia {diaActual - i - 1}": {
                "open": daily["open"][i],
                "high": daily["high"][i],
                "low": daily["low"][i],
                "close": daily["close"][i]
            }
        })

    return dias


# ---------------------------------


# ASIGNACION DE DATOS

# Diccionario con todos los datos de BITCOIN
btc = {}
# btc.update({
#     "Actual": dataActual("btc"),
#     "Diario": dataDiario("btc-usd", "30m", "10d")
# })
# print(btc)

# Diccionario con todos los datos de ETHERIUM
eth = {}
eth.update({
    "Actual": dataActual("eth"),
    "Diario": dataDiario("eth-usd", "30m", "10d")
})
print(eth)

# Diccionario con todos los datos de BINANCE
bnb = {}
# bnb.update({
#     "Actual": dataActual("bnb"),
#     "Diario": dataDiario("bnb-usd", "30m", "10d")
# })
# print(bnb)


# ---------------------------------


# CALCULO DE PUNTAS

# btc = {'Actual': {'precio actual': '38212.59000000', 'tiempo': '2021-05-20 03:18:01'}, 'Diario': {'dia 59': {'open': 36591.3828125, 'high': 37033.96484375, 'low': 32837.07421875, 'close': 34356.25}, 'dia 58': {'open': 35271.36328125, 'high': 35271.36328125, 'low': 30681.49609375, 'close': 32061.552734375}, 'dia 57': {'open': 32309.6953125, 'high': 35276.90625, 'low': 32309.6953125, 'close': 34286.76171875}, 'dia 56': {'open': 33795.80078125, 'high': 36855.71875, 'low': 33795.80078125, 'close': 36855.71875}, 'dia 55': {'open': 37344.1796875, 'high': 37344.1796875, 'low': 35061.87890625, 'close': 35916.109375}, 'dia 54': {'open': 35945.04296875, 'high': 35945.04296875, 'low': 34241.5078125, 'close': 35023.17578125}, 'dia 53': {'open': 35071.44921875, 'high': 35746.84765625, 'low': 34820.34375, 'close': 35724.62890625}, 'dia 52': {'open': 35642.77734375, 'high': 35642.77734375, 'low': 34824.16015625, 'close': 34988.4296875}, 'dia 51': {'open': 35253.296875, 'high': 37191.40625, 'low': 35253.296875, 'close': 37148.30078125}, 'dia 50': {'open': 37515.015625, 'high': 37515.015625, 'low': 36595.80859375, 'close': 37021.140625}, 'dia 49': {'open': 37041.99609375, 'high': 37734.875, 'low': 36828.828125, 'close': 36828.828125}, 'dia 48': {'open': 36916.39453125, 'high': 37472.61328125, 'low': 36683.5859375, 'close': 37472.61328125}, 'dia 47': {'open': 37637.28125, 'high': 37807.4453125, 'low': 37232.3046875, 'close': 37491.14453125}, 'dia 46': {'open': 37302.2421875, 'high': 37328.76171875, 'low': 36546.828125, 'close': 36546.828125}, 'dia 45': {'open': 36619.00390625, 'high': 37421.5625, 'low': 36619.00390625, 'close': 37402.22265625}, 'dia 44': {'open': 37435.93359375, 'high': 39543.9453125, 'low': 37435.93359375, 'close': 39487.88671875}, 'dia 43': {'open': 39483.16796875, 'high': 39976.32421875, 'low': 39117.22265625, 'close': 39485.60546875}, 'dia 42': {'open': 39575.73828125, 'high': 40340.96484375, 'low': 39575.73828125, 'close': 40113.5234375}, 'dia 41': {'open': 39968.9765625, 'high': 40367.0546875, 'low': 39920.23828125, 'close': 40143.2734375}, 'dia 40': {'open': 40059.33203125, 'high': 40059.33203125, 'low': 39249.91796875, 'close': 39249.91796875}, 'dia 39': {'open': 39323.59765625, 'high': 39726.7890625, 'low': 39076.61328125, 'close': 39651.93359375}, 'dia 38': {'open': 39475.48046875, 'high': 39669.484375, 'low': 38352.55078125, 'close': 38513.453125}, 'dia 37': {'open': 38441.18359375, 'high': 38663.0390625, 'low': 37975.375, 'close': 38658.76953125}, 'dia 36': {'open': 38568.96875, 'high': 38827.09765625, 'low': 38002.7890625, 'close': 38002.7890625}, 'dia 35': {'open': 37859.4375, 'high': 38262.8515625, 'low': 37782.95703125, 'close': 38145.59375}, 'dia 34': {'open': 38109.453125, 'high': 38704.17578125, 'low': 38109.453125, 'close': 38704.17578125}, 'dia 33': {'open': 38711.265625, 'high': 38962.34765625, 'low': 38260.24609375, 'close': 38724.68359375}, 'dia 32': {'open': 38647.77734375, 'high': 38946.1875, 'low': 38303.19921875, 'close': 38946.1875}, 'dia 31': {'open': 39144.81640625, 'high': 39413.78125, 'low': 38976.0625, 'close': 39413.78125}, 'dia 30': {'open': 39353.5859375, 'high': 40066.24609375, 'low': 39353.5859375, 'close': 39786.87109375}, 'dia 29': {'open': 39818.49609375, 'high': 39818.49609375, 'low': 39202.8828125, 'close': 39202.8828125}, 'dia 28': {'open': 39160.6328125, 'high': 39249.58203125, 'low': 38471.30078125, 'close': 38723.42578125}, 'dia 27': {'open': 38494.484375, 'high': 38734.4296875, 'low': 38119.58203125, 'close': 38402.41796875}, 'dia 26': {'open': 38298.609375, 'high': 38741.64453125, 'low': 37849.48828125, 'close': 37849.48828125}, 'dia 25': {'open': 37783.4921875, 'high': 38033.6015625, 'low': 37174.859375, 'close': 37730.44140625}, 'dia 24': {'open': 37731.27734375, 'high': 38680.44921875, 'low': 37731.27734375, 'close': 38680.44921875}, 'dia 23': {'open': 38949.26171875, 'high': 38949.26171875, 'low': 38713.02734375, 'close': 38754.5703125}, 'dia 22': {'open': 38832.7578125, 'high': 39496.78125, 'low': 38382.42578125, 'close': 39485.9140625}, 'dia 21': {'open': 39526.375, 'high': 39526.375, 'low': 38950.44921875, 'close': 38954.8125}, 'dia 20': {'open': 39006.1328125, 'high': 39397.90625, 'low': 39006.1328125, 'close': 39397.90625}, 'dia 19': {'open': 39466.0546875, 'high': 39505.0859375, 'low': 39135.421875, 'close': 39317.09765625}, 'dia 18': {'open': 39169.3828125, 'high': 39196.1640625, 'low': 37975.50390625, 'close': 37975.50390625}, 'dia 17': {'open': 37968.3046875, 'high': 38217.328125, 'low': 37907.09375, 'close': 37985.17578125}, 'dia 16': {'open': 37901.484375, 'high': 38378.59375, 'low': 37901.484375, 'close': 37991.23046875}, 'dia 15': {'open': 37692.71875, 'high': 37692.71875, 'low': 36925.83984375, 'close': 37002.44140625}, 'dia 14': {'open': 36753.66796875, 'high': 37882.58984375, 'low': 36753.66796875, 'close': 37882.58984375}, 'dia 13': {'open': 37903.6796875, 'high': 38161.1328125, 'low': 37152.92578125, 'close': 37152.92578125}, 'dia 12': {'open': 37078.4453125, 'high': 37078.4453125, 'low': 35922.09375, 'close': 35922.09375}, 'dia 11': {'open': 35613.703125, 'high': 35957.37890625, 'low': 35050.6171875, 'close': 35662.51953125}, 'dia 10': {'open': 35822.3984375, 'high': 36686.82421875, 'low': 35726.76953125, 'close': 35920.98828125}, 'dia 9': {'open': 36125.125, 'high': 37360.7890625, 'low': 36125.125, 'close': 37360.7890625}, 'dia 8': {'open': 37260.08203125, 'high': 37359.9453125, 'low': 36933.40625, 'close': 36984.0078125}, 'dia 7': {'open': 36967.69921875, 'high': 37136.19140625, 'low': 36562.9921875, 'close': 37118.015625}, 'dia 6': {'open': 37044.32421875, 'high': 38010.6796875, 'low': 37044.32421875, 'close': 37962.48828125}, 'dia 5': {'open': 38061.0859375, 'high': 38061.0859375, 'low': 37787.6484375, 'close': 37972.87109375}, 'dia 4': {'open': 37921.63671875, 'high': 38170.953125, 'low': 37623.03515625, 'close': 37705.015625}, 'dia 3': {'open': 37867.84765625, 'high': 38255.17578125, 'low': 37858.6875, 'close': 38255.17578125}, 'dia 2': {'open': 38224.54296875, 'high': 38612.1171875, 'low': 38089.79296875, 'close': 38612.1171875}, 'dia 1': {'open': 38526.1015625, 'high': 38526.1015625, 'low': 38486.28515625, 'close': 38486.28515625}, 'dia 0': {'open': 38329.09765625, 'high': 38329.09765625, 'low': 38329.09765625, 'close': 38329.09765625}}}
crypto = eth

# btc
if crypto == btc:
    recta = 30000
    grosor = 500
    maximo = 65100

# eth
elif crypto == eth:
    recta = 1600
    grosor = 50
    maximo = 3500

#bnb
elif crypto == bnb:
    recta = 200
    grosor = 7
    maximo = 450


while recta < maximo:
    contCumbres = 0
    contValles = 0

    for dia in range(len(crypto["Diario"])):
        if crypto["Diario"][f"dia {dia}"]["open"] == None:
            crypto["Diario"][f"dia {dia}"]["open"] = 0
        if recta < crypto["Diario"][f"dia {dia}"]["open"] < recta + grosor:

            if dia == 0 or dia == len(crypto["Diario"])-1:
                continue

            # si el dato es mas grande que el dato anterior y el proximo, entonces es cumbre
            if crypto["Diario"][f"dia {dia - 1}"]["open"] < crypto["Diario"][f"dia {dia}"]["open"] > crypto["Diario"][f"dia {dia + 1}"]["open"]:
                contCumbres += 1

            elif crypto["Diario"][f"dia {dia - 1}"]["open"] > crypto["Diario"][f"dia {dia}"]["open"] < crypto["Diario"][f"dia {dia + 1}"]["open"]:
                contValles += 1

    print("recta: ", recta)
    print("cumbres: ", contCumbres)
    print("valles: ", contValles)
    print()

    recta += grosor
    continue
