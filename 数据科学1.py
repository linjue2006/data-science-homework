#崔海锋的数据科学导论作业，均采用在anaconda下的基础环境进行运行，由于之前解释器错误，导致添加了验证代码来确定是否是否正确环境
import sys
from pathlib import Path
try:
    import pandas as pd
except ImportError:
    print("pandas未安装或当前解释器不可用。请运行: python -m pip install pandas")
    print(f"当前Python解释器: {sys.executable}")
    raise

print(f"Python版本: {sys.version.split()[0]}")
print(f"解释器路径: {sys.executable}")
print(f"当前工作目录: {Path.cwd()}")
print(f"pandas版本: {pd.__version__}")
print(f"pandas模块路径: {getattr(pd, '__file__', '未知')}\n")

csv_path = Path(r"D:\Data\china_gdp.csv")#r确定路径为原始字符串
if not csv_path.exists():
    alt_path = Path(__file__).resolve().parent / "china_gdp.csv"
    print(f"未找到 {csv_path}，改用 {alt_path}")
    csv_path = alt_path

print(f"使用CSV路径: {csv_path}\n")
df = pd.read_csv(csv_path)

print(df.head())

print('Average GDP:', df['Value'].mean())
print('Max GDP Year:', df.loc[df['Value'].idxmax(), 'Year'])
#以上部分为part1的代码
import json

with open('D:/Data/sample_api.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(type(data))
print(data[0])
#task2的第二个部分
df_json = pd.json_normalize(data)
df_json.head()
#task3的第一部分，非结构化数据可视化
from PIL import Image
import matplotlib.pyplot as plt
#task3的第二部分，非结构化数据可视化
img = Image.open('D:/Data/greatwall.jpg')
plt.imshow(img)
plt.axis('off')
plt.show()
#task3的第三部分，非结构化数据可视化
print('Format:', img.format)
print('Size:', img.size)
print('Mode:', img.mode)
#以下为task4的代码
import pandas as pd

data = {'Student': ['A','B','C','D'],
        'Height': [165, 172, 180, 158],
        'Gender': ['F','M','M','F'],
        'Grade': ['A','B','A','C']}
df = pd.DataFrame(data)
print(df)