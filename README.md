## Setup
Add a enviornment variables for STMP Authentication
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
or
```bash

docker build -t microcenter-stock-check .
docker run -e SENDER=<SENDER-EMAIL> -e RECIPIENT=<RECIPIENT-EMAIL> -e LINK=<ITEM-LINK> -e STORE=<STORE-ID> microcenter-stock-check

```

## Store Ids

- **Santa Clara Coming Soon!**, CA, store 041
- **Tustin**, CA, store 101
- **Denver**, CO, store 181
- **Miami Coming Soon!**, FL
- **Duluth**, GA, store 065
- **Marietta**, GA, store 041
- **Chicago**, IL, store 151
- **Westmont**, IL, store 025
- **Indianapolis**, IN, store 165
- **Overland Park**, KS, store 191
- **Cambridge**, MA, store 121
- **Rockville**, MD, store 085
- **Parkville**, MD, store 125
- **Madison Heights**, MI, store 055
- **St. Louis Park**, MN, store 045
- **Brentwood**, MO, store 095
- **Charlotte**, NC, store 175
- **North Jersey**, NJ, store 075
- **Westbury**, NY, store 171
- **Brooklyn**, NY, store 115
- **Flushing**, NY, store 145
- **Yonkers**, NY, store 105
- **Columbus**, OH, store 141
- **Mayfield Heights**, OH, store 051
- **Sharonville**, OH, store 071
- **St. Davids**, PA, store 061
- **Houston**, TX, store 155
- **Dallas**, TX, store 131
- **Fairfax**, VA, store 081
