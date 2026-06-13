---
name: finance_pro
description: 专业财务技能。处理各地区(EMEA, US, APAC)的专项税率逻辑，计算净收入，并能识别表现不佳(UNDER_PERFORMING)的警告。
---
# 财务核算规则

## 基础数据要求
计算净收入前，确保数据已有以下标准列名：
- `Region`：地区名称
- `Quantity`：销售数量
- `Unit_Price`：单价（float 类型）
- `Discount`：折扣金额

## 净收入计算公式
总收入 = Quantity × Unit_Price
净收入 = 总收入 - Discount

## 各地区税率
| 地区 | 税率 |
|------|------|
| US | 8% |
| EMEA | 15% |
| APAC | 12% |

应纳税额 = 净收入 × 税率
税后净收入 = 净收入 - 应纳税额

## 表现不佳(UNDER_PERFORMING)判定
如果一个 Region 的 **税后净收入总和** 低于 500，必须在最终总结中明确标出 'UNDER_PERFORMING'。

## 分析流程
请按以下顺序完成：
1. 先读取 market_wizard 技能清洗数据
2. 再读取此技能（finance_pro）计算财务指标
3. 使用 python_analyst 或 generate_report 工具输出可视化报告
4. 用中文给出完整洞察
