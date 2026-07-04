import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df202401 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202401.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202402 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202402.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202403 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202403.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202404 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202404.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202405 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202405.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202406 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202406.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202407 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202407.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202408 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202408.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202409 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202409.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202410 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202410.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202411 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202411.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202412 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202412.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202501 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202501.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202502 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202502.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202503 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202503.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202504 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202504.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202505 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202505.csv", encoding = "ISO-8859-1") # df is Pandas dataframe

df202506 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202506.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202507 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202507.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202508 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202508.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202509 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202509.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202510 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202510.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202511 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202511.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202512 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202512.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202601 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202601.csv", encoding = "ISO-8859-1") # df is Pandas dataframe
df202602 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202602.csv", encoding = "ISO-8859-1", low_memory=False)
df202603 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202603.csv", encoding = "ISO-8859-1")
df202604 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202604.csv", encoding = "ISO-8859-1")
df202605 = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/CRMLSListing202605.csv", encoding = "ISO-8859-1")

frames=[df202401,df202402,df202403,df202404,df202405, df202406, df202407, df202408, df202409, df202410, df202411, df202412, df202501, df202502, df202503, df202504, df202505,df202506, df202507, df202508, df202509,df202510,df202511,df202512, df202601, df202602, df202603, df202604, df202605]
listings=pd.concat(frames, ignore_index=True)
#listings = combine[combine.PropertyType=='Residential']
listings.to_csv("listings_all.csv", index=False)
print(listings.shape)
print(listings.columns)
print(listings.head())
print(listings["PropertyType"].unique())
print("Rows before filtering: "+ str(len(listings)))
listings = listings[listings.PropertyType=='Residential']
print("Rows after filtering: "+ str(len(listings)))
print(listings.isnull().sum())
allCols = listings.select_dtypes(include = "number").columns
for c in allCols:
    info = listings[c].dropna()
    if info.empty:
        continue
    plt.hist(info.values, bins=100)
    plt.title("Distribution of " + c)
    q1 = listings[c].quantile(0.25)
    q3 = listings[c].quantile(0.75)
    iqr = q3 - q1
    high = q3 + 1.5*iqr
    low = q1 - 1.5*iqr
    #plt.xlim(0, high)
    plt.show()
    plt.close()
    plt.boxplot(info.values)
    plt.title("Distribution of " + c)
    plt.show()
    plt.close()
cols = {"ClosePrice": 0, "LivingArea": 0, "DaysOnMarket": -1}
#i'm setting bounds which is the impossible values for the variable so they don't interfere with stats
# the value of each key is the highest value the key can't be
for col in cols:
    print(col)
    data = listings[col].copy()
    data[data <= cols[col]] = np.nan
    #listings[col] = listings[col].replace(0, np.nan)
    print(f" Minimum:  {data.min():,.2f}")
    print(f" Maximum:  {data.max():,.2f}")
    print(f" Mean:  {data.mean():,.2f}")
    print(f" Median:  {data.median():,.2f}")
    print(f" Mode:   {data.mode()[0]:,.2f}")
    print(f" 1st Quartile: {data.quantile(0.25):,.2f}")
    print(f" 3rd Quartile: {data.quantile(0.75):,.2f}")
    outliers = data[(data > high) | (data < low)]
    print(f" Outlier count: {len(outliers)}")
    print(f" Outlier values: {outliers.values}")
    print(f" Outlier minimum: {outliers.min()}")
    print(f" Outlier maximum: {outliers.max()}")
listings.to_csv("listings.csv", index=False)
print("\n -- columns above 90% null---")
totalCount = len(listings)
for col in listings.columns:
    nullCount = listings[col].isnull().sum()
    percent = nullCount/totalCount*100
    if percent >= 90:
        print(f"{col} at least 90% null values")

