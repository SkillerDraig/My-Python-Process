import random, time, json, os

SAVE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "savegame.json")

CLASSES = {
    "1": {"name": "Knight", "hp": 100, "atk": 12, "defense": 5, "gold": 50, "weapon": None},
    "2": {"name": "Mage",   "hp":  70, "atk": 16, "defense": 2, "gold": 30, "weapon": None},
    "3": {"name": "Archer", "hp":  85, "atk": 14, "defense": 3, "gold": 40, "weapon": None},
}

WEAPONS = {
    "1": {"name": "Iron Sword",    "atk_bonus": 6,  "cost": 40},
    "2": {"name": "Steel Axe",     "atk_bonus": 10, "cost": 70},
    "3": {"name": "Magic Staff",   "atk_bonus": 14, "cost": 110},
    "4": {"name": "Dragon Blade",  "atk_bonus": 20, "cost": 180},
}

LOCATIONS = {
    "village": {
        "name": "Village",
        "desc": "A quiet village. Weak monsters roam nearby.",
        "monsters": [
            {"name": "Goblin",   "hp": 30, "atk": 6,  "defense": 1, "gold": (5,  15)},
            {"name": "Wolf",     "hp": 40, "atk": 8,  "defense": 2, "gold": (8,  20)},
        ],
        "boss": None,
    },
    "cave": {
        "name": "Cave",
        "desc": "A dark cave. Stronger creatures lurk inside.",
        "monsters": [
            {"name": "Orc",      "hp": 55, "atk": 12, "defense": 4, "gold": (15, 35)},
            {"name": "Skeleton", "hp": 45, "atk": 10, "defense": 3, "gold": (12, 28)},
        ],
        "boss": None,
    },
    "dungeon": {
        "name": "Dungeon",
        "desc": "A deadly dungeon. The Demon King waits at the end.",
        "monsters": [
            {"name": "Zombie",   "hp": 60, "atk": 14, "defense": 5, "gold": (20, 45)},
            {"name": "Troll",    "hp": 80, "atk": 18, "defense": 7, "gold": (25, 55)},
        ],
        "boss": {"name": "Demon King", "hp": 150, "atk": 22, "defense": 12, "gold": (150, 300)},
    },
}

POTION_COST = 30
POTION_HEAL = 40

def pause(n=0.3):
    time.sleep(n)

def hr():
    print("-" * 40)

def player_atk(player):
    base = player["atk"]
    weapon = player.get("weapon")
    return base + (weapon["atk_bonus"] if weapon else 0)

def dmg(atk, defense):
    return max(0, atk - defense)

def save(player):
    data = dict(player)
    if data.get("weapon") is not None:
        data["weapon"] = dict(data["weapon"])
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("Game saved.")

def load():
    try:
        with open(SAVE_FILE) as f:
            player = json.load(f)
        if not isinstance(player.get("weapon"), dict):
            player["weapon"] = None
        for key in ("hp", "max_hp", "atk", "defense", "gold", "potions"):
            if key not in player:
                return None
        if "location" not in player or player["location"] not in LOCATIONS:
            player["location"] = "village"
        return player
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        return None

def create_player():
    print("\nChoose your class:")
    for k, c in CLASSES.items():
        print(f"  {k}. {c['name']}  HP:{c['hp']}  ATK:{c['atk']}  DEF:{c['defense']}  Gold:{c['gold']}")
    while True:
        choice = input("Enter 1-3: ").strip()
        if choice in CLASSES:
            c = CLASSES[choice]
            return {
                "name":     c["name"],
                "hp":       c["hp"],
                "max_hp":   c["hp"],
                "atk":      c["atk"],
                "defense":  c["defense"],
                "gold":     c["gold"],
                "potions":  1,
                "weapon":   None,
                "location": "village",
            }
        print("Invalid choice.")

def combat(player, enemy, is_boss=False):
    enemy_hp = enemy["hp"]
    label = "BOSS " if is_boss else ""
    print(f"\nA {label}{enemy['name']} appears!")
    hr()

    while True:
        weapon_name = player["weapon"]["name"] if player["weapon"] else "Fists"
        total_atk = player_atk(player)
        print(f"  You: {player['hp']}/{player['max_hp']} HP  ATK:{total_atk} ({weapon_name})")
        print(f"  {enemy['name']}: {enemy_hp} HP")
        print(f"  Potions: {player['potions']}")
        print("  1. Attack   2. Use Potion   3. Flee")
        action = input("  > ").strip()

        if action == "1":
            hit = dmg(total_atk, enemy["defense"])
            enemy_hp -= hit
            print(f"  You deal {hit} damage." if hit > 0 else "  Your attack is completely blocked!")
            pause()

            if enemy_hp <= 0:
                gold = random.randint(*enemy["gold"])
                player["gold"] += gold
                print(f"  You defeated the {enemy['name']}! +{gold} gold.")
                if is_boss:
                    print("\n  *** YOU WIN! The Demon King is defeated! ***")
                hr()
                return True

            hit = dmg(enemy["atk"], player["defense"])
            player["hp"] -= hit
            print(f"  {enemy['name']} deals {hit} damage." if hit > 0 else f"  {enemy['name']}'s attack is blocked!")
            pause()

            if player["hp"] <= 0:
                player["hp"] = 1
                print(f"  You were defeated by the {enemy['name']}...")
                hr()
                return False

        elif action == "2":
            if player["potions"] <= 0:
                print("  No potions left!")
            else:
                player["potions"] -= 1
                healed = min(POTION_HEAL, player["max_hp"] - player["hp"])
                player["hp"] += healed
                print(f"  You heal {healed} HP. ({player['hp']}/{player['max_hp']})")
            pause()

        elif action == "3":
            print("  You flee!")
            pause()
            return True

        else:
            print("  Invalid choice.")

def shop(player):
    while True:
        print(f"\n=== Shop === (Gold: {player['gold']})")
        current = player["weapon"]["name"] if player["weapon"] else "None"
        print(f"  Current weapon: {current}")
        hr()
        print(f"  1. Buy Health Potion  ({POTION_COST}g, heals {POTION_HEAL} HP)")
        print("  Weapons (replaces current):")
        for k, w in WEAPONS.items():
            print(f"  {int(k)+1}. {w['name']}  +{w['atk_bonus']} ATK  ({w['cost']}g)")
        print("  6. Leave")

        choice = input("  > ").strip()

        if choice == "1":
            if player["gold"] >= POTION_COST:
                player["gold"] -= POTION_COST
                player["potions"] += 1
                print(f"  Bought a potion! You now have {player['potions']}.")
            else:
                print("  Not enough gold.")
            pause()

        elif choice in ("2", "3", "4", "5"):
            wkey = str(int(choice) - 1)
            w = WEAPONS[wkey]
            if player["gold"] >= w["cost"]:
                player["gold"] -= w["cost"]
                player["weapon"] = w
                print(f"  You equipped {w['name']}! ATK +{w['atk_bonus']}.")
            else:
                print("  Not enough gold.")
            pause()

        elif choice == "6":
            break
        else:
            print("  Invalid choice.")

def explore(player):
    loc = LOCATIONS[player["location"]]
    print(f"\n=== {loc['name']} ===")
    print(f"  {loc['desc']}")
    hr()
    print("  1. Fight a monster")
    if loc["boss"]:
        print("  2. Challenge the BOSS (Demon King — come prepared!)")
        print("  3. Back")
    else:
        print("  2. Back")

    choice = input("  > ").strip()

    if choice == "1":
        enemy = dict(random.choice(loc["monsters"]))
        combat(player, enemy)

    elif choice == "2" and loc["boss"]:
        boss = dict(loc["boss"])
        combat(player, boss, is_boss=True)

def travel(player):
    print("\n=== Travel ===")
    loc_list = list(LOCATIONS.items())
    for i, (key, loc) in enumerate(loc_list, 1):
        marker = " <-- you are here" if key == player["location"] else ""
        print(f"  {i}. {loc['name']}{marker}")
    print(f"  {len(loc_list)+1}. Cancel")
    try:
        choice = int(input("  > "))
        if 1 <= choice <= len(loc_list):
            key = loc_list[choice - 1][0]
            player["location"] = key
            print(f"  You travel to {LOCATIONS[key]['name']}.")
    except ValueError:
        pass
    pause()

def main_menu(player):
    while True:
        loc_name = LOCATIONS[player["location"]]["name"]
        weapon_name = player["weapon"]["name"] if player["weapon"] else "None"
        print(f"\n=== {player['name']} | HP:{player['hp']}/{player['max_hp']} | ATK:{player_atk(player)} | DEF:{player['defense']} ===")
        print(f"    Weapon: {weapon_name}  |  Gold: {player['gold']}  |  Potions: {player['potions']}")
        print(f"    Location: {loc_name}")
        hr()
        print("  1. Explore")
        print("  2. Travel")
        print("  3. Shop")
        print("  4. Save")
        print("  5. Quit")

        choice = input("  > ").strip()

        if choice == "1":
            explore(player)
        elif choice == "2":
            travel(player)
        elif choice == "3":
            shop(player)
        elif choice == "4":
            save(player)
        elif choice == "5":
            save(player)
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

print("=== Adventure Game ===")
pause(0.5)

saved = load()
if saved:
    print(f"Save file found for '{saved['name']}'. Load it? (y/n)")
    if input("  > ").strip().lower() == "y":
        player = saved
        print(f"Welcome back, {player['name']}!")
    else:
        os.remove(SAVE_FILE)
        player = create_player()
else:
    player = create_player()

main_menu(player)
