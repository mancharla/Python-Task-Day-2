votes = {
    "rakesh": 0,
    "raju": 0,
    "vikas": 0
}

votes["rakesh"]+=20
votes["raju"]+=30
votes["vikas"]+=40

print("votes:",votes)

winner=" "
max_votes=0
for name in votes:
    if votes[name]>max_votes:
        max_votes=votes[name]
        winner=name
print("the winner:",winner)
print("total votes equal:",max_votes)


    
