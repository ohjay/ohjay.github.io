## Discussion Quiz 7 ##

from html.parser import HTMLParser
import re, calendar

MONTHS = {v: k for k, v in enumerate(calendar.month_abbr)}

def parse_date(fb_date_str):
    """Converts a Facebook date string (ex. 'Sunday, March 6, 2016 at 8:08pm PST')
    into a (YEAR, MONTH, DAY) tuple.
    
    >>> parse_date('Sunday, March 6, 2016 at 8:08pm PST')
    (2016, 3, 6)
    """
    m = re.match(r'[a-zA-Z]+, ([a-zA-Z]+) (\d{1,2}), (\d{4}).*', fb_date_str)
    return (int(m.group(3)), MONTHS[m.group(1)[:3]], int(m.group(2)))
    
class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children: assert isinstance(branch, Tree)
        self.children = list(children)
        
    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)
        
    def child_exists(self, label):
        """Returns true if any children have LABEL in their topmost nodes."""
        return any([c.label == label for c in self.children])
    
    def add_child(self, label):
        """Adds a child with label LABEL, if such a child doesn't already exist."""
        if not self.child_exists(label):
            self.children.append(Tree(label))
        
    def select_child(self, label):
        """Selects a child with label LABEL, if one exists.
        Otherwise returns None."""
        try: return [c for c in self.children if c.label == label][0]
        except IndexError: return None

class Q7Parser(HTMLParser):
    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs)
        "*** YOUR CODE HERE ***"
        
    def handle_starttag(self, tag, attrs):
        """Called when the parser finds a starting tag (<p>, <div>, etc.)."""
        "*** YOUR CODE HERE ***"
        
    def handle_data(self, data):
        """Called when the parser finds a string within some set of tags."""
        "*** YOUR CODE HERE ***"
    
    def get_events_on(self, year, month, day):
        """Returns a list of events that happened on (YEAR, MONTH, DAY)."""
        "*** YOUR CODE HERE ***"
        
with open('--- INSERT PATH TO timeline.htm HERE ---', 'r') as file:
    html = file.read().replace('&#039;', '\'').replace('&quot;', '"') \
            .replace('&amp;', '&')

parser = Q7Parser()
parser.feed(html)

# TODO: ...? Feel free to implement your own extensions!
