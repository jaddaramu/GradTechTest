medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

points = {
    1 : 3,
    2 : 2,
    3 : 1
}

def createMedalTable(results):
    medalResults = {}
    
    for result in results:
        for country in result["podium"]:
            
            currentCountry = country.split(".")
            
            rank = int(currentCountry[0])
            countryName = currentCountry[1]
            
            if countryName in medalResults:
                medalResults[countryName] += points[rank]
            else: 
                medalResults[countryName] = points[rank]
    
    return medalResults


def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable

test_function()
