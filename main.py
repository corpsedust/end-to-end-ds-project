# ...existing code...
import sys, os

# ensure src/ is on sys.path so `import ds_project` works when running this script directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))

from ds_project import logger
# ...existing code...s