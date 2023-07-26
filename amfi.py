import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_top_3_schemes():
    url = "https://www.amfiindia.com/research-information/other-data/mf-scheme-performance-details"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Step 2
    soup.select("#flexi-cap-scheme")[0]['selected'] = ''
    soup.select("#flexi-cap-scheme")[0]['selected'] = 'selected'

    # Step 3
    soup.select("#large-cap-scheme")[0]['selected'] = ''

    # Step 4
    soup.select("#repPeriod")[0].findAll('option')[3]['selected'] = ''
    soup.select("#repPeriod")[0].findAll('option')[4]['selected'] = 'selected'

    # Step 5
    soup.select("#direct")[0].click()
    soup.select("#direct")[0].click()

    # Step 6
    schemes = []
    for row in soup.select("tbody tr"):
        scheme = row.select("td:nth-child(2)")[0].text.strip()
        schemes.append(scheme)

    return schemes[:3]

def get_invested_amount_by_scheme(scheme, date):
    url = f"https://www.amfiindia.com/investor-corner/online-center/portfoliodisclosure?cp_sch_code={scheme}&type=0&date={date}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Step 11
    excel_file_link = soup.find("a", {"class": "download-table"})['href']
    excel_response = requests.get(excel_file_link)

    # Assuming the downloaded file is saved as 'monthly_portfolio_report.xls'
    with open("monthly_portfolio_report.xls", "wb") as f:
        f.write(excel_response.content)

    # You can use pandas to read the Excel file and process the data as required.
    df = pd.read_excel("monthly_portfolio_report.xls")
    # Process the data to find the total invested amount by the scheme.

    # Return the total invested amount for the scheme
    return total_invested_amount

def main():
    top_3_schemes = get_top_3_schemes()
    all_stocks_invested_amount = {}

    for scheme in top_3_schemes:
        # Replace 'YYYY-MM-DD' with the desired date format (e.g., '2023-06-30')
        invested_amount = get_invested_amount_by_scheme(scheme, 'YYYY-MM-DD')
        all_stocks_invested_amount[scheme] = invested_amount

    print(all_stocks_invested_amount)

if __name__ == "__main__":
    main()
