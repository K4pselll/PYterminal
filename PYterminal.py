import os
import sys
import random
print("PYterminal v1.0 PreRelease         Made by K4psell")
print("Type 'help' for a list of commands or type 'exit' to quit.")
user = username = os.getlogin()
print("Welcome back, " + user)
# The logic of commands
while True:
    command = input(f"{user}@PYterminal:~$ ")
    if command not in ["help", "exit", "echo", "clear", "version", "shutdown", "restart", "random", "RPG"] and not command.startswith("echo "):
        print(
            command + " is not recognized as a command. Type 'help' for a list of commands.")

    if command == "help":
        print("Avalible commands:")
        print("-------------TOOLS-------------------")
        print("help - Show this help message")
        print("exit - Exit the terminal")
        print("echo [text] - Print the specified text")
        print("clear - Clear the terminal screen")
        print("version - Display the terminal version")
        print("shudown - shutdown your system 'DISCLAIMER: NEEDS ADMIN PERMISSIONS'")
        print("restart - restart your system 'DISCLAIMER: NEEDS ADMIN PERMISSIONS'")
        print("---------------4FUN----------------")
        print("random - Generate a random number between your choice")
        print("RPG - opens a text based RPG minigame")
        print("Snake - opens a snake minigame")

    if command == "exit":
        print("Exiting...")
        break
    if command.startswith("echo "):
        text = command[5:]
        print(text)
    if command == "version":
        print("PYterminal version 1.0 PreRelease")
    if command == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')
    if command == "random":
        lower = int(input("Enter the lower bound> "))
        upper = int(input("Enter the upper bound> "))
        print("Random number:", random.randint(lower, upper))
    if command.startswith("shutdown"):
        os.system('shutdown /s /t 1' if os.name ==
                  'nt' else 'sudo shutdown now')
    if command == "restart":
        os.system('shutdown /r /t 1' if os.name == 'nt' else 'sudo reboot')
    if command == "RPG":
        print("RPG version 1.0 PreRelease")
        player_name = user
        player_health = 100
        player_attack = 15
        player_defense = 5
        enemy_name = "Goblin"
        enemy_health = 50
        enemy_attack = 10
        enemy_defense = 3
        print(f"A wild {enemy_name} appears!")
        while enemy_health > 0 and player_health > 0:

            print("avalible actions: attack, defend, run")
            action = input("choose your action>")
            if action == "attack":
                damage = player_attack - enemy_defense
                enemy_health = damage
                print(f"{player_name} attacks the {enemy_name} for {damage} damage!")
                enemy_health = player_attack - enemy_health + enemy_defense
                print(f"{enemy_name} has now {enemy_health} health left.")
                print(
                    f"{enemy_name} attacks back, and deals {enemy_attack} to {player_name}!")
                player_health = player_health - enemy_attack + player_defense
                print(f"{player_name} has now {player_health} health left.")

            elif action == "defend":
                print(f"{player_name} is defending!")
                reduced_damage = max(0, enemy_attack - (player_defense * 2))
                player_health -= reduced_damage
                print(
                    f"{enemy_name} attacks and deals {reduced_damage} damage to {player_name}!")
                print(f"{player_name} has now {player_health} health left.")
            elif action == "run":
                print(f"{player_name} flees from the battle!")
                break

