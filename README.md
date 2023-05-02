# Ubuntu 22.04

```sh
apt install python3.9-full
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9
pip install --force-reinstall accelerate torch tensorflow-intel transformers
```

# OSX

```sh
brew install python@3.9
curl -sS https://bootstrap.pypa.io/get-pip.py | python3.9
pip install --user --force-reinstall accelerate torch tensorflow-intel transformers
```

# Run Ubuntu

```sh
python3.9 dollytest2.py
```

This command will use 8.6G of RAM and run 4 minutes on 2CPU 2*14(28) Cores in Ubuntu

```sh
python3.9 dollytest12.py
```

This command will use 23.8G of RAM and run ~15 minutes on 2CPU 2*14(28) Cores in Ubuntu

# Run OSX

```sh
MacBook-Pro-Andrii:dolly2_evaluate_intel podarok$ date && python3.9 dollytest2.py && date
вт  2 тра 2023 11:24:54 EEST
Drupal is an open-source content management system (CMS) developed by Automattic, the company formerly known for WordPress. Drupal is used by hundreds of thousands of organizations for all kinds of content management, web application, and digital experience purposes.
[{'generated_text': 'Drupal is an open-source content management system (CMS) developed by Automattic, the company formerly known for WordPress. Drupal is used by hundreds of thousands of organizations for all kinds of content management, web application, and digital experience purposes.'}]
вт  2 тра 2023 11:26:42 EEST
```
