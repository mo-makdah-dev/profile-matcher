// Runs automatically on first DB creation
const dbName = "game_db";
const db = db.getSiblingDB(dbName);

// Collections
db.createCollection("players");
db.createCollection("campaigns");

// Indexes
db.players.createIndex({ player_id: 1 }, { unique: true });
db.campaigns.createIndex({ name: 1 }, { unique: true });

db.players.insertOne({
  player_id: "97983be2-98b7-11e7-90cf-082e5f28d836",
  credential: "apple_credential",
  created: "2021-01-10 13:37:17Z",
  modified: "2021-01-23 13:37:17Z",
  last_session: "2021-01-23 13:37:17Z",
  total_spent: 400,
  total_refund: 0,
  total_transactions: 5,
  last_purchase: "2021-01-22 13:37:17Z",
  active_campaigns: [],
  devices: [
    { id: 1, model: "apple iphone 11", carrier: "vodafone", firmware: "123" },
  ],
  level: 3,
  xp: 1000,
  total_playtime: 144,
  country: "CA",
  language: "fr",
  birthdate: "2000-01-10 13:37:17Z",
  gender: "male",
  inventory: { cash: 123, coins: 123, item_1: 1, item_34: 3, item_55: 2 },
  clan: { id: "123456", name: "Hello world clan" },
  _customfield: "mycustom",
});

// Seed campaign
db.campaigns.insertOne({
  game: "mygame",
  name: "mycampaign",
  priority: 10.5,
  matchers: {
    level: { min: 1, max: 3 },
    has: { country: ["US", "RO", "CA"], items: ["item_1"] },
    does_not_have: { items: ["item_4"] },
  },
  start_date: "2022-01-25 00:00:00Z",
  end_date: "2022-02-25 00:00:00Z",
  enabled: true,
  last_updated: "2021-07-13 11:46:58Z",
});
