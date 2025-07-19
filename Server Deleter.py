import requests
import time

def delete_guilds_starting_with(token, guild_name_start):
    headers = {
        "Authorization": token,
        "Content-Type": "application/json"
    }
    resp = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=headers)
    if resp.status_code != 200:
        print(f"Failed to fetch guilds: {resp.status_code} {resp.text}")
        return
    guilds = resp.json()
    found = False
    for guild in guilds:
        if isinstance(guild, dict) and guild.get('name', '').startswith(guild_name_start):
            found = True
            guild_id = guild['id']
            guild_name = guild['name']
            del_resp = requests.delete(f"https://discord.com/api/v10/guilds/{guild_id}", headers=headers)
            if del_resp.status_code == 204:
                print(f"Deleted guild {guild_name} ({guild_id})")
            else:
                print(f"Failed to delete guild {guild_name} ({guild_id}): {del_resp.status_code} {del_resp.text}")
            time.sleep(5)
    if not found:
        print(f"No guilds found starting with '{guild_name_start}'.")
#you can get it with extensions on chrome like "get discord token"
TOKEN = "Token LOL"

SERVER_NAME_START = "first two words that start of the servers you want to delete"

delete_guilds_starting_with(TOKEN, SERVER_NAME_START)
