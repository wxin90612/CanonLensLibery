import json

with open('/workspace/src/data/lenses.json', 'r', encoding='utf-8') as f:
    lenses = json.load(f)

# 统计现有适马镜头
sigma_lenses = [l for l in lenses if l['brand'] == 'Sigma']
print(f"现有适马镜头: {len(sigma_lenses)} 个")
for lens in sigma_lenses:
    print(f"- {lens['model']} ({lens['year']})")

print("\n需要补充的镜头:")
# 根据用户提供的信息，我们需要补充以下镜头
