import pandas as pd
import numpy as np
updated_sold_data = pd.read_csv("sold_cleaned_data.csv", low_memory=False)
updated_sold_data['CloseDate'] = pd.to_datetime(updated_sold_data['CloseDate'])
updated_sold_data['ListingContractDate'] = pd.to_datetime(updated_sold_data['ListingContractDate'])
updated_sold_data['PurchaseContractDate'] = pd.to_datetime(updated_sold_data['PurchaseContractDate'])
updated_sold_data['Year'] = updated_sold_data['CloseDate'].dt.year
updated_sold_data['Month'] = updated_sold_data['CloseDate'].dt.month
updated_sold_data['YrMo'] = updated_sold_data['CloseDate'].dt.to_period('M').astype(str)
updated_sold_data['price_ratio'] = (updated_sold_data['ClosePrice'] / updated_sold_data['OriginalListPrice']).round(2)
updated_sold_data['price_per_sq_ft'] = (updated_sold_data['ClosePrice'] / updated_sold_data['LivingArea']).round(2)
updated_sold_data['days_on_market'] = updated_sold_data['DaysOnMarket']
updated_sold_data['close_to_original_list_ratio'] = updated_sold_data['ClosePrice'] / updated_sold_data['OriginalListPrice']
updated_sold_data['listing_to_contract_days'] = (updated_sold_data['PurchaseContractDate'] - updated_sold_data['ListingContractDate']).dt.days
updated_sold_data['contract_to_close_days'] = (updated_sold_data['CloseDate'] - updated_sold_data['PurchaseContractDate']).dt.days
property_summary = updated_sold_data.groupby(['PropertyType', 'PropertySubType']).agg(properties_sold = ('ClosePrice', 'count'), avg_close_price = ('ClosePrice', 'mean'), median_close_price = ('ClosePrice', 'median'), avg_price_ratio=('price_ratio', 'mean'), avg_days_on_market=('DaysOnMarket', 'mean'), avg_listing_to_contract=('listing_to_contract_days', 'mean'), avg_contract_to_close= ('contract_to_close_days', 'mean'), avg_price_per_sq_ft=('price_per_sq_ft', 'mean')).reset_index()
county_summary = updated_sold_data.groupby(['CountyOrParish', 'MLSAreaMajor']).agg(properties_sold = ('ClosePrice', 'count'), avg_close_price = ('ClosePrice', 'mean'), median_close_price = ('ClosePrice', 'median'), avg_price_ratio=('price_ratio', 'mean'), avg_days_on_market=('DaysOnMarket', 'mean'), avg_price_per_sq_ft=('price_per_sq_ft', 'mean')).reset_index()
listOffice_summary = updated_sold_data.groupby('ListOfficeName').agg(properties_sold = ('ClosePrice', 'count'), avg_close_price = ('ClosePrice', 'mean'), median_close_price = ('ClosePrice', 'median'), avg_price_ratio=('price_ratio', 'mean'), avg_days_on_market=('DaysOnMarket', 'mean'), avg_price_per_sq_ft=('price_per_sq_ft', 'mean')).reset_index()
buyerOffice_summary = updated_sold_data.groupby('BuyerOfficeName').agg(properties_sold = ('ClosePrice', 'count'), avg_close_price = ('ClosePrice', 'mean'), median_close_price = ('ClosePrice', 'median'), avg_price_ratio=('price_ratio', 'mean'), avg_days_on_market=('DaysOnMarket', 'mean'), avg_price_per_sq_ft=('price_per_sq_ft', 'mean')).reset_index()
print(updated_sold_data[['ClosePrice', 'OriginalListPrice', 'LivingArea', 'price_ratio', 'price_per_sq_ft', 'days_on_market', 'Year', 'Month', 'YrMo', 'listing_to_contract_days', 'contract_to_close_days']].head())
print(property_summary.head())
print(county_summary.head())
print(listOffice_summary.head())
print(buyerOffice_summary.head())
updated_sold_data.to_csv("sold_with_metrics.csv", index=False)
property_summary.to_csv("property_summary.csv", index=False)
county_summary.to_csv("county_summary.csv", index=False)