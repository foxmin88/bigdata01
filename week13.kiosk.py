# ddl create (create_at field)
# dml update -> update
import requests

import kiosk as kk
#from temp import response

if __name__ == "__main__":
    url = f"https://wttr123.in/uiwang?format=%C+%t&lang=ko"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text.strip())
        else:
            print(f"상태 코드 : {response.status_code}")
    except Exception as err:
        print(f"오류 : {err}")
    kk.run()
    kk.print_receipt()
    kk.print_ticket_number()