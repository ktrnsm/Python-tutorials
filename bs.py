from bs4 import BeautifulSoup # html incelenirken karmaşadan kurtulmak için kullanılır.

code="""<!doctype html>"""
pars=BeautifulSoup(code,"html.parser")
write=pars.prettify
write2=pars.find_all("li")[1] # ilk indeksi getirir. li etiketlerinin tamamını liste biçimde döndürür.
print(write)