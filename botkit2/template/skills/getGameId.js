const Spark = require('node-sparky');

const spark = new Spark({ token: process.env.SPARK_TOKEN });

module.exports = function (controller) {
    
        controller.on('direct_message', function (bot, message) {
            console.log(message);
            var gameData = JSON.parse(message.text);
            var gameId = gameData.game_id;
        })}