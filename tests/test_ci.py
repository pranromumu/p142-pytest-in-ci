'''import sys
import requests

def test_python_environment():
    assert sys.version_info.major == 3
def test_dependency_is_available():
    assert requests.__name__ == "requests"
def test_basic_functionality():
    assert 10 + 5 == 15

'''
import sys
import requests

# ==========================================
# 🧪 SCENARIO 1: PYTHON ENVIRONMENT WORKS
# ==========================================
def test_python_environment():
    assert sys.version_info.major == 3

# ==========================================
# 🧪 SCENARIO 2: DEPENDENCY IS AVAILABLE
# ==========================================
def test_dependency_is_available():
    # This will fail if 'requests' wasn't installed from requirements.txt
    assert requests.__name__ == "requests"

# ==========================================
# 🧪 SCENARIO 3: BASIC FUNCTIONALITY WORKS
# ==========================================
def test_basic_functionality():
    assert 10 + 5 == 15