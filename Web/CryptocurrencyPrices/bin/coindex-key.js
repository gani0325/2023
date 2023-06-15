const program = require("commander");

program
  .command("set")
  .description("Manage API Key -- https://nomics.com")
  .action(key.set);

program.command("show").description("Show API Key").action(key.show);

program.command("remove").description("Remove API Key").action(key.remove);

program.parse(process.argv);
