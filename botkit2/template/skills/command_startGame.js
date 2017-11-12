//
// Command: startGame
//

const Spark = require('node-sparky');

const spark = new Spark({ token: process.env.SPARK_TOKEN });

module.exports = function (controller) {

    controller.hears(["start game"], "direct_message,direct_mention", function (bot, message) {

        bot.startConversation(message, function (err, convo) {

            convo.ask("What game would you like to play?\n- [1] Noughts and Crosses\n- [2] Sudoku\n- [3] Snake", [
                {
                    pattern: "^1|2|3$",
                    callback: function (response, convo) {
                        convo.say(`Sure! Click this link to start: dbb99cf8.ngrok.io/new/token/email/ Inviting other players now!`);
                        controller.on('direct_message', function (bot, message) {
                            console.log(message);
                            var gameData = JSON.parse(message.text);
                            var gameId = gameData.game_id;
                            spark.roomsGet({ type: 'direct' })
                            .then(rooms => rooms.forEach(room => spark.messageSend(
                                {roomId: room.id, text: `Someone is looking for a game! Click here.com to join! gameID: ${gameId}` })));
                        })
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
