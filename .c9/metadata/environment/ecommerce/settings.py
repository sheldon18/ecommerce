{"filter":false,"title":"settings.py","tooltip":"/ecommerce/settings.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":158,"column":0},"end":{"row":159,"column":53},"action":"insert","lines":["STATICFILES_LOCATION = 'static'","STATICFILES_STORAGE = 'custom_storages.StaticStorage'"],"id":446}],[{"start":{"row":158,"column":24},"end":{"row":158,"column":30},"action":"remove","lines":["static"],"id":447},{"start":{"row":158,"column":24},"end":{"row":158,"column":25},"action":"insert","lines":["m"]},{"start":{"row":158,"column":25},"end":{"row":158,"column":26},"action":"insert","lines":["e"]},{"start":{"row":158,"column":26},"end":{"row":158,"column":27},"action":"insert","lines":["d"]},{"start":{"row":158,"column":27},"end":{"row":158,"column":28},"action":"insert","lines":["i"]},{"start":{"row":158,"column":28},"end":{"row":158,"column":29},"action":"insert","lines":["a"]}],[{"start":{"row":158,"column":0},"end":{"row":158,"column":20},"action":"remove","lines":["STATICFILES_LOCATION"],"id":448},{"start":{"row":158,"column":0},"end":{"row":158,"column":1},"action":"insert","lines":["M"]},{"start":{"row":158,"column":1},"end":{"row":158,"column":2},"action":"insert","lines":["E"]},{"start":{"row":158,"column":2},"end":{"row":158,"column":3},"action":"insert","lines":["D"]}],[{"start":{"row":158,"column":0},"end":{"row":158,"column":3},"action":"remove","lines":["MED"],"id":449},{"start":{"row":158,"column":0},"end":{"row":158,"column":19},"action":"insert","lines":["MEDIAFILES_LOCATION"]}],[{"start":{"row":159,"column":0},"end":{"row":159,"column":18},"action":"remove","lines":["STATICFILES_STORAG"],"id":450},{"start":{"row":159,"column":0},"end":{"row":159,"column":1},"action":"remove","lines":["E"]}],[{"start":{"row":159,"column":0},"end":{"row":159,"column":1},"action":"insert","lines":["D"],"id":451},{"start":{"row":159,"column":1},"end":{"row":159,"column":2},"action":"insert","lines":["E"]},{"start":{"row":159,"column":2},"end":{"row":159,"column":3},"action":"insert","lines":["F"]},{"start":{"row":159,"column":3},"end":{"row":159,"column":4},"action":"insert","lines":["S"]},{"start":{"row":159,"column":4},"end":{"row":159,"column":5},"action":"insert","lines":["U"]}],[{"start":{"row":159,"column":4},"end":{"row":159,"column":5},"action":"remove","lines":["U"],"id":452},{"start":{"row":159,"column":3},"end":{"row":159,"column":4},"action":"remove","lines":["S"]}],[{"start":{"row":159,"column":3},"end":{"row":159,"column":4},"action":"insert","lines":["A"],"id":453},{"start":{"row":159,"column":4},"end":{"row":159,"column":5},"action":"insert","lines":["U"]},{"start":{"row":159,"column":5},"end":{"row":159,"column":6},"action":"insert","lines":["L"]},{"start":{"row":159,"column":6},"end":{"row":159,"column":7},"action":"insert","lines":["T"]}],[{"start":{"row":159,"column":7},"end":{"row":159,"column":8},"action":"insert","lines":["_"],"id":454},{"start":{"row":159,"column":8},"end":{"row":159,"column":9},"action":"insert","lines":["F"]},{"start":{"row":159,"column":9},"end":{"row":159,"column":10},"action":"insert","lines":["I"]},{"start":{"row":159,"column":10},"end":{"row":159,"column":11},"action":"insert","lines":["L"]},{"start":{"row":159,"column":11},"end":{"row":159,"column":12},"action":"insert","lines":["E"]},{"start":{"row":159,"column":12},"end":{"row":159,"column":13},"action":"insert","lines":["_"]}],[{"start":{"row":159,"column":13},"end":{"row":159,"column":14},"action":"insert","lines":["S"],"id":455},{"start":{"row":159,"column":14},"end":{"row":159,"column":15},"action":"insert","lines":["T"]},{"start":{"row":159,"column":15},"end":{"row":159,"column":16},"action":"insert","lines":["O"]},{"start":{"row":159,"column":16},"end":{"row":159,"column":17},"action":"insert","lines":["R"]},{"start":{"row":159,"column":17},"end":{"row":159,"column":18},"action":"insert","lines":["A"]},{"start":{"row":159,"column":18},"end":{"row":159,"column":19},"action":"insert","lines":["G"]}],[{"start":{"row":159,"column":19},"end":{"row":159,"column":20},"action":"insert","lines":["E"],"id":456}],[{"start":{"row":159,"column":40},"end":{"row":159,"column":45},"action":"remove","lines":["Stati"],"id":457},{"start":{"row":159,"column":40},"end":{"row":159,"column":41},"action":"remove","lines":["c"]}],[{"start":{"row":159,"column":40},"end":{"row":159,"column":41},"action":"insert","lines":["M"],"id":458},{"start":{"row":159,"column":41},"end":{"row":159,"column":42},"action":"insert","lines":["E"]}],[{"start":{"row":159,"column":41},"end":{"row":159,"column":42},"action":"remove","lines":["E"],"id":459}],[{"start":{"row":159,"column":41},"end":{"row":159,"column":42},"action":"insert","lines":["e"],"id":460},{"start":{"row":159,"column":42},"end":{"row":159,"column":43},"action":"insert","lines":["d"]},{"start":{"row":159,"column":43},"end":{"row":159,"column":44},"action":"insert","lines":["i"]},{"start":{"row":159,"column":44},"end":{"row":159,"column":45},"action":"insert","lines":["a"]}],[{"start":{"row":159,"column":40},"end":{"row":159,"column":52},"action":"remove","lines":["MediaStorage"],"id":461},{"start":{"row":159,"column":40},"end":{"row":159,"column":52},"action":"insert","lines":["MediaStorage"]}],[{"start":{"row":162,"column":0},"end":{"row":162,"column":21},"action":"remove","lines":["MEDIA_URL = '/media/'"],"id":462},{"start":{"row":162,"column":0},"end":{"row":162,"column":74},"action":"insert","lines":["MEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)"]}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":463}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":[" "],"id":464}],[{"start":{"row":91,"column":0},"end":{"row":92,"column":0},"action":"insert","lines":["",""],"id":465},{"start":{"row":92,"column":0},"end":{"row":93,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"insert","lines":["i"],"id":466},{"start":{"row":92,"column":1},"end":{"row":92,"column":2},"action":"insert","lines":["f"]}],[{"start":{"row":92,"column":2},"end":{"row":92,"column":3},"action":"insert","lines":[" "],"id":467},{"start":{"row":92,"column":3},"end":{"row":92,"column":4},"action":"insert","lines":["D"]},{"start":{"row":92,"column":4},"end":{"row":92,"column":5},"action":"insert","lines":["A"]},{"start":{"row":92,"column":5},"end":{"row":92,"column":6},"action":"insert","lines":["T"]},{"start":{"row":92,"column":6},"end":{"row":92,"column":7},"action":"insert","lines":["A"]}],[{"start":{"row":92,"column":3},"end":{"row":92,"column":7},"action":"remove","lines":["DATA"],"id":468},{"start":{"row":92,"column":3},"end":{"row":92,"column":15},"action":"insert","lines":["DATABASE_URL"]}],[{"start":{"row":92,"column":15},"end":{"row":92,"column":16},"action":"insert","lines":[" "],"id":469},{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"insert","lines":["i"]},{"start":{"row":92,"column":17},"end":{"row":92,"column":18},"action":"insert","lines":["n"]}],[{"start":{"row":92,"column":18},"end":{"row":92,"column":19},"action":"insert","lines":[" "],"id":470},{"start":{"row":92,"column":19},"end":{"row":92,"column":20},"action":"insert","lines":["o"]},{"start":{"row":92,"column":20},"end":{"row":92,"column":21},"action":"insert","lines":["s"]},{"start":{"row":92,"column":21},"end":{"row":92,"column":22},"action":"insert","lines":["."]}],[{"start":{"row":92,"column":22},"end":{"row":92,"column":23},"action":"insert","lines":["e"],"id":471},{"start":{"row":92,"column":23},"end":{"row":92,"column":24},"action":"insert","lines":["n"]},{"start":{"row":92,"column":24},"end":{"row":92,"column":25},"action":"insert","lines":["v"]},{"start":{"row":92,"column":25},"end":{"row":92,"column":26},"action":"insert","lines":["i"]}],[{"start":{"row":92,"column":22},"end":{"row":92,"column":26},"action":"remove","lines":["envi"],"id":472},{"start":{"row":92,"column":22},"end":{"row":92,"column":29},"action":"insert","lines":["environ"]}],[{"start":{"row":92,"column":29},"end":{"row":92,"column":30},"action":"insert","lines":[":"],"id":473}],[{"start":{"row":92,"column":30},"end":{"row":93,"column":0},"action":"insert","lines":["",""],"id":474},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":92,"column":3},"end":{"row":92,"column":4},"action":"insert","lines":["\""],"id":475}],[{"start":{"row":92,"column":16},"end":{"row":92,"column":17},"action":"insert","lines":["\""],"id":476}],[{"start":{"row":95,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":["DATABASES = {","    'default':","        dj_database_url.parse(os.environ.get('DATABASE_URL'))","}"],"id":477}],[{"start":{"row":93,"column":4},"end":{"row":96,"column":1},"action":"insert","lines":["DATABASES = {","    'default':","        dj_database_url.parse(os.environ.get('DATABASE_URL'))","}"],"id":478}],[{"start":{"row":95,"column":61},"end":{"row":96,"column":0},"action":"remove","lines":["",""],"id":479}],[{"start":{"row":95,"column":61},"end":{"row":97,"column":4},"action":"insert","lines":["","        ","    "],"id":480}],[{"start":{"row":97,"column":5},"end":{"row":98,"column":0},"action":"insert","lines":["",""],"id":481},{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"remove","lines":[" "],"id":482},{"start":{"row":98,"column":0},"end":{"row":98,"column":1},"action":"insert","lines":["e"]},{"start":{"row":98,"column":1},"end":{"row":98,"column":2},"action":"insert","lines":["l"]},{"start":{"row":98,"column":2},"end":{"row":98,"column":3},"action":"insert","lines":["s"]},{"start":{"row":98,"column":3},"end":{"row":98,"column":4},"action":"insert","lines":["e"]},{"start":{"row":98,"column":4},"end":{"row":98,"column":5},"action":"insert","lines":[":"]}],[{"start":{"row":98,"column":5},"end":{"row":98,"column":6},"action":"insert","lines":[" "],"id":483}],[{"start":{"row":98,"column":7},"end":{"row":98,"column":8},"action":"remove","lines":[" "],"id":484}],[{"start":{"row":98,"column":6},"end":{"row":98,"column":7},"action":"remove","lines":[" "],"id":485},{"start":{"row":98,"column":5},"end":{"row":98,"column":6},"action":"remove","lines":[" "]}],[{"start":{"row":98,"column":5},"end":{"row":98,"column":6},"action":"remove","lines":[" "],"id":486},{"start":{"row":98,"column":5},"end":{"row":99,"column":0},"action":"insert","lines":["",""]},{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"insert","lines":["    "]},{"start":{"row":99,"column":4},"end":{"row":99,"column":5},"action":"insert","lines":["p"]},{"start":{"row":99,"column":5},"end":{"row":99,"column":6},"action":"insert","lines":["r"]},{"start":{"row":99,"column":6},"end":{"row":99,"column":7},"action":"insert","lines":["i"]},{"start":{"row":99,"column":7},"end":{"row":99,"column":8},"action":"insert","lines":["n"]},{"start":{"row":99,"column":8},"end":{"row":99,"column":9},"action":"insert","lines":["t"]}],[{"start":{"row":99,"column":9},"end":{"row":99,"column":11},"action":"insert","lines":["()"],"id":487}],[{"start":{"row":99,"column":10},"end":{"row":99,"column":12},"action":"insert","lines":["\"\""],"id":488}],[{"start":{"row":99,"column":11},"end":{"row":99,"column":12},"action":"insert","lines":["D"],"id":489},{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"insert","lines":["t"]},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"insert","lines":["a"]},{"start":{"row":99,"column":14},"end":{"row":99,"column":15},"action":"insert","lines":["b"]},{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"insert","lines":["e"]}],[{"start":{"row":99,"column":15},"end":{"row":99,"column":16},"action":"remove","lines":["e"],"id":490},{"start":{"row":99,"column":14},"end":{"row":99,"column":15},"action":"remove","lines":["b"]},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"remove","lines":["a"]},{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"remove","lines":["t"]}],[{"start":{"row":99,"column":12},"end":{"row":99,"column":13},"action":"insert","lines":["a"],"id":491},{"start":{"row":99,"column":13},"end":{"row":99,"column":14},"action":"insert","lines":["t"]}],[{"start":{"row":99,"column":11},"end":{"row":99,"column":14},"action":"remove","lines":["Dat"],"id":492},{"start":{"row":99,"column":11},"end":{"row":99,"column":19},"action":"insert","lines":["Database"]}],[{"start":{"row":99,"column":19},"end":{"row":99,"column":20},"action":"insert","lines":[" "],"id":493},{"start":{"row":99,"column":20},"end":{"row":99,"column":21},"action":"insert","lines":["U"]},{"start":{"row":99,"column":21},"end":{"row":99,"column":22},"action":"insert","lines":["R"]},{"start":{"row":99,"column":22},"end":{"row":99,"column":23},"action":"insert","lines":["L"]}],[{"start":{"row":99,"column":23},"end":{"row":99,"column":24},"action":"insert","lines":[" "],"id":494},{"start":{"row":99,"column":24},"end":{"row":99,"column":25},"action":"insert","lines":["n"]},{"start":{"row":99,"column":25},"end":{"row":99,"column":26},"action":"insert","lines":["o"]},{"start":{"row":99,"column":26},"end":{"row":99,"column":27},"action":"insert","lines":["t"]}],[{"start":{"row":99,"column":27},"end":{"row":99,"column":28},"action":"insert","lines":[" "],"id":495},{"start":{"row":99,"column":28},"end":{"row":99,"column":29},"action":"insert","lines":["f"]},{"start":{"row":99,"column":29},"end":{"row":99,"column":30},"action":"insert","lines":["o"]},{"start":{"row":99,"column":30},"end":{"row":99,"column":31},"action":"insert","lines":["u"]},{"start":{"row":99,"column":31},"end":{"row":99,"column":32},"action":"insert","lines":["n"]},{"start":{"row":99,"column":32},"end":{"row":99,"column":33},"action":"insert","lines":["d"]}],[{"start":{"row":99,"column":33},"end":{"row":99,"column":34},"action":"insert","lines":["."],"id":496}],[{"start":{"row":99,"column":34},"end":{"row":99,"column":35},"action":"insert","lines":[" "],"id":497},{"start":{"row":99,"column":35},"end":{"row":99,"column":36},"action":"insert","lines":["U"]},{"start":{"row":99,"column":36},"end":{"row":99,"column":37},"action":"insert","lines":["s"]},{"start":{"row":99,"column":37},"end":{"row":99,"column":38},"action":"insert","lines":["i"]},{"start":{"row":99,"column":38},"end":{"row":99,"column":39},"action":"insert","lines":["n"]},{"start":{"row":99,"column":39},"end":{"row":99,"column":40},"action":"insert","lines":["g"]}],[{"start":{"row":99,"column":40},"end":{"row":99,"column":41},"action":"insert","lines":[" "],"id":498},{"start":{"row":99,"column":41},"end":{"row":99,"column":42},"action":"insert","lines":["S"]},{"start":{"row":99,"column":42},"end":{"row":99,"column":43},"action":"insert","lines":["Q"]},{"start":{"row":99,"column":43},"end":{"row":99,"column":44},"action":"insert","lines":["L"]}],[{"start":{"row":99,"column":44},"end":{"row":99,"column":45},"action":"insert","lines":[" "],"id":499},{"start":{"row":99,"column":45},"end":{"row":99,"column":46},"action":"insert","lines":["L"]},{"start":{"row":99,"column":46},"end":{"row":99,"column":47},"action":"insert","lines":["i"]}],[{"start":{"row":99,"column":46},"end":{"row":99,"column":47},"action":"remove","lines":["i"],"id":500},{"start":{"row":99,"column":45},"end":{"row":99,"column":46},"action":"remove","lines":["L"]},{"start":{"row":99,"column":44},"end":{"row":99,"column":45},"action":"remove","lines":[" "]}],[{"start":{"row":99,"column":44},"end":{"row":99,"column":45},"action":"insert","lines":["i"],"id":501},{"start":{"row":99,"column":45},"end":{"row":99,"column":46},"action":"insert","lines":["t"]},{"start":{"row":99,"column":46},"end":{"row":99,"column":47},"action":"insert","lines":["e"]}],[{"start":{"row":99,"column":47},"end":{"row":99,"column":48},"action":"insert","lines":[" "],"id":502},{"start":{"row":99,"column":48},"end":{"row":99,"column":49},"action":"insert","lines":["i"]},{"start":{"row":99,"column":49},"end":{"row":99,"column":50},"action":"insert","lines":["n"]},{"start":{"row":99,"column":50},"end":{"row":99,"column":51},"action":"insert","lines":["s"]},{"start":{"row":99,"column":51},"end":{"row":99,"column":52},"action":"insert","lines":["t"]},{"start":{"row":99,"column":52},"end":{"row":99,"column":53},"action":"insert","lines":["e"]},{"start":{"row":99,"column":53},"end":{"row":99,"column":54},"action":"insert","lines":["a"]},{"start":{"row":99,"column":54},"end":{"row":99,"column":55},"action":"insert","lines":["d"]}],[{"start":{"row":99,"column":57},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":503},{"start":{"row":100,"column":0},"end":{"row":100,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":85,"column":0},"end":{"row":85,"column":2},"action":"remove","lines":["# "],"id":504},{"start":{"row":86,"column":0},"end":{"row":86,"column":2},"action":"remove","lines":["# "]},{"start":{"row":87,"column":0},"end":{"row":87,"column":2},"action":"remove","lines":["# "]},{"start":{"row":88,"column":0},"end":{"row":88,"column":2},"action":"remove","lines":["# "]},{"start":{"row":89,"column":0},"end":{"row":89,"column":2},"action":"remove","lines":["# "]},{"start":{"row":90,"column":0},"end":{"row":90,"column":2},"action":"remove","lines":["# "]}],[{"start":{"row":85,"column":0},"end":{"row":91,"column":0},"action":"remove","lines":["DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}",""],"id":505}],[{"start":{"row":94,"column":4},"end":{"row":100,"column":0},"action":"insert","lines":["DATABASES = {","    'default': {","        'ENGINE': 'django.db.backends.sqlite3',","        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","    }","}",""],"id":506}],[{"start":{"row":98,"column":0},"end":{"row":98,"column":4},"action":"remove","lines":["    "],"id":507},{"start":{"row":97,"column":53},"end":{"row":98,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":97,"column":53},"end":{"row":99,"column":4},"action":"insert","lines":["","        ","    "],"id":508}],[{"start":{"row":99,"column":5},"end":{"row":100,"column":0},"action":"remove","lines":["",""],"id":509}],[{"start":{"row":99,"column":5},"end":{"row":101,"column":4},"action":"insert","lines":["","        ","    "],"id":510}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"remove","lines":["    "],"id":511},{"start":{"row":98,"column":8},"end":{"row":99,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":99,"column":0},"end":{"row":99,"column":4},"action":"remove","lines":["    "],"id":512},{"start":{"row":98,"column":9},"end":{"row":99,"column":4},"action":"remove","lines":["","    "]}],[{"start":{"row":101,"column":0},"end":{"row":102,"column":0},"action":"remove","lines":["",""],"id":513},{"start":{"row":100,"column":0},"end":{"row":101,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":100,"column":0},"end":{"row":101,"column":0},"action":"remove","lines":["",""],"id":514}],[{"start":{"row":29,"column":86},"end":{"row":29,"column":87},"action":"insert","lines":[","],"id":515}],[{"start":{"row":29,"column":87},"end":{"row":29,"column":88},"action":"insert","lines":[" "],"id":516}],[{"start":{"row":29,"column":88},"end":{"row":29,"column":90},"action":"insert","lines":["''"],"id":517}],[{"start":{"row":29,"column":89},"end":{"row":29,"column":130},"action":"insert","lines":["https://sheldons-ecommerce.herokuapp.com/"],"id":518}],[{"start":{"row":29,"column":89},"end":{"row":29,"column":97},"action":"remove","lines":["https://"],"id":519}],[{"start":{"row":29,"column":121},"end":{"row":29,"column":122},"action":"remove","lines":["/"],"id":520}],[{"start":{"row":29,"column":89},"end":{"row":29,"column":121},"action":"remove","lines":["sheldons-ecommerce.herokuapp.com"],"id":521},{"start":{"row":29,"column":89},"end":{"row":29,"column":122},"action":"insert","lines":["sheldons-ecommerce.herokuapp.com/"]}],[{"start":{"row":29,"column":121},"end":{"row":29,"column":122},"action":"remove","lines":["/"],"id":522}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":4},"action":"remove","lines":["    "],"id":523},{"start":{"row":87,"column":17},"end":{"row":88,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":88,"column":4},"end":{"row":88,"column":8},"action":"remove","lines":["    "],"id":524},{"start":{"row":88,"column":0},"end":{"row":88,"column":4},"action":"remove","lines":["    "]},{"start":{"row":87,"column":27},"end":{"row":88,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":87,"column":27},"end":{"row":87,"column":28},"action":"insert","lines":[" "],"id":525}],[{"start":{"row":89,"column":2},"end":{"row":89,"column":3},"action":"remove","lines":[" "],"id":530},{"start":{"row":89,"column":1},"end":{"row":89,"column":2},"action":"remove","lines":[" "]},{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"remove","lines":[" "]},{"start":{"row":88,"column":8},"end":{"row":89,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":88,"column":8},"end":{"row":88,"column":9},"action":"remove","lines":[" "],"id":531}],[{"start":{"row":88,"column":4},"end":{"row":88,"column":8},"action":"remove","lines":["    "],"id":532},{"start":{"row":88,"column":0},"end":{"row":88,"column":4},"action":"remove","lines":["    "]},{"start":{"row":87,"column":81},"end":{"row":88,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":4},"action":"insert","lines":["    "],"id":543},{"start":{"row":92,"column":0},"end":{"row":92,"column":4},"action":"insert","lines":["    "]},{"start":{"row":93,"column":0},"end":{"row":93,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":86,"column":0},"end":{"row":95,"column":5},"action":"remove","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }"],"id":555},{"start":{"row":86,"column":0},"end":{"row":95,"column":5},"action":"insert","lines":["if \"DATABASE_URL\" in os.environ:","    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}","else:","    print(\"Database URL not found. Using SQLite instead\")","    DATABASES = {","        'default': {","            'ENGINE': 'django.db.backends.sqlite3',","            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),","        }","    }"]}],[{"start":{"row":140,"column":38},"end":{"row":140,"column":39},"action":"remove","lines":[","],"id":560}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["# "],"id":565}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"insert","lines":["# "],"id":566}],[{"start":{"row":145,"column":40},"end":{"row":145,"column":50},"action":"remove","lines":["ACCESS_KEY"],"id":575},{"start":{"row":145,"column":40},"end":{"row":145,"column":41},"action":"insert","lines":["D"]}],[{"start":{"row":145,"column":40},"end":{"row":145,"column":41},"action":"remove","lines":["D"],"id":576}],[{"start":{"row":145,"column":40},"end":{"row":145,"column":41},"action":"insert","lines":["S"],"id":577},{"start":{"row":145,"column":41},"end":{"row":145,"column":42},"action":"insert","lines":["E"]},{"start":{"row":145,"column":42},"end":{"row":145,"column":43},"action":"insert","lines":["C"]}],[{"start":{"row":145,"column":43},"end":{"row":145,"column":44},"action":"insert","lines":["R"],"id":578},{"start":{"row":145,"column":44},"end":{"row":145,"column":45},"action":"insert","lines":["E"]},{"start":{"row":145,"column":45},"end":{"row":145,"column":46},"action":"insert","lines":["T"]}],[{"start":{"row":145,"column":46},"end":{"row":145,"column":47},"action":"insert","lines":["_"],"id":579},{"start":{"row":145,"column":47},"end":{"row":145,"column":48},"action":"insert","lines":["K"]},{"start":{"row":145,"column":48},"end":{"row":145,"column":49},"action":"insert","lines":["E"]},{"start":{"row":145,"column":49},"end":{"row":145,"column":50},"action":"insert","lines":["Y"]}],[{"start":{"row":14,"column":22},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":617},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":14},"action":"insert","lines":["if os.path.exists('env.py'):","    import env"],"id":618}],[{"start":{"row":16,"column":0},"end":{"row":17,"column":14},"action":"remove","lines":["if os.path.exists('env.py'):","    import env"],"id":619},{"start":{"row":15,"column":0},"end":{"row":16,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":22},"end":{"row":15,"column":0},"action":"remove","lines":["",""],"id":620}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["# "],"id":621}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":622}],[{"start":{"row":13,"column":1},"end":{"row":13,"column":2},"action":"insert","lines":[" "],"id":623}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":2},"action":"remove","lines":["# "],"id":624}]]},"ace":{"folds":[],"scrolltop":1920,"scrollleft":0,"selection":{"start":{"row":19,"column":0},"end":{"row":19,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":111,"state":"start","mode":"ace/mode/python"}},"timestamp":1584302367984,"hash":"00f2f6635dd5265beecd75d2999b2af1a2746ed1"}