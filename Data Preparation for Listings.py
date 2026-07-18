import numpy as np
import pandas as pd
listings = pd.read_csv("listings_all.csv", low_memory=False)
print("Rows before cleaning: ", listings.shape)
listings['CloseDate'] = pd.to_datetime(listings['CloseDate'], errors = "coerce")
listings['PurchaseContractDate'] = pd.to_datetime(listings['PurchaseContractDate'], errors = "coerce")
listings['ListingContractDate'] = pd.to_datetime(listings['ListingContractDate'], errors = "coerce")
listings['ContractStatusChangeDate'] = pd.to_datetime(listings['ContractStatusChangeDate'], errors = "coerce")
listings = listings.replace(r'^\s*$', np.nan, regex=True)
listings = listings.replace({"":np.nan, "N/A":np.nan, "NA":np.nan, "NULL":np.nan, "Unknown":np.nan, "-":np.nan, "########":np.nan})
listings = listings.dropna(axis=1, how='all')
threshold = 0.90
listings = listings.dropna(thresh = len(listings) * (1 - threshold) + 1, axis = 1)
listings.loc[listings['ListPrice'] <= 0, 'ListPrice'] = np.nan
listings.loc[listings['LivingArea'] <= 0, 'LivingArea'] = np.nan
listings.loc[listings['DaysOnMarket'] < 0, 'DaysOnMarket'] = np.nan
listings.loc[listings['BedroomsTotal'] < 0, 'BedroomsTotal'] = np.nan
listings.loc[listings['BathroomsTotalInteger'] < 0, 'BathroomsTotalInteger'] = np.nan
listings = listings.dropna(subset = ['ListPrice', 'LivingArea'])
key_cols = ['ClosePrice', 'LivingArea', 'DaysOnMarket', 'BedroomsTotal', 'BathroomsTotalInteger', 'Latitude', 'Longitude']
print(listings[key_cols].dtypes)
listings['listing_after_close_flag'] = listings['ListingContractDate'] > listings['CloseDate']
listings['purchase_after_close_flag'] = listings['PurchaseContractDate'] > listings['CloseDate']
listings['negative_timeline_flag'] = ((listings['ListingContractDate'] > listings['PurchaseContractDate']) | (listings['PurchaseContractDate'] > listings['CloseDate']))
listings = listings.dropna(subset = ['MiddleOrJuniorSchoolDistrict', 'ElementarySchoolDistrict', 'TaxYear', 'CoveredSpaces'])
listings['missing_coordinates_flag'] = listings['Latitude'].isnull() | listings['Longitude'].isnull()
listings['sentinel_zero_flag'] = (listings['Latitude'] == 0)| (listings['Longitude'] == 0)
listings['longitude_positive_flag'] = listings['Longitude'] > 0
listings['out_of_state_longitude_flag'] = (listings['Longitude'] < -124) | (listings['Longitude'] > -114)
listings['out_of_state_latitude_flag'] = (listings['Latitude'] < 32) | (listings['Latitude'] > 42)
print('----------Summary Distribution---------')
print('--- Date Consistency Flags ---')
print('Records where listing date is after close date:', listings['listing_after_close_flag'].sum())
print('Records where purchase contract date is after close date:', listings['purchase_after_close_flag'].sum())
print('Records where listing date is after purchase contract date: ', listings['negative_timeline_flag'].sum())
print('--- Geographic Flags ---')
print('Records with missing latitude or longitude:', listings['missing_coordinates_flag'].sum())
print('Records with latitude or longitude equal to zero:', listings['sentinel_zero_flag'].sum())
print('Records with positive longitude:', listings['longitude_positive_flag'].sum())
print('Records with out-of-state latitude:', listings['out_of_state_latitude_flag'].sum())
print('Records with out-of-state longitude:', listings['out_of_state_longitude_flag'].sum())
print("Rows after cleaning data:", len(listings))
listings.to_csv("listings_cleaned_data.csv", index=False)
