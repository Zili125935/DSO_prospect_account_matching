# DSO Prospect Account Matching

## Daily Use
### If this is the first time you use this script, please go to the [bottom of this page](https://github.com/Zili125935/semi_auto_process#environment-setup) to do the environment set up first

### US DSO customer
* Step 1:\
Rename the input Excel file to 'Import DSO.xlsx'\
copy the input Excel file under the folder 'DSO matching','DSO_prospect_account_matching'\
![input](https://github.com/Zili125935/semi_auto_process/assets/107199759/1c6ae8e4-580e-4e31-a672-3bdd88ec97e9)
**Please make sure rename the new input excel file as 'Import DSO.xlsx' everytime you use this script!**

* Step 2:\
Open 'Command Prompt', copy paste & enter
```
cd OneDrive - STG-Business\Desktop\Sunshine Act\semi_auto_process
git pull
python sunshine_run.py
```
* Note - \
Please note if the folder name is changed, you have to change the command as well.\
For example, if the folder 'Sunshine Act' has be changed to 'Sunshine', the first command will be\
```cd Desktop\Sunshine\semi_auto_process```

### Canada DSO customer
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
python run_dso_prospect_us.py
