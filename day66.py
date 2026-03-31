# regular expansion
import re

pattern = "king"
text = '''The 1937 tour of Germany by the Duke and Duchess of Windsor was opposed by the British government,
which feared that Nazi Germany would use the visit for propaganda. After Edward VIII's abdication in December 1936,
his brother George VI became king ting.
Given the title of Duke of Windsor, Edward married Wallis Simpson in June 1937.
He appeared to have been sympathetic to Germany in this period and announced his intention to travel there privately to tour factories.
He promised the British sing government that he would keep a low profile, and the tour went ahead between 12 and 23 October. 
The Windsors visited fing factories,
many of which were producing materiel as Germany rearmed, 
and the Duke inspected German'''

match = re.search(pattern,text)
print(match)

if match:
    print("match is found")
else:
    print("no found")