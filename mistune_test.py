import copy
import re
from mistune.mistune import Markdown


markdown = Markdown()
print markdown('''
> something
  something
  - something
  - something

] something
  something
  - something
  - something

''')
