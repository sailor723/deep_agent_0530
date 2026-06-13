---
name: market_wizard
description: 市场数据清洗技能。将市场部导出的数据（market, qty, prod_cat, price_per_unit, rebate）映射为标准列名（Region, Quantity, Product_Category, Unit_Price, Discount）。
---
# 市场数据清洗规则

## 列名映射
| 市场数据列 | 标准列名 | 说明 |
|-----------|---------|------|
| market | Region | 地区名称 |
| qty | Quantity | 销售数量 |
| prod_cat | Product_Category | 产品类别 |
| price_per_unit | Unit_Price | 单价（含 $ 符号和逗号） |
| rebate | Discount | 折扣金额 |

## 清洗步骤
1. 将上述列名映射为标准列名
2. 对 Unit_Price 列，移除 '$' 符号和逗号，转为 float 类型
3. 将清洗后的数据保存为 `enterprise_data/cleaned_marketing.csv`

## 工作流程
请按以下顺序完成分析任务：
1. 先读取此技能（market_wizard）清洗数据
2. 再读取 finance_pro 技能进行财务计算
3. 最后用 python_analyst 或 generate_report 输出结果
