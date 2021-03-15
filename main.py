from bs4 import BeautifulSoup
import re
from pathlib import Path

html = open("notes.html")
soup = BeautifulSoup(html, "html.parser")

Text = open("top.html", "r").read()
sched = soup.find_all(lambda tag: tag.name == "span" and tag.text == "1.2")[-1].parent
sched_list = sched.next_sibling
while sched_list.name != "dl":
	sched_list = sched_list.next_sibling

days = []
for date in sched_list.find_all("dt"):
	desc = date.next_sibling
	while desc.name != "dd":
		desc = desc.next_sibling
	days.append([date, desc])

ids = []

def get_lecture(x: int):
	""" Gets information about (1-indexed) lecture number """
	x -= 1
	global Text
	for links in days[x][1].find_all("a"):
		href = links.attrs.get("href", "")
		if href.startswith("temp.html#"):
			ids.append(href[10:])
			links.attrs["href"] = "output.html#" + href[10:]
	Text += str(days[x][0]) + str(days[x][1])

x = int(input())
get_lecture(x)

for _id in ids:
	header = soup.find(re.compile('^h[1-6]$'), {"id": _id})
	if header == None:
		Text += f'<h3 style="color:red"> ID not found: {_id} </h3>\n'
		continue
	Text += str(header)
	sib = header.next_sibling
	while sib != None and (sib.name == None or sib.name[:-1] != "h" or int(sib.name[-1]) > int(header.name[-1])):
		Text += str(sib)
		sib = sib.next_sibling

with open(Path(__file__).parent / "output.html", "w") as f_output:
	f_output.write(Text)  
