summer_plans = [
    [  # Plan 1: Beach Vacation
        ["Travel", ["Hawaii", "Maldives"]],
        ["Swimming", ["Beach", "Pool"]],
        ["Party", ["Luau", "Beach Bonfire"]],
        ["Exploration", ["Snorkeling", "Island Hopping"]],
    ],
    [  # Plan 2: European Adventure
        ["Travel", ["France", "Italy", "Spain"]],
        ["Sightseeing", ["Eiffel Tower", "Colosseum", "Sagrada Familia"]],
        ["Cuisine", ["French Cuisine", "Italian Pasta", "Spanish Tapas"]],
        ["Culture", ["Museums", "Art Galleries", "Historical Sites"]],
    ],
    [  # Plan 3: Road Trip
        ["Travel", ["Grand Canyon", "Yellowstone", "Route 66"]],
        ["Camping", ["National Parks"]],
        ["Hiking", ["Trails", "Mountains"]],
        ["Adventure", ["Rafting", "Ziplining"]],
    ]
]
#Array modification:
summer_plans[0].append("Sunbathing")
print(summer_plans[0])

summer_plans[2].clear()
print(summer_plans[2])

x = summer_plans[1].copy()
print(x)
#Array Analysis:
print(type(summer_plans[0]))

print(len(summer_plans[1]))

print(summer_plans.count("Swimming"))
#Array Extension and Operation:
fruits = ("pineapple", "orange", "lemon")

summer_plans[0].extend(fruits)
print(summer_plans[0])

summer_plans[1].pop(-1)
print(summer_plans[1])

summer_plans[2].reverse()
print(summer_plans[2])
#Printing Mutiple Element

print(summer_plans[1][1])
adventure = ["Rafting", "Ziplining"]
print(adventure)





