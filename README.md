# Ubuntu 22.04

```sh
apt install python3.9-full
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9
pip install --force-reinstall accelerate torch tensorflow-intel
```

# Run

```sh
python3.9 dollytest2.py
```

This command will use 8.6G of RAM and run 4 minutes on 2CPU 2*14(28) Cores 

```sh
python3.9 dollytest12.py
```

This command will use 23.8G of RAM and run ~15 minutes on 2CPU 2*14(28) Cores


