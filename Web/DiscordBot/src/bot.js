require("dotenv").config();

const Discord = require("discord.js");

const client = new Discord.Client({
  intents: [
    Discord.GatewayIntentBits.Guilds,
    Discord.GatewayIntentBits.GuildMessages,
  ],
});

client.on("ready", () => {
  console.log(`${client.user.tag} has logged in`);
});

client.login(process.env.DISCORDJS_BOT_TOKEN);
