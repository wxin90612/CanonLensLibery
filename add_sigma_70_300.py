import json

with open('/workspace/src/data/lenses.json', 'r', encoding='utf-8') as f:
    lenses = json.load(f)

new_lens = {
    'id': 'sigma-70-300-45-56-dl-macro',
    'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 70-300mm f/4-5.6 DL MACRO SUPER',
    'modelCode': '70-300/4-5.6 DL MACRO SUPER', 'nickname': '适马小黑', 'era': 'film', 'year': 1997,
    'type': 'zoom', 'focalLength': '70-300mm', 'aperture': 'f/4-5.6', 'isStabilized': False,
    'weight': 550, 'minFocusDistance': '1.5m', 'filterSize': '58mm',
    'priceNew': 2499, 'priceUsedMin': 300, 'priceUsedMax': 600, 'retentionRate': 25, 'ownershipCount': 'high',
    'pros': ['轻便', '长焦焦段', '微距功能', '价格便宜'],
    'cons': ['无防抖', '光圈小', '长焦端画质一般'],
    'commonIssues': ['对焦马达老化', '镜筒松动'],
    'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+70-300mm+f4-5.6+DL+MACRO+lens+telephoto+zoom+vintage&image_size=square',
    'purchaseAdvice': '入门长焦选择，性价比高',
    'specs': {'镜片组': '10片8组', '光圈叶片': '7片', '放大倍率': '0.25倍'}
}

lenses.append(new_lens)

with open('/workspace/src/data/lenses.json', 'w', encoding='utf-8') as f:
    json.dump(lenses, f, ensure_ascii=False, indent=2)

print(f"已添加镜头: {new_lens['model']}")
print(f"数据库总数: {len(lenses)} 个镜头")
