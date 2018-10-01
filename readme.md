# SCout - Standard Character Out
Small python 3 library to print uniformly formatted console output tagged as

* info,
* warning,
* error or
* header.

If your console supports it coloured output will be used.


# Installation

* `pip3 install git+https://github.com/holzkohlengrill/SCout.git`
* `pip3 install pypiscout`


# Usage
Similar to `print()`:

```python3
import pypiscout as sc

sc.header("Welcome to SCout :)")
sc.info("test")
sc.error("error")
sc.warning("Warning")
```

Example output:

<div align="left">
<img src="https://github.com/holzkohlengrill/SCout/raw/master/output.png" height="160" alt="Output Image: https://github.com/holzkohlengrill/SCout/raw/master/output.png"/>
</div>
