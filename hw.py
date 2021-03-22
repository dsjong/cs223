from bs4 import BeautifulSoup
import re
from pathlib import Path

html = open(Path(__file__).parent / "notes.html")
soup = BeautifulSoup(html, "html.parser")

Text = open(Path(__file__).parent / "top.html", "r").read()
header = soup.find_all(lambda tag: tag.name == "span" and tag.text == "8")[-1].parent

ids = []
sib = header.next_sibling
while sib != None and (sib.name == None or sib.name[:-1] != "h" or int(sib.name[-1]) > int(header.name[-1])):
	if sib.name and sib.name[:-1] == "h" and int(sib.name[-1]) == int(header.name[-1])+1:
		ids += [sib.get("id")]
	sib = sib.next_sibling

x = int(input())
_id = ids[x-1]
header = soup.find(re.compile('^h[1-6]$'), {"id": _id})
if header == None:
	Text += f'<h3 style="color:red"> ID not found: {_id} </h3>\n'
	exit()
Text += str(header)
sib = header.next_sibling
while sib != None and (sib.name == None or sib.name[:-1] != "h" or int(sib.name[-1]) > int(header.name[-1])):
	Text += str(sib)
	sib = sib.next_sibling

with open(Path(__file__).parent / "output.html", "w") as f_output:
	f_output.write(Text)  