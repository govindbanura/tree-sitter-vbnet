from tree_sitter import Language
import os
import subprocess


subprocess.run(["tree-sitter.cmd", "generate"], check=True)

Language.build_library("build/tree_sitter_vbnet.so", ["."])  # path to the cloned grammar folder
