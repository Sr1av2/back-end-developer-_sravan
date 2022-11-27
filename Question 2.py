import re
import urllib.request

url = input("Enter website URL:").strip()
html = urllib.request.urlopen(url)
site = html.read().decode("utf-8")

social_media = ["facebook.com", "linkedin.com", "youtube.com", "twitter.com", "instagram.com"]
anchor = re.findall("href=\"(.+?)\"", site)
print("Social links-")
for i in anchor:
	for j in social_media:
		if j in i:
			print(i)
			break

print()

email_list = re.findall("href=\".*mailto:(.+?)\"", site)
relevant_emails = []
domain = url.split("//")[-1]
for i in email_list:
	if i.split("@")[-1] == domain:
		relevant_emails.append(i)

phone = re.findall("href=\".*tel:(.+?)\"", site)[-1]
print("Email/s-")
if relevant_emails:
	for i in relevant_emails:
		print(i)
else:
	for i in email_list:
		print(i)

print()

print("Contact:")
print(phone)