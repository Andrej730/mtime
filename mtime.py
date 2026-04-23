"""
`mtime` stands for "measure time".

```
mtime python -c "from time import sleep; sleep(5)"
# real 5.044s
```
"""

import subprocess
import sys
from time import time


def main() -> None:
    if len(sys.argv) < 2:
        from pathlib import Path

        print(f"Usage: {Path(__file__).name} <command>", file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1:]
    start = time()
    result = subprocess.run(cmd)
    end = time()

    print(f"\nIt took {end - start:.3f}s.")
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()
