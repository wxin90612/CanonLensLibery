import json

# 读取现有镜头数据
with open('/workspace/src/data/lenses.json', 'r', encoding='utf-8') as f:
    lenses = json.load(f)

# 添加更多镜头
additional_lenses = [
    # 更多EF镜头
    {
        'id': 'canon-ef-17-40-4l-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 17-40mm f/4L USM',
        'modelCode': 'EF17-40/4L USM', 'nickname': '小三元超广', 'era': 'digital', 'year': 2003,
        'type': 'zoom', 'focalLength': '17-40mm', 'aperture': 'f/4', 'isStabilized': False,
        'weight': 545, 'minFocusDistance': '0.28m', 'filterSize': '77mm',
        'priceNew': 7999, 'priceUsedMin': 2000, 'priceUsedMax': 3500, 'retentionRate': 45, 'ownershipCount': 'high',
        'pros': ['L头品质', '轻便', '星芒效果好', '价格适中'],
        'cons': ['无防抖', '光圈较小'],
        'commonIssues': ['前组镜片易沾污'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+17-40mm+f4L+USM+lens+wide+angle+zoom&image_size=square',
        'purchaseAdvice': '风光入门首选',
        'specs': {'镜片组': '10片8组', '光圈叶片': '7片(圆形)', '放大倍率': '0.2倍'}
    },
    {
        'id': 'canon-ef-24-105-35-56-is-stm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 24-105mm f/3.5-5.6 IS STM',
        'modelCode': 'EF24-105/3.5-5.6 IS STM', 'nickname': '便携标变', 'era': 'digital', 'year': 2014,
        'type': 'zoom', 'focalLength': '24-105mm', 'aperture': 'f/3.5-5.6', 'isStabilized': True,
        'weight': 525, 'minFocusDistance': '0.35m', 'filterSize': '77mm',
        'priceNew': 5499, 'priceUsedMin': 2500, 'priceUsedMax': 4000, 'retentionRate': 55, 'ownershipCount': 'high',
        'pros': ['轻便', '焦段实用', '带防抖', 'STM安静'],
        'cons': ['光圈小', '边缘画质一般'],
        'commonIssues': ['对焦偶发不准'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+24-105mm+f3.5-5.6+IS+STM+lens+standard+zoom+compact&image_size=square',
        'purchaseAdvice': '便携旅游首选',
        'specs': {'镜片组': '13片10组', '光圈叶片': '7片(圆形)', '放大倍率': '0.23倍', '防抖': '4档'}
    },
    {
        'id': 'sigma-24-105-4-art',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 24-105mm f/4 DG OS HSM Art',
        'modelCode': '24-105/4 DG OS HSM Art', 'nickname': '适马Art标变', 'era': 'digital', 'year': 2016,
        'type': 'zoom', 'focalLength': '24-105mm', 'aperture': 'f/4', 'isStabilized': True,
        'weight': 815, 'minFocusDistance': '0.45m', 'filterSize': '82mm',
        'priceNew': 5999, 'priceUsedMin': 3000, 'priceUsedMax': 4500, 'retentionRate': 62, 'ownershipCount': 'medium',
        'pros': ['成像锐利', '带防抖', '做工扎实'],
        'cons': ['重量较大', '价格较高'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+24-105mm+f4+Art+lens+standard+zoom+professional&image_size=square',
        'purchaseAdvice': '标变性价比首选',
        'specs': {'镜片组': '17片13组', '光圈叶片': '9片(圆形)', '放大倍率': '0.21倍', '防抖': '4档'}
    },
    {
        'id': 'tamron-24-70-28-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 24-70mm f/2.8 Di VC USD',
        'modelCode': 'SP 24-70/2.8 Di VC USD (A007)', 'nickname': '腾龙2470', 'era': 'digital', 'year': 2012,
        'type': 'zoom', 'focalLength': '24-70mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 905, 'minFocusDistance': '0.38m', 'filterSize': '77mm',
        'priceNew': 6999, 'priceUsedMin': 2500, 'priceUsedMax': 4000, 'retentionRate': 45, 'ownershipCount': 'medium',
        'pros': ['恒定f/2.8', '带防抖', '价格适中'],
        'cons': ['重量较大', '边缘画质一般'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+24-70mm+f2.8+Di+VC+lens+standard+zoom+professional&image_size=square',
        'purchaseAdvice': '性价比标变选择',
        'specs': {'镜片组': '15片12组', '光圈叶片': '9片(圆形)', '放大倍率': '0.27倍', '防抖': '3档'}
    },
    {
        'id': 'canon-ef-s-18-135-35-56-is-stm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF-S 18-135mm f/3.5-5.6 IS STM',
        'modelCode': 'EF-S18-135/3.5-5.6 IS STM', 'nickname': 'APS-C天涯镜', 'era': 'digital', 'year': 2012,
        'type': 'zoom', 'focalLength': '18-135mm', 'aperture': 'f/3.5-5.6', 'isStabilized': True,
        'weight': 480, 'minFocusDistance': '0.45m', 'filterSize': '67mm',
        'priceNew': 2999, 'priceUsedMin': 800, 'priceUsedMax': 1500, 'retentionRate': 42, 'ownershipCount': 'high',
        'pros': ['焦段实用', '轻便', '带防抖'],
        'cons': ['APS-C专用', '光圈小', '长焦端画质一般'],
        'commonIssues': ['镜筒松动'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+EF-S+18-135mm+IS+STM+lens+APS-C+zoom+kit&image_size=square',
        'purchaseAdvice': 'APS-C一镜走天下首选',
        'specs': {'镜片组': '12片9组', '光圈叶片': '6片', '放大倍率': '0.21倍', '防抖': '3档'}
    },
    {
        'id': 'canon-ef-s-18-200-35-56-is',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF-S 18-200mm f/3.5-5.6 IS',
        'modelCode': 'EF-S18-200/3.5-5.6 IS', 'nickname': 'APS-C超级天涯', 'era': 'digital', 'year': 2008,
        'type': 'zoom', 'focalLength': '18-200mm', 'aperture': 'f/3.5-5.6', 'isStabilized': True,
        'weight': 595, 'minFocusDistance': '0.45m', 'filterSize': '72mm',
        'priceNew': 4499, 'priceUsedMin': 1000, 'priceUsedMax': 1800, 'retentionRate': 38, 'ownershipCount': 'medium',
        'pros': ['焦段覆盖广', '带防抖'],
        'cons': ['APS-C专用', '光圈小', '长焦端画质差'],
        'commonIssues': ['镜筒进灰', '对焦不准'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+EF-S+18-200mm+IS+lens+superzoom+APS-C&image_size=square',
        'purchaseAdvice': '旅游一镜走天下选择',
        'specs': {'镜片组': '16片12组', '光圈叶片': '6片', '放大倍率': '0.24倍', '防抖': '3档'}
    },
    {
        'id': 'sigma-10-20-35-45-ex',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 10-20mm f/3.5 EX DC HSM',
        'modelCode': '10-20/3.5 EX DC HSM', 'nickname': '适马超广', 'era': 'digital', 'year': 2010,
        'type': 'zoom', 'focalLength': '10-20mm', 'aperture': 'f/3.5', 'isStabilized': False,
        'weight': 560, 'minFocusDistance': '0.24m', 'filterSize': '82mm',
        'priceNew': 4499, 'priceUsedMin': 1200, 'priceUsedMax': 2000, 'retentionRate': 40, 'ownershipCount': 'medium',
        'pros': ['恒定f/3.5', 'APS-C超广角', '成像不错'],
        'cons': ['APS-C专用', '无防抖', '重量较大'],
        'commonIssues': ['对焦马达故障'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+10-20mm+f3.5+EX+lens+ultrawide+APS-C&image_size=square',
        'purchaseAdvice': 'APS-C风光入门首选',
        'specs': {'镜片组': '13片10组', '光圈叶片': '7片', '放大倍率': '0.15倍'}
    },
    {
        'id': 'tamron-28-300-35-63-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron 28-300mm f/3.5-6.3 Di VC PZD',
        'modelCode': '28-300/3.5-6.3 Di VC PZD (A010)', 'nickname': '全幅天涯镜', 'era': 'digital', 'year': 2012,
        'type': 'zoom', 'focalLength': '28-300mm', 'aperture': 'f/3.5-6.3', 'isStabilized': True,
        'weight': 805, 'minFocusDistance': '0.45m', 'filterSize': '67mm',
        'priceNew': 5999, 'priceUsedMin': 1500, 'priceUsedMax': 2800, 'retentionRate': 42, 'ownershipCount': 'medium',
        'pros': ['全幅一镜走天下', '带防抖', '焦段覆盖广'],
        'cons': ['光圈小', '长焦端画质一般', '重量较大'],
        'commonIssues': ['镜筒进灰', '对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+28-300mm+f3.5-6.3+Di+VC+lens+superzoom+fullframe&A010&image_size=square',
        'purchaseAdvice': '全幅旅游一镜走天下首选',
        'specs': {'镜片组': '18片14组', '光圈叶片': '7片(圆形)', '放大倍率': '0.3倍', '防抖': '3档'}
    },
    {
        'id': 'canon-ef-60-28-macro',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 60mm f/2.8 Macro USM',
        'modelCode': 'EF60/2.8 Macro USM', 'nickname': '微距入门', 'era': 'digital', 'year': 2005,
        'type': 'prime', 'focalLength': '60mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 385, 'minFocusDistance': '0.2m', 'filterSize': '52mm',
        'priceNew': 2999, 'priceUsedMin': 800, 'priceUsedMax': 1500, 'retentionRate': 45, 'ownershipCount': 'medium',
        'pros': ['1:1微距', '轻便', '价格适中', '人像也可用'],
        'cons': ['无防抖', '焦段较短'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+60mm+f2.8+Macro+lens+closeup+prime+compact&image_size=square',
        'purchaseAdvice': '微距入门首选',
        'specs': {'镜片组': '10片8组', '光圈叶片': '8片(圆形)', '放大倍率': '1倍'}
    },
    {
        'id': 'sigma-150-28-macro',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 150mm f/2.8 EX DG OS HSM Macro',
        'modelCode': '150/2.8 EX DG OS HSM Macro', 'nickname': '适马微距', 'era': 'digital', 'year': 2008,
        'type': 'prime', 'focalLength': '150mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 815, 'minFocusDistance': '0.39m', 'filterSize': '72mm',
        'priceNew': 5999, 'priceUsedMin': 2500, 'priceUsedMax': 4000, 'retentionRate': 52, 'ownershipCount': 'medium',
        'pros': ['1:1微距', '长焦微距', '带防抖', '背景虚化好'],
        'cons': ['重量较大', '价格较高'],
        'commonIssues': ['防抖机构故障'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+150mm+f2.8+macro+lens+telephoto+closeup&image_size=square',
        'purchaseAdvice': '专业微距选择',
        'specs': {'镜片组': '15片12组', '光圈叶片': '9片(圆形)', '放大倍率': '1倍', '防抖': '4档'}
    },
    # RF卡口补充
    {
        'id': 'canon-rf-15-35-28-l',
        'brand': 'Canon', 'mount': 'RF', 'model': 'Canon RF 15-35mm f/2.8L IS USM',
        'modelCode': 'RF15-35/2.8L IS USM', 'nickname': 'RF大三元超广', 'era': 'mirrorless', 'year': 2020,
        'type': 'zoom', 'focalLength': '15-35mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 795, 'minFocusDistance': '0.18m', 'filterSize': '82mm',
        'priceNew': 14999, 'priceUsedMin': 10000, 'priceUsedMax': 13000, 'retentionRate': 88, 'ownershipCount': 'high',
        'pros': ['超广角', '恒定f/2.8', '带防抖', '成像优秀'],
        'cons': ['价格昂贵', '重量较大'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+RF+15-35mm+f2.8L+IS+lens+ultrawide+mirrorless&image_size=square',
        'purchaseAdvice': 'RF口风光首选',
        'specs': {'镜片组': '16片12组', '光圈叶片': '9片(圆形)', '放大倍率': '0.23倍', '防抖': '5档'}
    },
    {
        'id': 'canon-rf-24-70-28-l',
        'brand': 'Canon', 'mount': 'RF', 'model': 'Canon RF 24-70mm f/2.8L IS USM',
        'modelCode': 'RF24-70/2.8L IS USM', 'nickname': 'RF镜皇', 'era': 'mirrorless', 'year': 2021,
        'type': 'zoom', 'focalLength': '24-70mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 805, 'minFocusDistance': '0.21m', 'filterSize': '82mm',
        'priceNew': 15999, 'priceUsedMin': 11000, 'priceUsedMax': 14000, 'retentionRate': 90, 'ownershipCount': 'high',
        'pros': ['成像锐利', '对焦快速', '带防抖', 'RF原生'],
        'cons': ['价格昂贵'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+RF+24-70mm+f2.8L+IS+lens+standard+zoom+professional&image_size=square',
        'purchaseAdvice': 'RF口标变首选',
        'specs': {'镜片组': '17片12组', '光圈叶片': '9片(圆形)', '放大倍率': '0.31倍', '防抖': '5档'}
    },
    {
        'id': 'canon-rf-70-200-28-l',
        'brand': 'Canon', 'mount': 'RF', 'model': 'Canon RF 70-200mm f/2.8L IS USM',
        'modelCode': 'RF70-200/2.8L IS USM', 'nickname': 'RF大三元长焦', 'era': 'mirrorless', 'year': 2021,
        'type': 'zoom', 'focalLength': '70-200mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 1070, 'minFocusDistance': '0.7m', 'filterSize': '77mm',
        'priceNew': 19999, 'priceUsedMin': 14000, 'priceUsedMax': 18000, 'retentionRate': 92, 'ownershipCount': 'high',
        'pros': ['超轻便', '成像锐利', '对焦快速', '防抖出色'],
        'cons': ['价格昂贵'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+RF+70-200mm+f2.8L+IS+lens+telephoto+professional+mirrorless&image_size=square',
        'purchaseAdvice': 'RF口长焦首选',
        'specs': {'镜片组': '21片15组', '光圈叶片': '9片(圆形)', '放大倍率': '0.34倍', '防抖': '5档'}
    },
    {
        'id': 'canon-rf-100-500-45-71-l',
        'brand': 'Canon', 'mount': 'RF', 'model': 'Canon RF 100-500mm f/4.5-7.1L IS USM',
        'modelCode': 'RF100-500/4.5-7.1L IS USM', 'nickname': 'RF大白', 'era': 'mirrorless', 'year': 2020,
        'type': 'zoom', 'focalLength': '100-500mm', 'aperture': 'f/4.5-7.1', 'isStabilized': True,
        'weight': 1370, 'minFocusDistance': '1.2m', 'filterSize': '77mm',
        'priceNew': 16999, 'priceUsedMin': 11000, 'priceUsedMax': 15000, 'retentionRate': 88, 'ownershipCount': 'high',
        'pros': ['超长焦', '相对轻便', '带防抖', '成像优秀'],
        'cons': ['光圈较小', '价格昂贵'],
        'commonIssues': ['对焦偶发拉风箱'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+RF+100-500mm+f4.5-7.1L+IS+lens+super+telephoto+mirrorless&image_size=square',
        'purchaseAdvice': 'RF口野生动物摄影首选',
        'specs': {'镜片组': '21片15组', '光圈叶片': '9片(圆形)', '放大倍率': '0.33倍', '防抖': '5档'}
    },
    {
        'id': 'canon-rf-28-70-2l',
        'brand': 'Canon', 'mount': 'RF', 'model': 'Canon RF 28-70mm f/2L USM',
        'modelCode': 'RF28-70/2L USM', 'nickname': 'RF超大光圈标变', 'era': 'mirrorless', 'year': 2022,
        'type': 'zoom', 'focalLength': '28-70mm', 'aperture': 'f/2', 'isStabilized': False,
        'weight': 1430, 'minFocusDistance': '0.3m', 'filterSize': '82mm',
        'priceNew': 24999, 'priceUsedMin': 18000, 'priceUsedMax': 22000, 'retentionRate': 90, 'ownershipCount': 'medium',
        'pros': ['超大光圈', '成像锐利', '焦外柔美'],
        'cons': ['重量大', '价格昂贵', '无防抖'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+RF+28-70mm+f2L+lens+fast+standard+zoom+professional&image_size=square',
        'purchaseAdvice': '专业人像/视频首选',
        'specs': {'镜片组': '21片15组', '光圈叶片': '10片(圆形)', '放大倍率': '0.21倍'}
    },
    # 更多适马Art镜头
    {
        'id': 'sigma-20-14-art',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 20mm f/1.4 DG HSM Art',
        'modelCode': '20/1.4 DG HSM Art', 'nickname': '适马Art超广角', 'era': 'mirrorless', 'year': 2018,
        'type': 'prime', 'focalLength': '20mm', 'aperture': 'f/1.4', 'isStabilized': False,
        'weight': 845, 'minFocusDistance': '0.2m', 'filterSize': '82mm',
        'priceNew': 6499, 'priceUsedMin': 3500, 'priceUsedMax': 5000, 'retentionRate': 68, 'ownershipCount': 'medium',
        'pros': ['超大光圈超广角', '成像锐利', '星空神器'],
        'cons': ['重量大', '无防抖', '价格较高'],
        'commonIssues': ['对焦马达异响'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+20mm+f1.4+Art+lens+wide+angle+fast+prime&image_size=square',
        'purchaseAdvice': '星空摄影首选',
        'specs': {'镜片组': '15片11组', '光圈叶片': '9片(圆形)', '放大倍率': '0.12倍'}
    },
    {
        'id': 'sigma-105-14-art',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 105mm f/1.4 DG HSM Art',
        'modelCode': '105/1.4 DG HSM Art', 'nickname': '适马Art长焦人像', 'era': 'mirrorless', 'year': 2018,
        'type': 'prime', 'focalLength': '105mm', 'aperture': 'f/1.4', 'isStabilized': False,
        'weight': 1645, 'minFocusDistance': '0.9m', 'filterSize': '86mm',
        'priceNew': 8999, 'priceUsedMin': 5000, 'priceUsedMax': 7000, 'retentionRate': 72, 'ownershipCount': 'medium',
        'pros': ['超大光圈', '焦外柔美', '成像锐利'],
        'cons': ['超级重(1645g)', '无防抖', '价格较高'],
        'commonIssues': ['对焦慢'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+105mm+f1.4+Art+lens+portrait+telephoto+prime&image_size=square',
        'purchaseAdvice': '专业人像首选',
        'specs': {'镜片组': '15片12组', '光圈叶片': '9片(圆形)', '放大倍率': '0.11倍'}
    },
    {
        'id': 'sigma-150-600-5-63-sport',
        'brand': 'Sigma', 'mount': 'EF', 'model': 'Sigma 150-600mm f/5-6.3 DG OS HSM Sport',
        'modelCode': '150-600/5-6.3 DG OS HSM Sport (S014)', 'nickname': '适马大炮S版', 'era': 'digital', 'year': 2014,
        'type': 'zoom', 'focalLength': '150-600mm', 'aperture': 'f/5-6.3', 'isStabilized': True,
        'weight': 2860, 'minFocusDistance': '2.6m', 'filterSize': '105mm',
        'priceNew': 14999, 'priceUsedMin': 8000, 'priceUsedMax': 12000, 'retentionRate': 75, 'ownershipCount': 'medium',
        'pros': ['超长焦', '成像优秀', '做工扎实', '防抖出色'],
        'cons': ['超级重(2860g)', '价格昂贵'],
        'commonIssues': ['镜筒伸缩卡顿'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Sigma+150-600mm+f5-6.3+Sport+lens+super+telephoto+professional&image_size=square',
        'purchaseAdvice': '专业野生动物摄影首选',
        'specs': {'镜片组': '24片16组', '光圈叶片': '9片(圆形)', '放大倍率': '0.2倍', '防抖': '4档'}
    },
    # 更多腾龙镜头
    {
        'id': 'tamron-24-70-28-g2',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron SP 24-70mm f/2.8 Di VC USD G2',
        'modelCode': 'SP 24-70/2.8 Di VC USD G2 (A032)', 'nickname': '腾龙二代2470', 'era': 'mirrorless', 'year': 2016,
        'type': 'zoom', 'focalLength': '24-70mm', 'aperture': 'f/2.8', 'isStabilized': True,
        'weight': 855, 'minFocusDistance': '0.24m', 'filterSize': '77mm',
        'priceNew': 7999, 'priceUsedMin': 4000, 'priceUsedMax': 6000, 'retentionRate': 72, 'ownershipCount': 'high',
        'pros': ['恒定f/2.8', '带防抖', '成像优秀', '性价比高'],
        'cons': ['重量较大'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+24-70mm+f2.8+G2+lens+standard+zoom+professional&image_size=square',
        'purchaseAdvice': '性价比标变首选',
        'specs': {'镜片组': '17片13组', '光圈叶片': '9片(圆形)', '放大倍率': '0.28倍', '防抖': '4档'}
    },
    {
        'id': 'tamron-35-150-28-4-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron 35-150mm f/2.8-4 Di VC OSD',
        'modelCode': '35-150/2.8-4 Di VC OSD (A043)', 'nickname': '腾龙长焦标变', 'era': 'mirrorless', 'year': 2018,
        'type': 'zoom', 'focalLength': '35-150mm', 'aperture': 'f/2.8-4', 'isStabilized': True,
        'weight': 755, 'minFocusDistance': '0.45m', 'filterSize': '67mm',
        'priceNew': 6499, 'priceUsedMin': 3500, 'priceUsedMax': 5000, 'retentionRate': 70, 'ownershipCount': 'medium',
        'pros': ['焦段实用', '轻便', '带防抖', '性价比高'],
        'cons': ['光圈非恒定'],
        'commonIssues': ['对焦偶发不准'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+35-150mm+f2.8-4+Di+VC+lens+telephoto+zoom+compact&image_size=square',
        'purchaseAdvice': '人像/旅行首选',
        'specs': {'镜片组': '15片12组', '光圈叶片': '9片(圆形)', '放大倍率': '0.21倍', '防抖': '3档'}
    },
    {
        'id': 'tamron-70-300-45-63-di',
        'brand': 'Tamron', 'mount': 'EF', 'model': 'Tamron 70-300mm f/4.5-6.3 Di III RXD',
        'modelCode': '70-300/4.5-6.3 Di III RXD (A047)', 'nickname': '腾龙轻便长焦', 'era': 'mirrorless', 'year': 2019,
        'type': 'zoom', 'focalLength': '70-300mm', 'aperture': 'f/4.5-6.3', 'isStabilized': False,
        'weight': 420, 'minFocusDistance': '0.9m', 'filterSize': '67mm',
        'priceNew': 3999, 'priceUsedMin': 2000, 'priceUsedMax': 3000, 'retentionRate': 75, 'ownershipCount': 'high',
        'pros': ['超轻便', '焦段实用', '价格适中'],
        'cons': ['无防抖', '光圈小'],
        'commonIssues': ['暂无明显问题'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Tamron+70-300mm+f4.5-6.3+Di+III+lens+telephoto+lightweight&image_size=square',
        'purchaseAdvice': '轻便长焦首选',
        'specs': {'镜片组': '14片10组', '光圈叶片': '9片(圆形)', '放大倍率': '0.25倍'}
    },
    # 胶片时代补充
    {
        'id': 'canon-ef-14-28-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 14mm f/2.8L USM',
        'modelCode': 'EF14/2.8L USM', 'nickname': '超广角定焦', 'era': 'film', 'year': 1997,
        'type': 'prime', 'focalLength': '14mm', 'aperture': 'f/2.8', 'isStabilized': False,
        'weight': 645, 'minFocusDistance': '0.2m', 'filterSize': '内置',
        'priceNew': 9999, 'priceUsedMin': 3000, 'priceUsedMax': 5000, 'retentionRate': 45, 'ownershipCount': 'medium',
        'pros': ['超广角', '大光圈', '星空神器'],
        'cons': ['无防抖', '价格较高', '灯泡头'],
        'commonIssues': ['前组镜片易沾污'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+14mm+f2.8L+USM+lens+ultrawide+prime+vintage&image_size=square',
        'purchaseAdvice': '风光摄影经典',
        'specs': {'镜片组': '12片8组', '光圈叶片': '7片', '放大倍率': '0.1倍'}
    },
    {
        'id': 'canon-ef-28-80-35-56-ii',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 28-80mm f/3.5-5.6 II',
        'modelCode': 'EF28-80/3.5-5.6 II', 'nickname': '老套头二代', 'era': 'film', 'year': 1995,
        'type': 'zoom', 'focalLength': '28-80mm', 'aperture': 'f/3.5-5.6', 'isStabilized': False,
        'weight': 215, 'minFocusDistance': '0.35m', 'filterSize': '58mm',
        'priceNew': 1499, 'priceUsedMin': 100, 'priceUsedMax': 300, 'retentionRate': 20, 'ownershipCount': 'high',
        'pros': ['超轻便', '价格便宜'],
        'cons': ['光圈小', '画质差', '无防抖'],
        'commonIssues': ['镜筒松动', '对焦不准'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+28-80mm+f3.5-5.6+II+lens+old+kit+lens&image_size=square',
        'purchaseAdvice': '练手用，不建议长期使用',
        'specs': {'镜片组': '8片7组', '光圈叶片': '5片', '放大倍率': '0.15倍'}
    },
    {
        'id': 'canon-ef-80-200-45-56-usm',
        'brand': 'Canon', 'mount': 'EF', 'model': 'Canon EF 80-200mm f/4.5-5.6 USM',
        'modelCode': 'EF80-200/4.5-5.6 USM', 'nickname': '入门长焦', 'era': 'film', 'year': 1992,
        'type': 'zoom', 'focalLength': '80-200mm', 'aperture': 'f/4.5-5.6', 'isStabilized': False,
        'weight': 410, 'minFocusDistance': '1.2m', 'filterSize': '52mm',
        'priceNew': 1999, 'priceUsedMin': 300, 'priceUsedMax': 600, 'retentionRate': 25, 'ownershipCount': 'high',
        'pros': ['轻便', '价格便宜'],
        'cons': ['光圈小', '画质一般', '无防抖'],
        'commonIssues': ['对焦马达老化'],
        'imageUrl': 'https://trae-api-cn.mchost.guru/api/ide/v1/text_to_image?prompt=Canon+80-200mm+f4.5-5.6+USM+lens+budget+telephoto+vintage&image_size=square',
        'purchaseAdvice': '入门长焦选择',
        'specs': {'镜片组': '10片8组', '光圈叶片': '5片', '放大倍率': '0.15倍'}
    }
]

# 添加到现有列表
lenses.extend(additional_lenses)

# 写入JSON文件
with open('/workspace/src/data/lenses.json', 'w', encoding='utf-8') as f:
    json.dump(lenses, f, ensure_ascii=False, indent=2)

print(f"Added {len(additional_lenses)} lenses. Total: {len(lenses)} lenses")
