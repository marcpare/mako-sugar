Mako Sugar
===

A preprocessor that adds some syntactic sugar to Mako templates.

Write:

    % call foo():
        hi
    % endcall
        
instead of:

    <%call expr="foo()">
        hi
    </%call>
    
Install with:

        t = Template(..., preprocessor=convert_calls)

or
        
        TemplateLookup(preprocessor=convert_calls)