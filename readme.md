[![PyPI version](https://badge.fury.io/py/pypiscout.svg)](https://badge.fury.io/py/pypiscout)

-------------------

# SCout - Standard Character Out
Lightweight python 3 library to print uniformly formatted console output tagged as

* debug
* info,
* weak warning
* warning,
* error or
* header.

There is the option to use custom tags and colours. If your console supports it coloured output will be used.

Since version 2 there is an extended logging functionality available which supports:

* Actions on warning in the event of warnings or errors
* Inverse verbosity options

The SCout Logger as well as Simple SCout can be used independently.


# Installation

* `pip3 install git+https://github.com/holzkohlengrill/SCout.git`
* `pip3 install pypiscout`


# Usage
Additionally [example files](examples) are provided.

## Simple SCout
Usie it similar to `print()`:

```python
from pypiscout import SCout as sc

sc.header("Welcome to SCout!")
sc.debug("Some debug message: 0xDEADBEEF")
sc.info("An info message")
sc.wwarning("Weak warnings are supported")
sc.warning("This is a warning")
sc.error("An error occured"))
```

### Example output:
<div align="left">
<img src="https://github.com/holzkohlengrill/SCout/raw/master/output_SCout.png" height="160" title="Simple SCout Output" alt="Output Image: https://github.com/holzkohlengrill/SCout/raw/master/output_SCout.png"/>
</div>


## SCout Logger
Optionally you can provide some settings for verbosity, warnings and errors.

### Inverse verbosity
Instead of providing more verbose output we use inverse verbosity levels (default = 0) which provides less output the higher the level.

| Level | Description                                             |
| ----- | ------------------------------------------------------- |
| -1    | Print all (debug, info, weak warnings, warning & error) |
| 0     | Print info, weak warnings, warning & error              |
| 1     | Print weak warnings, warning & error                    |
| 2     | Print warning & error                                   |
| 3     | Print error                                             |
| 4     | Do NOT print anything                                   |

### Usage
#### Basic usage
Implicit construction with default settings during the first call. In order to make it more readable call `sc()` upfront or use simple SCout if you don't need the Logger functionality.

```python
from pypiscout.SCout_Logger import Logger as sc

sc().header("Simple SCout")
sc().debug("Some debug message:", "0xDEADBEEF")
```

#### Edit current settings
```python
sc()(invVerbosity=0, actionWarning=None, actionError=lambda: sys.exit(-10))
```

```python
sc().header("SCout Logger")
sc().debug("Some debug message: 0xDEADBEEF")
sc().info("An info message")
sc().wwarning("Weak warning (does not support actions)")
sc().warning("This is a warning without defined action")
sc().error("Here the error action is defined as sys.exit(-10)")
```

### Example output:
<div align="left">
<img src="https://github.com/holzkohlengrill/SCout/raw/master/output_SCout_Logger.png" height="360" title="Simple SCout Output" alt="Output Image: https://github.com/holzkohlengrill/SCout/raw/master/output_SCout_Logger.png"/>
</div>
