import copy
import re
from mistune.mistune import Renderer, Markdown, BlockLexer, BlockGrammar

class columnRenderer(Renderer):
    def column(self, text):
        return '<column>\n%s\n</column>' % (text)

class columnLexer(BlockLexer):
    def enable_column(self):
        self.rules.column = re.compile(r'^'
            r'( *\[[^\n]+(\n[^\n]+)*\n*)'
            r'+')
        self.default_rules.insert(1, 'column')

    def output_column(self, m):
        text = m.group(1)
        return self.renderer.column(text)

renderer = columnRenderer()
block = columnLexer(renderer)
block.enable_column()
markdown = Markdown(renderer, block=block)
print markdown('''
> something
  something
  - something
  - something

[ something
  something
  - something
  - something

    code inside here?
    is there?

  | $a$ | b | c |
  |---|---|---|
  | 1 | 2 | 3 |
  | 4 | 5 | 6 |

''')
