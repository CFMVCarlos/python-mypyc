Here's an improved version of your README file. I've reorganized some sections for clarity, enhanced readability, and added additional formatting where needed:

---

# MyPyC Compilation for Python Functions

This repository demonstrates how to use `mypyc` to compile Python functions into optimized native code, significantly improving performance.

## Table of Contents

- [MyPyC Compilation for Python Functions](#mypyc-compilation-for-python-functions)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [How to Use `mypyc` to Compile Python Files](#how-to-use-mypyc-to-compile-python-files)
    - [Step 1: Compile Python Files with `mypyc`](#step-1-compile-python-files-with-mypyc)
    - [Step 2: Use the Compiled File in Python](#step-2-use-the-compiled-file-in-python)
  - [Automated Compilation with Batch Script](#automated-compilation-with-batch-script)
    - [`setup.cmd` Script](#setupcmd-script)
    - [Running the Script](#running-the-script)
  - [Setting Up the Project for Compilation (Optional)](#setting-up-the-project-for-compilation-optional)
  - [Why Use `mypyc`?](#why-use-mypyc)
    - [Advantages of `mypyc`](#advantages-of-mypyc)
    - [Disadvantages of `mypyc`](#disadvantages-of-mypyc)
    - [When to Use `mypyc`](#when-to-use-mypyc)
    - [When Not to Use `mypyc`](#when-not-to-use-mypyc)
  - [Summary](#summary)
  - [Author](#author)

---

## Overview

`MyPyC` is a tool that compiles Python code into C extensions, allowing Python programs to run faster. It integrates with `mypy` type annotations and is ideal for improving performance in CPU-bound tasks.

---

## How to Use `mypyc` to Compile Python Files

### Step 1: Compile Python Files with `mypyc`

To compile a Python file using `mypyc`, run the following command:

```bash
mypyc <filename>.py
```

This command compiles the Python file into a C extension and generates a `.pyd` file (on Windows). For example, if your file is `example.py`, the result will be something like:

```
<filename>.cp312-win_amd64.pyd
```

### Step 2: Use the Compiled File in Python

Once the `.pyd` file is generated, you can import it in Python just like a regular module:

```bash
python -c "import <filename>"
```

The compiled functions can now be imported and used in Python, providing a performance boost over the regular Python implementation.

---

## Automated Compilation with Batch Script

If you have multiple Python files to compile, you can automate the process with the included batch script.

### `setup.cmd` Script

The `setup.cmd` script compiles all `.py` files in the `functions` folder and moves the resulting `.pyd` files to the `compiled_functions` folder. It also ensures that the `compiled_functions` folder exists and handles the compilation automatically.

### Running the Script

To compile and move all files in the `functions` folder, run the batch script:

```bash
setup.cmd
```

This script will:
1. Compile all `.py` files in the `functions` folder using `mypyc`.
2. Move the resulting `.pyd` files to the `compiled_functions` folder.

---

## Setting Up the Project for Compilation (Optional)

If you'd like to use `setuptools` and `mypycify` to automate the compilation for Python packages, here's an example `setup.py` script:

```python
from setuptools import setup
from mypyc.build import mypycify

setup(
    name="functions",
    version="1.0",
    packages=["functions"],
    ext_modules=mypycify(
        ["functions"]  # Compile all .py files in the functions folder
    ),
    package_dir={
        "": "./compiled_functions"  # Specify the root directory for the source
    },
)
```

To build the extension, run:

```bash
python setup.py build_ext --inplace
```

This will compile the `.py` files and place the resulting `.pyd` files in the `compiled_functions` directory.

**Note:** This method was not used in this project due to issues during the compilation process.

---

## Why Use `mypyc`?

`MyPyC` compiles Python code into optimized C extensions, making your Python programs run faster. It works well with type annotations and is specifically designed to improve performance in CPU-bound tasks.

### Advantages of `mypyc`

1. **Performance Improvements**:  
   - `mypyc` can provide significant speedups (ranging from 20% to 200%) for CPU-bound tasks, particularly those with computationally intensive operations.
   
2. **Type Annotation Compatibility**:  
   - Works seamlessly with `mypy`-annotated code, which allows for both type safety and performance optimization.

3. **Improved Startup Time**:  
   - Compiling Python code to C can reduce the startup time for applications, especially those with heavy initial processing or many imports.

4. **Integration with the Python Ecosystem**:  
   - `mypyc` compiles existing Python code into C extensions, meaning you can continue to use the vast Python ecosystem without major changes.

5. **No Need to Rewrite Codebase**:  
   - Unlike `Cython`, which requires you to rewrite large portions of your code, `mypyc` allows you to improve performance incrementally by compiling existing Python files.

### Disadvantages of `mypyc`

1. **Limited Support for Dynamic Features**:  
   - `mypyc` works best with statically typed Python code. It may not handle highly dynamic features (e.g., `exec()`, `eval()`, dynamic attribute access) well.

2. **Compilation Overhead**:  
   - The need to compile Python files into C extensions adds an extra step to the build process, which can slow down development and deployment.

3. **Limited Ecosystem and Adoption**:  
   - `mypyc` is relatively new compared to other tools like `Cython` and may not be as widely supported or documented. It may also have compatibility issues with some libraries or Python features.

4. **Maintenance Challenges**:  
   - Managing both the Python source code and its compiled C extensions requires careful maintenance to avoid issues as the codebase evolves.

5. **Compatibility Issues**:  
   - Some third-party Python libraries, especially those using dynamic features, may not work well with `mypyc`.

### When to Use `mypyc`

- **Type-annotated code**: If your Python code uses type hints and you want to improve its performance.
- **CPU-bound tasks**: For numerical computations, data processing, or other performance-critical tasks.
- **Improving startup time**: When startup speed is crucial, especially in larger applications.

### When Not to Use `mypyc`

- **Dynamic code**: If your code relies heavily on dynamic Python features or uses libraries that `mypyc` does not support.
- **Rapid iteration**: If fast development cycles are more important than performance improvements.
- **Non-CPU-bound tasks**: If performance improvements do not justify the added complexity for non-CPU-bound code.

---

## Summary

`mypyc` is a valuable tool for improving the performance of Python code, especially when it involves CPU-bound operations and uses type annotations. While it offers many advantages, such as improved speed and seamless integration with the Python ecosystem, it also has some limitations, particularly with dynamic features and libraries.

This repository provides tools to:

1. Compile individual Python files with `mypyc`.
   ```bash
   mypyc <filename>.py
   ```

2. Import the compiled `.pyd` file into Python.
   ```bash
   python -c "import <filename>"
   ```

3. Automate the compilation process for all `.py` files in a folder using the `setup.cmd` script.
   ```bash
   setup.cmd
   ```

4. Use `setuptools` and `mypycify` to automate compilation for Python packages.

---

## Author

- [Carlos Valente](https://www.github.com/CFMVCarlos)