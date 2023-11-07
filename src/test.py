from brightway2 import *

# 创建项目
if 'simple_lca_project' not in projects:
    projects.create_project('simple_lca_project')
projects.set_current('simple_lca_project')

# 创建数据库
db = Database("simple_db")
db.write({
    ("simple_db", "raw_material_extraction"): {
        'name': 'Raw material extraction',
        'unit': 'kilogram',
        'exchanges': [{
            'input': ("simple_db", "raw_material_extraction"),
            'amount': 1,
            'type': 'production'
        }, {
            'input': ("simple_db", "CO2_emission"),
            'amount': 2.5,
            'type': 'biosphere'
        }]
    },
    ("simple_db", "CO2_emission"): {
        'name': 'CO2 emission',
        'unit': 'kilogram',
        'exchanges': [{
            'input': ("simple_db", "CO2_emission"),
            'amount': 1,
            'type': 'production'
        }]
    }
})

# 创建并注册一个影响评估方法
method_key = ("simple_method",)
method = Method(method_key)
method.register()
method.write([
    (("simple_db", "CO2_emission"), 1),  # 假设每公斤CO2的影响是1
])

# 进行LCA计算
functional_unit = {("simple_db", "raw_material_extraction"): 1}  # 定义功能单元
lca = LCA(functional_unit, method_key)
lca.lci()  # 库存分析
lca.lcia()  # 影响评估

print("The LCA score for raw material extraction is: ", lca.score)
