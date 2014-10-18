import re

def convert_calls(text):
    """preprocess short call syntax
    
    example:
    
    from mako_sugar import convert_calls
    t = Template(..., preprocessor=convert_calls)"""
    
    pattern = '(%\s*call(.*):\s*$)'
    def replace(matchobj):
        (line, expr) = matchobj.groups()
        return '<%%call expr="%s">' % expr.strip()    
    ret = re.sub(pattern, replace, text, flags=re.MULTILINE)
    
    pattern = '^\s*%\s*endcall\s*$'
    ret = re.sub(pattern, '</%call>', ret, flags=re.MULTILINE)
    
    return ret