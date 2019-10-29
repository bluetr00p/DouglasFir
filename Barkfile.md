# Barkfile specs

A basic barkfile will look like...
```json
{
    "name": "DouglasFir",
    "version": "1.0.0",
    "description": "To simplify installing and managing packages on all programming languages",
    "language": "python3",
    "main": "src/main.py",
    "startup": {
        "run": "python3"
    },
    "repo": {
        "repository": "github.com/bluetr00p/DouglasFir",
        "type": "git"
    },
    "author": "Lukas Werner @ <lukas@wernerresearch.com>",
    "license": "MIT",
    "dependencies": {
        "HelloWorld": "==1.0.0"
    }
}
```

### Must contain:
- Language
    - this is so that we can know what language to get packages from
- main file
    - This is so that we can launch the right file because naming conventions can vary
- startup Script
    - This is if we need to make sure to run something else to get you started