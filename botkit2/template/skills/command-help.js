//
// Command: help
//
module.exports = function (controller) {

    controller.hears(["help", "who"], 'direct_message,direct_mention', function (bot, message) {
        var text = "Here are my skills:";
        text += "\n- " + bot.enrichCommand(message, ".commons") + ": shows metadata about myself";
        text += "\n- " + bot.enrichCommand(message, "start game") + ": starts a game";
        text += "\n- " + bot.enrichCommand(message, "help") + ": spreads the word about my skills";        
        bot.reply(message, text);
    });
}
