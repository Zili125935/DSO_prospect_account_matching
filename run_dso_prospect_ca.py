import os
import sys
from datetime import datetime
import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import numpy as np
import difflib
import swifter
from rapidfuzz import process, fuzz, utils

def fuzzy_match(s, full_list):
    with_s = [x for x in full_list if x.startswith(s[0:1])]
    if with_s:
        res, score, _ = process.extractOne(s, with_s, scorer=fuzz.WRatio, processor=utils.default_process)
        if score > 85:
            return res

def main():
    cwd = os.getcwd()
    filedir_dso = r"%s\%s" % (cwd, 'Import DSO Canada.xlsx')
    filedir_cus = r"%s\%s" % (cwd, 'customer_attritube_node_ca.csv')
    print('processing...')
    df_customer = pd.read_csv(filedir_cus)
    df_customer['join_key'] = df_customer['customer_name_1'].astype(str).str.lower() + '-' + df_customer['city'].astype(str).str.lower()
    df_customer[['customer_number', 'join_key']]
    df_dso = pd.read_excel(filedir_dso)
    df_dso['join_key'] = df_dso['Name'].astype(str).str.lower()+ '-' + df_dso['City'].astype(str).str.lower()

    join_key_list = list(df_customer['join_key'].unique())
    df_dso['most_close_join_key'] = df_dso['join_key'].swifter.apply(lambda x: fuzzy_match(x, join_key_list))
    result_df = pd.merge(df_dso, df_customer, left_on='most_close_join_key', right_on='join_key', how='left')
    result_df.drop(['join_key_y', 'join_key_x','most_close_join_key'], axis=1, inplace=True)
    result_df_deduped = result_df.drop_duplicates()

    resdf = pd.merge(df_dso, df_customer, left_on='most_close_join_key', right_on='join_key', how='left')
    resdf = resdf[resdf['join_key_y'].isna()]

    time_string = datetime.now().strftime('%Y-%m-%d_%H%M%S')

    output_filedir = 'CA_matched_dso_customer_' + time_string + '.xlsx'
    result_df_deduped.to_excel(output_filedir, index=False)
    output_filedir = 'CA_not_found_' + time_string + '.xlsx'
    resdf.to_excel(output_filedir, index=False)
    print('completed! Result file saved as ' + output_filedir)

if __name__ == "__main__":
    sys.exit(main())