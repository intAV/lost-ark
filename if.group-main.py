import asyncio
import websockets
import time
import json

API_URL = "wss://api.lf.group/subscriptions?new-merchants=server"
PAYLOAD1 = '{"type":"connection_init","payload":{}}'
#PAYLOAD2 = '''{"id":"1","type":"start","payload":{"variables":{"filter":{"gameId":"LostArkEn","gameMode":"LostArkTravelingMerchants","from":"2023-04-28T00:00:00.000Z","lostArk":{"gifts":["Epic","Legendary"],"cards":["Kaysarr","Madnick","Mokamoka","Seria","Sian","Wei"]}},"options":{}},"extensions":{},"operationName":"EventCreate","query":"subscription EventCreate($filter: SearchEventsFilter!, $options: SubscriptionOptions) {\n  eventCreate(filter: $filter, options: $options) {\n    ...EventFull\n    __typename\n  }\n}\n\nfragment EventFull on Event {\n  ...EventInfo\n  chatId\n  owner {\n    ...UserMicro\n    __typename\n  }\n  ...EventSlots\n  __typename\n}\n\nfragment EventInfo on Event {\n  id\n  type\n  region\n  mode\n  inviteCode\n  name\n  pinned\n  hasWaitlist\n  owner {\n    id\n    username\n    avatarUrl\n    roles\n    __typename\n  }\n  backgroundUrl\n  description\n  externalUrl\n  createdAt\n  scheduledAt\n  scheduledTo\n  gameId\n  views\n  slotsCount\n  waitlistCount\n  status\n  deleted\n  takenSlotsCount\n  likesCount\n  reportsCount\n  slotsCountByRole {\n    role\n    count\n    taken\n    __typename\n  }\n  slotsCountByType {\n    type\n    count\n    taken\n    __typename\n  }\n  userSlot {\n    ...SlotNano\n    __typename\n  }\n  rating\n  language\n  platform\n  links {\n    websiteUrl\n    websiteTitle\n    __typename\n  }\n  wow {\n    ...EventWowFull\n    __typename\n  }\n  wowBurningCrusade {\n    ...EventWowTbcFull\n    __typename\n  }\n  lostArk {\n    ...EventLostArkFull\n    __typename\n  }\n  hearthstone {\n    ...EventHearthstoneFull\n    __typename\n  }\n  csgo {\n    ...EventCSGOFull\n    __typename\n  }\n  warzone {\n    ...EventWarzoneFull\n    __typename\n  }\n  lol {\n    ...EventLolFull\n    __typename\n  }\n  pubg {\n    ...EventPubgFull\n    __typename\n  }\n  cod {\n    ...EventCodFull\n    __typename\n  }\n  standoff2 {\n    ...EventStandoff2Full\n    __typename\n  }\n  ggd {\n    ...EventGgdFull\n    __typename\n  }\n  discord {\n    inviteUrl\n    channelUrl\n    messageUrl\n    __typename\n  }\n  __typename\n}\n\nfragment SlotNano on Slot {\n  id\n  type\n  role\n  team\n  user {\n    ...UserMicro\n    __typename\n  }\n  game {\n    ...GameFull\n    __typename\n  }\n  rating\n  ratingDiff\n  __typename\n}\n\nfragment UserMicro on User {\n  id\n  username\n  online\n  lastActiveAt\n  avatarUrl\n  rating\n  __typename\n}\n\nfragment GameFull on Game {\n  ... on Wow {\n    ...WowFull\n    __typename\n  }\n  ... on Hearthstone {\n    ...HearthstoneFull\n    __typename\n  }\n  ... on CSGO {\n    ...CSGOFull\n    __typename\n  }\n  ... on Warzone {\n    ...WarzoneFull\n    __typename\n  }\n  ... on WowBurningCrusade {\n    ...WowBurningCrusadeFull\n    __typename\n  }\n  ... on LostArk {\n    ...LostArkFull\n    __typename\n  }\n  ... on GameLol {\n    ...GameLolFull\n    __typename\n  }\n  ... on GameAny {\n    ...GameAnyFull\n    __typename\n  }\n  __typename\n}\n\nfragment WowFull on Wow {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  description\n  ilvl\n  ilvlPvp\n  level\n  wowRace\n  wowClass\n  realm\n  wowRole\n  wowFaction\n  updatedAt\n  rioScore\n  rioScorePrevious\n  thumbnailUrl\n  wowRegion\n  wowSpecialization\n  covenant\n  guild\n  raidSepulcherSummary\n  raidSepulcherNormalKilled\n  raidSepulcherHeroicKilled\n  raidSepulcherMythicKilled\n  arenaRating2x2\n  arenaRating2x2Max\n  arenaRating3x3\n  arenaRating3x3Max\n  arenaRatingBattlegrounds\n  arenaRatingBattlegroundsMax\n  __typename\n}\n\nfragment HearthstoneFull on Hearthstone {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  description\n  rating\n  hsRegion\n  __typename\n}\n\nfragment CSGOFull on CSGO {\n  id\n  gameId\n  deleted\n  hidden\n  description\n  csgoRegion\n  csgoRole\n  csgoRank\n  __typename\n}\n\nfragment WarzoneFull on Warzone {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  warzoneRegion\n  description\n  __typename\n}\n\nfragment WowBurningCrusadeFull on WowBurningCrusade {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  description\n  wowFaction\n  updatedAt\n  wowRace\n  wowClass\n  wowRole\n  wowRegion\n  level\n  ilvl\n  realm\n  arenaScore\n  wowRegion\n  __typename\n}\n\nfragment LostArkFull on LostArk {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  region\n  class\n  server\n  gearScore\n  legacyLvl\n  builds {\n    url\n    name\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment GameLolFull on GameLol {\n  id\n  gameId\n  deleted\n  hidden\n  preferredLine\n  preferredLine2\n  kills\n  deaths\n  assists\n  soloRank\n  flexRank\n  creepScore\n  normalWinCount\n  normalLoseCount\n  soloWinCount\n  soloLoseCount\n  flexWinCount\n  flexLoseCount\n  visionScore\n  champions {\n    id\n    name\n    icon\n    image\n    KDA\n    csm\n    __typename\n  }\n  __typename\n}\n\nfragment GameAnyFull on GameAny {\n  id\n  gameId\n  deleted\n  hidden\n  __typename\n}\n\nfragment EventWowFull on EventWow {\n  dungeon\n  faction\n  mythicPlusRating\n  region\n  ilvl\n  arenaRating\n  mythicPlusKey\n  raid\n  raidDifficulty\n  __typename\n}\n\nfragment EventWowTbcFull on EventWowBurningCrusade {\n  dungeon\n  faction\n  region\n  ilvl\n  arenaRating\n  heroic\n  __typename\n}\n\nfragment EventLostArkFull on EventLostArk {\n  abyssDungeonsDungeonGearScore\n  cubeDungeonGearScore\n  difficultyGearScore\n  region\n  guardianRaidsGuardian\n  abyssDungeonsAbyss\n  abyssDungeonsDungeon\n  cubeDungeon\n  bossRush\n  platinumFieldsField\n  otherActivity\n  difficulty\n  arena\n  arenaServer\n  arenaMode\n  raid\n  phase\n  continent\n  card\n  zone\n  gift\n  server\n  __typename\n}\n\nfragment EventHearthstoneFull on EventHearthstone {\n  region\n  rating\n  __typename\n}\n\nfragment EventCSGOFull on EventCSGO {\n  region\n  rank\n  __typename\n}\n\nfragment EventWarzoneFull on EventWarzone {\n  region\n  __typename\n}\n\nfragment EventLolFull on EventLol {\n  region\n  rank\n  lobbyPassword\n  __typename\n}\n\nfragment EventPubgFull on EventPubg {\n  server\n  password\n  __typename\n}\n\nfragment EventCodFull on EventCod {\n  server\n  password\n  __typename\n}\n\nfragment EventStandoff2Full on EventStandoff2 {\n  inviteLink\n  __typename\n}\n\nfragment EventGgdFull on EventGgd {\n  code\n  __typename\n}\n\nfragment EventSlots on Event {\n  slots {\n    ...SlotInfo\n    __typename\n  }\n  waitlist {\n    ...SlotInfo\n    __typename\n  }\n  __typename\n}\n\nfragment SlotInfo on Slot {\n  id\n  type\n  role\n  team\n  user {\n    ...UserMicro\n    lfg {\n      ...LfgFull\n      __typename\n    }\n    __typename\n  }\n  game {\n    __typename\n    ...GameFull\n  }\n  rating\n  ratingDiff\n  __typename\n}\n\nfragment LfgFull on Lfg {\n  id\n  ...BasicLfg\n  ...LfgGames\n  __typename\n}\n\nfragment BasicLfg on Lfg {\n  gameId\n  type\n  modes\n  alias\n  region\n  description\n  tags\n  rank\n  lostArk {\n    card\n    continent\n    server\n    region\n    gift\n    zone\n    legacyLvl\n    __typename\n  }\n  wow {\n    region\n    __typename\n  }\n  lol {\n    region\n    __typename\n  }\n  pubgMobile {\n    kdRatioDuo\n    kdRatioSquad\n    rank\n    uuid\n    __typename\n  }\n  codMobile {\n    rank\n    uuid\n    __typename\n  }\n  standoff2 {\n    profileId\n    __typename\n  }\n  csgo {\n    faceitLvl\n    __typename\n  }\n  __typename\n}\n\nfragment LfgGames on Lfg {\n  games {\n    ...GameFull\n    __typename\n  }\n  __typename\n}"}}'''

#解析消息
def parse(message):
	tt = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() + 28803))
	if "eventCreate" in message:
		msg = json.loads(message.replace('false', '"false"') \
         .replace('null', '"null"'))
		json_data = msg.get('payload').get('data').get('eventCreate').get('lostArk')
		#区域
		region = json_data.get('region')
		#服务器
		server = json_data.get('server')
		#地图大陆
		continent = json_data.get('continent')
		#地图区
		zone = json_data.get('zone')
		#卡片
		card = json_data.get('card')
		#礼物
		gift = json_data.get('gift')

		msg = 'server:[{}/{}]  map:[{}/{}]  card:[{}]  gift:[{}]' \
     .format(region, server, continent, zone, card, gift)
		print('[{}]  msg:{}'.format(tt, msg))
	else:
		print(tt, message)


async def main():
	conn_handler = await websockets.connect(API_URL)
	with open("p.txt","r") as f:
		PAYLOAD2 = f.readlines()
	await conn_handler.send(PAYLOAD1)
	await conn_handler.send(PAYLOAD2)
	while True:
		message = await conn_handler.recv()
		parse(message)

asyncio.get_event_loop().run_until_complete(main())