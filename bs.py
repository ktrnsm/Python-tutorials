from bs4 import BeautifulSoup

code="""<!doctype html>"""
pars=BeautifulSoup(code,"html.parser")
write=pars.prettify
print(write)