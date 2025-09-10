from bs4 import BeautifulSoup

url = "view-source:https://br.shein.com/?onelink=7/4cvn2dvukbbq&requestId=olw-4t8q1wxkxr82&network=g&kwd=kwd-1667706624&pf=GOOGLE&keyword=shein&target=&placement=&gad_source=1&gad_campaignid=22138282692&gbraid=0AAAAADm0yO71G0yG3eoTvA0K7uXiracDC&gclid=Cj0KCQjw64jDBhDXARIsABkk8J4xgCMYF7-zmTxOgrCLFKZwq1T6p-PdbNYDy-jVOcQ3ErJLGcDmKYoaAsGbEALw_wcB&url_from=brgooglebrandshein_srsa_normal2_onelink01_20250120"
response = request.get(url)

print("status:", response.status_code)

soup =  BeautifulSoup(response.text, "html.parser")

titulo = soup.title.string

print("titulo da pagina:", titulo)