# https://www.youtube.com/watch?v=T1vqS1NL89E&ab_channel=PythonEngineer

import gspread # pip install gspread

'''SETUP
- google developer console: https://console.developers.google.com
- new project -> activate drive and sheets api
- credentials -> service account -> name + role=editor
  ->create key and download json
- share client_email fom json in your sheets
'''

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key("19dLgpGsLAW4K4yiSdbpsA-njCGiDwhiYXa3uaWFJbsY") # or by sheet name: gc.open("TestList")
worksheet = sh.sheet1

### retrieve data ###
res = worksheet.get_all_values()
print(len(res))
print(res)
res = worksheet.get_all_records()
print(len(res))
print(res)