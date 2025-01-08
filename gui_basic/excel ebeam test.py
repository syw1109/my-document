import pandas as pd
import os

# 바탕화면 경로 가져오기
desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')

# 엑셀 파일 경로
excel_file_path = os.path.join(desktop_path, 'Ebeam Path.xlsx')

# 엑셀 파일의 Sheet1을 데이터프레임으로 읽기
df = pd.read_excel(excel_file_path, sheet_name='Sheet1')

# 데이터프레임 확인
print(df)
