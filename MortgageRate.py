#Fetching mortgage rate data from FRED
import pandas as pd
sold = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/sold_filtered.csv")
listings = pd.read_csv("C:/Users/iradeokule/Desktop/crmls/listings.csv")
url = "https://fred.stlouisfed.org/graph/fredgraph.csv?id=MORTGAGE30US"
mortgage = pd.read_csv(url, parse_dates=['observation_date'])
mortgage.columns = ['date', 'rate_30yr_fixed']
#resample weekly rates to monthly averages
mortgage['year_month'] = mortgage['date'].dt.to_period('M')
mortgage_monthly = (mortgage.groupby('year_month')['rate_30yr_fixed'].mean().reset_index())
#create a matching year_month key on MLS datasets
sold['year_month'] = pd.to_datetime(sold['CloseDate']).dt.to_period('M')
listings['year_month'] = pd.to_datetime(listings['CloseDate']).dt.to_period('M')
#Merging data
sold_with_rates = sold.merge(mortgage_monthly, on='year_month', how='left')
listings_with_rates = listings.merge(mortgage_monthly, on='year_month', how='left')
#Checking for any unmatched rows
print(sold_with_rates['rate_30yr_fixed'].isnull().sum())
print(listings_with_rates['rate_30yr_fixed'].isnull().sum())
print(sold_with_rates[['CloseDate', 'year_month', 'ClosePrice','rate_30yr_fixed']].head())
#saving the datasets
sold_with_rates.to_csv("sold_with_rates.csv", index=False)
listings_with_rates.to_csv("listings_with_rates.csv", index=False)