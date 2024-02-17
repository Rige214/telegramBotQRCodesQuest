import json
import configuration


quest_list = [configuration.STEP_ONE, configuration.STEP_TWO, configuration.STEP_FOUR, configuration.STEP_THREE]

for k in quest_list:
    q_list = {
        "step_one": hash(quest_list[quest_list.index(k)]),
        "step_two": hash(quest_list[quest_list.index(k)]),
        "step_three": hash(quest_list[quest_list.index(k)]),
        "step_four": hash(quest_list[quest_list.index(k)])
    }

    with open(f'stepsQuests.json', 'w') as file:
        json.dump(q_list, file)

print('JSON-key generated successful')
