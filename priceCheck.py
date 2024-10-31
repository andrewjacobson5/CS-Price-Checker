# Andrew Jacobson 2024

import tkinter as tk
import requests

weapon = {
    "ak47": "AK-47%20%7C%20",
    "aug": "AUG%20%7C%20",
    "awp": "AWP%20%7C%20",
    "bizon": "PP-Bizon%20%7C%20",
    "cz75": "CZ75-Auto%20%7C%20",
    "deagle": "Desert%20Eagle%20%7C%20",
    "dualberettas": "Dual%20Berettas%20%7C%20",
    "famas": "FAMAS%20%7C%20",
    "fiveseven": "Five-SeveN%20%7C%20",
    "g3sg1": "G3SG1%20%7C%20",
    "galil": "Galil%20AR%20%7C%20",
    "glock18": "Glock-18%20%7C%20",
    "m4a1s": "M4A1-S%20%7C%20",
    "m4a4": "M4A4%20%7C%20",
    "mac10": "MAC-10%20%7C%20",
    "mag7": "MAG-7%20%7C%20",
    "mp5": "MP5-SD%20%7C%20",
    "mp7": "MP7%20%7C%20",
    "mp9": "MP9%20%7C%20",
    "negev": "Negev%20%7C%20",
    "nova": "Nova%20%7C%20",
    "p2000": "P2000%20%7C%20",
    "p250": "P250%20%7C%20",
    "p90": "P90%20%7C%20",
    "sawedoff": "Sawed-Off%20%7C%20",
    "scar20": "SCAR-20%20%7C%20",
    "sg553": "SG%20553%20%7C%20",
    "scout": "SSG%2008%20%7C%20",
    "tec9": "Tec-9%20%7C%20",
    "ump45": "UMP-45%20%7C%20",
    "usps": "USP-S%20%7C%20",
    "xm1014": "XM1014%20%7C%20"
}
knives = {
    "bayonet": "★%20Bayonet%20%7C%20",
    "bowie": "★%20Bowie%20Knife%20%7C%20",
    "butterfly": "★%20Butterfly%20Knife%20%7C%20",
    "falchion": "★%20Falchion%20Knife%20%7C%20",
    "flip": "★%20Flip%20Knife%20%7C%20",
    "gut": "★%20Gut%20Knife%20%7C%20",
    "huntsman": "★%20Huntsman%20Knife%20%7C%20",
    "karambit": "★%20Karambit%20%7C%20",
    "m9bayonet": "★%20M9%20Bayonet%20%7C%20",
    "navaja": "★%20Navaja%20Knife%20%7C%20",
    "nomad": "★%20Nomad%20Knife%20%7C%20",
    "paracord": "★%20Paracord%20Knife%20%7C%20",
    "skeleton": "★%20Skeleton%20Knife%20%7C%20",
    "stiletto": "★%20Stiletto%20Knife%20%7C%20",
    "talon": "★%20Talon%20Knife%20%7C%20",
    "ursus": "★%20Ursus%20Knife%20%7C%20",
    "kukri": "★%20Kukri%20Knife%20%7C%20"
}

wear = {
    "fn": "(Factory%20New)",
    "mw": "(Minimal%20Wear)",
    "ft": "(Field-Tested)",
    "ww": "(Well-Worn)",
    "bs": "(Battle-Scarred)"
}

def get_price_and_volume():
    weapon_in = weapon_entry.get().lower()
    if " " in weapon_in:
        weapon_in = weapon_in.replace(" ", "")
           
    skin_in = skin_entry.get().title()
    wear_in = wear_entry.get()
    
    new_url = default_url
    
    if stattrak_var.get():
        if weapon_in in weapon:
            new_url += "StatTrak™%20"

    if weapon_in in weapon:
        new_url += weapon.get(weapon_in, "")
    elif weapon_in in knives:
        new_url += knives.get(weapon_in, "")
    else:
        price_label.config(text="Invalid weapon")
        return

    if new_url:
        if " " in skin_in:
            new_url += skin_in.replace(" ", "%20") + "%20"
        else:
            new_url += skin_in + "%20"
        new_url += wear.get(wear_in, "")

    response = requests.get(new_url)
    data = response.json()
    median_price = data.get("median_price")
    lowest_price = data.get("lowest_price")
    volume = data.get("volume")
    print(new_url)
    if median_price:
        price_label.config(text=f"Median Price: {median_price}")
    elif lowest_price:
        price_label.config(text=f"Lowest Price: {lowest_price}")
    else:
        price_label.config(text="No price found: Either float capped or none on market")

    if volume:
        volume_label.config(text=f"Volume: {volume}")
    else:
        volume_label.config(text="No volume found: Either float capped or none on market")

# GUI setup
root = tk.Tk()
root.title("CS2 Skin Price Checker")

frame = tk.Frame(root)
frame.pack(padx=70, pady=20)

weapon_label = tk.Label(frame, text="Weapon:")
weapon_label.grid(row=0, column=0, sticky="w")
weapon_entry = tk.Entry(frame)
weapon_entry.grid(row=0, column=1)

skin_label = tk.Label(frame, text="Skin:")
skin_label.grid(row=1, column=0, sticky="w")
skin_entry = tk.Entry(frame)
skin_entry.grid(row=1, column=1)

stattrak_var = tk.BooleanVar()
stattrak_checkbox = tk.Checkbutton(frame, text="StatTrak", variable=stattrak_var)
stattrak_checkbox.grid(row=1, column=2, sticky="w")


wear_label = tk.Label(frame, text="Wear:")
wear_label.grid(row=2, column=0, sticky="w")
wear_entry = tk.Entry(frame)
wear_entry.grid(row=2, column=1)

check_button = tk.Button(frame, text="Check Price", command=get_price_and_volume)
check_button.grid(row=3, columnspan=2)

price_label = tk.Label(frame, text="")
price_label.grid(row=4, columnspan=2)

volume_label = tk.Label(frame, text="")
volume_label.grid(row=5, columnspan=2)

default_url = "https://steamcommunity.com/market/priceoverview/?country=US&currency=!&appid=730&market_hash_name="

root.mainloop()
