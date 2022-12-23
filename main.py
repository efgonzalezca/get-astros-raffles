import requests
from requests_html import HTMLSession
 
url = "https://superastro.com.co/resultados-super-astro-sol-super-astro-luna.php"
 
try:
    session = HTMLSession(verify=False)
    response = session.get(url)
     
except requests.exceptions.RequestException as e:
    print('error por ssl')
    
try:
    result_astro_sol = response.html.find('#respuestasol', first=True).find('table tr', first=False)
    result_astro_luna = response.html.find('#respuestaluna', first=True).find('table tr', first=False)
except AttributeError as e:
    print(e)

for result in range(len(result_astro_luna)):
    if result == 0:
        continue
    if result < 2:
        tmp = result_astro_luna[result].text.split('\n')
        astro_luna = {
            "number": tmp[0],
            "sign": tmp[1].upper(),
            "draw": tmp[2],
            "date": tmp[3]
        }
    else:
       break

for result in range(len(result_astro_sol)):
    if result == 0:
        continue
    if result < 2:
        tmp = result_astro_sol[result].text.split('\n')
        astro_sol = {
            "number": tmp[0],
            "sign": tmp[1].upper(),
            "draw": tmp[2],
            "date": tmp[3]
        }
    else:
       break

print('Astro Luna: ', astro_luna)
print('Astro Sol: ', astro_sol)