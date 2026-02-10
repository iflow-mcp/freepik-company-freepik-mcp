from setuptools import setup, find_packages

setup(
    name="iflow-mcp_freepik-company-freepik-mcp",
    version="0.1.4",
    description="FastMCP server for integrating with Freepik APIs",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "aiofiles>=24.1.0",
        "fastmcp>=2.7.1",
        "httpx>=0.27.2",
        "pillow>=11.2.1",
        "pydantic-settings>=2.9.1",
        "pyyaml>=6.0.2",
    ],
    entry_points={
        "console_scripts": [
            "freepik-fastmcp=iflow_mcp_freepik_company_freepik_mcp.main:main",
        ],
    },
    python_requires=">=3.11",
)
