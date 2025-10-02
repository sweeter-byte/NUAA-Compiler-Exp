# PL/0词法分析器

## 项目简介
本项目实现了PL/0语言的词法分析器，按照编译原理教材P45-46的算法思想，使用循环分支方法完成。

## 功能特性
- ✅ 识别15个关键字（program, const, var, procedure, begin, end, if, then, else, while, do, call, read, write, odd）
- ✅ 识别标识符和整数常量
- ✅ 识别所有运算符（+, -, *, /, =, <>, <, <=, >, >=）
- ✅ 识别界符（(, ), ;, ,, :=）
- ✅ 错误检测和精确定位（行号、列号）
- ✅ 输出Token序列到中间文件

## 环境要求
- Python 3.6+
- 无需额外依赖包

## 运行方法

### 方式1：使用命令行参数
```bash
cd src
python main.py ../tests/test_cases/test1_basic.pl0
```

### 方式2：交互式运行
```bash
cd src
python main.py
# 然后按提示输入文件路径
```

## 文件说明
```
├── README.md                   # 本文件
├── docs/                       # 文档目录
│   └── 实验报告.pdf           # 实验报告
├── src/                        # 源代码
│   ├── token_type.py          # Token类型定义
│   ├── token.py               # Token类
│   ├── lexer.py               # 词法分析器
│   └── main.py                # 主程序
├── tests/                      # 测试目录
│   └── test_cases/            # 测试用例
└── output/                     # 输出结果
```

## 测试用例
- **test1_basic.pl0**: 基本功能测试
- **test2_expression.pl0**: 表达式测试
- **test3_procedure.pl0**: 过程声明测试
- **test4_error.pl0**: 错误检测测试
- **test5_complex.pl0**: 复杂程序测试

## 输出格式
词法分析器将生成包含以下信息的Token序列文件：
- 序号
- 行号
- 列号
- Token类型
- Token值

## 错误处理
程序能检测以下词法错误：
1. 非法字符
2. 数字后直接跟字母
3. 单独的冒号（应为:=）
4. 注释未闭合

## 作者信息
- 姓名：[你的姓名]
- 学号：[你的学号]
- 班级：[你的班级]
- 日期：[日期]

## 参考资料
- 编译原理教材 P45-46页
- PL/0语言BNF描述
