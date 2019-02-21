import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import requests
import bs4
from samp_client.client import SampClient

Client = discord.Client()
BOT_PREFIX = ("og ")
client = Bot(command_prefix=BOT_PREFIX)
print("")
print(" [Arlecchino] > Botul a fost connectat")

haapy_emoji_1 = (str(random.choice([" :slight_smile: ", ":flushed: ", ":kissing_heart: ", ":relaxed: ", ":kissing: ",":yum: ",":smile: "])))
haapy_emoji_2 = (str(random.choice([" :slight_smile: ", ":flushed: ", ":kissing_heart: ", ":relaxed: ", ":kissing: ",":yum: ",":smile: "])))
haapy_emoji_3 = (str(random.choice([" :slight_smile: ", ":flushed: ", ":kissing_heart: ", ":relaxed: ", ":kissing: ",":yum: ",":smile: "])))
haapy_emoji_4 = (str(random.choice([" :slight_smile: ", ":flushed: ", ":kissing_heart: ", ":relaxed: ", ":kissing: ",":yum: ",":smile: "])))
haapy_emoji_5 = (str(random.choice([" :slight_smile: ", ":flushed: ", ":kissing_heart: ", ":relaxed: ", ":kissing: ",":yum: ",":smile: "])))
haapy_emoji_6 = (str(random.choice([" :slight_smile: ", ":flushed: ", ":kissing_heart: ", ":relaxed: ", ":kissing: ",":yum: ",":smile: "])))
sad_emoji_1 = (str(random.choice([" :confused: ", ":slight_frown: ", ":confounded: ", ":frowning: ", ":cry: ",":no_mouth: ",":scream: "])))
sad_emoji_2 = (str(random.choice([" :confused: ", ":slight_frown: ", ":confounded: ", ":frowning: ", ":cry: ",":no_mouth: ",":scream: "])))
sad_emoji_3 = (str(random.choice([" :confused: ", ":slight_frown: ", ":confounded: ", ":frowning: ", ":cry: ",":no_mouth: ",":scream: "])))
sad_emoji_4 = (str(random.choice([" :confused: ", ":slight_frown: ", ":confounded: ", ":frowning: ", ":cry: ",":no_mouth: ",":scream: "])))
sad_emoji_5 = (str(random.choice([" :confused: ", ":slight_frown: ", ":confounded: ", ":frowning: ", ":cry: ",":no_mouth: ",":scream: "])))
sad_emoji_6 = (str(random.choice([" :confused: ", ":slight_frown: ", ":confounded: ", ":frowning: ", ":cry: ",":no_mouth: ",":scream: "])))
work_emoji =  (str(random.choice([" :wrench: "," :hammer_pick: ",":tools: ",":pick: ",":key2: ",":microscope: "])))
# url

url = "https://earthpanel.og-times.ro/"
url_staff = "https://earthpanel.og-times.ro/staff"
url_bids = "https://earthpanel.og-times.ro/bids/"

# // Merge
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
async def cati_membrii_staff_online():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all(class_="label label-primary menu-caption")
        c = b[0].text
        await client.say(":hammer: Sunt " + (str(c)) + " membrii staff online")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

# // Merge
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cati_admini_online():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url_staff)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url_staff)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all(href="#admins")
        c = (str(b[0].text)).replace("Admins", "").replace("(", "").replace(")", "").strip()
        await client.say((str(work_emoji)) + "Sunt " + c + " administratori online")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cati_helperi_online():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url_staff)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url_staff)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all(href="#helpers")
        c = (str(b[0].text)).replace("Helpers", "").replace("(", "").replace(")", "")
        await client.say((str(work_emoji)) + "Sunt " + c + " helperi online")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cati_lideri_online():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url_staff)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url_staff)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all(href="#leaders")
        c = (str(b[0].text)).replace("Leaders", "").replace("(", "").replace(")", "")
        await client.say((str(work_emoji)) + "Sunt " + c + " lideri online")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cati_jucatori_online():
    await client.say(":shield: Comanda a fost executata\nSe asteapta un raspuns...")
    try:
        with SampClient(address="earth.og-times.ro", port=7777) as host:
            info = host.get_server_info()
            await client.say((str(work_emoji)) + "Pe server sunt " + (str(info.players)) + " jucatori online")
    except:
        await client.say("Posibil sa nu mearga serverul")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cati_jucatori_conectati_azi():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all("h2")
        c = (str(b[1].text))
        await client.say((str(work_emoji)) + "Momentan sunt " + c + " playeri conectati astazi  pe server")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cati_playeri_inregistrati():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all("h2")
        c = (str(b[2].text))
        await client.say((str(work_emoji)) + "Momentan sunt " + c + " playeri inregistrati pe server")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cate_case_licitate():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url_bids)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        c = requests.post(url_bids)
        soup = bs4.BeautifulSoup(c.text, "lxml")
        b = soup.find_all(class_="task-title-sp")
        d = "```"+(str(b[0].text) + "\n"+(str(b[1].text) +"\n"+(str(b[2].text) +"\n"+(str(b[3].text) +"\n"+(str(b[4].text) +"\n"+(str(b[5].text) +"\n"+(str(b[6].text) +
                                "\n"+(str(b[7].text) +"\n"+(str(b[8].text) +"\n"+(str(b[9].text) +"\n"+(str(b[10].text)))))))))))+"```")
        await client.say(d)
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cate_case_inregistrate():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all("h2")
        c = (str(b[4].text))
        await client.say((str(work_emoji)) + "Momentan sunt " + c + " case inregistrate pe server")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cate_businesses_uri_inregistrate():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all("h2")
        c = (str(b[5].text))
        await client.say((str(work_emoji)) + "Momentan sunt "+c + " businesses-uri inregistrate pe server")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")



@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cate_reclamatii_necitite():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        c = requests.post(url)
        soup = bs4.BeautifulSoup(c.text, "lxml")
        b = soup.find_all(class_="label label-primary menu-caption")
        d = (str(b[1].text))
        if d == "":
            await client.say((str(work_emoji)) + "Posibil sa nu existe reclamatii")
        else:
            await client.say((str(work_emoji)) + "Exista " + d + " reclamatii necitite")

    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cate_cereri_de_unban_necitite():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        c = requests.post(url)
        soup = bs4.BeautifulSoup(c.text, "lxml")
        b = soup.find_all(class_="label label-primary menu-caption")
        d = (str(b[2].text))
        if d == "":
            await client.say((str(work_emoji)) + "Posibil sa nu existe cereri")
        else:
            await client.say((str(work_emoji)) + "Exista "+ d + " cereri unban necitite")

    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cate_sume_licitate():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        c = requests.post(url)
        soup = bs4.BeautifulSoup(c.text, "lxml")
        b = soup.find_all(class_="label label-primary menu-caption")
        d = (str(b[3].text))
        if d == "":
            await client.say((str(work_emoji)) + "Posibil sa nu existe sume licitate")
        else:
            await client.say((str(work_emoji)) + "Exista "+ d + " sume licitate")

    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def cate_vehicule_inregistrate():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    if a.status_code == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all("h2")
        c = (str(b[3].text))
        await client.say((str(work_emoji)) + "Momentan sunt " + c + " vehicule inregistrate pe server")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def status_panel():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = requests.get(url)
    b = a.status_code
    if b == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def status_server():
    await client.say(":shield: Comanda a fost executata\nSe asteapta un raspuns...")
    with SampClient(address="earth.og-times.ro", port=7777) as host:
        info = host.get_server_info()
        await client.say(":heart: Hostname: > "+info.hostname+"\n"+":yellow_heart: Gamemode: > "+info.gamemode+"\n"+":green_heart: Language: > "+info.language+"\n"+":blue_heart: Parolat: > "+(str(info.password))+"\n"+":purple_heart: MAXPlayers: > "+(str(info.max_players))+"\n"+":heart: Players: > "+(str(info.players)))


@client.command(pass_context=True)
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)
async def verific_informatii_player(ctx,username):
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    d = requests.get(url)
    e = d.status_code
    if e == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url2 = "https://earthpanel.og-times.ro/profile/" + username
        await client.say(":dagger: Profil: " + url2)
        e1 = requests.get(url2)
        e2 = (str(e1.url))
        if "https://earthpanel.og-times.ro/404" in e2:
            await client.say((str(work_emoji)) + "Contul nu exista in OG-Times panel")
        else:
            await client.say((str(work_emoji)) + "Contul exista in OG-Times panel")
            try:
                url4 = "https://earthpanel.og-times.ro/profile/" + username
                nn = requests.post(url4)
                soup1 = bs4.BeautifulSoup(nn.text, "lxml")
                mm1 = soup1.find_all("td")
                mm2 = soup1.find_all("th")
                b0 = (str(mm2[0].text)).strip()
                b1 = (str(mm2[1].text)).strip()
                b2 = (str(mm2[2].text)).strip()
                b3 = (str(mm2[3].text)).strip()
                b4 = (str(mm2[4].text)).strip()
                b5 = (str(mm2[5].text)).strip()
                b6 = (str(mm2[6].text)).strip()
                b7 = (str(mm2[7].text)).strip()
                b8 = (str(mm2[8].text)).strip()
                b9 = (str(mm2[9].text)).strip()

                a0 = (str(mm1[0].text)).strip()
                a1 = (str(mm1[1].text)).strip()
                a2 = (str(mm1[2].text)).strip()
                a3 = (str(mm1[3].text)).strip()
                a4 = (str(mm1[4].text)).strip()
                a5 = (str(mm1[5].text)).strip()
                a6 = (str(mm1[6].text)).strip()
                a7 = (str(mm1[7].text)).strip()
                a8 = (str(mm1[8].text)).strip()
                a9 = (str(mm1[9].text)).strip()

                await client.say(
                     b0 + " " + a0 + "\n" + b1 + " " + a1 + "\n" + b2 + " " + a2 + "\n" + b3 + " " + a3 + "\n" + b4 + " " + a4 + "\n" + b5 + " " + a5 + "\n" + b6 + " " + a6 +
                    "\n" + b7 + " " + a7 + "\n" + b8 + " " + a8 + "\n" + b9 + " " + a9)
            except:
                await client.say(
                    b0 + " " + a0 + "\n" + b1 + " " + a1 + "\n" + b2 + " " + a2 + "\n" + b3 + " " + a3 + "\n" + b4 + " " + a4 + "\n" + b5 + " " + a5 + "\n" + b6 + " " + a6 +
                    "\n" + b7 + " " + a7 + "\n" + b8 + " " + a8)
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_topul_clanurilor():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        urlxx = "https://earthpanel.og-times.ro/clans"
        a = requests.post(urlxx)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")
        await client.say((str(haapy_emoji_1)) + (str((jucator[2].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_2)) + (str((jucator[3].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_3)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_4)) + (str((jucator[5].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_5)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_6)) + (str((jucator[7].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_5)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_3)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_2)) + (str((jucator[11].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_1)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_2)) + (str((jucator[13].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_3)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_4)) + (str((jucator[15].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_5)) + (str((jucator[16].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_1)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_2)) + (str((jucator[18].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_3)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_4)) + (str((jucator[20].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_5)) + (str((jucator[21].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_6)) + (str((jucator[22].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_5)) + (str((jucator[23].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_4)) + (str((jucator[24].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_3)) + (str((jucator[25].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_2)) + (str((jucator[26].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_1)) + (str((jucator[27].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_2)) + (str((jucator[28].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_3)) + (str((jucator[29].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_4)) + (str((jucator[30].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_5)) + (str((jucator[31].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_1)) + (str((jucator[32].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_2)) + (str((jucator[33].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_3)) + (str((jucator[34].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_4)) + (str((jucator[35].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_5)) + (str((jucator[36].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_6)) + (str((jucator[37].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_5)) + (str((jucator[38].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_4)) + (str((jucator[39].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n" +
                         (str(haapy_emoji_3)) + (str((jucator[40].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n")


    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_staff():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url_staff)
        soup = bs4.BeautifulSoup(a.text,"lxml")
        jucator = soup.find_all("tr")
        await client.say((str((jucator[2].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" + 
            (str(haapy_emoji_1)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" + 
            (str(haapy_emoji_2)) + (str((jucator[4].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" + 
            (str(haapy_emoji_3)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" + 
            (str(haapy_emoji_4)) + (str((jucator[6].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" + 
            (str(haapy_emoji_5)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" + 
            (str(haapy_emoji_6)) + (str((jucator[8].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" + 
            (str(haapy_emoji_5)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_4)) + (str((jucator[10].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_3)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_1)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_2)) + (str((jucator[14].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_3)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_6)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_5)) + (str((jucator[19].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_4)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_3)) + (str((jucator[21].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_2)) + (str((jucator[22].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_1)) + (str((jucator[23].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_2)) + (str((jucator[24].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n" +
            (str(haapy_emoji_3)) + (str((jucator[25].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "") + "\n")


    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_ultimele_war_uri():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        urlwar = "https://earthpanel.og-times.ro/wars"
        a = requests.post(urlwar)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        left = soup.find_all(class_="pull-left")
        right = soup.find_all(class_="pull-right")
        center = soup.find_all("center")  # numere impare
        inurmacu = soup.find_all(class_="cd-date")
        datade = soup.find_all(class_="cd-details")

        left1 = (str(left[0].text))
        right1 = (str(right[0].text))
        center1 = (str(center[1].text)).strip()
        inurmacu1 = (str(inurmacu[0].text))
        datade1 = (str(datade[0].text))

        left2 = (str(left[1].text))
        right2 = (str(right[1].text))
        center2 = (str(center[3].text)).strip()
        inurmacu2 = (str(inurmacu[1].text))
        datade2 = (str(datade[1].text))

        left3 = (str(left[2].text))
        right3 = (str(right[2].text))
        center3 = (str(center[5].text)).strip()
        inurmacu3 = (str(inurmacu[2].text))
        datade3 = (str(datade[2].text))

        await client.say((str("\n:traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: \n")) + (str(":gun:  ")) + str(left1) + (str("\n   :crossed_swords: ")) + (str("\n:gun:  ")) + (str(right1)) + (str("\n :medal: War castigat de ")) + (str(center1)) + (str("\n :date: In urma cu  ")) + (str(inurmacu1)) + (str("\n :date: Data/Ora ")) + (str(datade1)) +"\n"+ (str(":traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light:\n")) +
                         (str(":traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: \n")) + (str(":gun:  ")) + str(left2) + (str("\n   :crossed_swords: ")) + (str("\n:gun:  ")) + (str(right2)) + (str("\n :medal: War castigat de ")) + (str(center2)) + (str("\n :date: In urma cu  ")) + (str(inurmacu2)) + (str("\n :date: Data/Ora ")) + (str(datade2)) + "\n" + (str(":traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light:\n")) +
                         (str(":traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: \n")) + (str(":gun:  ")) + str(left3) + (str("\n   :crossed_swords: ")) + (str("\n:gun:  ")) + (str(right3)) + (str("\n :medal: War castigat de ")) + (str(center3)) + (str("\n :date: In urma cu  ")) + (str(inurmacu3)) + (str("\n :date: Data/Ora ")) + (str(datade3)) + "\n" + (str(":traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light: :traffic_light:\n")))


    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_updates():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")

        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        a = soup.find_all("strong")
        b = a[0].text
        await client.say(":blush: Ultimul update este " + b + "")

    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")




@client.command(pass_context=True)
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_online_offline_user(ctx,username):
    #await client.purge_from(ctx.message.channel, limit=1)
    #await client.send_message(ctx.message.author, "Please Wait 30 Seconds Before Using This Command Again.")
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        urlzz = "https://earthpanel.og-times.ro/profile/" + username
        a = requests.post(urlzz)
        b = a.url
        if b == (str("https://earthpanel.og-times.ro/404")):
            await client.say((str(work_emoji)) + "Contul nu exista")
        else:
            await client.say((str(work_emoji)) + "Contul exista\nSe asteapta un raspuns...")
            urlxyz = "https://earthpanel.og-times.ro/profile/" + username
            a = requests.post(urlxyz)
            soup = bs4.BeautifulSoup(a.text,"lxml")
            if (str('<i class="fa fa-circle txt-success"></i>')) in (str(soup)):
                await client.say("Contul " + username + " este online")
            else:
                await client.say("Contul " + username + " este offline")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command(pass_context=True)
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_ban(ctx,nume):
    #await client.purge_from(ctx.message.channel, limit=1)
    #await client.send_message(ctx.message.author, "Please Wait 30 Seconds Before Using This Command Again.")
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    vvv = "https://earthpanel.og-times.ro/"
    x3 = requests.get(vvv)
    x1 = x3.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url = "https://earthpanel.og-times.ro/profile/" + nume
        a = requests.post(url)
        b = a.url
        if b == (str("https://earthpanel.og-times.ro/404")):
            await client.say((str(work_emoji)) + "Contul nu exista")
        else:
            await client.say((str(work_emoji)) + "Contul exista\nSe asteapta un raspuns...")
            urlxyz = "https://earthpanel.og-times.ro/profile/" + nume
            a = requests.post(urlxyz)
            soup = bs4.BeautifulSoup(a.text, "lxml")
            sss = soup.find_all(class_="alert alert-danger")
            try:
                await client.say((str(":confused: "))+str((sss[0].text).split()).replace(",", "").replace("'", "").replace("[", "").replace("]", ""))
            except:
                await client.say((str(":smile: "))+"Acest cont nu are ban")

    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command(pass_context=True)
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_premium(ctx,premiu):
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        urlx = "https://earthpanel.og-times.ro/profile/" + premiu
        a = requests.post(urlx)
        b = a.url
        if b == (str("https://earthpanel.og-times.ro/404")):
            await client.say((str(work_emoji)) + "Contul nu exista")
        else:
            await client.say((str(work_emoji)) + "Contul exista\nSe asteapta un raspuns...")
            soup = bs4.BeautifulSoup(a.text, "lxml")
            if "premium user" in (str(soup)):
                await client.say(":kissing_smiling_eyes: Cont-ul are premium")
            else:
                await client.say(":thinking: Cont-ul nu are premium")


    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")


@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_ultimele_banuri():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url1 = "https://earthpanel.og-times.ro/bans"
        a = requests.post(url1)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("td")
        await client.say((str(sad_emoji_1)) + (str(jucator[0].text).strip()) + " " + (str(jucator[1].text).strip()) + " " + (str(jucator[2].text).strip()) + " " + (str(jucator[3].text).strip()) + " " + (str(jucator[4].text).strip()) + " " + (str(jucator[5].text).strip()) + "\n\n" +
                         (str(sad_emoji_2)) + (str(jucator[6].text).strip()) + " " + (str(jucator[7].text).strip()) + " " + (str(jucator[8].text).strip()) + " " + (str(jucator[9].text).strip()) + " " + (str(jucator[10].text).strip()) + " " + (str(jucator[11].text).strip()) + "\n\n" +
                         (str(sad_emoji_3)) + (str(jucator[12].text).strip()) + " " + (str(jucator[13].text).strip()) + " " + (str(jucator[14].text).strip()) + " " + (str(jucator[15].text).strip()) + " " + (str(jucator[16].text).strip()) + " " + (str(jucator[17].text).strip()) + "\n\n" +
                         (str(sad_emoji_4)) + (str(jucator[18].text).strip()) + " " + (str(jucator[19].text).strip()) + " " + (str(jucator[20].text).strip()) + " " + (str(jucator[21].text).strip()) + " " + (str(jucator[22].text).strip()) + " " + (str(jucator[23].text).strip()) + "\n\n" +
                         (str(sad_emoji_5)) + (str(jucator[24].text).strip()) + " " + (str(jucator[25].text).strip()) + " " + (str(jucator[26].text).strip()) + " " + (str(jucator[27].text).strip()) + " " + (str(jucator[28].text).strip()) + " " + (str(jucator[29].text).strip()) + "\n\n" +
                         (str(sad_emoji_6)) + (str(jucator[30].text).strip()) + " " + (str(jucator[31].text).strip()) + " " + (str(jucator[32].text).strip()) + " " + (str(jucator[33].text).strip()) + " " + (str(jucator[34].text).strip()) + " " + (str(jucator[35].text).strip()) + "\n\n" +
                         (str(sad_emoji_1)) + (str(jucator[36].text).strip()) + " " + (str(jucator[37].text).strip()) + " " + (str(jucator[38].text).strip()) + " " + (str(jucator[39].text).strip()) + " " + (str(jucator[40].text).strip()) + " " + (str(jucator[41].text).strip()) + "\n\n" +
                         (str(sad_emoji_3)) + (str(jucator[42].text).strip()) + " " + (str(jucator[43].text).strip()) + " " + (str(jucator[44].text).strip()) + " " + (str(jucator[45].text).strip()) + " " + (str(jucator[46].text).strip()) + " " + (str(jucator[47].text).strip()) + "\n\n" +
                         (str(sad_emoji_5)) + (str(jucator[48].text).strip()) + " " + (str(jucator[49].text).strip()) + " " + (str(jucator[50].text).strip()) + " " + (str(jucator[51].text).strip()) + " " + (str(jucator[52].text).strip()) + " " + (str(jucator[53].text).strip()) + "\n\n" +
                         (str(sad_emoji_2)) + (str(jucator[54].text).strip()) + " " + (str(jucator[55].text).strip()) + " " + (str(jucator[56].text).strip()) + " " + (str(jucator[57].text).strip()) + " " + (str(jucator[58].text).strip()) + " " + (str(jucator[59].text).strip()) + "\n\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command(pass_context=True)
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_daca_exista(ctx,username):
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    d = requests.get(url)
    e = d.status_code
    if e == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url2 = "https://earthpanel.og-times.ro/profile/" + username
        e1 = requests.get(url2)
        e2 = (str(e1.url))
        if "https://earthpanel.og-times.ro/404" in e2:
            await client.say((str(work_emoji)) + "Contul nu exista in OG-Times panel")
        else:
            url2 = "https://earthpanel.og-times.ro/profile/" + username
            await client.say((str(work_emoji)) + "Contul exista in OG-Times panel")
            await client.say(":dagger: Profil: " + url2)

    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)


async def verific_top_mafioti():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    d = requests.get(url)
    e = d.status_code
    if e == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_gng = "https://earthpanel.og-times.ro/topgangsters"
        a = requests.post(url_gng)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("td")
        await client.say((str(":dagger: Player-ul si numarul sau de kill-uri\n")) + (str(haapy_emoji_6)) + (str(":first_place: ")) + (str(jucator[2].text)).strip() + (str("   :crossed_swords: ")) + (str(jucator[3].text)).strip() + "\n" +
                         (str(haapy_emoji_1)) + (str(":second_place: ")) +  (str(jucator[6].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[7].text)).strip() + "\n" +
                         (str(haapy_emoji_2)) + (str(":third_place: ")) +   (str(jucator[10].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[11].text)).strip() +"\n" +
                         (str(haapy_emoji_3)) + (str(jucator[14].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[15].text)).strip() +"\n" +
                         (str(haapy_emoji_4)) + (str(jucator[18].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[19].text)).strip() +"\n" +
                         (str(haapy_emoji_5)) + (str(jucator[22].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[23].text)).strip() +"\n" +
                         (str(haapy_emoji_6)) + (str(jucator[26].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[27].text)).strip() +"\n" +
                         (str(haapy_emoji_2)) + (str(jucator[30].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[31].text)).strip() +"\n" +
                         (str(haapy_emoji_5)) + (str(jucator[34].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[35].text)).strip() +"\n" +
                         (str(haapy_emoji_1)) + (str(jucator[38].text)).strip() + (str("   :crossed_swords: ")) +  (str(jucator[39].text)).strip() +"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_top_jucatori():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    d = requests.get(url)
    e = d.status_code
    if e == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_topplayers = "https://earthpanel.og-times.ro/topplayers"
        a = requests.post(url_topplayers)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("td")
        await client.say((str(haapy_emoji_1)) + (str(jucator[2].text)).strip() + "\n" +
                         (str(haapy_emoji_2)) + (str(jucator[7].text)).strip() + "\n" +
                         (str(haapy_emoji_3)) + (str(jucator[12].text)).strip() + "\n" +
                         (str(haapy_emoji_4)) + (str(jucator[17].text)).strip() + "\n" +
                         (str(haapy_emoji_5)) + (str(jucator[22].text)).strip() + "\n" +
                         (str(haapy_emoji_6)) + (str(jucator[27].text)).strip() + "\n" +
                         (str(haapy_emoji_5)) + (str(jucator[32].text)).strip() + "\n" +
                         (str(haapy_emoji_4)) + (str(jucator[37].text)).strip() + "\n" +
                         (str(haapy_emoji_3)) + (str(jucator[42].text)).strip() + "\n" +
                         (str(haapy_emoji_2)) + (str(jucator[47].text)).strip() + "\n" +
                         (str(haapy_emoji_1)) + (str(jucator[52].text)).strip() + "\n" +
                         (str(haapy_emoji_2)) + (str(jucator[57].text)).strip() + "\n" +
                         (str(haapy_emoji_3)) + (str(jucator[62].text)).strip() + "\n" +
                         (str(haapy_emoji_4)) + (str(jucator[67].text)).strip() + "\n" +
                         (str(haapy_emoji_5)) + (str(jucator[72].text)).strip() + "\n" +
                         (str(haapy_emoji_6)) + (str(jucator[77].text)).strip() + "\n" +
                         (str(haapy_emoji_5)) + (str(jucator[82].text)).strip() + "\n" +
                         (str(haapy_emoji_4)) + (str(jucator[87].text)).strip() + "\n" +
                         (str(haapy_emoji_3)) + (str(jucator[92].text)).strip() + "\n" +
                         (str(haapy_emoji_2)) + (str(jucator[97].text)).strip() + "\n")
    else:
        await client.say("Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_jucatorii_saptamanii():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    d = requests.get(url)
    e = d.status_code
    if e == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all("div", class_="media-body")
        c = (str(b[0].text)).strip()
        c1 = (str(b[1].text)).strip()
        c2 = (str(b[2].text)).strip()

        await client.say((str(":heart: ")) + c + "\n " + (str(":heart:"))  + c1 + "\n "+ (str(":heart:")) + c2 + "\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def verific_ultimele_actiuni():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    d = requests.get(url)
    e = d.status_code
    if e == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        a = requests.post(url)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        b = soup.find_all("td")
        a1 = random.choice([":green_apple: ",":apple: ",":pear: ",":tangerine: ", ":lemon: ", ":watermelon: ",":grapes: ", ":pineapple: ", ":tomato: "])
        b1 = random.choice([":green_apple: ", ":apple: ", ":pear: ",":tangerine: ", ":lemon: ", ":watermelon: ",":grapes: ", ":pineapple: ", ":tomato: "])
        c1 = random.choice([":green_apple: ", ":apple: ", ":pear: ",":tangerine: ", ":lemon: ", ":watermelon: ",":grapes: ", ":pineapple: ", ":tomato: "])
        d1 = random.choice([":green_apple: ", ":apple: ", ":pear: ",":tangerine: ", ":lemon: ", ":watermelon: ",":grapes: ", ":pineapple: ", ":tomato: "])
        e1 = random.choice([":green_apple: ", ":apple: ", ":pear: ",":tangerine: ", ":lemon: ", ":watermelon: ",":grapes: ", ":pineapple: ", ":tomato: "])
        f1 = random.choice([":green_apple: ", ":apple: ", ":pear: ",":tangerine: ", ":lemon: ", ":watermelon: ",":grapes: ", ":pineapple: ", ":tomato: "])
        g1 = random.choice([":green_apple: ", ":apple: ", ":pear: ",":tangerine: ", ":lemon: ", ":watermelon: ",":grapes: ", ":pineapple: ", ":tomato: "])
        await client.say((str(a1)) + (str(b[0].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[1].text)) + "\n" +
                         (str(b1)) + (str(b[2].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[3].text)) + "\n" +
                         (str(c1)) + (str(b[4].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[5].text)) + "\n" +
                         (str(d1)) + (str(b[6].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[7].text)) + "\n" +
                         (str(e1)) + (str(b[8].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[9].text)) + "\n" +
                         (str(f1)) + (str(b[10].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[11].text)) + "\n" +
                         (str(g1)) + (str(b[12].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[13].text)) + "\n" +
                         (str(b1)) + (str(b[14].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[15].text)) + "\n" +
                         (str(d1)) + (str(b[16].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[17].text)) + "\n" +
                         (str(a1)) + (str(b[18].text)) + (str(":kissing_smiling_eyes: ")) + (str(b[19].text)))
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")

@client.command(pass_context=True)
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def fondator():
    await client.say(":shield: Comanda a fost executata\nSe asteapta un raspuns...")
    await client.say("https://i.ibb.co/QdKgHcG/image-5-1-1-1.png")
    await client.say("https://i.ibb.co/4MdHTmx/sa-mp-022.png")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def smash_or_pass():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = random.choice(["https://i.ibb.co/KLTq24Q/energie.png\n ```energiant```",
                       "https://i.ibb.co/bNtHJ5j/faker.png\n```faker```",
                       "https://i.ibb.co/H7bG7gS/florineliosif.png\n```DaGGoth```",
                       "https://i.ibb.co/2N9XJWV/georgiana.png\n```giorgiana```",
                       "https://i.ibb.co/W5xzrxw/massive.png\n```massive```",
                       "https://i.ibb.co/vZmvghL/radu.png\n```radu```",
                       "https://i.ibb.co/f4S1HDw/tobacco.png\n```tobacco```",
                       "https://i.ibb.co/DY205gB/ulpian.png\n```ulpian```",
                       "https://i.ibb.co/cv6WMmx/vld47.png\n```vladut47```",])
    await client.say(a)
    await client.say("Smash or Pass?")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def daucubanu():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = random.choice(["cap","pajura"])
    if a == "cap":
        await client.say(":regional_indicator_c:  Capul monedei este " + a)
    else:
        await client.say(":regional_indicator_p:  Capul monedei este " + a)

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def pacanele():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    a = random.choice([":green_apple:",":black_joker:",":lemon:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])
    b = random.choice([":lemon:",":peach:",":black_joker:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])
    c = random.choice([":green_apple:",":lemon:",":black_joker:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])

    d = random.choice([":green_apple:",":lemon:",":black_joker:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])
    e = random.choice([":green_apple:",":lemon:",":black_joker:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])
    f = random.choice([":green_apple:",":lemon:",":black_joker:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])

    g = random.choice([":green_apple:",":lemon:",":black_joker:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])
    h = random.choice([":green_apple:",":lemon:",":black_joker:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])
    i = random.choice([":green_apple:",":lemon:",":black_joker:",":peach:",":cherries:",":pineapple:",":tomato:",":eggplant:",":hot_pepper:",":corn:",":melon:",":strawberry:",":watermelon:",":pear:"])
    xyz = random.choice([2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 16, 18, 19, 20, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 35, 36, 38, 39, 40, 41, 42, 44, 46, 47, 48, 50, 51, 55, 56, 57, 58, 59, 60, 61, 62, 64, 65, 68, 70, 71, 72, 73, 75, 76, 77, 78, 79, 82, 83, 84, 85, 86, 88, 89, 90, 92, 93, 98, 99, 100])


    await client.say("▬▬▬▬▬▬▬▬\n▐"+" "+a+" "+" "+b+" "+" "+c+""+"▐\n▐"+" "+d+"  "+e+"  "+f+"▐"+"\n▐"+" "+g+"  "+h+"  "+i+"▐\n▬▬▬▬▬▬▬▬\n▐                          ▐\n▐                          ▐\n▐  SlotMachine ▐\n▐                          ▐\n▐          :moneybag:         ▐\n▬▬▬▬▬▬▬▬")
    await client.say("ViorelScuipVenin > "+(str(xyz))+" lei")
    if xyz == 100:
        await client.say((str(work_emoji)) + "Ai castigat o bunaciune")
        await client.say("https://i.ytimg.com/vi/GCv96fpnWkE/maxresdefault.jpg")
    if xyz == 50:
        await client.say((str(work_emoji)) + "Ai castigat o bunaciune")
        await client.say((str(work_emoji)) + "http://www.banktapet.pl/pictures/2014/1008/1/hot-beautiful-girl-on-bed-high-definition-wallpaper-52042.jpg")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def multumiri():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    await client.say("Multumiri tuturor celor care au ajutat la construirea si inbunatatirea BOT-ului\n"+"Respecte catre"+"\n :heart: Webber\n :heart: Ronload\n :heart: Sakal // phenomz0r.net\n :heart: Skyled\n :heart: Tukson")

@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_fbi():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_2 = "https://earthpanel.og-times.ro/group/complaints/2"
        a = requests.post(url_2)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_lspd():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_1 = "https://earthpanel.og-times.ro/group/complaints/1"
        a = requests.post(url_1)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_ng():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_3 = "https://earthpanel.og-times.ro/group/complaints/3"
        a = requests.post(url_3)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_paramedic():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_4 = "https://earthpanel.og-times.ro/group/complaints/4"
        a = requests.post(url_4)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_taxi_lv():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_5 = "https://earthpanel.og-times.ro/group/complaints/5"
        a = requests.post(url_5)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_russian_mafia():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_6 = "https://earthpanel.og-times.ro/group/complaints/6"
        a = requests.post(url_6)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_grove_street():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_7 = "https://earthpanel.og-times.ro/group/complaints/7"
        a = requests.post(url_7)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_los_aztecas():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_8 = "https://earthpanel.og-times.ro/group/complaints/8"
        a = requests.post(url_8)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_dragon_triad():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_9 = "https://earthpanel.og-times.ro/group/complaints/9"
        a = requests.post(url_9)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_ballas_familiy():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_10 = "https://earthpanel.og-times.ro/group/complaints/10"
        a = requests.post(url_10)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_los_vagos():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_11 = "https://earthpanel.og-times.ro/group/complaints/11"
        a = requests.post(url_11)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_hitman():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_12 = "https://earthpanel.og-times.ro/group/complaints/12"
        a = requests.post(url_12)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_school_instructors_lv():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_13 = "https://earthpanel.og-times.ro/group/complaints/13"
        a = requests.post(url_13)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_taxi_ls():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_14 = "https://earthpanel.og-times.ro/group/complaints/14"
        a = requests.post(url_14)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_news_reporters():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_15 = "https://earthpanel.og-times.ro/group/complaints/15"
        a = requests.post(url_15)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_lvpd():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_16 = "https://earthpanel.og-times.ro/group/complaints/16"
        a = requests.post(url_16)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_school_instructors_ls():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_17 = "https://earthpanel.og-times.ro/group/complaints/17"
        a = requests.post(url_17)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_sfpd():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_18 = "https://earthpanel.og-times.ro/group/complaints/18"
        a = requests.post(url_18)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_paramedic_sf():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_19 = "https://earthpanel.og-times.ro/group/complaints/19"
        a = requests.post(url_19)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)


async def reclamatii_taxi_sf():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_20 = "https://earthpanel.og-times.ro/group/complaints/20"
        a = requests.post(url_20)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_italian_mafia():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_21 = "https://earthpanel.og-times.ro/group/complaints/21"
        a = requests.post(url_21)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_avipsa():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_22 = "https://earthpanel.og-times.ro/group/complaints/22"
        a = requests.post(url_22)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_nang_boys():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_23 = "https://earthpanel.og-times.ro/group/complaints/23"
        a = requests.post(url_23)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_school_instructors_sf():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_24 = "https://earthpanel.og-times.ro/group/complaints/24"
        a = requests.post(url_24)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_tow_car():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_25 = "https://earthpanel.og-times.ro/group/complaints/25"
        a = requests.post(url_25)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")
@client.command()
@commands.cooldown(rate=1, per=5.0, type=commands.BucketType.channel)

async def reclamatii_council():
    await client.say(":shield: Comanda a fost executata\n:alarm_clock: Se asteapta un raspuns...")
    x = requests.get(url)
    x1 = x.status_code
    if x1 == 200:
        await client.say(":gear: Panel-ul OG-Times merge")
        url_26 = "https://earthpanel.og-times.ro/group/complaints/26"
        a = requests.post(url_26)
        soup = bs4.BeautifulSoup(a.text, "lxml")
        jucator = soup.find_all("tr")

        await client.say((str(haapy_emoji_1)) + (str((jucator[1].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[2].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[3].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[4].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[5].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_1)) + (str((jucator[6].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_2)) + (str((jucator[7].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_3)) + (str((jucator[8].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_4)) + (str((jucator[9].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[10].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[11].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[12].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[13].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_4)) + (str((jucator[14].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_5)) + (str((jucator[15].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n"+
                         (str(haapy_emoji_4)) + (str((jucator[16].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_5)) + (str((jucator[17].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_1)) + (str((jucator[18].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n" +
                         (str(haapy_emoji_2)) + (str((jucator[19].text).split())).replace("'", "").replace(",","").replace("[", "").replace("]", "") + "\n"+
                         (str(haapy_emoji_3)) + (str((jucator[20].text).split())).replace("'", "").replace(",", "").replace("[", "").replace("]", "")+"\n")
    else:
        await client.say(":head_bandage: Panel-ul OG-Times nu merge")






client.run(os.environ['BOT_TOKEN'])

