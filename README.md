# tree-sitter-vbnet

A VB.NET (Visual Basic .NET) grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Tree-sitter](https://img.shields.io/badge/tree--sitter-grammar-green)](https://tree-sitter.github.io/tree-sitter/)

## Overview

This repository provides a comprehensive tree-sitter grammar for parsing VB.NET source code. It supports the full range of VB.NET language features including classes, modules, LINQ queries, async/await, and more.

## Features

### Supported Language Constructs

-   **Declarations**
    -   Classes, Structures, Interfaces, Modules
    -   Enums and Delegates
    -   Namespaces
    -   Generic types with constraints
-   **Type Members**
    -   Fields, Properties (including auto-implemented)
    -   Methods (Sub/Function)
    -   Constructors
    -   Events and Event handlers
    -   Operators
-   **Expressions**
    -   Binary and unary operators
    -   Lambda expressions
    -   LINQ query syntax
    -   Object and array creation
    -   Type casting and conversions
    -   Async/await expressions
    -   Null-conditional operators (`?.`)
-   **Statements**
    -   Control flow (If/Then/Else, Select Case, loops)
    -   Exception handling (Try/Catch/Finally)
    -   Using statements
    -   With blocks
    -   Error handling (On Error)
-   **Special VB.NET Features**
    -   Case-insensitive keywords
    -   Line continuations (`_`)
    -   Implicit line continuations
    -   My namespace keywords (Me, MyBase, MyClass)
    -   Handles clauses
    -   Implements and Inherits statements
    -   XML literals (planned)

### Modifiers and Attributes

-   Access modifiers (Public, Private, Protected, Friend, etc.)
-   Inheritance modifiers (MustInherit, NotInheritable, Overrides, etc.)
-   Other modifiers (Shared, ReadOnly, Async, Iterator, etc.)
-   Attribute declarations with arguments

## Installation

### Building from source

1.  **Clone the repository**
   
```bash
git clone https://github.com/govindbanura/tree-sitter-vbnet
cd tree-sitter-vbnet
```

2. **Install tree-sitter CLI** (if not already installed)
```bash
npm install -g tree-sitter-cli
```

3. **Generate the parser**
```bash
tree-sitter generate
```

4. **Build the shared library**

Create a Python script `build.py`:
```python
from tree_sitter import Language

# Build the shared library
Language.build_library(
    "build/tree_sitter_vbnet.so",  # Output path for the shared library
    ["."]  # Path to the grammar directory
)
```

Run the build script:
```bash
python build.py
```

This will create a `tree_sitter_vbnet.so` file in the `build/` directory.

## Usage

### Python

```python
from tree_sitter import Language, Parser

# Load the language library
VBNET_LANGUAGE = Language("build/tree_sitter_vbnet.so", "vbnet")

# Create a parser
parser = Parser()
parser.set_language(VBNET_LANGUAGE)

# Parse some code
source_code = b"""
Public Class HelloWorld
    Public Shared Sub Main()
        Console.WriteLine("Hello, World!")
    End Sub
End Class
"""

tree = parser.parse(source_code)
root_node = tree.root_node

# Traverse the syntax tree
def traverse(node, indent=0):
    print("  " * indent + node.type)
    for child in node.children:
        traverse(child, indent + 1)

traverse(root_node)
```

### JavaScript/Node.js

```javascript
const Parser = require('tree-sitter');
const VBNet = require('tree-sitter-vbnet');

const parser = new Parser();
parser.setLanguage(VBNet);

const sourceCode = `
Public Class HelloWorld
    Public Shared Sub Main()
        Console.WriteLine("Hello, World!")
    End Sub
End Class
`;

const tree = parser.parse(sourceCode);
console.log(tree.rootNode.toString());
```

### Rust

Add this to your `Cargo.toml`:

```toml
[dependencies]
tree-sitter = "0.20"
tree-sitter-vbnet = { git = "https://github.com/govindbanura/tree-sitter-vbnet" }
```

## Development

### Prerequisites

- Node.js (v12 or higher)
- Python 3.6+ (for building the shared library)
- tree-sitter CLI
- A C compiler (for building the parser)

### Setup

```bash
# Clone the repository
git clone https://github.com/govindbanura/tree-sitter-vbnet
cd tree-sitter-vbnet

# Install tree-sitter CLI
npm install -g tree-sitter-cli

# Generate the parser
tree-sitter generate

# Build the shared library
python build.py

# Run tests
tree-sitter test
```

### Project Structure

```
tree-sitter-vbnet/
├── grammar.js          # Grammar definition
├── src/                # Generated parser code
│   ├── parser.c        # Generated parser
│   └── tree_sitter/    # Parser header files
├── build.py            # Script to build shared library
└── package.json

```

### Testing

The grammar includes a comprehensive test suite. To run tests:

```bash
# Run all tests
tree-sitter test

# Run specific test
tree-sitter test -f "class declaration"

# Update test snapshots
tree-sitter test --update
```

### Adding Tests

Add test cases to `test/corpus/` files:

```
==================
Class Declaration
==================

Public Class MyClass
End Class

---

(source_file
  (class_declaration
    (member_modifier)
    name: (identifier)
    body: (empty_statement)))
```


## Grammar Design

### Precedence

The grammar uses carefully designed precedence rules to handle VB.NET's expression hierarchy correctly:

- Member access and invocation (highest)
- Unary operators
- Exponentiation
- Multiplicative operators
- Integer division and modulo
- Additive operators
- String concatenation
- Shift operators
- Relational operators
- Equality operators
- Logical operators (And, Or, Xor)
- Conditional expressions
- Assignment (lowest)

### Conflicts

The grammar handles several parsing ambiguities:

- Distinguishing between array access and method invocation
- Differentiating constructors from regular methods
- Resolving conflicts between field declarations and statements
- Handling optional parentheses in method calls


## Known Limitations

- XML literals are not yet supported
- Some edge cases in implicit line continuation
- Limited support for compiler directives beyond basic preprocessor directives

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Add tests for new features
- Ensure all tests pass before submitting PR
- Follow the existing code style
- Update documentation as needed

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Tree-sitter](https://tree-sitter.github.io/tree-sitter/) for the parsing framework
- The VB.NET language specification and documentation
- Contributors and users of this grammar

## Related Projects

- [tree-sitter](https://github.com/tree-sitter/tree-sitter)
- [tree-sitter-c-sharp](https://github.com/tree-sitter/tree-sitter-c-sharp)
- [Microsoft VB.NET Documentation](https://docs.microsoft.com/en-us/dotnet/visual-basic/)

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/govindbanura/tree-sitter-vbnet/issues) page
2. Review the test cases in `test/corpus/` for examples
3. Open a new issue with a minimal reproducible example

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a list of changes in each release.
