#moonveil new
import requests
import pandas as pd
import datetime
from typing import Dict, List, Optional
import datetime
import re

def get_account():
    user_input = input("Enter space-separated userid: ")
    accounts = re.split(r'\n|\s+', user_input.strip())
    unique_accounts_input=[]

    for x in accounts:
        if x not in unique_accounts_input: 
        # and x.endswith("@gmail.com"):
            unique_accounts_input.append(x)
    # print(unique_accounts_input)
    return unique_accounts_input



def new_file(final_df):
    current_date = datetime.datetime.now()
    current_date_str = current_date.strftime("%B-%d")
    csv_file_1=f"/Users/shaimaahmed/Documents/KGeN/game_apis/gamename_{current_date_str}.csv"
    final_df.to_csv(csv_file_1, index=False) 
    print(f"File saved to: {csv_file_1}") 

# Make API request with error handling
def fetch_rank_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Process rank data more efficiently
def process_rank_data(data):
    rows = []
    if not data or "rankList" not in data:
        return pd.DataFrame(columns=['userid', 'score', 'name'])
        
    for entry in data["rankList"]:
        data = entry.get("Data", {})
        for player_id, player_info in data.items():
            rows.append({
                'userid': player_info.get('userid'),
                'score': player_info.get('score'),
                'name': player_info.get('name')
            })
    
    return pd.DataFrame(rows, columns=['userid', 'score','name'])


# Main execution

def main():
    final_df_2=pd.DataFrame()
    for pg in range(1,3):
        url =f"api_endpoint/{pg}"

        data = fetch_rank_data(url)
        if data:
            final_df = process_rank_data(data)
            print(f"Successfully processed {len(final_df)} player records")
            final_df_2 = pd.concat([final_df_2,final_df], ignore_index=True)
    uid_list=get_account()
    # print(uid_list)
    filtered_df = final_df_2[final_df_2['userid'].isin(uid_list)]
    new_file(final_df_2)
    
if __name__ == '__main__':
    main()
