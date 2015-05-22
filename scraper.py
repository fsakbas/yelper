import itertools as it
import json
import scraperwiki
import pandas

# <codecell>

## Consts
PLAYER_DATA_URL = "http://fantasy.premierleague.com/web/api/elements/"

# <codecell>

def ExtractPlayerDF(Data):
    colNames = ['Date', 'Round', 'Opponent', 'MP', 'GS', 'A', 'CS', 'GC', 'OG', 'PS',
                'PM', 'YC', 'RC', 'S', 'B', 'ESP', 'BPS', 'NT', 'Value', 'Points']
    fixtures = Data['fixture_history']['all']
    playerDF = pandas.DataFrame(fixtures, columns = colNames)

    playerDF['ID'] = Data['id']
    playerDF['Code'] = Data['code']
    playerDF['WebName'] = Data['web_name']
    playerDF['FirstName'] = Data['first_name']
    playerDF['SecondName'] = Data['second_name']
    playerDF['Position'] = Data['type_name']
    playerDF['Team'] = Data['team_name']

    colOrder = ['ID', 'Code', 'Round', 'WebName', 'FirstName', 'SecondName', 'Position', 'Team',
                'Date', 'Opponent', 'MP', 'GS', 'A', 'CS', 'GC', 'OG', 'PS', 'PM', 'YC',
                'RC', 'S', 'B', 'ESP', 'BPS', 'NT', 'Value', 'Points']

    return playerDF[colOrder]

# <codecell>

## Download data
print '[LOG] Downloading Data Started'

playersDataRaw = []
for i in it.count(1):
    url = PLAYER_DATA_URL + str(i)
    try:
        playerDataJson = scraperwiki.scrape(url)
        playersDataRaw.append(json.loads(playerDataJson))
        print '[LOG] Player Index ', i, ' data downloaded successfully.'
    except:
        print '[LOG] Last Player Index downloaded: ' + str(i)
        break

print '[LOG] Downloading Data Ended'

# <codecell>

## Mine Players Data
## and concat all into one DataFrame

print '[LOG] Processing Data Started'

PlayersData = pandas.concat(map(ExtractPlayerDF, playersDataRaw), ignore_index = True)

print '[LOG] Processing Data Ended'

# <codecell>

## Save DataFrame to SQLite

print '[LOG] Transfering data to SQLite format'

scraperwiki.sqlite.save(unique_keys = ['Code', 'Round'],
                        data = PlayersData.to_dict(orient = 'records'))


print scraperwiki.sqlite.show_tables()
