# Copyright (c) 2025 Luboš Kulhan
# Licensed under the MIT License.

# This is a non-commercial fan project inspired by the Dark Souls series
# by FromSoftware. All Dark Souls names, characters, and content belong
# to their respective owners.

import os
import random as r
from time import sleep

# Variables ----------------------------------------
player_champion = None
player_boss = None
shield_bash_stagger = False
determination_active = False
counter_attack = False
special_move_cooldown = 0
special_move_ready = True
boss_intro = None
phase_2_text_part1 = None
phase_2_text_part2 = None
boss_win_text = None
boss_defeated_text = None
boss_phase2_win_text = None
boss_phase2_defeated_text = None
boss_phase2_defeated_reignite = None
boss_phase2_defeated_extinguish = None
phase_2_active = False
phase_2_stat_modified = False
difficulty_mode = "Normal"
real_champ_damage = None
real_boss_damage = None
frost_on_player = 0
crystal_sage_copy_alive = True
Gundyr_trophy = False
Vordt_trophy = False
Sage_trophy = False
Watchers_trophy = False
Sulyvahn_trophy = False
Yhorm_trophy = False
SoC_trophy = False

# Champion consumables ----------------------------------------
estus_flask_heal = 90
estus_flask_count = 3 # number of estus flasks available
turtle_neck_recovery = 80
turtle_neck_count = 1 # number of turtle necks available
exalted_flesh_count = 1 # number of exalted fleshes available
exalted_flesh_active = False # boost damage for 1 turn

# Champion Class ----------------------------------------
class Champion:
    def __init__(self, name, HP, damage, stamina, evade, damage_type, damage_resistance, damage_weakness):
        self.name = name
        self.HP = HP
        self.damage = damage
        self.stamina = stamina
        self.evade = evade # percentage chance to evade an attack
        self.damage_type = damage_type  # Standard, Slash, Strike, Magic, Fire
        self.damage_resistance = damage_resistance
        self.damage_weakness = damage_weakness

# Boss Class ----------------------------------------
class Boss:
    def __init__ (self, name,HP, damage, evade, damage_type, damage_resistance, damage_weakness):
        self.name = name
        self.HP = HP
        self.damage = damage
        self.evade = evade # percentage chance to evade an attack
        self.damage_type = damage_type  # Standard, Slash, Strike, Magic, Fire, Dark
        self.damage_resistance = damage_resistance
        self.damage_weakness = damage_weakness

# Champions ----------------------------------------
champions = [
    Champion("Knight", 150,80,100,40,"Standard","Slash","Strike/Magic"),
    Champion("Paladin", 200,60,110,30,"Strike","Slash","Strike/Magic"),
    Champion("Assassin", 120,100,90,70,"Slash","Strike/Magic","Slash/Fire"),
    Champion("Sorcerer", 110,120,90,40,"Magic","Magic","Slash/Fire"),
    Champion("Samurai", 130,80,100,50,"Slash","Strike","Magic/Fire"),
    Champion("Pyromancer", 110,90,90,40,"Fire","Fire","Slash")
]

# Bosses ----------------------------------------
bosses = [
    Boss("Iudex Gundyr",1300,40,5,"Standard","Slash","Strike/Magic"),
    Boss("Vordt of the Boreal Valley",1500,40,0,"Strike","Slash","Strike"),
    Boss("Crystal Sage",1250,60,5,"Magic","Magic","Slash/Fire"),
    Boss("Abyss Watchers",800,50,15,"Standard","Magic","Slash/Fire"),
    Boss("Pontiff Sulyvahn",1600,50,15,"Fire","Slash","Strike/Magic"),
    Boss("Yhorm the Giant",2000,50,0,"Standard","Slash","Strike"),
    Boss("Soul of Cinder",1500,60,5,"Fire","Fire","Strike/Magic")
]

# Functions ----------------------------------------
def clear_screen():    # Function to clear the screen
    os.system('cls' if os.name == 'nt' else 'clear') # Works for Windows and Unix-based systems
def exit_game():    # Function to exit the game
    os._exit(1)
def skip():
    print("\nPress Enter to continue.")
    input()
    clear_screen()

def main_menu():    # Main menu function
    global difficulty_mode
    while True:
        print("Welcome to Dark Souls 3 Pantheon!")
        print("1. Start Game\n2. Champions list\n3. Bosses list\n4. Consumables list\n5. Damage types\n6. Achivements\n7. Credits\n8. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                clear_screen()
                dif_choice = input("Choose your difficulty, Normal (1) or Hard (2): ")
                try:
                    if dif_choice == '1':
                        difficulty_mode = "Normal"
                        print("\nYou have chosen Normal mode. Foes will hold back.")
                        skip()
                        choose_champion_boss()
                    elif dif_choice == '2':
                        difficulty_mode = "Hard"
                        print("\nYou have chosen Hard mode. Foes will show no mercy.")
                        skip()
                        choose_champion_boss()
                    else:
                        clear_screen()
                        print("Invalid input. Try again.\n")
                        skip()
                except:
                        clear_screen()
                        print("Invalid input. Try again.\n")
                        skip()
            elif choice == '2':
                clear_screen()
                champion_list()
            elif choice == '3':
                clear_screen()
                boss_list()
            elif choice == '4':
                clear_screen()
                consumables_list()
            elif choice == '5':
                clear_screen()
                damage_types()
            elif choice == '6':
                clear_screen()
                players_achivements()
            elif choice == '7':
                clear_screen()
                credits()
            elif choice == '8':
                clear_screen()
                print("Farewell ashen one...")
                sleep(2)
                clear_screen()
                exit_game()
            else:
                clear_screen()
                print("Invalid input. Try again.\n")
                skip()
        except:
            clear_screen()
            print("Invalid input. Try again.\n")
            skip()

def players_achivements():
    pass
def choose_champion_boss():     # Function to choose champion and boss
    global player_champion
    global player_boss

    while(True):
        i = 0
        print("List of Champions:")
        for champ in champions:
            print(f"{i + 1}. {champ.name} - HP: {champ.HP}, Damage: {champ.damage}, Stamina: {champ.stamina}, Evade: {champ.evade}%")
            i += 1
        try:
            player_choice = int(input(f"Choose your champion (1-{len(champions)}): "))
            player_champion = champions[player_choice-1]
            print(f"You have chosen {player_champion.name}!")
            clear_screen()
            break
        except (IndexError,ValueError):
            clear_screen()
            print("Invalid input. Try again.\n")
            skip()

    while(True):
        y = 0
        print("List of Bosses:")
        for boss in bosses:
            print(f"{y + 1}. {boss.name} - HP: {boss.HP}, Damage: {boss.damage}")
            y+= 1
        try:
            player_choice = int(input(f"Pick a boss you want to fight (1-{len(bosses)}): "))
            player_boss = bosses[player_choice-1]
            print(f"You have chosen {player_boss.name}!")
            clear_screen()
            fight()
        except (IndexError,ValueError):
            clear_screen()
            print("Invalid input. Try again.\n")
            skip()
def champion_list():    # Function to display champion list
    print("List of Champions:\n")
    print("Knight\nOnce a proud guardian of a fallen kingdom, he now roams the ash-choked lands, bound by memory and regret.\nWeapon: Broadsword\n")
    print("Paladin\nForgoten defender of godhome, whose prayers echo unanswered in the silence of dead gods.\nWeapon: Great Mace\n")
    print("Assassin\nPhantom of carnage, moving unseen through shadow, his blade whispering of forgotten sins.\nWeapon: Dagger\n")
    print("Sorcerer\nScholar consumed by the very sorcery she wanted to master, her soul flickering like dying embers.\nWeapon: Staff\n")
    print("Samurai\nSwordsman who perfected his art at the cost of his humanity, now bound to the dance of endless battle.\nWeapon: Uchigatana\n")
    print("Pyromancer\nOnce a Fire Keeper, she broke her sacred vow and embraced the flame’s forbidden touch. Now she burns eternally, neither servant nor savior.\nWeapong: Pyromancy Flame\n")
    skip()   
def boss_list():    # Function to display boss list     ADD PHASE 2 DESCRIPTION!
    print("List of Bosses:\n")
    print("Iudex Gundyr\nOnce a judge of the First Flame, he now stands forever at the threshold, his halberd stained with the blood of uncounted challengers.\n")
    print("Vordt of the Boreal Valley\nBeast once crowned in frost and fury, now a raging shell of servitude, its greatfrost mace tearing through all who dare approach.\n")
    print("Crystal Sage\nA fractured mind trapped in a crystalline prison, his staff channeling spells that echo the chaos of a world long lost to time.\n")
    print("Abyss Watchers\nBound by the cursed flame of the Abyss, they rise and fall in endless battle, their bloodied swords and blades singing of unity and doom.\n")
    print("Pontiff Sulyvahn\nTyrant cloaked in grandeur, whose silvered twin swords and whispered lies turned a city of faith into a citadel of shadow.\n")
    print("Yhorm the Giant\nOnce a lord of fire and storm, he now lumbers through ruin, his great machete is a monument to a kingdom swallowed by ash.\n")
    print("Soul of Cinder\nThe ever-burning echo of countless heroes, it rises and falls with the First Flame, its Firelink Sword striking down all who seek to tamper with the flame.\n")
    skip()
def consumables_list():
    print("List of consumables:\n")
    print("Estus flask\nSacred vial of golden fire, capable of healing flesh and spirit alike, carried by those who walk amidst death.\n")
    print("Turtle neck\nBitter draught meat from the shell of a rare creature, it revitalizes the weary, restoring stamina to body and limb.\n")
    print("Exalted flesh\nChunk of strange, crimson flesh that pulses with latent power, granting those who consume it the strength to strike with greater force.\n")
    skip()
def damage_types():
    print("List of damage types:\n")
    print("Standard\nPlain, unadorned strikes that rely on raw force; steady against most foes but lacks specialization.\n")
    print("Slash\nA cutting edge that tears through flesh and fabric, leaving wounds that fester; less effective against heavy armor.\n")
    print("Strike\nBlunt, crushing blows that batter armor and bone alike; weaker against lightly armored or nimble foes.\n")
    print("Magic\nArcane energy woven from study and will, capable of piercing both body and mind; weak against foes hardened by magic.\n")
    print("Fire\nFlames that burn and sear, capable of rending flesh and spirit; less effective against flame followers and demons alike.\n")
    skip()

def update_trophy(boss_name):
    trophy_file = "trophy.txt"

    trophies = {}
    with open(trophy_file, "r") as file:
        for x in file:
            name, value = x.strip().split(" = ")
            if value == "True":
                trophies[name] = True
            else:
                trophies[name] = False

    boss_trophy = f"{boss_name}"
    if boss_trophy in trophies:
        trophies[boss_trophy] = True

    with open(trophy_file, "w") as file:
        for name, value in trophies.items():
            file.write(f"{name} = {value}\n")

def credits():
    print("Game made by Luboš Kulhan.\nLast update in 2025-12-22.")
    skip()

def boss_text(boss,champion):
    global boss_intro
    global boss_win_text
    global boss_defeated_text
    global phase_2_text_part1
    global phase_2_text_part2
    global boss_phase2_win_text
    global boss_phase2_defeated_text
    global boss_phase2_defeated_reignite
    global boss_phase2_defeated_extinguish
    match player_boss.name:
        case "Iudex Gundyr":
            boss_intro = f"\n{boss} kneels in silence... then rises to judge the unkindled once more.\n"
            boss_win_text = f"{champion} is cast down, their flame unworthy in the eyes of {boss}. The forgotten judge returns to his vigil."
            boss_defeated_text = f"{boss} falls to one knee, his duty finally ended. As he turns to dust, {champion} senses the weight of judgment fade into stillness."
            boss_phase2_win_text = f"{champion} falls, consumed by the black ichor. No mercy remains — only the echoes of judgment endure."
            boss_phase2_defeated_text = f"{boss} collapses at last, shattered by the unkindled's resolve. As his form dissolves to ash, {champion} perceives the lingering judgment slowly fading into stillness."
            phase_2_text_part1 = f"{boss} falls to one knee, trembling"
            phase_2_text_part2 = "then rises anew, his form twisted by black grotesque ichor. His attacks heavier, but slower."
        case "Vordt of the Boreal Valley": 
            boss_intro = f"\nA chilling wind sweeps the air as {boss} emerges from the frost.\n"
            boss_win_text = f"{champion} is crushed beneath the icy fury of {boss}. The frozen beast bellows into the void, bound forever to his madness."
            boss_defeated_text = f"With a final, shuddering roar, {boss} collapses. Frost turns to mist as {champion} stands amidst the silence of a long-dead kingdom."
            boss_phase2_win_text = f"{champion} is torn apart beneath the relentless onslaught of Vordt, each icy strike etching agony into flesh and bone."
            boss_phase2_defeated_text = f"{boss} finally falls, his monstrous howls echoing across the frozen valley. {champion} stands battered, yet the icy shadow lingers long after the roar fades."
            phase_2_text_part1 = f"{boss} falters, frost cracking across his massive frame"
            phase_2_text_part2 = "Vordt's body is enshrouded in a blizzard of icy wrath, and the battlefield trembles under his freezing roar!"
        case "Crystal Sage":
            boss_intro = f"\nA hooded figure shuffles from the mist, staff cracked, robes tattered. {boss} mutters forgotten incantations.\n"
            boss_win_text = f"{champion} is unmade by a storm of crystal shards. The Sage’s hollow chant fades into silence."
            boss_defeated_text = f"{boss} falls, staff splintering. Shards scatter like dead stars. {champion} stands in the ruins of a library long burned."
            boss_phase2_win_text = f"{champion} is torn asunder by the relentless barrage of crystalline magic. Each spell twists reality, leaving only disorientation and ruin in its wake."
            boss_phase2_defeated_text = f"{boss} collapses, fragments of light scattering like broken time itself. {champion} barely stands, the echoes of arcane fury still ringing in their ears."
            phase_2_text_part1 = f"{boss} fractures, her form splitting into twin apparitions. One real, one false"
            phase_2_text_part2 = "the Sage's deception begins."
        case "Abyss Watchers":
            boss_intro = f"\nA chorus of clashing steel echoes through the dark as {boss} surge forward.\n"
            boss_win_text = f"{champion} is overwhelmed by the frenzied blades of {boss}. Their cursed vigil continues, unbroken and unyielding."
            boss_defeated_text = f"{boss} falters, their final clash silenced at last. {champion} stands amidst the ashen remains of a brotherhood lost to darkness."
            boss_phase2_win_text = f"{champion} is cut down by the relentless coordination of Abyss Watcher, each strike precise, merciless, and unrelenting."
            boss_phase2_defeated_text = f"{boss} crumbles, their abyssal flame snuffed out. {champion} stands weary, the shadows of their brotherhood lingering long after the fight."
            phase_2_text_part1 = f"As the last Abyss Watcher falls, the {champion} stands victorious"
            phase_2_text_part2 = "then the souls of the fallen gather, filling an empty vessel. From it, one final Abyss Watcher rises, filled with the suffering and fury of his fallen brothers."
        case "Pontiff Sulyvahn":
            boss_intro = f"\nTwin swords gleam in the dim light as {boss} descends, a crownless sovereign of fire and deceit.\n"
            boss_win_text = f"{champion} falls beneath the merciless onslaught of {boss}. The Pontiff’s dominion persists, cruel and unchallenged."
            boss_defeated_text = f"{boss} crumples, his ambition turned to ash. {champion} feels the oppressive weight of tyranny lift, if only for a fleeting moment."
            boss_phase2_win_text = f"{champion} is overwhelmed by {boss}'s relentless assault, each strike a cold testament to power corrupted. Mercy has long fled from this hall."
            boss_phase2_defeated_text = f"At last, {boss} crumbles, his silvered blades clattering to the ground. {champion} feels the oppressive weight of tyranny lift, if only for a moment."
            phase_2_text_part1 = f"{boss} falters, shadows twisting around him"
            phase_2_text_part2 = "then he surges forth, twin swords blazing, swifter and deadlier than ever, each strike a storm of wrath and steel."
        case "Yhorm the Giant":
            boss_intro = f"\nThe ground trembles with each step as {boss} rises.\n"
            boss_win_text = f"{champion} is crushed beneath the towering might of {boss}. His sorrowful roar echoes across the desolate land."
            boss_defeated_text = f"{boss} collapses, the last ember of his dominion snuffed out. {champion} stands amidst the ruins of a kingdom long forgotten."
            boss_phase2_win_text = f"{champion} is incinerated in {boss}'s profane inferno. The giant's grief consumes all."
            boss_phase2_defeated_text = f"{boss} falls silent, profane flames guttering to ash. {champion} stands over the broken throne, storm fading."
            phase_2_text_part1 = f"{boss} staggers, clutching his chest"
            phase_2_text_part2 = "then roars in anguish. Profane flame erupts from his wounds, storm clouds gathering above. The betrayed lord unleashes his final fury."
        case "Soul of Cinder":
            boss_intro = f"\nThe echo of countless fallen souls whispers as {boss} approaches.\n"
            boss_win_text = f"{champion} falls, their flame extinguished. {boss} roams once more, awaiting the next challenger."
            boss_defeated_text = f"{boss} collapses into ash and silence. Yet even in victory, {champion} feels the weight of a thousand untold sacrifices."
            boss_phase2_win_text = f"{champion} falls before the first Lord's unyielding will. The throne remains eternal."
            boss_phase2_defeated_reignite = f"{boss} scatters to final embers. {champion} kneels before the First Flame and feeds it their soul. The cycle endures."
            boss_phase2_defeated_extinguish = f"{boss} scatters to final embers. {champion} turns from the First Flame and walks into shadow. The Age of Dark begins."
            if 1 == r.randint(1,100):
                phase_2_text_part1 = "Plim Plim Plom, Plim Plom Plim, Plim Plom"
            else:
                phase_2_text_part1 = f"{boss} crumbles to ash"
                phase_2_text_part2 = "then reignites with blinding fury. Gwyn's soul dominates—the progenitor of flame rejects defeat."

    return (
        boss_intro or "",
        boss_win_text or "",
        boss_defeated_text or "",
        phase_2_text_part1 or "",
        phase_2_text_part2 or "",
        boss_phase2_win_text or "",
        boss_phase2_defeated_text or "",
        boss_phase2_defeated_reignite or "",
        boss_phase2_defeated_extinguish or ""
    )        

def boss_phase_2_tansition():
    print(phase_2_text_part1,end="",flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        sleep(1.5)
    print(f"\n{phase_2_text_part2}")
    sleep(3)
    skip()

def fight():
    global estus_flask_count
    global estus_flask_heal
    global turtle_neck_count
    global turtle_neck_recovery
    global exalted_flesh_count
    global exalted_flesh_active
    global shield_bash_stagger
    global determination_active
    global special_move_cooldown
    global special_move_ready
    global counter_attack
    global boss_intro
    global boss_win_text
    global boss_defeated_text
    global real_champ_damage
    global real_boss_damage
    global boss_phase2_defeated_reignite
    global boss_phase2_defeated_extinguish
    global phase_2_active
    global phase_2_stat_modified
    global phase_2_text_part1
    global phase_2_text_part2
    global frost_on_player
    global crystal_sage_copy_alive
    boss_current_HP = player_boss.HP
    player_current_HP = player_champion.HP
    player_current_stamina = player_champion.stamina

    # Boss text
    boss_text(player_boss.name,player_champion.name)

    # Start of the battle
    print(f"From the white mist, {player_champion.name} emerges.\n")
    for a in range(3):
        print(".")
        sleep(1)
    print(boss_intro)
    for a in range(3):
        print(".")
        sleep(1)
    skip()

    while True:

        if player_champion.damage_type in player_boss.damage_resistance:
            real_champ_damage = player_champion.damage * 0.8
            damage_champ_text = f"{player_champion.name}'s attack proves less potent, dealing only {int(real_champ_damage)} damage."
        elif player_champion.damage_type in player_boss.damage_weakness:
            real_champ_damage = player_champion.damage * 1.2
            damage_champ_text = f"{player_boss.name} recoils — {player_champion.name} attack strikes deep, dealing {int(real_champ_damage)} damage."
        else:
            real_champ_damage = player_champion.damage
            damage_champ_text = f"{player_champion.name} attacks {player_boss.name}, dealing {int(real_champ_damage)} damage."

        if player_boss.damage_type in player_champion.damage_resistance:
            real_boss_damage = player_boss.damage * 0.9
            damage_boss_text = f"{player_boss.name}'s attack lacks its usual strength, dealing only {int(real_boss_damage)} damage."
        elif player_boss.damage_type in player_champion.damage_weakness:
            real_boss_damage = player_boss.damage * 1.1
            damage_boss_text = f"{player_champion.name} takes a heavy hit — {player_boss.name} deals {int(real_boss_damage)} damage."
        else:
            real_boss_damage = player_boss.damage
            damage_boss_text = f"{player_boss.name} hits {player_champion.name}, dealing {int(real_boss_damage)} damage."

        # Player's turn
        while True:
            if frost_on_player == 2:
                print("You will take damage from frost this round!\n")
            print(f"{player_champion.name} - HP: {int(player_current_HP)}, Stamina: {player_current_stamina}")
            print(f"{player_boss.name} - HP: {int(boss_current_HP)}\n")
            print("Choose your action:")
            print("1. Attack")
            print("2. Consumables")
            print("3. Skip turn")
            player_action = input("Enter your choice: ")

            # Attack menu
            if player_action == '1':
                clear_screen()
                if special_move_ready:
                    print("Choose attack to execute:")
                    print("1. Basic Attack (25 stamina)")
                    print("2. Special Move (50 stamina)")
                    print("3. Back")
                else:
                    print("Choose attack to execute:")
                    print("1. Basic Attack (25 stamina)")
                    print("2. Special Move on cooldown")
                    print("3. Back")
                attack_choice = input("Enter your choice: ")

                if attack_choice == '1':
                    if player_current_stamina >= 25:
                        evade_chance_boss = r.randint(1,100)
                        if (evade_chance_boss <= player_boss.evade) and shield_bash_stagger == False:
                            player_current_stamina -= 25
                            clear_screen()
                            print(f"{player_boss.name} steps aside, causing {player_champion.name} to miss their attack!\n\n")
                            player_current_HP -= (real_boss_damage * 0.5)
                            print(f"{player_boss.name} counter attacks, dealing {int(real_boss_damage * 0.5)} damage to {player_champion.name}!")
                            skip()
                            if player_current_HP <= 0 and phase_2_active == True:
                                print(boss_phase2_win_text)
                                sleep(3)
                                skip()
                                main_menu()
                            elif player_current_HP <= 0:
                                print(boss_win_text)
                                sleep(3)
                                skip()
                                main_menu()
                            else:
                                pass
                        elif (phase_2_active and player_boss.name == "Crystal Sage") and  (evade_chance_boss < 50) and crystal_sage_copy_alive:
                            clear_screen()
                            player_current_stamina -= 25
                            crystal_sage_copy_alive = False
                            print(f"{player_champion.name} shatters the false Sage, leaving only {player_boss.name} standing.")
                            skip()
                        else:
                            if determination_active and exalted_flesh_active:
                                clear_screen()
                                boosted_damage = real_champ_damage * 1.2 * 1.2
                                player_current_stamina -= 25
                                boss_current_HP -= boosted_damage
                                print(f"{player_champion.name} strikes with fury and determination, dealing {int(boosted_damage)} damage!")
                                skip()
                            elif determination_active:
                                clear_screen()
                                boosted_damage = real_champ_damage * 1.2
                                player_current_stamina -= 25
                                boss_current_HP -= boosted_damage
                                print(f"{player_champion.name} strikes with determination, dealing {int(boosted_damage)} damage!")
                                skip()
                            elif exalted_flesh_active:
                                clear_screen()
                                boosted_damage = real_champ_damage * 1.2
                                player_current_stamina -= 25
                                boss_current_HP -= boosted_damage
                                print(f"{player_champion.name} strikes with fury, dealing {int(boosted_damage)} damage!")
                                skip()
                            else:
                                clear_screen()
                                player_current_stamina -= 25
                                boss_current_HP -= real_champ_damage
                                print(damage_champ_text)
                                skip()
                    else:
                        clear_screen()
                        print("Not enough stamina to attack!")
                        skip()
                elif attack_choice == '2':
                    clear_screen()
                    if player_current_stamina >= 50 and special_move_ready:
                        if player_champion.name == "Knight":
                            shield_bash_stagger = True
                            player_current_stamina -= 50
                            special_move_ready = False
                            special_move_cooldown = 0
                            if (phase_2_active and player_boss.name == "Crystal Sage") and  (evade_chance_boss < 50) and crystal_sage_copy_alive:
                                crystal_sage_copy_alive = False
                                print(f"The Knight crashes into {player_boss.name}'s illusion with his shield.\nIllusion falters, leaving only {player_boss.name} standing.")
                            else:
                                print(f"The Knight crashes into {player_boss.name} with his shield.\n{player_boss.name} is staggered.")
                            skip()
                        elif player_champion.name == "Paladin":
                            determination_active = True
                            player_current_stamina -= 50
                            special_move_ready = False
                            special_move_cooldown = 0
                            print(f"The Paladin lifts his mace toward the heavens.\nFaith hardens his attacks.")
                            skip()
                        elif player_champion.name == "Assassin":
                            player_current_stamina -= 50
                            special_move_ready = False
                            special_move_cooldown = 0
                            if (phase_2_active and player_boss.name == "Crystal Sage") and  (evade_chance_boss < 50) and crystal_sage_copy_alive:
                                crystal_sage_copy_alive = False
                                print(f"The Assassin vanishes in a blur, his blade seeking the cracks in armor.\n{player_boss.name}'s illusion got criticaly stabed, leaving only {player_boss.name} standing.")
                            else:
                                boss_current_HP -= player_champion.damage * 2.5
                                print(f"The Assassin vanishes in a blur, his blade seeking the cracks in armor.\n{player_boss.name} got criticaly stabed for {int(player_champion.damage * 2.5)} damage!")
                            skip()
                        elif player_champion.name == "Sorcerer":
                            moon_damage = real_champ_damage + player_current_stamina * 1.75
                            boss_current_HP -= moon_damage
                            player_current_stamina = 0
                            special_move_ready = False
                            special_move_cooldown = 0
                            if (phase_2_active and player_boss.name == "Crystal Sage") and  (evade_chance_boss < 50) and crystal_sage_copy_alive:
                                crystal_sage_copy_alive = False
                                print(f"The Sorcerer channels all her stamina, shaping a dark moon of arcane force.\n{player_boss.name} is blasted aside for {int(moon_damage)} HP!")
                                print(f"\nHer illusion is torn appart.")
                            else:
                                print(f"The Sorcerer channels all her stamina, shaping a dark moon of arcane force.\n{player_boss.name} is blasted aside for {int(moon_damage)} HP!")
                            skip()
                        elif player_champion.name == "Samurai":
                            counter_attack = True
                            player_current_stamina -= 50
                            special_move_ready = False
                            special_move_cooldown = 0
                            print(f"The Samurai tightens his stance.\nReady to counter {player_boss.name} next attack.")
                            skip()
                        elif player_champion.name == "Pyromancer":
                            player_current_stamina -= 50
                            special_move_ready = False
                            special_move_cooldown = 0
                            flame_damage = real_champ_damage + player_current_HP * 2
                            player_current_HP = player_current_HP / 2
                            if (phase_2_active and player_boss.name == "Crystal Sage") and  (evade_chance_boss < 50) and crystal_sage_copy_alive:
                                crystal_sage_copy_alive = False
                                print(f"The Pyromancer sets herself aflame, sacrificing {int(player_current_HP)} HP.\nShe grasps {player_boss.name}'s illusion — burning it alive, leaving only {player_boss.name} standing.")
                            else:
                                boss_current_HP -= flame_damage
                                print(f"The Pyromancer sets herself aflame, sacrificing {int(player_current_HP)} HP.\nShe grasps {player_boss.name} — burning her for {int(flame_damage)} HP!")
                            skip()
                    else:
                        print("Not enough stamina to perform special move!")
                        skip()
                        clear_screen()
                elif attack_choice == '3':
                    clear_screen()
                    continue
                else:
                    clear_screen()
                    print("Invalid input. Try again.\n")
                    skip()

            # Consumables menu       
            elif player_action == '2':
                clear_screen()
                print("\nChoose consumable to use:")
                print(f"1. Estus Flask ({estus_flask_count} left)")
                print(f"2. Turtle Neck ({turtle_neck_count} left)")
                print(f"3. Exalted Flesh ({exalted_flesh_count} left)")
                print("4. Back")
                consumable_choice = input("Enter your choice: ")

                if consumable_choice == '1':
                    clear_screen()
                    if estus_flask_count > 0:
                        player_current_HP += estus_flask_heal
                        estus_flask_count -= 1
                        print(f"{player_champion.name} drinks from Estus Flask, restoring {estus_flask_heal} HP!")
                        if player_current_HP > player_champion.HP:
                            player_current_HP = player_champion.HP
                        skip()
                    else:
                        print("The estus flask is empty!")
                        skip()
                elif consumable_choice == '2':
                    clear_screen()
                    if turtle_neck_count > 0:
                        player_current_stamina += turtle_neck_recovery
                        turtle_neck_count -= 1
                        print(f"{player_champion.name} consumes a Turtle Neck, restoring {turtle_neck_recovery} stamina!")
                        if player_current_stamina > player_champion.stamina:
                            player_current_stamina = player_champion.stamina
                        skip()
                    else:
                        print("No turtle necks left!")
                        skip()
                elif consumable_choice == '3':
                    clear_screen()
                    if exalted_flesh_count > 0:
                        exalted_flesh_count -= 1
                        exalted_flesh_active = True
                        print(f"{player_champion.name} consumes Exalted Flesh, boosting damage for this turn!")
                        skip()
                    else:
                        print("No exalted fleshes left!")
                        skip()
                elif consumable_choice == '4':
                    clear_screen()
                    continue
                else:
                    clear_screen()
                    print("Invalid input. Try again.\n")
                    skip()

            # Skip attack
            elif player_action == '3':
                clear_screen()
                print(f"{player_champion.name} needs to gather strenght for next attack.")
                skip()
                break
            else:
                clear_screen()
                print("Invalid input. Try again.\n")
                skip()
            
            # Boss dead checker and phase 2 activator
            if difficulty_mode == "Normal":
                if boss_current_HP <= 0:
                    clear_screen()
                    print(boss_defeated_text)
                    sleep(3)
                    skip()
                    main_menu()
            else: # Difficulty Hard
                if phase_2_active == True and boss_current_HP <= 0:
                    clear_screen()
                    print(boss_phase2_defeated_text)
                    sleep(3)
                    skip()
                    main_menu()
                else:
                    if phase_2_active == False:

                        if (player_boss.name == "Soul of Cinder" or player_boss.name == "Abyss Watchers") and boss_current_HP <= 0:
                            phase_2_active = True
                            boss_current_HP = player_boss.HP
                            boss_phase_2_tansition()
                        elif boss_current_HP <= (player_boss.HP*0.5) and (player_boss.name not in ["Abyss Watchers", "Soul of Cinder"]):
                            phase_2_active = True
                            boss_phase_2_tansition()

        # Boss's turn
        evade_chance = r.randint(1,100)
        match player_boss.name:
            case "Iudex Gundyr":    # Iudex Gundyr ----------------------------------------------------
                player_champion_base_evade = player_champion.evade
                if phase_2_active == True:
                    real_boss_damage = (real_boss_damage*1.2)
                    player_champion_base_evade = player_champion.evade + 10

                if player_boss.damage_type in player_champion.damage_resistance:
                    damage_boss_text = f"{player_boss.name}'s attack lacks its usual strength, dealing only {int(real_boss_damage)} damage."
                elif player_boss.damage_type in player_champion.damage_weakness:
                    damage_boss_text = f"{player_champion.name} takes a heavy hit — {player_boss.name} deals {int(real_boss_damage)} damage."
                else:
                    damage_boss_text = f"{player_boss.name} hits {player_champion.name}, dealing {int(real_boss_damage)} damage."

                if shield_bash_stagger:
                    print(f"{player_boss.name} stands back on its feet, ready for next attack.")
                    shield_bash_stagger = False
                    skip()
                else:            
                    if player_current_stamina >= 15 and evade_chance < player_champion_base_evade:
                        print(f"{player_champion.name} evades {player_boss.name}'s attack!")
                        skip()
                    else:
                        if counter_attack:
                            counter_damage_player = (real_champ_damage * 1.75)
                            counter_damage_boss = (real_boss_damage/3)
                            player_current_HP -= counter_damage_boss
                            boss_current_HP -= counter_damage_player
                            print(f"{player_champion.name} counters {player_boss.name} attack, slashing him for {int(counter_damage_player)} damage.\n{player_champion.name} is wounded only for {int(counter_damage_boss)} damage.")
                            skip()
                        else:
                            player_current_HP -= real_boss_damage
                            print(damage_boss_text)
                            skip()

                    if player_current_HP <= 0 and phase_2_active == True:
                        print(boss_phase2_win_text)
                        sleep(3)
                        skip()
                        main_menu()
                    elif player_current_HP <= 0:
                        print(boss_win_text)
                        sleep(3)
                        skip()
                        main_menu()

                    if difficulty_mode == "Normal":
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                    else: # Difficulty Hard
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_phase2_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                        elif phase_2_active == False and (boss_current_HP <= (player_boss.HP*0.5)):
                            phase_2_active = True
                            boss_phase_2_tansition()

            case "Vordt of the Boreal Valley": # Vordth of the Boreal Valley ----------------------------------------------------
                player_champion_base_evade = player_champion.evade
                if phase_2_active:
                    player_champion_base_evade = player_champion.evade - 10
                    frost_on_player += 1
                    if frost_on_player >= 3:
                        frost_on_player = 0
                        frost_damage = (player_boss.damage*0.5)
                        player_current_HP -= frost_damage
                        print(f"The cold is unbearable — {player_champion.name} suffers {int(frost_damage)} damage!")
                        skip()
                        if player_current_HP <= 0:
                            print(f"{player_boss.name} succumbs to the frost... yet even without an audience, Vordt still roars.")
                            skip()
                            main_menu()

                if player_boss.damage_type in player_champion.damage_resistance:
                    damage_boss_text = f"{player_boss.name}'s attack lacks its usual strength, dealing only {int(real_boss_damage)} damage."
                elif player_boss.damage_type in player_champion.damage_weakness:
                    damage_boss_text = f"{player_champion.name} takes a heavy hit — {player_boss.name} deals {int(real_boss_damage)} damage."
                else:
                    damage_boss_text = f"{player_boss.name} hits {player_champion.name}, dealing {int(real_boss_damage)} damage."

                if shield_bash_stagger:
                    print(f"{player_boss.name} stands back on its feet, ready for next attack.")
                    shield_bash_stagger = False
                    skip()
                else:            
                    if player_current_stamina >= 15 and evade_chance < player_champion_base_evade:
                        print(f"{player_champion.name} evades {player_boss.name}'s attack!")
                        skip()
                    else:
                        if counter_attack:
                            counter_damage_player = (real_champ_damage * 1.75)
                            counter_damage_boss = (real_boss_damage/3)
                            player_current_HP -= counter_damage_boss
                            boss_current_HP -= counter_damage_player
                            print(f"{player_champion.name} counters {player_boss.name} attack, slashing him for {int(counter_damage_player)} damage.\n{player_champion.name} is wounded only for {int(counter_damage_boss)} damage.")
                            skip()
                        else:
                            player_current_HP -= real_boss_damage
                            print(damage_boss_text)
                            skip()

                    if player_current_HP <= 0 and phase_2_active == True:
                        print(boss_phase2_win_text)
                        sleep(3)
                        skip()
                        main_menu()
                    elif player_current_HP <= 0:
                        print(boss_win_text)
                        sleep(3)
                        skip()
                        main_menu()
            
                    if difficulty_mode == "Normal":
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                    else: # Difficulty Hard
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_phase2_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                        elif phase_2_active == False and (boss_current_HP <= (player_boss.HP*0.5)):
                            phase_2_active = True
                            boss_phase_2_tansition()

            case "Crystal Sage": # Crystal Sage ----------------------------------------------------
                if phase_2_active and crystal_sage_copy_alive == False:
                    real_boss_damage = (player_boss.damage * 1.1)
                    crystal_sage_copy_alive = True
                    print(f"Reality warps as {player_boss.name} summons another illusion.")
                    skip()
                if player_boss.damage_type in player_champion.damage_resistance:
                    damage_boss_text = f"{player_boss.name}'s attack lacks its usual strength, dealing only {int(real_boss_damage)} damage."
                elif player_boss.damage_type in player_champion.damage_weakness:
                    damage_boss_text = f"{player_champion.name} takes a heavy hit — {player_boss.name} deals {int(real_boss_damage)} damage."
                else:
                    damage_boss_text = f"{player_boss.name} hits {player_champion.name}, dealing {int(real_boss_damage)} damage."

                if shield_bash_stagger:
                    print(f"{player_boss.name} stands back on its feet, ready for next attack.")
                    shield_bash_stagger = False
                    skip()
                else:            
                    if player_current_stamina >= 15 and evade_chance < player_champion.evade:
                        print(f"{player_champion.name} evades {player_boss.name}'s attack!")
                        skip()
                    else:
                        if counter_attack:
                            counter_damage_player = (real_champ_damage * 1.75)
                            counter_damage_boss = (real_boss_damage/3)
                            player_current_HP -= counter_damage_boss
                            boss_current_HP -= counter_damage_player
                            print(f"{player_champion.name} counters {player_boss.name} attack, slashing him for {int(counter_damage_player)} damage.\n{player_champion.name} is wounded only for {int(counter_damage_boss)} damage.")
                            skip()
                        else:
                            player_current_HP -= real_boss_damage
                            print(damage_boss_text)
                            skip()

                    if player_current_HP <= 0 and phase_2_active == True:
                        print(boss_phase2_win_text)
                        sleep(3)
                        skip()
                        main_menu()
                    elif player_current_HP <= 0:
                        print(boss_win_text)
                        sleep(3)
                        skip()
                        main_menu()
            
                    if difficulty_mode == "Normal":
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                    else: # Difficulty Hard
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_phase2_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                        elif phase_2_active == False and (boss_current_HP <= (player_boss.HP*0.5)):
                            phase_2_active = True
                            boss_phase_2_tansition()

            case "Abyss Watchers": # Abyss Watchers ----------------------------------------------------
                if phase_2_active:
                    phase_2_stat_modified = True
            
                if player_boss.damage_type in player_champion.damage_resistance:
                    damage_boss_text = f"{player_boss.name}'s attack lacks its usual strength, dealing only {int(real_boss_damage)} damage."
                elif player_boss.damage_type in player_champion.damage_weakness:
                    damage_boss_text = f"{player_champion.name} takes a heavy hit — {player_boss.name} deals {int(real_boss_damage)} damage."
                else:
                    damage_boss_text = f"{player_boss.name} hits {player_champion.name}, dealing {int(real_boss_damage)} damage."

                if shield_bash_stagger:
                    print(f"{player_boss.name} stands back on its feet, ready for next attack.")
                    shield_bash_stagger = False
                    skip()
                else:            
                    if player_current_stamina >= 15 and evade_chance < player_champion.evade:
                        print(f"{player_champion.name} evades {player_boss.name}'s attack!")
                        skip()
                    else:
                        if counter_attack:
                            counter_damage_player = (real_champ_damage * 1.75)
                            counter_damage_boss = (real_boss_damage/3)
                            player_current_HP -= counter_damage_boss
                            boss_current_HP -= counter_damage_player
                            print(f"{player_champion.name} counters {player_boss.name} attack, slashing him for {int(counter_damage_player)} damage.\n{player_champion.name} is wounded only for {int(counter_damage_boss)} damage.")
                            skip()
                        else:
                            player_current_HP -= real_boss_damage
                            print(damage_boss_text)
                            skip()

                    if player_current_HP <= 0 and phase_2_active == True:
                        print(boss_phase2_win_text)
                        sleep(3)
                        skip()
                        main_menu()
                    elif player_current_HP <= 0:
                        print(boss_win_text)
                        sleep(3)
                        skip()
                        main_menu()
            
                    if difficulty_mode == "Normal":
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                    else: # Difficulty Hard
                        if boss_current_HP <= 0 and phase_2_active == True:
                            clear_screen()
                            print(boss_phase2_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                        elif phase_2_active == False and boss_current_HP <= 0:
                            boss_current_HP = player_boss.HP
                            phase_2_active = True
                            boss_phase_2_tansition()

            case "Pontiff Sulyvahn": # Pontiff Sulyvahn ----------------------------------------------------
                if phase_2_active:
                    pass
                
                if player_boss.damage_type in player_champion.damage_resistance:
                    damage_boss_text = f"{player_boss.name}'s attack lacks its usual strength, dealing only {int(real_boss_damage)} damage."
                elif player_boss.damage_type in player_champion.damage_weakness:
                    damage_boss_text = f"{player_champion.name} takes a heavy hit — {player_boss.name} deals {int(real_boss_damage)} damage."
                else:
                    damage_boss_text = f"{player_boss.name} hits {player_champion.name}, dealing {int(real_boss_damage)} damage."

                if shield_bash_stagger:
                    print(f"{player_boss.name} stands back on its feet, ready for next attack.")
                    shield_bash_stagger = False
                    skip()
                else:
                    if player_current_stamina >= 15 and evade_chance < player_champion.evade:
                        print(f"{player_champion.name} evades {player_boss.name}'s attack!")
                        skip()
                    else:
                        if counter_attack:
                            counter_damage_player = (real_champ_damage * 1.75)
                            counter_damage_boss = (real_boss_damage/3)
                            player_current_HP -= counter_damage_boss
                            boss_current_HP -= counter_damage_player
                            print(f"{player_champion.name} counters {player_boss.name} attack, slashing him for {int(counter_damage_player)} damage.\n{player_champion.name} is wounded only for {int(counter_damage_boss)} damage.")
                            skip()
                        else:
                            player_current_HP -= real_boss_damage
                            print(damage_boss_text)
                            skip()

                    if player_current_HP <= 0 and phase_2_active == True:
                        print(boss_phase2_win_text)
                        sleep(3)
                        skip()
                        main_menu()
                    elif player_current_HP <= 0:
                        print(boss_win_text)
                        sleep(3)
                        skip()
                        main_menu()
            
                    if difficulty_mode == "Normal":
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                    else: # Difficulty Hard
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_phase2_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                        elif phase_2_active == False and (boss_current_HP <= (player_boss.HP*0.5)):
                            phase_2_active = True
                            boss_phase_2_tansition()

            case "Yhorm the Giant": # Yhorm the Giant ----------------------------------------------------
                if phase_2_active:
                    pass
               
                if player_boss.damage_type in player_champion.damage_resistance:
                    damage_boss_text = f"{player_boss.name}'s attack lacks its usual strength, dealing only {int(real_boss_damage)} damage."
                elif player_boss.damage_type in player_champion.damage_weakness:
                    damage_boss_text = f"{player_champion.name} takes a heavy hit — {player_boss.name} deals {int(real_boss_damage)} damage."
                else:
                    damage_boss_text = f"{player_boss.name} hits {player_champion.name}, dealing {int(real_boss_damage)} damage."

                if shield_bash_stagger:
                    print(f"{player_boss.name} stands back on its feet, ready for next attack.")
                    shield_bash_stagger = False
                    skip()
                else:            
                    if player_current_stamina >= 15 and evade_chance < player_champion.evade:
                        print(f"{player_champion.name} evades {player_boss.name}'s attack!")
                        skip()
                    else:
                        if counter_attack:
                            counter_damage_player = (real_champ_damage * 1.75)
                            counter_damage_boss = (real_boss_damage/3)
                            player_current_HP -= counter_damage_boss
                            boss_current_HP -= counter_damage_player
                            print(f"{player_champion.name} counters {player_boss.name} attack, slashing him for {int(counter_damage_player)} damage.\n{player_champion.name} is wounded only for {int(counter_damage_boss)} damage.")
                            skip()
                        else:
                            player_current_HP -= real_boss_damage
                            print(damage_boss_text)
                            skip()

                    if player_current_HP <= 0 and phase_2_active == True:
                        print(boss_phase2_win_text)
                        sleep(3)
                        skip()
                        main_menu()
                    elif player_current_HP <= 0:
                        print(boss_win_text)
                        sleep(3)
                        skip()
                        main_menu()
            
                    if difficulty_mode == "Normal":
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                    else: # Difficulty Hard
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_phase2_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                        elif phase_2_active == False and (boss_current_HP <= (player_boss.HP*0.5)):
                            phase_2_active = True
                            boss_phase_2_tansition()

            case "Soul of Cinder": # Soul of Cinder ----------------------------------------------------
                if phase_2_active:
                    phase_2_stat_modified = True
            
                if player_boss.damage_type in player_champion.damage_resistance:
                    damage_boss_text = f"{player_boss.name}'s attack lacks its usual strength, dealing only {int(real_boss_damage)} damage."
                elif player_boss.damage_type in player_champion.damage_weakness:
                    damage_boss_text = f"{player_champion.name} takes a heavy hit — {player_boss.name} deals {int(real_boss_damage)} damage."
                else:
                    damage_boss_text = f"{player_boss.name} hits {player_champion.name}, dealing {int(real_boss_damage)} damage."

                if shield_bash_stagger:
                    print(f"{player_boss.name} stands back on its feet, ready for next attack.")
                    shield_bash_stagger = False
                    skip()
                else:            
                    if player_current_stamina >= 15 and evade_chance < player_champion.evade:
                        print(f"{player_champion.name} evades {player_boss.name}'s attack!")
                        skip()
                    else:
                        if counter_attack:
                            counter_damage_player = (real_champ_damage * 1.75)
                            counter_damage_boss = (real_boss_damage/3)
                            player_current_HP -= counter_damage_boss
                            boss_current_HP -= counter_damage_player
                            print(f"{player_champion.name} counters {player_boss.name} attack, slashing him for {int(counter_damage_player)} damage.\n{player_champion.name} is wounded only for {int(counter_damage_boss)} damage.")
                            skip()
                        else:
                            player_current_HP -= real_boss_damage
                            print(damage_boss_text)
                            skip()

                    if player_current_HP <= 0 and phase_2_active == True:
                        print(boss_phase2_win_text)
                        sleep(3)
                        skip()
                        main_menu()
                    elif player_current_HP <= 0:
                        print(boss_win_text)
                        sleep(3)
                        skip()
                        main_menu()
            
                    if difficulty_mode == "Normal":
                        if boss_current_HP <= 0:
                            clear_screen()
                            print(boss_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                    else: # Difficulty Hard
                        if boss_current_HP <= 0 and phase_2_active == True:
                            clear_screen()
                            print(boss_phase2_defeated_text)
                            sleep(3)
                            skip()
                            main_menu()
                        elif phase_2_active == False and boss_current_HP <= 0:
                            boss_current_HP = player_boss.HP
                            phase_2_active = True
                            boss_phase_2_tansition()
                    
        exalted_flesh_active = False
        shield_bash_stagger = False
        determination_active = False
        counter_attack = False
        player_current_stamina = player_champion.stamina
        special_move_cooldown += 1
        if special_move_cooldown == 3:
            special_move_ready = True
            special_move_cooldown = 0
        clear_screen()

# The game ----------------------------------------
update_trophy("Vordt of the Boreal Valley")
clear_screen()
while True:
    main_menu()