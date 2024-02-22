import configuration
import json
import zlib


q_list = (
    configuration.StepStatus.one.value,
    configuration.StepStatus.two.value,
    configuration.StepStatus.three.value,
    configuration.StepStatus.four.value,
)

with open("stepsQuests.json", "w") as fp:
    json.dump({
        f"{step}": zlib.crc32(q_list[k].encode('utf-8'))
        for k, step in enumerate(q_list)
    }, fp)

print('JSON-key generated successful')
