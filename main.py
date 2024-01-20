import requests
pars_res_list=[]
response=requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text=response.text
response_parse=response_text.split("<td>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("$"):
        for parse_elem_2 in parse_elem_1.split("</td>"):
            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
                pars_res_list.append(parse_elem_2)

ДоларСША=pars_res_list[7]
print(f"ДоларСША - {ДоларСША}")