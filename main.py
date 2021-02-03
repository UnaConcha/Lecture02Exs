import requests #need to grab something from the internet
import secrets

def get_data(url: str):#entry pt to program
   final_data = []
   final_url = f"{url}&api_key={secrets.apikey}&page=8 "
   response = requests.get(url)

   #number of possible response good-200, 500-error on server side, 400-error that I did something wrong from client request side
   if response.status_code != 200:
       print(response.text)
       return[]
   json_data = response.json()
   page_data = json_data["results"]
   final_data.extend(page_data)
   #print("Good Data")
   return final_data

   #pass is for when i know something goes there but its not there yet. pass lets it pass without an eror


def main():
    url = #grab off github after class
    all_data = get_data(url)
    for school_data in all_data:
        print(school_data)
    print(all_data)

if __name__ == '__main__':
    main()


