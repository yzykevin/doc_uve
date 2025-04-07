# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'UVE'
copyright = '2021-2025, Saltyfish'
author = 'Saltyfish'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
html_static_path = ['_static']

language = 'en,cn'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import os
import sphinx_rtd_theme
html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# html_theme = 'alabaster'
html_static_path = ['_static']
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "/")
html_js_files = [
    ("readthedocs.js", {"defer": "defer"}),
]

# -- Options for EPUB output -------------------------------------------------
epub_show_urls = 'footnote'  # 在 EPUB 中显示 URL 的方式
epub_title = project  # 使用项目名称作为 EPUB 标题
epub_author = author  # 使用作者信息
epub_publisher = author  # 使用作者作为出版者
epub_identifier = html_baseurl  # 使用 base URL 作为标识符
epub_scheme = 'URL'  # 标识符的类型
epub_cover = ('_static/cover.png', '')  # 可选：指定封面图片


latex_engine = 'xelatex'
latex_use_xindy = False
latex_elements = {
    'preamble': '\\usepackage[UTF8]{ctex}\n',
}
