import json
import configuration


quest_list = [configuration.STEP_ONE, configuration.STEP_TWO, configuration.STEP_FOUR, configuration.STEP_THREE]

q_list = {
        "step_one": hash(quest_list[0]),
        "step_two": hash(quest_list[1]),
        "step_three": hash(quest_list[2]),
        "step_four": hash(quest_list[3]),
}

with open(f'stepsQuests.json', 'w') as file:
    json.dump(q_list, file)
print(q_list)
print('JSON-key generated successful')
