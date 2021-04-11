# No fun facts

The best way to culture people on Twitter : [@no_fun_facts](https://twitter.com/no_fun_facts)

## Quick Start

Create a file `credential.json` within root directory and fill up your twitter details :

```json
{ 
    "consumer_key" : "XXXXXXXXXXXXXX",
    "consumer_secret" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",    
    "access_token" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
    "access_token_secret" : "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

Install prerequisite

```python
pip install -r requirements.txt
```

Run the code 

```python 
python main.py
```


## To do

- Clean page from useless infobox_vx or bandeau-container
- Fix parentheseception regex match issue
- Control tweets are 280 char' max before posting