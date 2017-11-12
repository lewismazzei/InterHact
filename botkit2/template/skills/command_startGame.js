//
// Command: startGame
//

module.exports = function (controller) {

    controller.hears(["start"], "direct_message,direct_mention", function (bot, message) {

        console.log(message)

        bot.startConversation(message, function (err, convo) {

            convo.ask("What game would you like to play?\n- [1] Noughts and Crosses\n- [2] Sudoku\n- [3] Snake", [
                {
                    pattern: "^1|2|3$",
                    callback: function (response, convo) {
                        convo.say(`Sure! Click this link to start: dbb99cf8.ngrok.io/new/${message.original_message.personId}/${message.original_message.personEmail}/ Inviting other players now!`);
                        convo.next();
                    },
                },
                {
                    default: true,
                    callback: function (response, convo) {
                        convo.say("Sorry that option is not valid. Enter either 1, 2 or 3 :)");
                        convo.repeat();
                        convo.next();
                    }
                }
            ]);
        });
    });
};
