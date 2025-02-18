import json
with open('/Users/assemmukhtarkyzy/Desktop/pp2/lab4/json/sample-data.json', 'r') as file:
    data = json.load(file)

print("Interface Status")
print("=" * 95)

print(f"{'DN':<50} {'Description':<20} {'Speed':<6} {'MTU':<4}")
print("-" * 80)

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    format_interface = "{:<50} {:<25} {:<10} {:<10}".format(
        attributes.get('dn', ''),
        attributes.get('descr', ''),
        attributes.get('speed', ''),
        attributes.get('mtu', '')
    )
    print(format_interface)

