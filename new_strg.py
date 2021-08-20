import get_data as gd
import pandas_ta as ta
import time


df = gd.get_klines("BTCUSDT", "1h", "24 hours ago UTC+1")
data = df.ta.vp(close = df["Close"], volume = df["Volume"], width=10)
high_vols = []
for i in data["total_Volume"].index:
    high_vols.append(data["total_Volume"][i])

high_vol_1 = max(high_vols)
high_vols.remove(high_vol_1)
high_vol_2 = max(high_vols)
high_vols.remove(high_vol_2)
high_vol_3 = max(high_vols)

#print(high_vol_1, high_vol_2, high_vol_3)





for i in data.index:
    if data["total_Volume"][i] == high_vol_1:
        #print(data["low_Close"][i], data["high_Close"][i],  "first hvn")
        mean_fst_hvn = data["mean_Close"][i]
        low_Close_fst = data["low_Close"][i]
        high_Close_fst = data["high_Close"][i]

    if data["total_Volume"][i] == high_vol_2:
        #print(data["low_Close"][i], data["high_Close"][i], "second hvn")
        mean_snd_hvn = data["mean_Close"][i]
        low_Close_snd = data["low_Close"][i]
        high_Close_snd = data["high_Close"][i]

    if data["total_Volume"][i] == high_vol_3:
        #print(data["low_Close"][i], data["high_Close"][i], "third hvn")
        mean_trd_hvn = data["mean_Close"][i]
        low_Close_trd = data["low_Close"][i]
        high_Close_trd = data["high_Close"][i]

fst = 0
snd = 0
trd = 0
for i in df.index:
    close = df["Close"][-1]
    if df["Close"][i] >= low_Close_fst and df["Close"][i] <= high_Close_fst and fst == 0:
        pc = ((close / mean_fst_hvn) - 1) * 100
        print("first hvn ", pc)
        fst = 1

    if df["Close"][i] >= low_Close_snd and df["Close"][i] <= high_Close_snd and snd == 0:
        pc = ((close / mean_snd_hvn) - 1) * 100
        if pc <= 4:
            print("buy now @ ", close)
        #print("second hvn ", pc)
        snd = 1

    if df["Close"][i] >= low_Close_trd and df["Close"][i] <= high_Close_trd and trd == 0:
        pc = ((close / mean_trd_hvn) - 1) * 100
        print("third hvn ", pc)
        trd = 1
