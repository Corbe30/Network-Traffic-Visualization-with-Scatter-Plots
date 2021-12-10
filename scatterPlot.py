import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

plt.style.use('seaborn')

location = 'E:/Shashank/Jaypee/sem5/CNS Lab/Project/'
files = ["Hulk-NoDefense", "TCPFlood-NoDefense", "Slowloris-NoDefense", "Slowhttptest-NoDefense"]

for file in files:
    csv_location = location + file + ".csv"
    data = pd.read_csv(csv_location)

    if(file=="Hulk-NoDefense") or (file=="TCPFlood-NoDefense"):
        pktlen = data[' Bwd Packet Length Std']
    else:
        data = data[data[" Flow IAT Mean"].astype(int) < 6000000]
        pktlen = data[' Flow IAT Mean']
    
    timest = data[' Timestamp']

    colors = np.where(data[" Label"]=="BENIGN",'orange','blue')
    plt.scatter(timest, pktlen, s=15, alpha=0.6, linewidths=1, c=colors)

    plt.title('Benign attacks')
    plt.xlabel('timestamp')

    if(file=="Hulk-NoDefense") or (file=="TCPFlood-NoDefense"):
        plt.ylabel('bwd packet length standard')
    else:
        plt.ylabel('flow IAT mean')

    plt.tight_layout()
    img_location = location + file + ".png"
    plt.savefig(img_location)