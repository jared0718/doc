name: Python package

on: [ push ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        # This is the version of the action for setting up Python, not the Python version.
        uses: actions/setup-python@v5
        with:
          # Semantic version range syntax or exact version of a Python version
          python-version: '3.9'
          # Optional - x64 or x86 architecture, defaults to x64
          architecture: 'x64'
      # You can test your matrix by printing the current Python version
      - name: 安装依赖
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: 开始测试
        run: pytest tests.py --doctest-modules --junitxml=junit/test-results-${{ matrix.python-version }}.xml
               - name: Upload pytest test results
               uses: actions/upload-artifact@v4
               with:
                 name: pytest-results-${{ matrix.python-version }}
                 path: junit/test-results-${{ matrix.python-version }}.xml
          # Use always() to always run this step to publish test results when there are test failures
               if: ${{ always() }}
