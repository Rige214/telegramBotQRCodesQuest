import json
import qrcode


with open('stepsQuests.json', 'r') as j:
    json_data = json.load(j)
    print(json_data)

for jsd in json_data:
    data = f"{json_data[jsd]}"
    filename = f"{jsd}.png"
    img = qrcode.make(data)
    img.save(f"generated_qrcods/{filename}")

print('QRcode generated successful')
