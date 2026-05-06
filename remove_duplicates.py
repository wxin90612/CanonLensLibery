import json

with open('/workspace/src/data/lenses.json', 'r', encoding='utf-8') as f:
    lenses = json.load(f)

print(f"原始数量: {len(lenses)}")

seen_ids = set()
unique_lenses = []
duplicates = []

for lens in lenses:
    if lens['id'] in seen_ids:
        duplicates.append(lens['id'])
    else:
        seen_ids.add(lens['id'])
        unique_lenses.append(lens)

print(f"重复的ID: {duplicates}")
print(f"去重后数量: {len(unique_lenses)}")

with open('/workspace/src/data/lenses.json', 'w', encoding='utf-8') as f:
    json.dump(unique_lenses, f, ensure_ascii=False, indent=2)

print("已清理重复数据")
