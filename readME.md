### Local Development Setup

1. Clone the repository

```bash
git clone git@github.com:RightClickITSolutions/napims-360.git
```

2. Install all UI Client dependencies

```bash
yarn install --no-lockfile --production=false --silent
```

3. Setup Python virtual env
```bash
python3 -m venv .venv
```

4. Activate env
```bash
source .venv/bin/activate
```

5. Install all Server dependencies
```bash
pip install -r conf/requirements-dev.txt
```