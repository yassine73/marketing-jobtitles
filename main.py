import pandas as pd

file_path = 'marketing_titles.xlsx'
data = pd.read_excel(file_path, sheet_name=None)

functions = [data['function'].columns[0]] + data['function'].iloc[:,0].tolist()
seniorities = [data['seniority'].columns[0]] + data['seniority'].iloc[:,0].tolist()

job_titles = []
for func in functions:
    for seniority in seniorities:
        if func and seniority:
            job_titles.append(f'{func.strip()} {seniority.strip()}')

output = pd.DataFrame(job_titles, columns=['job_title'])
output.to_csv('job_titles.csv', index=False)