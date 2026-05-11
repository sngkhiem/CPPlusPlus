# CP++

CP++ is a domain-specific language for competitive programming test generation and solution verification. It is designed for problem setters who need to create valid test data, produce official outputs, and optionally compare an alternative solution against the official solution.

The DSL describes a problem's test configuration and input generation logic in one `.CPPP` file. CP++ parses that file, builds an AST, validates variable usage, generates a C++ test generator, runs the official solution, and optionally runs an alternative solution for comparison.

## System Diagram

## Environment Setup

### Prerequisites

- Java runtime for ANTLR generation.
- Anaconda/Minicodna.
- `g++` for compiling generated C++ files and solution files.

### Installation

1. Clone the repository.

```bash
git clone https://github.com/sngkhiem/CPPlusPlus
cd CPPlusPlus
```

2. Create the environment from `PPL.yml`.

```bash
conda env create -f PPL.yml
```

3. Activate the environment.

```bash
conda activate PPL
```

## Usage

Regenerate the ANTLR parser after changing `grammar/CPPP.g4`.

```bash
python run.py gen
```

Run CP++ on a DSL file. Only `.CPPP` files are accepted.

```bash
python run.py test tests/testcase.CPPP
```

## Example

```txt
PRIME1 {
    config {
        input "PRIME1.inp"
        output "PRIME1.out"
        tests 10
        sol "tests/sol.cpp"
        test_sol "tests/test_sol.cpp"
        compare 5000
    }
    generate {
        var int t range(1, 5);
        print t;

        repeat(t) {
            var ll n range(10000000000, 1000000000000000000);
            print n;
        }
    }
}
```

This creates 10 test folders for `PRIME1`. Each test contains generated input and official output from `sol.cpp`. Because `compare 5000` is present, CP++ also runs `test_sol.cpp` on the same input with a 5000ms time limit, then compares its output with the official output;

## Grammar Structure

A `.CPPP` file contains one or more subtask blocks.

```txt
program       := subtaskBlock+
subtaskBlock  := subtaskName "{" configBlock genBlock "}"
subtaskName   := ID+
```

Each subtask has a `config` block and a `generate` block.

```txt
config {
}

generate {
    ...
}
```

`config` fields:

- `input`: generated input file name for each test.
- `output`: official output file name for each test.
- `tests`: number of test cases to generate.
- `sol`: official C++ solution used to produce expected output.
- `test_sol`: alternative C++ solution used for comparison.
- `compare`: optional flag. If present, CP++ runs `test_sol` and compares it against `sol` (an optional value after `compare` is used as the time limit in milliseconds.)

Generation statements:

```txt
var type name options;
var array<type> name[size] options;
print expr;
repeat(expr) {
    ...
}
```

Supported primitive types:

- `int`
- `ll`
- `float`
- `double`
- `char`
- `string`

Supported compound types:

- `array<T>`
- `tree(expr)`
- `graph(expr, expr)`

Tree and graph generation:

```txt
var tree(n) tr;
print tr;

var graph(n, m) g simple connected;
print g;
```

- `tree(n)` generates `n - 1` edges as pairs `u v`.
- `graph(n, m)` generates `m` edges as pairs `u v`.
- `print tr` prints each tree edge on its own line.
- `print g` prints each graph edge on its own line.

## Allowed Options

Options are written after a variable declaration.

```txt
var int n range(1, 100000);
var array<int> a[n] distinct sorted range(1, 1000000000);
```

Supported options:

- `range(l, r)`: sets the random range.
- `distinct`: array values must be unique.
- `sorted`: array values are sorted after generation.
- `distince`: accepted as a typo-compatible alias for `distinct`.
- `simple`: graph has no self-loops and no duplicate edges.
- `connected`: graph starts from a generated spanning tree before adding random edges.
- `directed`: graph duplicate checks use ordered pairs.
- `weighted`: graph edges include a random weight.

Range behavior:

- For `int`, `ll`, `float`, and `double`, `range(l, r)` controls the generated numeric value.
- For `char`, `range(l, r)` controls ASCII code. The default is `97..122`, which is lowercase `a..z`.
- For `string`, `range(l, r)` controls string length. Characters are generated from lowercase `a..z`.
- For arrays, `range(l, r)` controls each generated element.

Graph option behavior:

- `simple connected` is useful for most undirected connected graph tests.
- `weighted` prints graph edges as `u v w`.
- Without `weighted`, graph edges are printed as `u v`.
- For a simple undirected graph, make sure `m <= n * (n - 1) / 2`; otherwise generation may not terminate.
- For a simple directed graph, make sure `m <= n * (n - 1)`.

## Output Structure

For each subtask, CP++ creates files under `tests/<subtask_name>/`.

```txt
tests/
    PRIME1/
        gen.cpp
        test1/
            PRIME1.inp
            PRIME1.out
            test_sol.out
```

`test_sol.out` is only generated when `compare` is present in the config block.
