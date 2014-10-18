import re
import unittest
from nose.tools import *
from mako.template import Template
from mako_sugar import convert_calls

def result_lines(result):
    return [x.strip() for x in re.split(r'\r?\n', re.sub(r' +', ' ', result)) if x.strip() != '']

class Calltest(unittest.TestCase):
    
    def test_preprocess(self):
        t = """
        % call foo():
            hi
        % endcall
        """
        s = """
        <%call expr="foo()">
            hi
        </%call>
        """
        t = convert_calls(t)
        assert_equals(result_lines(t), result_lines(s))
        
    def test_preprocess2(self):
        t = """
        %call foo():
            hi
        %endcall
        """
        s = """
        <%call expr="foo()">
            hi
        </%call>
        """
        t = convert_calls(t)
        assert_equals(result_lines(t), result_lines(s))
        
    def test_call(self):
        t = Template("""
        <%def name="foo()">
            foo
            ${caller.body()}
            foo
        </%def>

        % call foo():
            bar
        % endcall
        """, preprocessor=convert_calls)

        assert_equals(result_lines(t.render()), ['foo', 'bar', 'foo'])