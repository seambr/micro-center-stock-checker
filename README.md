## Setup
Add a .env file with the following format
```dotenv
APP_PASSWORD = ...
SENDER = ...
RECIPIENT = ...
```
## Usage
```bash
python main.py <link> --store <store-id> --delay <seconds>
# default delay: 3600sec
```