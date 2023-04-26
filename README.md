## lost ark merchant api
## [修改] 
#### 发现一个新的API 可以监控任意大区任意时刻的流浪商人 
#### websocket API :wss://api.lf.group/subscriptions?new-merchants=server
#### payload1：{"type":"connection_init","payload":{}}

#### payload2：
<details><summary><font size="4" color="orange">Show Code</font></summary><pre><code>
{"id":"1","type":"start","payload":{"variables":{"filter":{"gameId":"LostArkEn","gameMode":"LostArkTravelingMerchants","from":"2023-03-30T00:00:00.000Z","lostArk":{"gifts":["Epic","Legendary"],"cards":["Kaysarr","Madnick","Mokamoka","Seria","Sian","Wei"]}},"options":{}},"extensions":{},"operationName":"EventCreate","query":"subscription EventCreate($filter: SearchEventsFilter!, $options: SubscriptionOptions) {\n  eventCreate(filter: $filter, options: $options) {\n    ...EventFull\n    __typename\n  }\n}\n\nfragment EventFull on Event {\n  ...EventInfo\n  chatId\n  owner {\n    ...UserBasic\n    __typename\n  }\n  ...EventSlots\n  __typename\n}\n\nfragment EventInfo on Event {\n  id\n  type\n  region\n  mode\n  inviteCode\n  name\n  pinned\n  hasWaitlist\n  owner {\n    id\n    username\n    avatarUrl\n    isFollowing\n    roles\n    __typename\n  }\n  organization {\n    id\n    name\n    alias\n    avatarUrl\n    __typename\n  }\n  backgroundUrl\n  description\n  externalUrl\n  createdAt\n  scheduledAt\n  scheduledTo\n  gameId\n  views\n  slotsCount\n  waitlistCount\n  status\n  deleted\n  takenSlotsCount\n  likesCount\n  reportsCount\n  slotsCountByRole {\n    role\n    count\n    taken\n    __typename\n  }\n  slotsCountByType {\n    type\n    count\n    taken\n    __typename\n  }\n  userSlot {\n    ...SlotNano\n    __typename\n  }\n  rating\n  language\n  platform\n  links {\n    websiteUrl\n    websiteTitle\n    __typename\n  }\n  wow {\n    ...EventWowFull\n    __typename\n  }\n  wowBurningCrusade {\n    ...EventWowTbcFull\n    __typename\n  }\n  lostArk {\n    ...EventLostArkFull\n    __typename\n  }\n  hearthstone {\n    ...EventHearthstoneFull\n    __typename\n  }\n  dota2 {\n    ...EventDota2Full\n    __typename\n  }\n  csgo {\n    ...EventCSGOFull\n    __typename\n  }\n  warzone {\n    ...EventWarzoneFull\n    __typename\n  }\n  lol {\n    ...EventLolFull\n    __typename\n  }\n  pubg {\n    ...EventPubgFull\n    __typename\n  }\n  cod {\n    ...EventCodFull\n    __typename\n  }\n  standoff2 {\n    ...EventStandoff2Full\n    __typename\n  }\n  ggd {\n    ...EventGgdFull\n    __typename\n  }\n  discord {\n    inviteUrl\n    channelUrl\n    messageUrl\n    __typename\n  }\n  __typename\n}\n\nfragment SlotNano on Slot {\n  id\n  type\n  role\n  team\n  user {\n    ...UserBasic\n    __typename\n  }\n  game {\n    ...GameFull\n    __typename\n  }\n  rating\n  ratingDiff\n  __typename\n}\n\nfragment UserBasic on User {\n  id\n  username\n  description\n  language\n  avatarUrl\n  createdAt\n  views\n  rating\n  likesCount\n  reportsCount\n  age\n  gender\n  online\n  lastActiveAt\n  invitesCount\n  referralCode\n  discord {\n    userId\n    username\n    __typename\n  }\n  twitch {\n    login\n    username\n    __typename\n  }\n  twitter {\n    userId\n    username\n    __typename\n  }\n  battlenet {\n    battletag\n    region\n    __typename\n  }\n  steam {\n    userId\n    username\n    avatarUrl\n    __typename\n  }\n  riot {\n    id\n    gameName\n    tagName\n    createdAt\n    updatedAt\n    __typename\n  }\n  youtube {\n    channelId\n    __typename\n  }\n  __typename\n}\n\nfragment GameFull on Game {\n  ... on Wow {\n    ...WowFull\n    __typename\n  }\n  ... on Hearthstone {\n    ...HearthstoneFull\n    __typename\n  }\n  ... on Dota2 {\n    ...Dota2Full\n    __typename\n  }\n  ... on CSGO {\n    ...CSGOFull\n    __typename\n  }\n  ... on Warzone {\n    ...WarzoneFull\n    __typename\n  }\n  ... on WowBurningCrusade {\n    ...WowBurningCrusadeFull\n    __typename\n  }\n  ... on LostArk {\n    ...LostArkFull\n    __typename\n  }\n  ... on GameLol {\n    ...GameLolFull\n    __typename\n  }\n  ... on GameAny {\n    ...GameAnyFull\n    __typename\n  }\n  __typename\n}\n\nfragment WowFull on Wow {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  description\n  ilvl\n  ilvlPvp\n  level\n  wowRace\n  wowClass\n  realm\n  wowRole\n  wowFaction\n  updatedAt\n  rioScore\n  rioScorePrevious\n  thumbnailUrl\n  wowRegion\n  wowSpecialization\n  covenant\n  guild\n  raidSepulcherSummary\n  raidSepulcherNormalKilled\n  raidSepulcherHeroicKilled\n  raidSepulcherMythicKilled\n  arenaRating2x2\n  arenaRating2x2Max\n  arenaRating3x3\n  arenaRating3x3Max\n  arenaRatingBattlegrounds\n  arenaRatingBattlegroundsMax\n  __typename\n}\n\nfragment HearthstoneFull on Hearthstone {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  description\n  rating\n  hsRegion\n  __typename\n}\n\nfragment Dota2Full on Dota2 {\n  id\n  gameId\n  deleted\n  hidden\n  description\n  mmrScore\n  dota2Role\n  dota2Region\n  __typename\n}\n\nfragment CSGOFull on CSGO {\n  id\n  gameId\n  deleted\n  hidden\n  description\n  csgoRegion\n  csgoRole\n  csgoRank\n  __typename\n}\n\nfragment WarzoneFull on Warzone {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  warzoneRegion\n  description\n  __typename\n}\n\nfragment WowBurningCrusadeFull on WowBurningCrusade {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  description\n  wowFaction\n  updatedAt\n  wowRace\n  wowClass\n  wowRole\n  wowRegion\n  level\n  ilvl\n  realm\n  arenaScore\n  wowRegion\n  __typename\n}\n\nfragment LostArkFull on LostArk {\n  id\n  gameId\n  deleted\n  hidden\n  alias\n  region\n  class\n  server\n  gearScore\n  legacyLvl\n  builds {\n    url\n    name\n    id\n    __typename\n  }\n  __typename\n}\n\nfragment GameLolFull on GameLol {\n  id\n  gameId\n  deleted\n  hidden\n  preferredLine\n  preferredLine2\n  kills\n  deaths\n  assists\n  soloRank\n  flexRank\n  creepScore\n  normalWinCount\n  normalLoseCount\n  soloWinCount\n  soloLoseCount\n  flexWinCount\n  flexLoseCount\n  visionScore\n  champions {\n    id\n    name\n    icon\n    image\n    KDA\n    csm\n    __typename\n  }\n  __typename\n}\n\nfragment GameAnyFull on GameAny {\n  id\n  gameId\n  deleted\n  hidden\n  __typename\n}\n\nfragment EventWowFull on EventWow {\n  dungeon\n  faction\n  mythicPlusRating\n  region\n  ilvl\n  arenaRating\n  mythicPlusKey\n  raid\n  raidDifficulty\n  __typename\n}\n\nfragment EventWowTbcFull on EventWowBurningCrusade {\n  dungeon\n  faction\n  region\n  ilvl\n  arenaRating\n  heroic\n  __typename\n}\n\nfragment EventLostArkFull on EventLostArk {\n  abyssDungeonsDungeonGearScore\n  cubeDungeonGearScore\n  difficultyGearScore\n  region\n  guardianRaidsGuardian\n  abyssDungeonsAbyss\n  abyssDungeonsDungeon\n  cubeDungeon\n  bossRush\n  platinumFieldsField\n  otherActivity\n  difficulty\n  arena\n  arenaServer\n  arenaMode\n  raid\n  phase\n  continent\n  card\n  zone\n  gift\n  server\n  __typename\n}\n\nfragment EventHearthstoneFull on EventHearthstone {\n  region\n  rating\n  __typename\n}\n\nfragment EventDota2Full on EventDota2 {\n  region\n  mmrScore\n  __typename\n}\n\nfragment EventCSGOFull on EventCSGO {\n  region\n  rank\n  __typename\n}\n\nfragment EventWarzoneFull on EventWarzone {\n  region\n  __typename\n}\n\nfragment EventLolFull on EventLol {\n  region\n  rank\n  lobbyPassword\n  __typename\n}\n\nfragment EventPubgFull on EventPubg {\n  server\n  password\n  __typename\n}\n\nfragment EventCodFull on EventCod {\n  server\n  password\n  __typename\n}\n\nfragment EventStandoff2Full on EventStandoff2 {\n  inviteLink\n  __typename\n}\n\nfragment EventGgdFull on EventGgd {\n  code\n  __typename\n}\n\nfragment EventSlots on Event {\n  slots {\n    ...SlotInfo\n    __typename\n  }\n  waitlist {\n    ...SlotInfo\n    __typename\n  }\n  __typename\n}\n\nfragment SlotInfo on Slot {\n  id\n  type\n  role\n  team\n  user {\n    ...UserBasic\n    lfg {\n      ...LfgFull\n      __typename\n    }\n    __typename\n  }\n  game {\n    __typename\n    ...GameFull\n  }\n  rating\n  ratingDiff\n  __typename\n}\n\nfragment LfgFull on Lfg {\n  id\n  ...BasicLfg\n  ...LfgGames\n  __typename\n}\n\nfragment BasicLfg on Lfg {\n  gameId\n  type\n  modes\n  alias\n  region\n  description\n  tags\n  rank\n  lostArk {\n    card\n    continent\n    server\n    region\n    gift\n    zone\n    legacyLvl\n    __typename\n  }\n  wow {\n    region\n    __typename\n  }\n  lol {\n    region\n    __typename\n  }\n  pubgMobile {\n    kdRatioDuo\n    kdRatioSquad\n    rank\n    uuid\n    __typename\n  }\n  codMobile {\n    rank\n    uuid\n    __typename\n  }\n  standoff2 {\n    profileId\n    __typename\n  }\n  csgo {\n    faceitLvl\n    __typename\n  }\n  __typename\n}\n\nfragment LfgGames on Lfg {\n  games {\n    ...GameFull\n    __typename\n  }\n  __typename\n}"}}
</code></pre></details>


#### API 来源: [lf.group/lost-ark/merchants](https://lf.group/lost-ark/merchants?gift=Epic%2CLegendary&card=Wei%2CMokamoka%2CMadnick%2CSeria%2CKaysarr%2CSian&region=Unset)





<!--
# lost-ark
### ![visitors](https://visitor-badge.glitch.me/badge?page_id=intAV.lost-ark) 
 失落的方舟流浪商人QQ通知(免费版) 
### 使用到的API:discord.py + go_cqhttp(QQ通知) + replit.com(平台免费运行) 

### 1.https://discordpy.readthedocs.io/en/stable/ 
#### 创建一个discord机器人然后创建讨论群，添加机器人:LFG，设置好游戏区服，有流浪商人公投的时候就会在讨论群直接通知
### 2.https://docs.go-cqhttp.org/guide/#go-cqhttp 
#### 申请一个新QQ，在replit挂两天，如果被风控了就绑定身份证解锁
### 3.https://www.freecodecamp.org/chinese/news/create-a-discord-bot-with-python/
#### replit + uptimerobot.com 免费运行
-->
### ![QQ截图20221215131917](https://user-images.githubusercontent.com/38396198/207778940-d7b3e1c5-9461-4778-ab48-2928b716153c.png)

