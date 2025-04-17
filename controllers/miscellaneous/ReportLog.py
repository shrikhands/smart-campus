import pandas as pd

def saveReport(data):
    print("get func:")
    print(data.get('report_crime_type'))
    
    export_data = pd.DataFrame({'address': [data.get('report_address')], 
                                'crime_type': [data.get('report_crime_type')],
                                'data': [data.get('report_date')],
                                'disposition': [data.get('report_disposition')],
                                'time_hour': [data.get('report_hour')],
                                'part_of_day': [data.get('report_part_day')],
                                'public_information': [data.get('report_public_info')]})
    
    data_to_excel = pd.ExcelWriter("CrimeLog.xlsx",engine='xlsxwriter')
    #data_to_excel = pd.ExcelWriter("data_reduced.xlsx",engine='xlsxwriter')
    export_data.to_excel(data_to_excel, sheet_name='Sheet1')
    data_to_excel.save()
