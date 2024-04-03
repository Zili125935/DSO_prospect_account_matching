# DSO Prospect Account Matching

## Daily Use
### If this is the first time you use this script, please go to the [bottom of this page](https://github.com/Zili125935/DSO_prospect_account_matching/tree/main?tab=readme-ov-file#environment-set-up) to do the environment set up first

### US DSO customer
* Step 1:\
Rename the input Excel file to 'Import DSO.xlsx'
```
Import DSO.xlsx
```
* Please make sure you change the input file header. \
Here is the example
```
https://stgcs.sharepoint.com/sites/US01_P_NAMDA/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FUS01%5FP%5FNAMDA%2FShared%20Documents%2FDSO%20prospect%20check%2FTemplate&viewid=2aab679b%2De916%2D4a18%2D9229%2D7d6e45206e57
```
copy the input Excel file under the folder 'DSO matching','DSO_prospect_account_matching'\
![issue DSO](https://github.com/Zili125935/DSO_prospect_account_matching/assets/107199759/a5e4e3fa-e5a7-4a56-a34f-5489f71949ad)
**Please make sure rename the new input excel file as 'Import DSO.xlsx' everytime you use this script!**

* Step 2:\
Open 'Command Prompt', copy paste & enter
```
cd OneDrive - STG-Business\Desktop\DSO Matching\DSO_prospect_account_matching
git pull
python run_dso_prospect_us.py
```
* Note - \
Please note if the folder name is changed, you have to change the command as well.\
For example, if the folder 'DSO Matching' has be changed to 'Account Matching', the first command will be\
```cd Desktop\Account Matching\DSO_prospect_account_matching```

### Canada DSO customer
* Step 1:\
Rename the input Excel file to 'Import DSO Canada.xlsx'
```
Import DSO Canada.xlsx
```
copy the input Excel file under the folder 'DSO matching','DSO_prospect_account_matching'\
![DSO Canada](https://github.com/Zili125935/DSO_prospect_account_matching/assets/107199759/ff75e5d4-7c20-48f4-b29e-43ef37571bae)
**Please make sure rename the new input excel file as 'Import DSO Canada.xlsx' everytime you use this script!**

* Step 2:\
Open 'Command Prompt', copy paste & enter
```
cd OneDrive - C:\Users\u125935\OneDrive - STG-Business\Desktop\DSO Matching\DSO_prospect_account_matching
git pull
python run_dso_prospect_ca.py
```
* Note - \
Please note if the folder name is changed, you have to change the command as well.\
For example, if the folder 'DSO Matching' has be changed to 'Account Matching', the first command will be\
```cd Desktop\Account Matching\DSO_prospect_account_matching```

## Environment Set-up
#### Prerequisite - install Python and Git

Open 'Command Prompt' and follow the instruction\
![command](https://github.com/Zili125935/semi_auto_process/assets/107199759/0686dfed-c293-4395-8ca9-ffecd353f1cc)


* Step 1:\
 Open Command prompt and choose the location you want to save the auto process.\
 For example, if you want save the file in the 'DSO Matching' under 'Desktop', you can type 
```
cd OneDrive - STG-Business\Desktop\DSO Matching
```
* Step 2:\
 clone the repo to your local, please copy and paste the following command in your command line
```
git clone https://github.com/Zili125935/DSO_prospect_account_matching.git
cd DSO_prospect_account_matching
pip install -r requirements.txt
```
*Remember to click 'enter'
* Step 3:\
Rename the input excel file to 'Import DSO.xlsx' \
copy the input excel file under folder 'DSO_prospect_account_matching'
* Note -\
Please make sure you change the input file header. Here is the example
```
https://stgcs.sharepoint.com/sites/US01_P_NAMDA/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FUS01%5FP%5FNAMDA%2FShared%20Documents%2FDSO%20prospect%20check%2FTemplate&viewid=2aab679b%2De916%2D4a18%2D9229%2D7d6e45206e57
```

* Step 4:\
Go back to Command, copy & paste the following command to run the script
```
python run_dso_prospect_us.py
