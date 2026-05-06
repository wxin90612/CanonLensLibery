
import json

with open('src/data/lenses.json', 'r', encoding='utf-8') as f:
    lenses = json.load(f)

# 为现有镜头添加型号代码
model_codes = {
    # Canon EF
    'canon-ef-70-200-28l-is-usm': 'EF70-200/2.8L IS',
    'canon-ef-70-200-28l-is-ii': 'EF70-200/2.8L IS II',
    'canon-ef-24-70-28l-usm': 'EF24-70/2.8L',
    'canon-ef-16-35-28l-usm': 'EF16-35/2.8L',
    'canon-ef-16-35-28l-ii': 'EF16-35/2.8L II',
    'canon-ef-100-400-is-usm': 'EF100-400/4.5-5.6L IS',
    'canon-ef-50-18-stm': 'EF50/1.8 STM',
    'canon-ef-40-28-stm': 'EF40/2.8 STM',
    'canon-ef-s-18-55-is-stm': 'EF-S18-55/3.5-5.6 IS STM',
    'canon-ef-s-17-55-28-is': 'EF-S17-55/2.8 IS',
    'canon-ef-70-200-28l-is-iii': 'EF70-200/2.8L IS III',
    'canon-ef-70-200-4l-is-ii': 'EF70-200/4L IS II',
    'canon-ef-24-70-28l-ii': 'EF24-70/2.8L II',
    'canon-ef-100-28l-is-macro': 'EF100/2.8L IS Macro',
    'canon-ef-28-135-35-56-is': 'EF28-135/3.5-5.6 IS',
    'canon-ef-75-300-45-56-iii': 'EF75-300/4-5.6 III',
    'canon-ef-75-300-45-56-is-usm': 'EF75-300/4-5.6 IS',
    'canon-ef-300-4l-is-usm': 'EF300/4L IS',
    # Canon RF
    'canon-rf-24-105-4l-is': 'RF24-105/4L IS',
    'canon-rf-35-18-macro': 'RF35/1.8 Macro',
    'canon-rf-85-2-macro': 'RF85/2 Macro',
    'canon-rf-100-400-56-8-is': 'RF100-400/5.6-8 IS',
    'canon-rf-70-200-4l-is': 'RF70-200/4L IS',
    # Sigma
    'sigma-18-35-18-art': '18-35/1.8 DC HSM Art',
    'sigma-50-14-ex': '50/1.4 EX DG HSM',
    'sigma-24-70-28-ex': '24-70/2.8 EX DG HSM',
    'sigma-70-200-28-ex': '70-200/2.8 EX DG OS HSM',
    'sigma-50-150-28-ex': '50-150/2.8 EX DC OS HSM',
    'sigma-24-60-28-ex': '24-60/2.8 EX DG',
    'sigma-85-14-dg-dn': '85/1.4 DG DN Art',
    # Tamron
    'tamron-28-75-28-xr': 'SP 28-75/2.8 XR Di (A09)',
    'tamron-70-200-28-di': 'SP 70-200/2.8 Di (A001)',
    'tamron-90-28-macro': 'SP 90/2.8 Di Macro (G005)',
    'tamron-70-180-28-di': '70-180/2.8 Di III VXD (A056)',
    'tamron-50-400-45-63-di': '50-400/4.5-6.3 Di III VXD (A067)'
}

for lens in lenses:
    if lens['id'] in model_codes:
        lens['modelCode'] = model_codes[lens['id']]
    else:
        lens['modelCode'] = ''

# 补充更多镜头
additional_lenses = [
    {
        'id': 'tamron-18-200-35-63-di-ii',
        'brand': 'Tamron',
        'mount': 'EF',
        'model': 'Tamron 18-200mm f/3.5-6.3 Di II VC',
        'modelCode': '18-200/3.5-6.3 Di II VC (B018)',
        'nickname': '天涯镜B018',
        'year': 2011,
        'type': 'zoom',
        'focalLength': '18-200mm',
        'aperture': 'f/3.5-6.3',
        'isStabilized': True,
        'weight': 400,
        'minFocusDistance': '0.45m',
        'filterSize': '62mm',
        'priceNew': 3499,
        'priceUsedMin': 800,
        'priceUsedMax': 1500,
        'retentionRate': 42,
        'ownershipCount': 'high',
        'pros': ['一镜走天下', '轻便', '带防抖', '性价比高'],
        'cons': ['光圈小', '长焦端画质一般'],
        'commonIssues': ['镜筒进灰', '对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+18-200mm+f3.5-6.3+Di+II+VC+lens+superzoom+B018&image_size=square',
        'purchaseAdvice': '入门一镜走天下首选',
        'specs': {
            '镜片组': '14片11组',
            '光圈叶片': '7片(圆形)',
            '放大倍率': '0.42倍',
            '防抖': '4档'
        }
    },
    {
        'id': 'tamron-17-50-28-xr',
        'brand': 'Tamron',
        'mount': 'EF',
        'model': 'Tamron SP 17-50mm f/2.8 XR Di II VC',
        'modelCode': 'SP 17-50/2.8 XR Di II VC (B005)',
        'nickname': 'APS-C标变',
        'year': 2009,
        'type': 'zoom',
        'focalLength': '17-50mm',
        'aperture': 'f/2.8',
        'isStabilized': True,
        'weight': 570,
        'minFocusDistance': '0.29m',
        'filterSize': '72mm',
        'priceNew': 4999,
        'priceUsedMin': 1200,
        'priceUsedMax': 2200,
        'retentionRate': 48,
        'ownershipCount': 'high',
        'pros': ['APS-C专用', '恒定f/2.8', '带防抖', '性价比高'],
        'cons': ['APS-C专用', '边缘画质一般'],
        'commonIssues': ['对焦马达异响', '镜筒进灰'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+17-50mm+f2.8+XR+Di+II+VC+lens+APS-C+zoom+B005&image_size=square',
        'purchaseAdvice': 'APS-C用户性价比之选',
        'specs': {
            '镜片组': '19片14组',
            '光圈叶片': '7片(圆形)',
            '放大倍率': '0.25倍',
            '防抖': '4档'
        }
    },
    {
        'id': 'tamron-24-70-28-g2',
        'brand': 'Tamron',
        'mount': 'EF',
        'model': 'Tamron SP 24-70mm f/2.8 Di VC USD G2',
        'modelCode': 'SP 24-70/2.8 Di VC USD G2 (A032)',
        'nickname': 'G2标变',
        'year': 2017,
        'type': 'zoom',
        'focalLength': '24-70mm',
        'aperture': 'f/2.8',
        'isStabilized': True,
        'weight': 825,
        'minFocusDistance': '0.38m',
        'filterSize': '82mm',
        'priceNew': 7999,
        'priceUsedMin': 3500,
        'priceUsedMax': 5500,
        'retentionRate': 58,
        'ownershipCount': 'high',
        'pros': ['恒定f/2.8', '带防抖', '对焦快速', '成像优秀'],
        'cons': ['重量较大', '价格较高'],
        'commonIssues': ['对焦马达偶发异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+SP+24-70mm+f2.8+Di+VC+USD+G2+lens+professional+zoom+A032&image_size=square',
        'purchaseAdvice': '性价比标变之选',
        'specs': {
            '镜片组': '17片12组',
            '光圈叶片': '9片(圆形)',
            '放大倍率': '0.2倍',
            '防抖': '5档'
        }
    },
    {
        'id': 'sigma-18-200-35-63-dc',
        'brand': 'Sigma',
        'mount': 'EF',
        'model': 'Sigma 18-200mm f/3.5-6.3 DC OS HSM',
        'modelCode': '18-200/3.5-6.3 DC OS HSM (C014)',
        'nickname': '适马天涯镜',
        'year': 2013,
        'type': 'zoom',
        'focalLength': '18-200mm',
        'aperture': 'f/3.5-6.3',
        'isStabilized': True,
        'weight': 430,
        'minFocusDistance': '0.45m',
        'filterSize': '62mm',
        'priceNew': 3299,
        'priceUsedMin': 700,
        'priceUsedMax': 1300,
        'retentionRate': 40,
        'ownershipCount': 'medium',
        'pros': ['一镜走天下', '轻便', '带防抖'],
        'cons': ['光圈小', '长焦端画质一般'],
        'commonIssues': ['镜筒进灰', '对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+18-200mm+f3.5-6.3+DC+OS+HSM+lens+superzoom+C014&image_size=square',
        'purchaseAdvice': '入门一镜走天下选择',
        'specs': {
            '镜片组': '16片13组',
            '光圈叶片': '7片(圆形)',
            '放大倍率': '0.39倍',
            '防抖': '4档'
        }
    },
    {
        'id': 'sigma-24-70-28-art',
        'brand': 'Sigma',
        'mount': 'EF',
        'model': 'Sigma 24-70mm f/2.8 DG OS HSM Art',
        'modelCode': '24-70/2.8 DG OS HSM Art (A017)',
        'nickname': '适马标变Art',
        'year': 2017,
        'type': 'zoom',
        'focalLength': '24-70mm',
        'aperture': 'f/2.8',
        'isStabilized': True,
        'weight': 1020,
        'minFocusDistance': '0.38m',
        'filterSize': '82mm',
        'priceNew': 8999,
        'priceUsedMin': 4500,
        'priceUsedMax': 7000,
        'retentionRate': 65,
        'ownershipCount': 'high',
        'pros': ['恒定f/2.8', '带防抖', '锐度极高', '做工优秀'],
        'cons': ['重量大', '价格较高'],
        'commonIssues': ['对焦马达偶发异响', '镜筒进灰'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+24-70mm+f2.8+DG+OS+HSM+Art+lens+professional+zoom+A017&image_size=square',
        'purchaseAdvice': 'Art系列性价比之选',
        'specs': {
            '镜片组': '19片15组',
            '光圈叶片': '9片(圆形)',
            '放大倍率': '0.2倍',
            '防抖': '4档'
        }
    },
    {
        'id': 'canon-ef-50-14-usm',
        'brand': 'Canon',
        'mount': 'EF',
        'model': 'EF 50mm f/1.4 USM',
        'modelCode': 'EF50/1.4 USM',
        'nickname': '小痰盂升级款',
        'year': 2000,
        'type': 'prime',
        'focalLength': '50mm',
        'aperture': 'f/1.4',
        'isStabilized': False,
        'weight': 290,
        'minFocusDistance': '0.45m',
        'filterSize': '58mm',
        'priceNew': 2899,
        'priceUsedMin': 600,
        'priceUsedMax': 1200,
        'retentionRate': 42,
        'ownershipCount': 'high',
        'pros': ['轻便小巧', '价格实惠', '焦外柔美', '经典标头'],
        'cons': ['无防抖', '对焦速度一般', '塑料卡口'],
        'commonIssues': ['对焦环松动', '光圈叶片油润'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+50mm+f1.4+USM+lens+classic+prime&image_size=square',
        'purchaseAdvice': '入门首选，性价比极高',
        'specs': {
            '镜片组': '7片6组',
            '光圈叶片': '8片(圆形)',
            '放大倍率': '0.15倍'
        }
    },
    {
        'id': 'canon-ef-85-18-usm',
        'brand': 'Canon',
        'mount': 'EF',
        'model': 'EF 85mm f/1.8 USM',
        'modelCode': 'EF85/1.8 USM',
        'nickname': '人像入门镜',
        'year': 2000,
        'type': 'prime',
        'focalLength': '85mm',
        'aperture': 'f/1.8',
        'isStabilized': False,
        'weight': 425,
        'minFocusDistance': '0.85m',
        'filterSize': '58mm',
        'priceNew': 3999,
        'priceUsedMin': 1000,
        'priceUsedMax': 2000,
        'retentionRate': 50,
        'ownershipCount': 'high',
        'pros': ['轻便', '价格适中', '人像焦外好', '对焦快速'],
        'cons': ['无防抖', '边缘画质一般', '塑料感'],
        'commonIssues': ['对焦环阻尼变涩', '镀膜老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+85mm+f1.8+USM+lens+portrait+affordable&image_size=square',
        'purchaseAdvice': '人像入门首选，二手超值',
        'specs': {
            '镜片组': '8片6组',
            '光圈叶片': '8片(圆形)',
            '放大倍率': '0.11倍'
        }
    },
    {
        'id': 'canon-ef-s-55-250-4-56-is',
        'brand': 'Canon',
        'mount': 'EF',
        'model': 'EF-S 55-250mm f/4-5.6 IS',
        'modelCode': 'EF-S55-250/4-5.6 IS',
        'nickname': '小钢炮',
        'year': 2007,
        'type': 'zoom',
        'focalLength': '55-250mm',
        'aperture': 'f/4-5.6',
        'isStabilized': True,
        'weight': 390,
        'minFocusDistance': '1.1m',
        'filterSize': '58mm',
        'priceNew': 2499,
        'priceUsedMin': 400,
        'priceUsedMax': 800,
        'retentionRate': 32,
        'ownershipCount': 'high',
        'pros': ['轻便', '带防抖', 'APS-C专用', '便宜'],
        'cons': ['APS-C专用', '光圈小', '画质一般'],
        'commonIssues': ['镜筒松动', '对焦不准'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+EF-S+55-250mm+f4-5.6+IS+lens+APS-C+telephoto&image_size=square',
        'purchaseAdvice': 'APS-C入门长焦首选',
        'specs': {
            '镜片组': '12片10组',
            '光圈叶片': '7片(圆形)',
            '放大倍率': '0.29倍',
            '防抖': '4档'
        }
    },
    {
        'id': 'tamron-16-300-35-63-di-ii',
        'brand': 'Tamron',
        'mount': 'EF',
        'model': 'Tamron 16-300mm f/3.5-6.3 Di II VC PZD',
        'modelCode': '16-300/3.5-6.3 Di II VC PZD (B016)',
        'nickname': '超级天涯镜',
        'year': 2014,
        'type': 'zoom',
        'focalLength': '16-300mm',
        'aperture': 'f/3.5-6.3',
        'isStabilized': True,
        'weight': 615,
        'minFocusDistance': '0.39m',
        'filterSize': '67mm',
        'priceNew': 4999,
        'priceUsedMin': 1200,
        'priceUsedMax': 2200,
        'retentionRate': 45,
        'ownershipCount': 'medium',
        'pros': ['超大变焦比', '一镜走天下', '带防抖'],
        'cons': ['光圈小', '长焦端画质一般', '重量较大'],
        'commonIssues': ['镜筒进灰', '对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+16-300mm+f3.5-6.3+Di+II+VC+PZD+lens+superzoom+B016&image_size=square',
        'purchaseAdvice': '旅游一镜走天下首选',
        'specs': {
            '镜片组': '16片12组',
            '光圈叶片': '7片(圆形)',
            '放大倍率': '0.3倍',
            '防抖': '4档'
        }
    },
    {
        'id': 'sigma-150-600-5-63-contemporary',
        'brand': 'Sigma',
        'mount': 'EF',
        'model': 'Sigma 150-600mm f/5-6.3 DG OS HSM Contemporary',
        'modelCode': '150-600/5-6.3 DG OS HSM Contemporary (C015)',
        'nickname': '适马大炮C版',
        'year': 2014,
        'type': 'zoom',
        'focalLength': '150-600mm',
        'aperture': 'f/5-6.3',
        'isStabilized': True,
        'weight': 1930,
        'minFocusDistance': '2.6m',
        'filterSize': '95mm',
        'priceNew': 9999,
        'priceUsedMin': 4500,
        'priceUsedMax': 7000,
        'retentionRate': 60,
        'ownershipCount': 'medium',
        'pros': ['超长焦', '带防抖', '成像优秀', '性价比高'],
        'cons': ['重量大', '光圈小', '价格较高'],
        'commonIssues': ['镜筒伸缩卡顿', '脚架环松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+150-600mm+f5-6.3+Contemporary+lens+super+telephoto+C015&image_size=square',
        'purchaseAdvice': '打鸟入门首选',
        'specs': {
            '镜片组': '20片14组',
            '光圈叶片': '9片(圆形)',
            '放大倍率': '0.2倍',
            '防抖': '4档'
        }
    },
    {
        'id': 'canon-rf-50-18-stm',
        'brand': 'Canon',
        'mount': 'RF',
        'model': 'RF 50mm f/1.8 STM',
        'modelCode': 'RF50/1.8 STM',
        'nickname': 'RF小痰盂',
        'year': 2020,
        'type': 'prime',
        'focalLength': '50mm',
        'aperture': 'f/1.8',
        'isStabilized': False,
        'weight': 160,
        'minFocusDistance': '0.3m',
        'filterSize': '43mm',
        'priceNew': 1299,
        'priceUsedMin': 700,
        'priceUsedMax': 1000,
        'retentionRate': 75,
        'ownershipCount': 'high',
        'pros': ['极便宜', '轻便', 'STM安静', '对焦快速'],
        'cons': ['无防抖', '塑料感'],
        'commonIssues': ['卡口脆弱'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+RF+50mm+f1.8+STM+lens+compact+prime&image_size=square',
        'purchaseAdvice': 'RF入门必买',
        'specs': {
            '镜片组': '7片6组',
            '光圈叶片': '7片(圆形)',
            '放大倍率': '0.25倍'
        }
    }
]

lenses.extend(additional_lenses)

with open('src/data/lenses.json', 'w', encoding='utf-8') as f:
    json.dump(lenses, f, ensure_ascii=False, indent=2)

from collections import Counter
print(f'更新后镜头数量: {len(lenses)}')
print(f'新增镜头: {len(additional_lenses)}')
print()
print('品牌分布:')
brand_count = Counter(l['brand'] for l in lenses)
for brand, count in brand_count.items():
    print(f'  {brand}: {count}')
print()
print('年份范围:', min(l['year'] for l in lenses), '-', max(l['year'] for l in lenses))
print()
print('已添加的型号代码:')
for lens in lenses[:15]:
    if lens.get('modelCode'):
        print(f'  {lens["model"]}: {lens["modelCode"]}')

