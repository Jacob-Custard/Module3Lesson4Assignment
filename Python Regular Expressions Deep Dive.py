# Task 1 Email Extraction Enhancement: You have a script that extracts email addresses from a text but
#needs to be refined to exclude certain domains (e.g. exclude.com). Modify the script to extract all addresses except
#those from the specified domain.
#code example: 
#text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
#emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
#print(emails)

import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com, user4@gmail.com, user5@aol.com, user6@exclude.com, user7@aol.com, user8@exclude.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@(?!exclude)[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)                                                                            #added a negative lookahead to the script so it would exclude the specified email addresses.                                                   
print(emails)
