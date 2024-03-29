# DSO Prospect Account Matching
## Daily Use
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
copy the input excel file under folder 'semi_auto_process'

* Step 4:\
Go back to Command, copy & paste the following command to run the script
```
python sunshine_run.py
