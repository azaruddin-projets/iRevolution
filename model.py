import pandas as pd

import pandas as pd

data = {
"model":[
"iphone 11",
"iphone 12",
"iphone 13",
"iphone 14",
"iphone 15",
"iphone 15 plus",
"iphone 15 pro",
"iphone 15 pro max",
"iphone 16",
"iphone 16 plus",
"iphone 16 pro",
"iphone 16 pro max",
"iphone 17",
"iphone 17 pro",
"iphone 17 pro max"
],

"launch_price":[
64900,
79900,
79900,
79900,
79900,
89900,
134900,
159900,
69900,
79900,
134900,
159900,
82900,
134900,
149900
],

"current_price":[
49900,
45900,
52900,
59900,
69900,
74900,
124900,
139900,
64900,
73900,
119900,
134900,
79900,
129900,
144900
],

"highest_price":[
64900,
79900,
79900,
79900,
79900,
89900,
134900,
159900,
69900,
79900,
134900,
159900,
82900,
134900,
149900
],

"lowest_price":[
31300,
42000,
48999,
46999,
54900,
64900,
109900,
129900,
60499,
69900,
109900,
99900,
58999,
109999,
139999
]

}

df = pd.DataFrame(data)



def get_price_details(phone):

    phone = phone.lower().strip()

    result = df[df["model"] == phone]

    if result.empty:
        return None

    launch = int(result["launch_price"].values[0])
    current = int(result["current_price"].values[0])
    highest = int(result["highest_price"].values[0])
    lowest = int(result["lowest_price"].values[0])

    discount = round(((launch-current)/launch)*100,2)

    return {
        "model": phone.title(),
        "launch": launch,
        "current": current,
        "discount": discount,
        "highest": highest,
        "lowest": lowest
    }