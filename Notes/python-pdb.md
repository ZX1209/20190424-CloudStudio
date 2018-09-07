# 
python -m pdb you_python_file.py



# 
```python
import pdb

def make_bread():
    pdb.set_trace()
    return "I don't have time"

print(make_bread())
```