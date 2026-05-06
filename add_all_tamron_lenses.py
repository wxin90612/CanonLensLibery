import json

with open('/workspace/src/data/lenses.json', 'r', encoding='utf-8') as f:
    lenses = json.load(f)

existing_ids = {l['id'] for l in lenses}

new_lenses = [
    # 全画幅超广角变焦
    {
        'id': 'tamron-15-30-28-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 15-30mm f/2.8 Di VC USD',
        'modelCode': 'SP 15-30/2.8 Di VC USD (A012)', 'nickname': '腾龙超广一代', 'era': 'digital', 'year': 2014,
        'type': 'zoom', 'focalLength': '15-30mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 1150, 'minFocusDistance': '0.28m', 'filterSize': '95mm',
        'priceNew': 8999, 'priceUsedMin': 3000, 'priceUsedMax': 5000, 'retentionRate': 55, 'ownershipCount': 'medium',
        'pros': ['超广角', '恒定f/2.8', '带防抖'],
        'cons': ['重量大', '价格较高'],
        'commonIssues': ['镜筒松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+15-30mm+f2.8+Di+VC+lens+ultrawide+A012&image_size=square',
        'purchaseAdvice': '风光摄影首选',
        'specs': {'镜片组': '18片13组', '光圈叶片': '9片(圆形)', '放大倍率': '0.15倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-15-30-28-g2',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 15-30mm f/2.8 Di VC USD G2',
        'modelCode': 'SP 15-30/2.8 Di VC USD G2 (A041)', 'nickname': '腾龙超广二代', 'era': 'mirrorless', 'year': 2018,
        'type': 'zoom', 'focalLength': '15-30mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 1180, 'minFocusDistance': '0.22m', 'filterSize': '95mm',
        'priceNew': 9999, 'priceUsedMin': 5000, 'priceUsedMax': 8000, 'retentionRate': 72, 'ownershipCount': 'medium',
        'pros': ['超广角', '恒定f/2.8', '防抖出色', '防水防尘'],
        'cons': ['重量大', '价格较高'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+15-30mm+f2.8+Di+VC+G2+lens+ultrawide+A041&image_size=square',
        'purchaseAdvice': '专业风光首选',
        'specs': {'镜片组': '19片14组', '光圈叶片': '9片(圆形)', '放大倍率': '0.2倍', '防抖': '4档'}
    },
    {
        'id': 'tamron-17-35-28-4-osd',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron 17-35mm f/2.8-4 Di OSD',
        'modelCode': '17-35/2.8-4 Di OSD (A037)', 'nickname': '腾龙轻便超广', 'era': 'mirrorless', 'year': 2017,
        'type': 'zoom', 'focalLength': '17-35mm', 'aperture': 'f/2.8-4', 'isStabilized': False,
        'weight': 545, 'minFocusDistance': '0.28m', 'filterSize': '77mm',
        'priceNew': 4999, 'priceUsedMin': 2000, 'priceUsedMax': 3500, 'retentionRate': 58, 'ownershipCount': 'medium',
        'pros': ['轻便', '广角焦段', '价格适中'],
        'cons': ['无防抖'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+17-35mm+f2.8-4+Di+OSD+lens+wide+angle+A037&image_size=square',
        'purchaseAdvice': '风光入门首选',
        'specs': {'镜片组': '12片9组', '光圈叶片': '7片(圆形)', '放大倍率': '0.15倍'}
    },
    # 全画幅标准变焦
    {
        'id': 'tamron-28-75-28-xr',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP AF 28-75mm f/2.8 XR Di LD Aspherical (IF)',
        'modelCode': 'SP AF 28-75/2.8 XR Di LD', 'nickname': '腾龙经典标变', 'era': 'film', 'year': 2002,
        'type': 'zoom', 'focalLength': '28-75mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 580, 'minFocusDistance': '0.33m', 'filterSize': '67mm',
        'priceNew': 4499, 'priceUsedMin': 500, 'priceUsedMax': 1000, 'retentionRate': 25, 'ownershipCount': 'medium',
        'pros': ['恒定f/2.8', '轻便', '经典'],
        'cons': ['无防抖', '边缘画质一般'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+28-75mm+f2.8+XR+Di+LD+lens+standard+zoom+vintage&image_size=square',
        'purchaseAdvice': '性价比标变选择',
        'specs': {'镜片组': '14片11组', '光圈叶片': '7片', '放大倍率': '0.25倍'}
    },
    {
        'id': 'tamron-28-300-35-63-xr',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron Di 28-300mm f/3.5-6.3 XR VC',
        'modelCode': 'Di 28-300/3.5-6.3 XR VC', 'nickname': '腾龙天涯镜', 'era': 'digital', 'year': 2006,
        'type': 'zoom', 'focalLength': '28-300mm', 'aperture': 'f/3.5-6.3', 'isStabilized': True,
        'weight': 750, 'minFocusDistance': '0.5m', 'filterSize': '62mm',
        'priceNew': 4999, 'priceUsedMin': 800, 'priceUsedMax': 1500, 'retentionRate': 35, 'ownershipCount': 'medium',
        'pros': ['焦段覆盖广', '带防抖'],
        'cons': ['光圈小', '长焦端画质一般'],
        'commonIssues': ['镜筒进灰'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+28-300mm+f3.5-6.3+XR+VC+lens+superzoom&image_size=square',
        'purchaseAdvice': '旅游一镜走天下',
        'specs': {'镜片组': '16片12组', '光圈叶片': '7片', '放大倍率': '0.25倍', '防抖': '2档'}
    },
    {
        'id': 'tamron-28-200-38-56-xr',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron Di AF 28-200mm f/3.8-5.6 XR',
        'modelCode': 'Di AF 28-200/3.8-5.6 XR', 'nickname': '腾龙便携大变焦', 'era': 'film', 'year': 2001,
        'type': 'zoom', 'focalLength': '28-200mm', 'aperture': 'f/3.8-5.6', 'isStabilized': False,
        'weight': 405, 'minFocusDistance': '0.5m', 'filterSize': '58mm',
        'priceNew': 2999, 'priceUsedMin': 300, 'priceUsedMax': 600, 'retentionRate': 22, 'ownershipCount': 'medium',
        'pros': ['轻便', '焦段实用', '价格便宜'],
        'cons': ['无防抖', '光圈小'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+28-200mm+f3.8-5.6+XR+lens+compact+zoom+vintage&image_size=square',
        'purchaseAdvice': '入门便携选择',
        'specs': {'镜片组': '13片11组', '光圈叶片': '7片', '放大倍率': '0.2倍'}
    },
    # 全画幅中长焦变焦
    {
        'id': 'tamron-70-200-28-g2',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 70-200mm f/2.8 Di VC USD G2',
        'modelCode': 'SP 70-200/2.8 Di VC USD G2 (A025)', 'nickname': '腾龙长焦二代', 'era': 'mirrorless', 'year': 2017,
        'type': 'zoom', 'focalLength': '70-200mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 1215, 'minFocusDistance': '1.0m', 'filterSize': '77mm',
        'priceNew': 10999, 'priceUsedMin': 5000, 'priceUsedMax': 8000, 'retentionRate': 70, 'ownershipCount': 'medium',
        'pros': ['恒定f/2.8', '防抖出色', '成像优秀'],
        'cons': ['重量大', '价格较高'],
        'commonIssues': ['脚架环松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+70-200mm+f2.8+Di+VC+G2+lens+telephoto+A025&image_size=square',
        'purchaseAdvice': '专业长焦首选',
        'specs': {'镜片组': '21片15组', '光圈叶片': '9片(圆形)', '放大倍率': '0.25倍', '防抖': '4档'}
    },
    {
        'id': 'tamron-70-210-4-vc',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron Di 70-210mm f/4 VC USD',
        'modelCode': 'Di 70-210/4 VC USD (A034)', 'nickname': '腾龙轻便长焦', 'era': 'mirrorless', 'year': 2018,
        'type': 'zoom', 'focalLength': '70-210mm', 'aperture': 'f/4', 'isStabilized': True,
        'weight': 780, 'minFocusDistance': '1.0m', 'filterSize': '67mm',
        'priceNew': 5999, 'priceUsedMin': 3000, 'priceUsedMax': 4500, 'retentionRate': 68, 'ownershipCount': 'medium',
        'pros': ['轻便', '恒定f/4', '带防抖'],
        'cons': ['光圈较小'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+70-210mm+f4+VC+USD+lens+telephoto+lightweight+A034&image_size=square',
        'purchaseAdvice': '轻便长焦首选',
        'specs': {'镜片组': '16片12组', '光圈叶片': '9片(圆形)', '放大倍率': '0.2倍', '防抖': '4档'}
    },
    {
        'id': 'tamron-70-300-45-56-a17',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron Di 70-300mm f/4-5.6 LD',
        'modelCode': 'Di 70-300/4-5.6 LD (A17)', 'nickname': '腾龙入门长焦', 'era': 'digital', 'year': 2005,
        'type': 'zoom', 'focalLength': '70-300mm', 'aperture': 'f/4-5.6', 'isStabilized': False,
        'weight': 435, 'minFocusDistance': '1.5m', 'filterSize': '58mm',
        'priceNew': 1999, 'priceUsedMin': 300, 'priceUsedMax': 600, 'retentionRate': 28, 'ownershipCount': 'high',
        'pros': ['轻便', '价格便宜', '焦段实用'],
        'cons': ['无防抖', '画质一般'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+70-300mm+f4-5.6+LD+lens+budget+telephoto+A17&image_size=square',
        'purchaseAdvice': '入门长焦选择',
        'specs': {'镜片组': '10片8组', '光圈叶片': '7片', '放大倍率': '0.2倍'}
    },
    {
        'id': 'tamron-70-300-45-56-vc',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 70-300mm f/4-5.6 VC USD',
        'modelCode': 'SP 70-300/4-5.6 VC USD (A005)', 'nickname': '腾龙防抖长焦', 'era': 'digital', 'year': 2007,
        'type': 'zoom', 'focalLength': '70-300mm', 'aperture': 'f/4-5.6', 'isStabilized': True,
        'weight': 585, 'minFocusDistance': '1.5m', 'filterSize': '62mm',
        'priceNew': 3999, 'priceUsedMin': 1000, 'priceUsedMax': 2000, 'retentionRate': 48, 'ownershipCount': 'medium',
        'pros': ['带防抖', '焦段实用', '价格适中'],
        'cons': ['光圈小'],
        'commonIssues': ['防抖机构异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+70-300mm+f4-5.6+VC+USD+lens+telephoto+A005&image_size=square',
        'purchaseAdvice': '长焦性价比首选',
        'specs': {'镜片组': '13片10组', '光圈叶片': '9片(圆形)', '放大倍率': '0.25倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-200-500-5-63-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP AF 200-500mm f/5-6.3 Di LD (IF)',
        'modelCode': 'SP AF 200-500/5-6.3 Di LD (IF)', 'nickname': '腾龙巨炮', 'era': 'film', 'year': 2003,
        'type': 'zoom', 'focalLength': '200-500mm', 'aperture': 'f/5-6.3', 'isStabilized': False,
        'weight': 1980, 'minFocusDistance': '3.0m', 'filterSize': '82mm',
        'priceNew': 7999, 'priceUsedMin': 2000, 'priceUsedMax': 3500, 'retentionRate': 38, 'ownershipCount': 'low',
        'pros': ['超长焦', '价格适中'],
        'cons': ['重量大', '无防抖', '光圈小'],
        'commonIssues': ['镜筒松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+200-500mm+f5-6.3+Di+LD+lens+super+telephoto+vintage&image_size=square',
        'purchaseAdvice': '野生动物摄影入门',
        'specs': {'镜片组': '14片11组', '光圈叶片': '7片', '放大倍率': '0.12倍'}
    },
    # 全画幅大变焦
    {
        'id': 'tamron-35-150-28-4-vc',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron Di 35-150mm f/2.8-4 VC OSD',
        'modelCode': 'Di 35-150/2.8-4 VC OSD (A043)', 'nickname': '腾龙人像旅行', 'era': 'mirrorless', 'year': 2018,
        'type': 'zoom', 'focalLength': '35-150mm', 'aperture': 'f/2.8-4', 'isStabilized': True,
        'weight': 755, 'minFocusDistance': '0.45m', 'filterSize': '67mm',
        'priceNew': 6499, 'priceUsedMin': 3500, 'priceUsedMax': 5000, 'retentionRate': 70, 'ownershipCount': 'medium',
        'pros': ['焦段实用', '轻便', '带防抖', '性价比高'],
        'cons': ['光圈非恒定'],
        'commonIssues': ['对焦偶发不准'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+35-150mm+f2.8-4+Di+VC+lens+portrait+travel+A043&image_size=square',
        'purchaseAdvice': '人像/旅行首选',
        'specs': {'镜片组': '15片12组', '光圈叶片': '9片(圆形)', '放大倍率': '0.21倍', '防抖': '3档'}
    },
    # 全画幅定焦
    {
        'id': 'tamron-35-14-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 35mm f/1.4 Di USD',
        'modelCode': 'SP 35/1.4 Di USD (F045)', 'nickname': '腾龙旗舰人文', 'era': 'mirrorless', 'year': 2018,
        'type': 'prime', 'focalLength': '35mm', 'aperture': 'f/1.4', 'isStabilized': False,
        'weight': 630, 'minFocusDistance': '0.3m', 'filterSize': '67mm',
        'priceNew': 5999, 'priceUsedMin': 3000, 'priceUsedMax': 4500, 'retentionRate': 68, 'ownershipCount': 'medium',
        'pros': ['大光圈', '成像锐利', '人文焦段'],
        'cons': ['无防抖', '价格较高'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+35mm+f1.4+Di+USD+lens+wide+angle+fast+prime+F045&image_size=square',
        'purchaseAdvice': '人文摄影首选',
        'specs': {'镜片组': '11片9组', '光圈叶片': '9片(圆形)', '放大倍率': '0.12倍'}
    },
    {
        'id': 'tamron-35-18-vc',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 35mm f/1.8 Di VC USD',
        'modelCode': 'SP 35/1.8 Di VC USD (F012)', 'nickname': '腾龙防抖人文', 'era': 'digital', 'year': 2014,
        'type': 'prime', 'focalLength': '35mm', 'aperture': 'f/1.8', 'isStabilized': True,
        'weight': 480, 'minFocusDistance': '0.3m', 'filterSize': '58mm',
        'priceNew': 3999, 'priceUsedMin': 1500, 'priceUsedMax': 2500, 'retentionRate': 55, 'ownershipCount': 'medium',
        'pros': ['带防抖', '人文焦段', '价格适中'],
        'cons': ['光圈较小'],
        'commonIssues': ['防抖机构异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+35mm+f1.8+Di+VC+lens+wide+angle+prime+F012&image_size=square',
        'purchaseAdvice': '人文摄影性价比首选',
        'specs': {'镜片组': '10片8组', '光圈叶片': '9片(圆形)', '放大倍率': '0.15倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-45-18-vc',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 45mm f/1.8 Di VC USD',
        'modelCode': 'SP 45/1.8 Di VC USD (F013)', 'nickname': '腾龙防抖标准', 'era': 'digital', 'year': 2015,
        'type': 'prime', 'focalLength': '45mm', 'aperture': 'f/1.8', 'isStabilized': True,
        'weight': 415, 'minFocusDistance': '0.35m', 'filterSize': '58mm',
        'priceNew': 3499, 'priceUsedMin': 1500, 'priceUsedMax': 2500, 'retentionRate': 52, 'ownershipCount': 'medium',
        'pros': ['带防抖', '标准焦段', '轻便'],
        'cons': ['光圈较小'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+45mm+f1.8+Di+VC+lens+standard+prime+F013&image_size=square',
        'purchaseAdvice': '标准定焦选择',
        'specs': {'镜片组': '9片7组', '光圈叶片': '9片(圆形)', '放大倍率': '0.17倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-85-18-vc',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 85mm f/1.8 Di VC USD',
        'modelCode': 'SP 85/1.8 Di VC USD (F016)', 'nickname': '腾龙防抖人像', 'era': 'digital', 'year': 2016,
        'type': 'prime', 'focalLength': '85mm', 'aperture': 'f/1.8', 'isStabilized': True,
        'weight': 545, 'minFocusDistance': '0.8m', 'filterSize': '72mm',
        'priceNew': 4999, 'priceUsedMin': 2500, 'priceUsedMax': 4000, 'retentionRate': 62, 'ownershipCount': 'medium',
        'pros': ['带防抖', '人像焦段', '成像优秀'],
        'cons': ['价格较高'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+85mm+f1.8+Di+VC+lens+portrait+prime+F016&image_size=square',
        'purchaseAdvice': '人像定焦首选',
        'specs': {'镜片组': '10片8组', '光圈叶片': '9片(圆形)', '放大倍率': '0.12倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-90-28-macro-vc',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 90mm f/2.8 Di Macro VC USD',
        'modelCode': 'SP 90/2.8 Di Macro VC USD (F017)', 'nickname': '腾龙防抖微距', 'era': 'digital', 'year': 2013,
        'type': 'prime', 'focalLength': '90mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 555, 'minFocusDistance': '0.29m', 'filterSize': '62mm',
        'priceNew': 4999, 'priceUsedMin': 2000, 'priceUsedMax': 3500, 'retentionRate': 65, 'ownershipCount': 'medium',
        'pros': ['1:1微距', '带防抖', '成像优秀'],
        'cons': ['价格较高'],
        'commonIssues': ['防抖机构异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+90mm+f2.8+Macro+VC+lens+closeup+prime+F017&image_size=square',
        'purchaseAdvice': '专业微距首选',
        'specs': {'镜片组': '12片9组', '光圈叶片': '9片(圆形)', '放大倍率': '1倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-180-35-macro',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP AF 180mm f/3.5 Di LD (IF) Macro',
        'modelCode': 'SP AF 180/3.5 Di LD (IF) Macro (B01)', 'nickname': '腾龙长焦微距', 'era': 'film', 'year': 2000,
        'type': 'prime', 'focalLength': '180mm', 'aperture': 'f/3.5', 'isStabilized': False,
        'weight': 920, 'minFocusDistance': '0.45m', 'filterSize': '72mm',
        'priceNew': 5999, 'priceUsedMin': 1500, 'priceUsedMax': 2500, 'retentionRate': 42, 'ownershipCount': 'medium',
        'pros': ['1:1微距', '长焦微距', '背景虚化好'],
        'cons': ['重量大', '无防抖', '价格较高'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+180mm+f3.5+Macro+lens+telephoto+closeup+B01&image_size=square',
        'purchaseAdvice': '专业微距选择',
        'specs': {'镜片组': '14片11组', '光圈叶片': '9片(圆形)', '放大倍率': '1倍'}
    },
    # APS-C广角变焦
    {
        'id': 'tamron-10-24-35-45-vc',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron 10-24mm f/3.5-4.5 Di II VC HLD',
        'modelCode': '10-24/3.5-4.5 Di II VC HLD (B023)', 'nickname': '腾龙APS-C超广二代', 'era': 'mirrorless', 'year': 2016,
        'type': 'zoom', 'focalLength': '10-24mm', 'aperture': 'f/3.5-4.5', 'isStabilized': True,
        'weight': 415, 'minFocusDistance': '0.2m', 'filterSize': '77mm',
        'priceNew': 4499, 'priceUsedMin': 2000, 'priceUsedMax': 3500, 'retentionRate': 58, 'ownershipCount': 'medium',
        'pros': ['APS-C超广角', '带防抖', '轻便'],
        'cons': ['APS-C专用'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+10-24mm+f3.5-4.5+Di+II+VC+lens+ultrawide+APS-C+B023&image_size=square',
        'purchaseAdvice': 'APS-C风光首选',
        'specs': {'镜片组': '13片10组', '光圈叶片': '7片', '放大倍率': '0.15倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-11-18-45-56-a13',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP AF 11-18mm f/4.5-5.6 Di II LD Aspherical (IF)',
        'modelCode': 'SP AF 11-18/4.5-5.6 Di II LD (A13)', 'nickname': '腾龙APS-C超广', 'era': 'digital', 'year': 2003,
        'type': 'zoom', 'focalLength': '11-18mm', 'aperture': 'f/4.5-5.6', 'isStabilized': False,
        'weight': 345, 'minFocusDistance': '0.2m', 'filterSize': '77mm',
        'priceNew': 3499, 'priceUsedMin': 500, 'priceUsedMax': 1000, 'retentionRate': 32, 'ownershipCount': 'medium',
        'pros': ['APS-C超广角', '轻便', '价格适中'],
        'cons': ['APS-C专用', '无防抖', '光圈小'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+11-18mm+f4.5-5.6+Di+II+lens+ultrawide+APS-C+A13&image_size=square',
        'purchaseAdvice': 'APS-C风光入门首选',
        'specs': {'镜片组': '11片8组', '光圈叶片': '7片', '放大倍率': '0.12倍'}
    },
    # APS-C标准变焦
    {
        'id': 'tamron-17-50-28-a16',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP AF 17-50mm f/2.8 XR Di II LD Aspherical (IF)',
        'modelCode': 'SP AF 17-50/2.8 XR Di II LD (A16)', 'nickname': '腾龙APS-C标变', 'era': 'digital', 'year': 2006,
        'type': 'zoom', 'focalLength': '17-50mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 430, 'minFocusDistance': '0.27m', 'filterSize': '67mm',
        'priceNew': 2999, 'priceUsedMin': 500, 'priceUsedMax': 1000, 'retentionRate': 35, 'ownershipCount': 'high',
        'pros': ['恒定f/2.8', '轻便', '价格适中'],
        'cons': ['APS-C专用', '无防抖'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+17-50mm+f2.8+XR+Di+II+lens+APS-C+zoom+A16&image_size=square',
        'purchaseAdvice': 'APS-C标变首选',
        'specs': {'镜片组': '13片10组', '光圈叶片': '7片', '放大倍率': '0.2倍'}
    },
    # APS-C大变焦
    {
        'id': 'tamron-18-200-35-63-a14',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron AF 18-200mm f/3.5-6.3 XR Di II LD Aspherical (IF) Macro',
        'modelCode': 'AF 18-200/3.5-6.3 XR Di II LD (A14)', 'nickname': '腾龙第一代天涯', 'era': 'digital', 'year': 2005,
        'type': 'zoom', 'focalLength': '18-200mm', 'aperture': 'f/3.5-6.3', 'isStabilized': False,
        'weight': 405, 'minFocusDistance': '0.45m', 'filterSize': '62mm',
        'priceNew': 2999, 'priceUsedMin': 300, 'priceUsedMax': 600, 'retentionRate': 28, 'ownershipCount': 'high',
        'pros': ['轻便', '焦段覆盖广', '价格便宜'],
        'cons': ['APS-C专用', '无防抖', '光圈小'],
        'commonIssues': ['镜筒进灰'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+18-200mm+f3.5-6.3+XR+Di+II+lens+superzoom+APS-C+A14&image_size=square',
        'purchaseAdvice': 'APS-C入门一镜走天下',
        'specs': {'镜片组': '13片11组', '光圈叶片': '7片', '放大倍率': '0.25倍'}
    },
    {
        'id': 'tamron-18-250-35-63-a18',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron AF 18-250mm f/3.5-6.3 Di II LD Aspherical (IF) Macro',
        'modelCode': 'AF 18-250/3.5-6.3 Di II LD (A18)', 'nickname': '腾龙13.9倍变焦', 'era': 'digital', 'year': 2007,
        'type': 'zoom', 'focalLength': '18-250mm', 'aperture': 'f/3.5-6.3', 'isStabilized': False,
        'weight': 480, 'minFocusDistance': '0.45m', 'filterSize': '62mm',
        'priceNew': 3499, 'priceUsedMin': 500, 'priceUsedMax': 1000, 'retentionRate': 32, 'ownershipCount': 'medium',
        'pros': ['焦段覆盖极广', '轻便'],
        'cons': ['APS-C专用', '无防抖', '光圈小'],
        'commonIssues': ['镜筒松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+18-250mm+f3.5-6.3+Di+II+lens+superzoom+APS-C+A18&image_size=square',
        'purchaseAdvice': 'APS-C超级天涯选择',
        'specs': {'镜片组': '14片11组', '光圈叶片': '7片', '放大倍率': '0.25倍'}
    },
    {
        'id': 'tamron-18-270-35-63-b003',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron AF 18-270mm f/3.5-6.3 Di II VC LD Aspherical (IF) Macro',
        'modelCode': 'AF 18-270/3.5-6.3 Di II VC LD (B003)', 'nickname': '腾龙带防抖天涯', 'era': 'digital', 'year': 2009,
        'type': 'zoom', 'focalLength': '18-270mm', 'aperture': 'f/3.5-6.3', 'isStabilized': True,
        'weight': 550, 'minFocusDistance': '0.49m', 'filterSize': '67mm',
        'priceNew': 3999, 'priceUsedMin': 800, 'priceUsedMax': 1500, 'retentionRate': 38, 'ownershipCount': 'medium',
        'pros': ['焦段覆盖极广', '带防抖'],
        'cons': ['APS-C专用', '光圈小'],
        'commonIssues': ['防抖机构异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+18-270mm+f3.5-6.3+Di+II+VC+lens+superzoom+APS-C+B003&image_size=square',
        'purchaseAdvice': 'APS-C旅游首选',
        'specs': {'镜片组': '15片12组', '光圈叶片': '7片', '放大倍率': '0.25倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-18-270-35-63-b008',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron 18-270mm f/3.5-6.3 Di II VC PZD',
        'modelCode': '18-270/3.5-6.3 Di II VC PZD (B008)', 'nickname': '腾龙超声波天涯', 'era': 'digital', 'year': 2012,
        'type': 'zoom', 'focalLength': '18-270mm', 'aperture': 'f/3.5-6.3', 'isStabilized': True,
        'weight': 525, 'minFocusDistance': '0.45m', 'filterSize': '67mm',
        'priceNew': 4499, 'priceUsedMin': 1000, 'priceUsedMax': 2000, 'retentionRate': 42, 'ownershipCount': 'medium',
        'pros': ['焦段覆盖极广', '带防抖', 'PZD安静'],
        'cons': ['APS-C专用', '光圈小'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+18-270mm+f3.5-6.3+Di+II+VC+PZD+lens+superzoom+APS-C+B008&image_size=square',
        'purchaseAdvice': 'APS-C旅游首选',
        'specs': {'镜片组': '15片12组', '光圈叶片': '7片(圆形)', '放大倍率': '0.25倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-18-400-35-63-b028',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron 18-400mm f/3.5-6.3 Di II VC HLD',
        'modelCode': '18-400/3.5-6.3 Di II VC HLD (B028)', 'nickname': '腾龙超级变焦', 'era': 'mirrorless', 'year': 2016,
        'type': 'zoom', 'focalLength': '18-400mm', 'aperture': 'f/3.5-6.3', 'isStabilized': True,
        'weight': 630, 'minFocusDistance': '0.45m', 'filterSize': '72mm',
        'priceNew': 4999, 'priceUsedMin': 2000, 'priceUsedMax': 3500, 'retentionRate': 52, 'ownershipCount': 'medium',
        'pros': ['22.2倍超大变焦', '带防抖', 'HLD马达'],
        'cons': ['APS-C专用', '光圈小', '长焦端画质一般'],
        'commonIssues': ['镜筒进灰'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+18-400mm+f3.5-6.3+Di+II+VC+lens+superzoom+APS-C+B028&image_size=square',
        'purchaseAdvice': 'APS-C终极一镜走天下',
        'specs': {'镜片组': '16片13组', '光圈叶片': '9片(圆形)', '放大倍率': '0.3倍', '防抖': '3档'}
    },
    # APS-C微距定焦
    {
        'id': 'tamron-60-2-macro',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP AF 60mm f/2 Di II LD (IF) Macro 1:1',
        'modelCode': 'SP AF 60/2 Di II LD (IF) Macro (G005)', 'nickname': '腾龙APS-C微距', 'era': 'digital', 'year': 2006,
        'type': 'prime', 'focalLength': '60mm', 'aperture': 'f/2', 'isStabilized': False,
        'weight': 405, 'minFocusDistance': '0.18m', 'filterSize': '52mm',
        'priceNew': 3499, 'priceUsedMin': 1000, 'priceUsedMax': 2000, 'retentionRate': 48, 'ownershipCount': 'medium',
        'pros': ['1:1微距', '大光圈', '轻便'],
        'cons': ['APS-C专用', '无防抖'],
        'commonIssues': ['对焦环松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+60mm+f2+Macro+lens+closeup+APS-C+G005&image_size=square',
        'purchaseAdvice': 'APS-C微距首选',
        'specs': {'镜片组': '10片8组', '光圈叶片': '9片(圆形)', '放大倍率': '1倍'}
    }
]

filtered_new_lenses = [l for l in new_lenses if l['id'] not in existing_ids]

lenses.extend(filtered_new_lenses)

with open('/workspace/src/data/lenses.json', 'w', encoding='utf-8') as f:
    json.dump(lenses, f, ensure_ascii=False, indent=2)

print(f"已添加 {len(filtered_new_lenses)} 个新的腾龙镜头")
print(f"数据库总数: {len(lenses)} 个镜头")
