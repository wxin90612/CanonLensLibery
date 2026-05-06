import json

with open('/workspace/src/data/lenses.json', 'r', encoding='utf-8') as f:
    lenses = json.load(f)

new_lenses = [
    {
        'id': 'tamron-150-600-5-63-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 150-600mm f/5-6.3 Di VC USD',
        'modelCode': 'SP 150-600/5-6.3 Di VC USD (A011)', 'nickname': '腾龙大炮一代', 'era': 'digital', 'year': 2014,
        'type': 'zoom', 'focalLength': '150-600mm', 'aperture': 'f/5-6.3', 'isStabilized': True,
        'weight': 1950, 'minFocusDistance': '2.5m', 'filterSize': '95mm',
        'priceNew': 8999, 'priceUsedMin': 3000, 'priceUsedMax': 5000, 'retentionRate': 52, 'ownershipCount': 'medium',
        'pros': ['超长焦', '带防抖', '成像不错', '性价比高'],
        'cons': ['重量大', '光圈较小'],
        'commonIssues': ['镜筒伸缩卡顿', '防抖机构异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+150-600mm+f5-6.3+Di+VC+lens+super+telephoto+A011&image_size=square',
        'purchaseAdvice': '野生动物摄影性价比首选',
        'specs': {'镜片组': '23片16组', '光圈叶片': '9片(圆形)', '放大倍率': '0.2倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-150-600-5-63-g2',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 150-600mm f/5-6.3 Di VC USD G2',
        'modelCode': 'SP 150-600/5-6.3 Di VC USD G2 (A022)', 'nickname': '腾龙大炮二代', 'era': 'mirrorless', 'year': 2016,
        'type': 'zoom', 'focalLength': '150-600mm', 'aperture': 'f/5-6.3', 'isStabilized': True,
        'weight': 2050, 'minFocusDistance': '2.2m', 'filterSize': '95mm',
        'priceNew': 10999, 'priceUsedMin': 5000, 'priceUsedMax': 8000, 'retentionRate': 68, 'ownershipCount': 'medium',
        'pros': ['超长焦', '防抖出色', '成像优秀', '对焦快速'],
        'cons': ['重量大', '价格较高'],
        'commonIssues': ['脚架环松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+150-600mm+f5-6.3+Di+VC+G2+lens+super+telephoto+A022&image_size=square',
        'purchaseAdvice': '专业野生动物摄影首选',
        'specs': {'镜片组': '24片16组', '光圈叶片': '9片(圆形)', '放大倍率': '0.22倍', '防抖': '4档'}
    }
]

lenses.extend(new_lenses)

with open('/workspace/src/data/lenses.json', 'w', encoding='utf-8') as f:
    json.dump(lenses, f, ensure_ascii=False, indent=2)

print(f"已添加 {len(new_lenses)} 个腾龙150-600镜头")
print(f"数据库总数: {len(lenses)} 个镜头")
