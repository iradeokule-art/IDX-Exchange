import numpy as np
import pandas as pd
#from altair import Longitude

sold = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/sold_filtered.csv", low_memory=False)
print("Rows before cleaning:", len(sold))
#Converting fields to datetime to enhance date comparisons and timeline verifications
sold['CloseDate'] = pd.to_datetime(sold['CloseDate'], errors = "coerce")
sold['PurchaseContractDate'] = pd.to_datetime(sold['PurchaseContractDate'], errors = "coerce")
sold['ListingContractDate'] = pd.to_datetime(sold['ListingContractDate'], errors = "coerce")
sold['ContractStatusChangeDate'] = pd.to_datetime(sold['ContractStatusChangeDate'], errors = "coerce")
sold = sold.replace(r'^\s*$', np.nan, regex=True)
sold = sold.replace({"":np.nan, "N/A":np.nan, "NA":np.nan, "NULL":np.nan, "Unknown":np.nan, "-":np.nan})
sold = sold.dropna(axis=1, how='all')
threshold = 0.90
sold = sold.dropna(thresh = len(sold) * (1 - threshold) + 1, axis = 1)
sold.loc[sold['ClosePrice'] <= 0, 'ClosePrice'] = np.nan
sold.loc[sold['LivingArea'] <= 0, 'LivingArea'] = np.nan
sold.loc[sold['DaysOnMarket'] < 0, 'DaysOnMarket'] = np.nan
sold.loc[sold['BedroomsTotal'] < 0, 'BedroomsTotal'] = np.nan
sold.loc[sold['BathroomsTotalInteger'] < 0, 'BathroomsTotalInteger'] = np.nan
key_cols = ['ClosePrice', 'LivingArea', 'DaysOnMarket', 'BedroomsTotal', 'BathroomsTotalInteger', 'Latitude', 'Longitude']
print(sold[key_cols].dtypes)
sold = sold.dropna(subset = ['ClosePrice', 'LivingArea'])
sold['listing_after_close_flag'] = sold['ListingContractDate'] > sold['CloseDate']
sold['purchase_after_close_flag'] = sold['PurchaseContractDate'] > sold['CloseDate']
sold['negative_timeline_flag'] = ((sold['ListingContractDate'] > sold['PurchaseContractDate']) | (sold['PurchaseContractDate'] > sold['CloseDate']))
#sold.loc[sold['Latitude'] == 0, 'latitude'] = np.nan
#sold.loc[sold['Longitude'] == 0, 'longitude'] = np.nan
#sold.loc[sold['Longitude'] > 0, 'longitude'] = np.nan
sold['missing_coordinates_flag'] = sold['Latitude'].isnull() | sold['Longitude'].isnull()
sold['sentinel_zero_flag'] = (sold['Latitude'] == 0)| (sold['Longitude'] == 0)
sold['longitude_positive_flag'] = sold['Longitude'] > 0
sold['out_of_state_longitude_flag'] = (sold['Longitude'] < -124) | (sold['Longitude'] > -114)
sold['out_of_state_latitude_flag'] = (sold['Latitude'] < 32) | (sold['Latitude'] > 42)
print('----------Summary Distribution---------')
print('--- Date Consistency Flags ---')
print('Records where listing date is after close date:', sold['listing_after_close_flag'].sum())
print('Records where purchase contract date is after close date:', sold['purchase_after_close_flag'].sum())
print('Records where listing date is after purchase contract date: ', sold['negative_timeline_flag'].sum())
print('--- Geographic Flags ---')
print('Records with missing latitude or longitude:', sold['missing_coordinates_flag'].sum())
print('Records with latitude or longitude equal to zero:', sold['sentinel_zero_flag'].sum())
print('Records with positive longitude:', sold['longitude_positive_flag'].sum())
print('Records with out-of-state latitude:', sold['out_of_state_latitude_flag'].sum())
print('Records with out-of-state longitude:', sold['out_of_state_longitude_flag'].sum())
print("Rows after cleaning data:", len(sold))
sold.to_csv("sold_cleaned_data.csv", index=False)
