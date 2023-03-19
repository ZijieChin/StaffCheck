cols = {
    'CP': [
        'DMS司机明细数据',
        '业务托收电话号码',
        '中金签收',
        '乐配通用户',
        '员工个人及亲属信息',
        '客户资料清单'
    ],
    '中金签收': [
        'DMS司机明细数据',
        '业务托收电话号码',
        'CP',
        '乐配通用户',
        '员工个人及亲属信息',
        '客户资料清单'
    ],
    '乐配通用户': [],
    '员工个人及亲属信息': [],
    '客户资料清单': [],
    '业务托收电话号码': [],
    'DMS司机明细数据': [],
    '营业所大区对应表': [],
}

# 仅需要检查手机号是否重复的表及对应列
dupcols = [
    {
        'table': 'CP',
        'col': 'user_name',
        'check': [
            {'table': 'DMS司机明细数据', 'col': '司机电话', 'show': '司机名称'},
            {'table': '业务托收电话号码', 'col': '服务号码', 'show': '服务号码'},
            {'table': '员工个人及亲属信息', 'col': '手机号码', 'show': '员工编码'},
        ]
    },
    {
        'table': '中金签收',
        'col': '手机号码',
        'check': [
            {'table': 'DMS司机明细数据', 'col': '司机电话', 'show': '司机名称'},
            {'table': '业务托收电话号码', 'col': '服务号码', 'show': '服务号码'},
            {'table': '员工个人及亲属信息', 'col': '手机号码', 'show': '员工编码'},
        ]
    },
]

# 需检查手机号是否重复，若重复则检查客户号是否相同的表及对应列
dupcustomcols = [
    {
        'table': 'CP',
        'phone': 'user_name',
        'custom': 'outlet_no',
        'check': [
            {'table': '中金签收', 'phone': '手机号码', 'custom': '客户编号', 'show': '客户编号'},
            {'table': '乐配通用户', 'phone': '手机号', 'custom': '伙伴编号', 'show': '伙伴编号'},
            {'table': '客户资料清单', 'phone': '手机号码', 'custom': '客户编号', 'show': '客户编号'},
        ]
    },
    {
        'table': '中金签收',
        'phone': '手机号码',
        'custom': '客户编号',
        'check': [
            {'table': 'CP', 'phone': 'user_name', 'custom': 'outlet_no', 'show': 'outlet_no'},
            {'table': '乐配通用户', 'phone': '手机号', 'custom': '伙伴编号', 'show': '伙伴编号'},
            {'table': '客户资料清单', 'phone': '手机号码', 'custom': '客户编号', 'show': '客户编号'},
        ]
    },
]

filepath = './Files'
