# Comparative photo sort

*photo labeling and sorting tool*

---

<!-- TODO: Fill readme
- [ ] Feature list
- [ ] Demo video
- [ ] Installation instruction
- [ ] Usage instruction
- [ ] Contribution instruction
 -->

## Installation

### From source

#### For users

```bash
git clone --depth 1 git@github.com:Phinnik/comparative_photo_sort.git
pip install -r requirements/user.txt
pip install .
```

#### For development

1. Install project
    ```bash
    git clone git@github.com:Phinnik/comparative_photo_sort.git
    pip install -r requirements/user.txt
    pip install -r requirements/develop.txt
    pip install -e .
    ```
1. Install pre-commit hooks
    ```bash
    pre-commit install
    ```
