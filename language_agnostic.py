# Instructions: 
# Import the file to vscode
# cd path/to/your/file
# debug & run

import json

def draw_ver_bc(json_payload):
    try:
        dt = json.loads(json_payload)
    except json.JSONDecodeError:
        print("Invalid")
        return

    title = dt.get("title", "")
    x_title = dt.get("xtitle", "")
    y_title = dt.get("ytitle", "")

    print(f"{title.center(30)}")
    print("count")
    print("-----")

    max_count = max(item[list(item.keys())[0]] for item in dt.get("items", []))

    for i in range(max_count, 0, -1):
        for item in dt.get("items", []):
            if len(item) == 1:
                category, value = list(item.items())[0]
                print(f"\033[91m{'*' if value >= i else ' '}\033[0m{' ' * 8}", end="")
        print()

        if i == 1:  
            for item in dt.get("items", []):
                if len(item) == 1:
                    category, _ = list(item.items())[0]
                    print(f"{category:{9}}", end="")
            print()

    asset_names = " ".join(category for item in dt.get("items", []) for category in item.keys())
    print(f"{' ' * 48}")
    print(f"{' ' * 40}{x_title}")

json_payload = '''
{
    "title": "stock count",
    "xtitle": "asset",
    "ytitle": "count",
    "items": [
        {"chairs": 20},
        {"tables": 5},
        {"stands": 7},
        {"lamps": 8},
        {"cups": 10}
    ]
}
'''
draw_ver_bc(json_payload)
