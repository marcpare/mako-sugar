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
    
Also comes with nicer defs:
    
    % def foo():
        hi
    % enddef
    
And nicer imports:

    % import /components.html as comp
    % from /components.mako import link_to_modal
    % import customer.lib.presenters as p
    % import ${context['namespace_name']} as dyn
    
Install with:

        from mako_sugar import sugar
        
        # Any one of these options...
        t = Template(..., preprocessor=sugar())
        t = Template(..., preprocess=sugar(exclude=['def', 'call', 'import']))
        TemplateLookup(preprocessor=sugar())