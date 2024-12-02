from setuptools import setup, find_packages

setup(
    name="plot_util",                   # 包的名称
    version="0.0.1",                     # 版本号
    author="runoob09",                  # 作者
    author_email="2499469495@qq.com", # 作者邮箱
    description="绘制强化学习算法表现性能图的工具", # 简要描述
    long_description=open("README.md").read(),  # 从 README.md 获取详细描述
    long_description_content_type="text/markdown",  # 描述内容类型
    url="https://github.com/runoob09/plot_util.git",  # 项目的 URL（例如 GitHub）
    packages=find_packages(),            # 自动发现包
    classifiers=[                        # 分类标签（可选）
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',             # Python 版本要求
)
