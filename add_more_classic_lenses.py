import json

with open('/workspace/src/data/lenses.json', 'r', encoding='utf-8') as f:
    lenses = json.load(f)

additional_lenses = [
    # 佳能经典镜头
    {
        'id': 'canon-ef-20-28-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 20mm f/2.8 USM',
        'modelCode': 'EF20/2.8 USM', 'nickname': '超广角定焦', 'era': 'film', 'year': 1994,
        'type': 'prime', 'focalLength': '20mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 385, 'minFocusDistance': '0.25m', 'filterSize': '72mm',
        'priceNew': 4499, 'priceUsedMin': 1000, 'priceUsedMax': 2000, 'retentionRate': 42, 'ownershipCount': 'medium',
        'pros': ['超广角', '大光圈', '轻便'],
        'cons': ['无防抖'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+20mm+f2.8+USM+lens+ultrawide+prime&image_size=square',
        'purchaseAdvice': '风光摄影选择',
        'specs': {'镜片组': '10片7组', '光圈叶片': '7片', '放大倍率': '0.12倍'}
    },
    {
        'id': 'canon-ef-24-28-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 24mm f/2.8 USM',
        'modelCode': 'EF24/2.8 USM', 'nickname': '广角定焦', 'era': 'film', 'year': 1995,
        'type': 'prime', 'focalLength': '24mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 305, 'minFocusDistance': '0.25m', 'filterSize': '58mm',
        'priceNew': 3499, 'priceUsedMin': 800, 'priceUsedMax': 1500, 'retentionRate': 38, 'ownershipCount': 'medium',
        'pros': ['广角', '轻便', '价格适中'],
        'cons': ['无防抖'],
        'commonIssues': ['对焦环松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+24mm+f2.8+USM+lens+wide+angle+prime&image_size=square',
        'purchaseAdvice': '广角入门首选',
        'specs': {'镜片组': '9片7组', '光圈叶片': '7片', '放大倍率': '0.15倍'}
    },
    {
        'id': 'canon-ef-40-28-stm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 40mm f/2.8 STM',
        'modelCode': 'EF40/2.8 STM', 'nickname': '饼干头', 'era': 'digital', 'year': 2012,
        'type': 'prime', 'focalLength': '40mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 130, 'minFocusDistance': '0.3m', 'filterSize': '52mm',
        'priceNew': 1299, 'priceUsedMin': 500, 'priceUsedMax': 800, 'retentionRate': 52, 'ownershipCount': 'high',
        'pros': ['超轻便', '饼干镜头', 'STM安静'],
        'cons': ['无防抖', '光圈较小'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+40mm+f2.8+STM+lens+pancake+compact+prime&image_size=square',
        'purchaseAdvice': '便携挂机首选',
        'specs': {'镜片组': '6片5组', '光圈叶片': '7片(圆形)', '放大倍率': '0.17倍'}
    },
    {
        'id': 'canon-ef-50-14-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 50mm f/1.4 USM',
        'modelCode': 'EF50/1.4 USM', 'nickname': '标准定焦', 'era': 'digital', 'year': 1993,
        'type': 'prime', 'focalLength': '50mm', 'aperture': 'f/1.4', 'isStabilized': False,
        'weight': 380, 'minFocusDistance': '0.45m', 'filterSize': '58mm',
        'priceNew': 3999, 'priceUsedMin': 1000, 'priceUsedMax': 2000, 'retentionRate': 55, 'ownershipCount': 'high',
        'pros': ['大光圈', '成像优秀', '焦外柔美'],
        'cons': ['无防抖', '对焦偶尔犹豫'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+50mm+f1.4+USM+lens+standard+fast+prime&image_size=square',
        'purchaseAdvice': '标准定焦首选',
        'specs': {'镜片组': '8片6组', '光圈叶片': '8片(圆形)', '放大倍率': '0.15倍'}
    },
    {
        'id': 'canon-ef-85-18-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 85mm f/1.8 USM',
        'modelCode': 'EF85/1.8 USM', 'nickname': '人像入门', 'era': 'digital', 'year': 1992,
        'type': 'prime', 'focalLength': '85mm', 'aperture': 'f/1.8', 'isStabilized': False,
        'weight': 475, 'minFocusDistance': '0.85m', 'filterSize': '58mm',
        'priceNew': 3999, 'priceUsedMin': 1000, 'priceUsedMax': 2000, 'retentionRate': 52, 'ownershipCount': 'high',
        'pros': ['人像焦段', '大光圈', '价格适中'],
        'cons': ['无防抖'],
        'commonIssues': ['对焦环松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+85mm+f1.8+USM+lens+portrait+prime&image_size=square',
        'purchaseAdvice': '人像入门首选',
        'specs': {'镜片组': '8片6组', '光圈叶片': '8片(圆形)', '放大倍率': '0.12倍'}
    },
    {
        'id': 'canon-ef-100-28-l-is-macro',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 100mm f/2.8L IS USM Macro',
        'modelCode': 'EF100/2.8L IS USM Macro', 'nickname': '新百微', 'era': 'digital', 'year': 2009,
        'type': 'prime', 'focalLength': '100mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 630, 'minFocusDistance': '0.3m', 'filterSize': '67mm',
        'priceNew': 6999, 'priceUsedMin': 3000, 'priceUsedMax': 5000, 'retentionRate': 75, 'ownershipCount': 'high',
        'pros': ['1:1微距', '带防抖', 'L头品质', '人像也可用'],
        'cons': ['价格较高'],
        'commonIssues': ['防抖机构异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+100mm+f2.8L+IS+Macro+lens+closeup+professional&image_size=square',
        'purchaseAdvice': '专业微距首选',
        'specs': {'镜片组': '14片12组', '光圈叶片': '9片(圆形)', '放大倍率': '1倍', '防抖': '4档'}
    },
    {
        'id': 'canon-ef-200-28-l-ii-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 200mm f/2.8L II USM',
        'modelCode': 'EF200/2.8L II USM', 'nickname': '空气切割机II', 'era': 'digital', 'year': 2000,
        'type': 'prime', 'focalLength': '200mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 765, 'minFocusDistance': '1.5m', 'filterSize': '72mm',
        'priceNew': 10999, 'priceUsedMin': 4000, 'priceUsedMax': 6000, 'retentionRate': 68, 'ownershipCount': 'medium',
        'pros': ['大光圈长焦', '成像优秀', '相对轻便'],
        'cons': ['无防抖', '价格较高'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+200mm+f2.8L+II+USM+lens+telephoto+portrait+prime&image_size=square',
        'purchaseAdvice': '专业人像长焦首选',
        'specs': {'镜片组': '10片7组', '光圈叶片': '8片(圆形)', '放大倍率': '0.12倍'}
    },
    {
        'id': 'canon-ef-400-56-l-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 400mm f/5.6L USM',
        'modelCode': 'EF400/5.6L USM', 'nickname': '小炮', 'era': 'film', 'year': 1993,
        'type': 'prime', 'focalLength': '400mm', 'aperture': 'f/5.6', 'isStabilized': False,
        'weight': 1250, 'minFocusDistance': '3.5m', 'filterSize': '77mm',
        'priceNew': 12999, 'priceUsedMin': 4000, 'priceUsedMax': 6000, 'retentionRate': 58, 'ownershipCount': 'medium',
        'pros': ['超长焦', '相对轻便', 'L头品质'],
        'cons': ['无防抖', '价格较高'],
        'commonIssues': ['脚架环松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+400mm+f5.6L+USM+lens+super+telephoto+white&image_size=square',
        'purchaseAdvice': '鸟类摄影入门首选',
        'specs': {'镜片组': '10片8组', '光圈叶片': '8片(圆形)', '放大倍率': '0.14倍'}
    },
    {
        'id': 'canon-ef-28-135-35-56-is-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 28-135mm f/3.5-5.6 IS USM',
        'modelCode': 'EF28-135/3.5-5.6 IS USM', 'nickname': '旅游镜', 'era': 'digital', 'year': 2001,
        'type': 'zoom', 'focalLength': '28-135mm', 'aperture': 'f/3.5-5.6', 'isStabilized': True,
        'weight': 540, 'minFocusDistance': '0.5m', 'filterSize': '72mm',
        'priceNew': 4999, 'priceUsedMin': 800, 'priceUsedMax': 1500, 'retentionRate': 38, 'ownershipCount': 'high',
        'pros': ['焦段实用', '带防抖', '轻便'],
        'cons': ['光圈小', '边缘画质一般'],
        'commonIssues': ['防抖机构老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+28-135mm+IS+USM+lens+standard+zoom+travel&image_size=square',
        'purchaseAdvice': '旅游一镜走天下选择',
        'specs': {'镜片组': '12片9组', '光圈叶片': '6片', '放大倍率': '0.2倍', '防抖': '3档'}
    },
    # 适马经典镜头
    {
        'id': 'sigma-12-24-45-56-ex',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 12-24mm f/4.5-5.6 EX DG HSM',
        'modelCode': '12-24/4.5-5.6 EX DG HSM', 'nickname': '适马超广', 'era': 'digital', 'year': 2003,
        'type': 'zoom', 'focalLength': '12-24mm', 'aperture': 'f/4.5-5.6', 'isStabilized': False,
        'weight': 635, 'minFocusDistance': '0.3m', 'filterSize': '内置',
        'priceNew': 5999, 'priceUsedMin': 1500, 'priceUsedMax': 2500, 'retentionRate': 45, 'ownershipCount': 'medium',
        'pros': ['超广角', '全幅可用', '灯泡头'],
        'cons': ['无防抖', '光圈小', '价格较高'],
        'commonIssues': ['前组镜片易沾污'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+12-24mm+f4.5-5.6+EX+lens+ultrawide+zoom&image_size=square',
        'purchaseAdvice': '风光摄影选择',
        'specs': {'镜片组': '13片11组', '光圈叶片': '7片', '放大倍率': '0.12倍'}
    },
    {
        'id': 'sigma-24-70-28-ex',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 24-70mm f/2.8 EX DG HSM',
        'modelCode': '24-70/2.8 EX DG HSM', 'nickname': '适马标变', 'era': 'digital', 'year': 2008,
        'type': 'zoom', 'focalLength': '24-70mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 835, 'minFocusDistance': '0.38m', 'filterSize': '77mm',
        'priceNew': 5999, 'priceUsedMin': 1500, 'priceUsedMax': 2500, 'retentionRate': 42, 'ownershipCount': 'medium',
        'pros': ['恒定f/2.8', '成像不错', '价格适中'],
        'cons': ['无防抖', '重量较大'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+24-70mm+f2.8+EX+lens+standard+zoom&image_size=square',
        'purchaseAdvice': '标变性价比选择',
        'specs': {'镜片组': '15片12组', '光圈叶片': '9片(圆形)', '放大倍率': '0.28倍'}
    },
    {
        'id': 'sigma-70-200-28-ex',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 70-200mm f/2.8 EX DG OS HSM',
        'modelCode': '70-200/2.8 EX DG OS HSM (APO)', 'nickname': '小黑', 'era': 'digital', 'year': 2010,
        'type': 'zoom', 'focalLength': '70-200mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 1320, 'minFocusDistance': '1.0m', 'filterSize': '77mm',
        'priceNew': 7999, 'priceUsedMin': 3000, 'priceUsedMax': 5000, 'retentionRate': 58, 'ownershipCount': 'medium',
        'pros': ['恒定f/2.8', '带防抖', '成像优秀'],
        'cons': ['重量大', '价格较高'],
        'commonIssues': ['防抖机构异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+70-200mm+f2.8+EX+OS+lens+telephoto+zoom&image_size=square',
        'purchaseAdvice': '长焦性价比首选',
        'specs': {'镜片组': '20片14组', '光圈叶片': '9片(圆形)', '放大倍率': '0.22倍', '防抖': '4档'}
    },
    {
        'id': 'sigma-18-50-28-ex',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 18-50mm f/2.8 EX DC Macro',
        'modelCode': '18-50/2.8 EX DC Macro', 'nickname': '适马APS-C标变', 'era': 'digital', 'year': 2005,
        'type': 'zoom', 'focalLength': '18-50mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 510, 'minFocusDistance': '0.2m', 'filterSize': '67mm',
        'priceNew': 3499, 'priceUsedMin': 600, 'priceUsedMax': 1200, 'retentionRate': 42, 'ownershipCount': 'high',
        'pros': ['恒定f/2.8', '微距功能', 'APS-C专用'],
        'cons': ['APS-C专用', '无防抖'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+18-50mm+f2.8+EX+lens+APS-C+zoom&image_size=square',
        'purchaseAdvice': 'APS-C标变首选',
        'specs': {'镜片组': '13片10组', '光圈叶片': '7片(圆形)', '放大倍率': '0.34倍'}
    },
    # 腾龙经典镜头
    {
        'id': 'tamron-17-35-28-4-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 17-35mm f/2.8-4 Di LD Aspherical',
        'modelCode': 'SP 17-35/2.8-4 Di LD (A05)', 'nickname': '腾龙超广', 'era': 'digital', 'year': 2002,
        'type': 'zoom', 'focalLength': '17-35mm', 'aperture': 'f/2.8-4', 'isStabilized': False,
        'weight': 545, 'minFocusDistance': '0.25m', 'filterSize': '77mm',
        'priceNew': 4999, 'priceUsedMin': 1000, 'priceUsedMax': 2000, 'retentionRate': 40, 'ownershipCount': 'medium',
        'pros': ['超广角', '大光圈', '价格适中'],
        'cons': ['无防抖'],
        'commonIssues': ['镜筒松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+17-35mm+f2.8-4+Di+lens+wide+angle+zoom&image_size=square',
        'purchaseAdvice': '风光摄影选择',
        'specs': {'镜片组': '12片9组', '光圈叶片': '7片', '放大倍率': '0.15倍'}
    },
    {
        'id': 'tamron-70-200-28-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 70-200mm f/2.8 Di VC USD',
        'modelCode': 'SP 70-200/2.8 Di VC USD (A001)', 'nickname': '腾龙大三元', 'era': 'digital', 'year': 2007,
        'type': 'zoom', 'focalLength': '70-200mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 1150, 'minFocusDistance': '1.2m', 'filterSize': '77mm',
        'priceNew': 8999, 'priceUsedMin': 3000, 'priceUsedMax': 5000, 'retentionRate': 55, 'ownershipCount': 'medium',
        'pros': ['恒定f/2.8', '带防抖', '成像优秀'],
        'cons': ['重量大', '价格较高'],
        'commonIssues': ['防抖机构异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+70-200mm+f2.8+Di+VC+lens+telephoto+zoom&image_size=square',
        'purchaseAdvice': '长焦性价比首选',
        'specs': {'镜片组': '19片15组', '光圈叶片': '9片(圆形)', '放大倍率': '0.22倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-55-200-45-56-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron 55-200mm f/4-5.6 Di II LD Macro',
        'modelCode': '55-200/4-5.6 Di II LD Macro (A15)', 'nickname': '腾龙入门长焦', 'era': 'digital', 'year': 2005,
        'type': 'zoom', 'focalLength': '55-200mm', 'aperture': 'f/4-5.6', 'isStabilized': False,
        'weight': 385, 'minFocusDistance': '1.2m', 'filterSize': '52mm',
        'priceNew': 1999, 'priceUsedMin': 300, 'priceUsedMax': 600, 'retentionRate': 30, 'ownershipCount': 'high',
        'pros': ['轻便', '价格便宜', '微距功能'],
        'cons': ['APS-C专用', '无防抖', '光圈小'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+55-200mm+f4-5.6+Di+II+lens+telephoto+APS-C&image_size=square',
        'purchaseAdvice': 'APS-C长焦入门首选',
        'specs': {'镜片组': '11片8组', '光圈叶片': '7片', '放大倍率': '0.2倍'}
    },
    {
        'id': 'tamron-90-28-macro',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 90mm f/2.8 Di Macro 1:1',
        'modelCode': 'SP 90/2.8 Di Macro (272E)', 'nickname': '腾龙微距', 'era': 'digital', 'year': 2004,
        'type': 'prime', 'focalLength': '90mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 405, 'minFocusDistance': '0.29m', 'filterSize': '55mm',
        'priceNew': 3499, 'priceUsedMin': 1000, 'priceUsedMax': 2000, 'retentionRate': 52, 'ownershipCount': 'medium',
        'pros': ['1:1微距', '轻便', '价格适中'],
        'cons': ['无防抖'],
        'commonIssues': ['对焦环松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+90mm+f2.8+Macro+lens+closeup+prime&image_size=square',
        'purchaseAdvice': '微距入门首选',
        'specs': {'镜片组': '11片9组', '光圈叶片': '9片(圆形)', '放大倍率': '1倍'}
    },
    # 更多RF镜头
    {
        'id': 'canon-rf-16-28-28-is',
        'brand': 'Canon', 'mount': 'RF', 'model': 'Canon RF 16-28mm f/2.8 IS STM',
        'modelCode': 'RF16-28/2.8 IS STM', 'nickname': 'RF超广', 'era': 'mirrorless', 'year': 2023,
        'type': 'zoom', 'focalLength': '16-28mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 395, 'minFocusDistance': '0.15m', 'filterSize': '72mm',
        'priceNew': 7999, 'priceUsedMin': 5000, 'priceUsedMax': 7000, 'retentionRate': 85, 'ownershipCount': 'high',
        'pros': ['超广角', '恒定f/2.8', '轻便', '带防抖'],
        'cons': ['价格较高'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+RF+16-28mm+f2.8+IS+lens+ultrawide+zoom+mirrorless&image_size=square',
        'purchaseAdvice': 'RF口超广首选',
        'specs': {'镜片组': '12片9组', '光圈叶片': '9片(圆形)', '放大倍率': '0.25倍', '防抖': '5档'}
    },
    {
        'id': 'canon-rf-600-11-is',
        'brand': 'Canon', 'mount': 'RF', 'model': 'Canon RF 600mm f/11 IS STM',
        'modelCode': 'RF600/11 IS STM', 'nickname': 'RF中炮', 'era': 'mirrorless', 'year': 2020,
        'type': 'prime', 'focalLength': '600mm', 'aperture': 'f/11', 'isStabilized': True,
        'weight': 840, 'minFocusDistance': '3.5m', 'filterSize': '内置',
        'priceNew': 6499, 'priceUsedMin': 3500, 'priceUsedMax': 5000, 'retentionRate': 78, 'ownershipCount': 'medium',
        'pros': ['超轻便超长焦', '带防抖', 'RF原生'],
        'cons': ['光圈固定f/11'],
        'commonIssues': ['对焦慢'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+RF+600mm+f11+IS+lens+super+telephoto+compact+mirrorless&image_size=square',
        'purchaseAdvice': 'RF口超长焦入门首选',
        'specs': {'镜片组': '11片9组', '光圈叶片': '10片(圆形)', '放大倍率': '0.15倍', '防抖': '5档'}
    },
    # 更多胶片时代镜头
    {
        'id': 'canon-ef-100-300-56-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 100-300mm f/5.6L USM',
        'modelCode': 'EF100-300/5.6L USM', 'nickname': 'L头长焦', 'era': 'film', 'year': 1995,
        'type': 'zoom', 'focalLength': '100-300mm', 'aperture': 'f/5.6', 'isStabilized': False,
        'weight': 650, 'minFocusDistance': '1.5m', 'filterSize': '58mm',
        'priceNew': 6999, 'priceUsedMin': 1500, 'priceUsedMax': 2500, 'retentionRate': 48, 'ownershipCount': 'medium',
        'pros': ['L头品质', '轻便', '恒定光圈'],
        'cons': ['无防抖', '光圈较小'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+100-300mm+f5.6L+USM+lens+telephoto+zoom+vintage&image_size=square',
        'purchaseAdvice': '胶片时代长焦经典',
        'specs': {'镜片组': '10片8组', '光圈叶片': '8片(圆形)', '放大倍率': '0.12倍'}
    },
    {
        'id': 'canon-ef-75-300-45-56-iii',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 75-300mm f/4-5.6 III',
        'modelCode': 'EF75-300/4-5.6 III', 'nickname': '入门长焦', 'era': 'film', 'year': 1996,
        'type': 'zoom', 'focalLength': '75-300mm', 'aperture': 'f/4-5.6', 'isStabilized': False,
        'weight': 480, 'minFocusDistance': '1.5m', 'filterSize': '58mm',
        'priceNew': 1999, 'priceUsedMin': 200, 'priceUsedMax': 500, 'retentionRate': 25, 'ownershipCount': 'high',
        'pros': ['轻便', '价格便宜', '焦段实用'],
        'cons': ['无防抖', '画质一般'],
        'commonIssues': ['镜筒松动', '对焦不准'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+75-300mm+f4-5.6+III+lens+budget+telephoto+vintage&image_size=square',
        'purchaseAdvice': '入门长焦选择',
        'specs': {'镜片组': '10片8组', '光圈叶片': '5片', '放大倍率': '0.15倍'}
    }
]

lenses.extend(additional_lenses)

with open('/workspace/src/data/lenses.json', 'w', encoding='utf-8') as f:
    json.dump(lenses, f, ensure_ascii=False, indent=2)

print(f"已添加 {len(additional_lenses)} 个镜头")
print(f"数据库总数: {len(lenses)} 个镜头")
