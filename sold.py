import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

sold0 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202602.csv", encoding = "ISO-8859-1")
sold1 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202603.csv", encoding = "ISO-8859-1")
sold2 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202604.csv", encoding = "ISO-8859-1")
sold3 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202605.csv", encoding = "ISO-8859-1")
sold4 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202601.csv", encoding = "ISO-8859-1")
sold_2026 = pd.concat([sold0, sold1,sold2,sold3,sold4], ignore_index=True)
#sold_2026= sold_2026[sold_2026.PropertyType=='Residential']
sold5 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202401_filled.csv", encoding = "ISO-8859-1")
sold6 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202402.csv", encoding = "ISO-8859-1")
sold7 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202403_filled.csv", encoding = "ISO-8859-1")
sold8 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202404_filled.csv", encoding = "ISO-8859-1", low_memory= False)
sold9 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202405_filled.csv",encoding = "ISO-8859-1")
sold10 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202406_filled.csv", encoding = "ISO-8859-1")
sold11 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202407_filled.csv", encoding = "ISO-8859-1")
sold12 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202408.csv", encoding = "ISO-8859-1")
sold13 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202409.csv", encoding = "ISO-8859-1")
sold14 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202410.csv", encoding = "ISO-8859-1")
sold15 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202411.csv", encoding = "ISO-8859-1")
sold16 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202412.csv", encoding = "ISO-8859-1")
sold_2024 = pd.concat([sold5,sold6,sold7,sold8,sold9,sold10,sold11,sold12,sold13,sold14,sold15,sold16], ignore_index=True)
#sold_2024 = sold_2024[sold_2024.PropertyType=='Residential']
sold17 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202501_filled.csv", encoding = "ISO-8859-1")
sold18 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202502.csv", encoding = "ISO-8859-1")
sold19 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202503.csv", encoding = "ISO-8859-1")
sold20 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202504.csv", encoding = "ISO-8859-1")
sold21 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202505.csv", encoding = "ISO-8859-1")
sold22 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202506.csv", encoding = "ISO-8859-1", low_memory= False)
sold23 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202507.csv", encoding = "ISO-8859-1")
sold24 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202508.csv", encoding = "ISO-8859-1")
sold25 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202509.csv", encoding = "ISO-8859-1")
sold26 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202510.csv", encoding = "ISO-8859-1")
sold27 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202511.csv", encoding = "ISO-8859-1")
sold28 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSSold202512.csv", encoding = "ISO-8859-1")
sold_2025 = pd.concat([sold17, sold18, sold19, sold20, sold21, sold22, sold23, sold24, sold25, sold26, sold27, sold28], ignore_index=True)
#sold_2025 = sold_2025[sold_2025.PropertyType=='Residential']
sold = pd.concat([sold_2024, sold_2025,sold_2026], ignore_index=True)
#sold = sold[sold['PropertyType']=='Residential']
sold.to_csv("sold_all.csv", index=False)
#406660 rows for sold
print(sold.shape)
print(sold.columns)
print(sold.head())
print(sold["PropertyType"].unique())
print("Rows before filtering: ", len(sold))
sold = sold[sold.PropertyType =='Residential']
print("Rows after filtering: ", len(sold))
print(sold.isnull().sum())
allCols = sold.select_dtypes(include = "number").columns
for c in allCols:
    info = sold[c].dropna()
    if info.empty:
        continue
    plt.hist(info.values, bins=100)
    plt.title("Distribution of " + c)
    q1 = sold[c].quantile(0.25)
    q3 = sold[c].quantile(0.75)
    iqr = q3 - q1
    #high = q3 + 1.5*iqr
    #plt.xlim(0, high)
    plt.show()
    plt.close()
    plt.boxplot(info.values)
    plt.title("Distribution of " + c)
    plt.show()
    plt.close()
cols = {"ClosePrice": 0, "LivingArea": 0, "DaysOnMarket": -1}
for col in cols:
    print(col)
    data = sold[col].copy()
    data[data <= cols[col]] = np.nan
    print(f" Minimum:   {data.min():,.2f}")
    print(f" Maximum:  {data.max():,.2f}")
    print(f" Mean:  {data.mean():,.2f}")
    print(f" Median: {data.median():,.2f}")
    print(f" Mode:  {data.mode()[0]:,.2f}")
    print(f" 1st quartile:  {data.quantile(0.25):,.2f}")
    print(f" 3rd quartile:  {data.quantile(0.75):,.2f}")
    outliers = data[(data > high) | (data < low)]
    print(f" Outlier count: {len(outliers)}")
    print(f" Outlier values: {outliers.values}")
    print(f" Outlier minimum: {outliers.min()}")
    print(f" Outlier maximum: {outliers.max()}")
sold.to_csv("sold_filtered.csv", index=False)
print("\n-- columns above 90% null---")
totalCount = len(sold)
for col in sold.columns:
    nullCount = sold[col].isnull().sum()
    percent = nullCount/totalCount*100
    if percent >= 90:
        print(f"{col}: {percent:.2f}%")
