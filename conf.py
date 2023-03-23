cols = {
    'CP': [
        'DMS司机明细数据',
        '业务托收电话号码',
        '中金签收',
        '乐配通用户',
        '员工手机号',
        '员工家庭电话',
        '员工亲属',
        '员工紧急联系人',
        '客户资料清单'
    ],
    '中金签收': [
        'DMS司机明细数据',
        '业务托收电话号码',
        'CP',
        '乐配通用户',
        '员工手机号',
        '员工家庭电话',
        '员工亲属',
        '员工紧急联系人',
        '客户资料清单'
    ],
    '乐配通用户': [
        'DMS司机明细数据',
        '业务托收电话号码',
        '员工手机号',
        '员工家庭电话',
        '员工亲属',
        '员工紧急联系人',
        '客户资料清单'
    ],
    '员工个人及亲属信息': [],
    '客户资料清单': [],
    '业务托收电话号码': [],
    'DMS司机明细数据': [
        'CP',
        '业务托收电话号码',
        '员工手机号',
        '员工家庭电话',
        '员工亲属',
        '员工紧急联系人',
        '客户资料清单'
    ],
    '营业所大区对应表': [],
}

# 仅需要检查手机号是否重复的表及对应列
dupcols = [
    {
        'table': 'CP',
        'col': 'user_name',
        'check': [
            {'table': 'DMS司机明细数据', 'col': '司机电话', 'show': '司机名称', 'tablecol': 'DMS司机明细数据'},
            {'table': '业务托收电话号码', 'col': '服务号码', 'show': '服务号码', 'tablecol': '业务托收电话号码'},
            {'table': '员工个人及亲属信息', 'col': '手机号码', 'show': '员工编码', 'tablecol': '员工手机号'},
            {'table': '员工个人及亲属信息', 'col': '家庭电话', 'show': '员工编码', 'tablecol': '员工家庭电话'},
            {'table': '员工个人及亲属信息', 'col': '紧急联络人的电话', 'show': '员工编码', 'tablecol': '员工紧急联系人'},
            {'table': '员工个人及亲属信息', 'col': '亲戚电话', 'show': '员工编码', 'tablecol': '员工亲属'},
        ]
    },
    {
        'table': '中金签收',
        'col': '手机号码',
        'check': [
            {'table': 'DMS司机明细数据', 'col': '司机电话', 'show': '司机名称', 'tablecol': 'DMS司机明细数据'},
            {'table': '业务托收电话号码', 'col': '服务号码', 'show': '服务号码', 'tablecol': '业务托收电话号码'},
            {'table': '员工个人及亲属信息', 'col': '手机号码', 'show': '员工编码', 'tablecol': '员工手机号'},
            {'table': '员工个人及亲属信息', 'col': '家庭电话', 'show': '员工编码', 'tablecol': '员工家庭电话'},
            {'table': '员工个人及亲属信息', 'col': '紧急联络人的电话', 'show': '员工编码', 'tablecol': '员工紧急联系人'},
            {'table': '员工个人及亲属信息', 'col': '亲戚电话', 'show': '员工编码', 'tablecol': '员工亲属'},
        ]
    },
    {
        'table': '乐配通用户',
        'col': '手机号',
        'check': [
            {'table': 'DMS司机明细数据', 'col': '司机电话', 'show': '司机名称', 'tablecol': 'DMS司机明细数据'},
            {'table': '业务托收电话号码', 'col': '服务号码', 'show': '服务号码', 'tablecol': '业务托收电话号码'},
            {'table': '员工个人及亲属信息', 'col': '手机号码', 'show': '员工编码', 'tablecol': '员工手机号'},
            {'table': '员工个人及亲属信息', 'col': '家庭电话', 'show': '员工编码', 'tablecol': '员工家庭电话'},
            {'table': '员工个人及亲属信息', 'col': '紧急联络人的电话', 'show': '员工编码', 'tablecol': '员工紧急联系人'},
            {'table': '员工个人及亲属信息', 'col': '亲戚电话', 'show': '员工编码', 'tablecol': '员工亲属'},
        ]
    },
    {
        'table': 'DMS司机明细数据',
        'col': '司机电话',
        'check': [
            {'table': '业务托收电话号码', 'col': '服务号码', 'show': '服务号码', 'tablecol': '业务托收电话号码'},
            {'table': '员工个人及亲属信息', 'col': '手机号码', 'show': '员工编码', 'tablecol': '员工手机号'},
            {'table': '员工个人及亲属信息', 'col': '家庭电话', 'show': '员工编码', 'tablecol': '员工家庭电话'},
            {'table': '员工个人及亲属信息', 'col': '紧急联络人的电话', 'show': '员工编码',
             'tablecol': '员工紧急联系人'},
            {'table': '员工个人及亲属信息', 'col': '亲戚电话', 'show': '员工编码', 'tablecol': '员工亲属'},
            {'table': '中金签收', 'col': '手机号码', 'show': '客户编号', 'tablecol': '中金签收'},
            {'table': '乐配通用户', 'col': '手机号', 'show': '伙伴编号', 'tablecol': '乐配通用户'},
            {'table': '客户资料清单', 'col': '手机号码', 'show': '客户编号', 'tablecol': '客户资料清单'},
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
            {'table': '中金签收', 'phone': '手机号码', 'custom': '客户编号', 'show': '客户编号', 'tablecol': '中金签收'},
            {'table': '乐配通用户', 'phone': '手机号', 'custom': '伙伴编号', 'show': '伙伴编号', 'tablecol': '乐配通用户'},
            {'table': '客户资料清单', 'phone': '手机号码', 'custom': '客户编号', 'show': '客户编号', 'tablecol': '客户资料清单'},
        ]
    },
    {
        'table': '中金签收',
        'phone': '手机号码',
        'custom': '客户编号',
        'check': [
            {'table': 'CP', 'phone': 'user_name', 'custom': 'outlet_no', 'show': 'outlet_no', 'tablecol': 'CP'},
            {'table': '乐配通用户', 'phone': '手机号', 'custom': '伙伴编号', 'show': '伙伴编号', 'tablecol': '乐配通用户'},
            {'table': '客户资料清单', 'phone': '手机号码', 'custom': '客户编号', 'show': '客户编号', 'tablecol': '客户资料清单'},
        ]
    },
    {
        'table': '乐配通用户',
        'phone': '手机号',
        'custom': '伙伴编号',
        'check': [
            {'table': '客户资料清单', 'phone': '手机号码', 'custom': '客户编号', 'show': '客户编号', 'tablecol': '客户资料清单'},
        ]
    },
]

filepath = './Files'
outputpath = './Output'
