---
name: Parsing error
about: Report code that produces ERROR nodes
title: '[PARSE ERROR] '
labels: 'parsing-error'
assignees: ''
---

## Error Description
*Brief description of valid VB.NET code that fails to parse correctly.*

## Code That Fails to Parse
*The VB.NET code that produces ERROR nodes.*

```vbnet
' Paste the problematic VB.NET code
```

## Parse Tree Output
*The current parse tree showing ERROR nodes.*

```output
(source_file
  (ERROR ...)
)
```

## Expected Parse Tree
*What the parse tree should look like for this code.*

```output
(source_file
  ...
)
```

## VB.NET Version/Context
*Information about the VB.NET version or project type.*

- VB.NET version/framework:
- Project type (Console, WinForms, etc.):
- Is this syntax commonly used?

## Workaround
*If you've found a way to rewrite the code that parses correctly.*

```vbnet
' Working alternative (if any)
```
