import tkinter as tk
import requests

# Weapon and wear dictionaries remain the same
weapon = {
    "ak47": "AK-47%20%7C%20",
    "aug": "AUG%20%7C%20",
    "awp": "AWP%20%7C%20",
    "bizon": "PP-Bizon%20%7C%20",
    "cz75": "CZ75-Auto%20%7C%20",
    "deagle": "Desert%20Eagle%20%7C%20",
    "dual_berettas": "Dual%20Berettas%20%7C%20",
    "famas": "FAMAS%20%7C%20",
    "five_seven": "Five-SeveN%20%7C%20",
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
    "sawed_off": "Sawed-Off%20%7C%20",
    "scar20": "SCAR-20%20%7C%20",
    "sg553": "SG%20553%20%7C%20",
    "ssg08": "SSG%2008%20%7C%20",
    "tec9": "Tec-9%20%7C%20",
    "ump45": "UMP-45%20%7C%20",
    "usp_silencer": "USP-S%20%7C%20",
    "xm1014": "XM1014%20%7C%20"
}

wear = {
    "fn": "(Factory%20New)",
    "mw": "(Minimal%20Wear)",
    "ft": "(Field-Tested)",
    "ww": "(Well-Worn)",
    "bs": "(Battle-Scarred)"
}

# Function to get price and volume data
def get_price_and_volume():
    weapon_in = weapon_entry.get().lower()
    skin_in = skin_entry.get().title()
    wear_in = wear_entry.get()
    
    new_url = default_url
    
    if stattrak_var.get():
        new_url += "StatTrak™%20"

    new_url += weapon.get(weapon_in, "")

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
        price_label.config(text="No price found")

    if volume:
        volume_label.config(text=f"Volume: {volume}")
    else:
        volume_label.config(text="No volume found")

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
