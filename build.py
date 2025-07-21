from tree_sitter import Language

Language.build_library("build/tree_sitter_vbnet.so", ["."])  # path to the cloned grammar folder
