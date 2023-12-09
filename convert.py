import pandas as pd
import json

# Excel 파일 읽기
data = pd.read_excel('국가코드.xlsx')

# 데이터 변환
result = []
for _, row in data.iterrows():
    entry = {
        "Country": row['Country'],
        "Code": row['Code']
    }
    result.append(entry)

# JSON으로 변환
json_data = json.dumps(result, indent=2)

# JSON 데이터 출력
print(json_data)