//
// Command: sendInvites	
//

const Spark = require('node-sparky');

const spark = new Spark({  retoken: process.env.SPARK_TOKEN });

module.exports = function (controller) {

		controller.hears(["(.*)"], 'direct_message,direct_mention', function (bot, message) {
				console.log(message);	
	            var text = JSON.parse(message.text);
	            if (text.game_id) {
		            var gameId = text.game_id;
		            spark.roomsGet({ type: 'direct' })
		            .then(rooms => {
		                rooms.forEach(room => 
		                	{if (true) {
		                		spark.personGet(room.creatorId).then(person => {
		                		
		                			if (room.creatorId != message.original_message.personId) {
		                			spark.messageSend({roomId: room.id,
		                							   text: `Someone is looking for a game! Click dbb99cf8.ngrok.io/join/${gameId}/${person.emails[0]}/${person.id}/${room.id}/ to join!`})
		                			}

		                		})
		                	}}
		                	)
		            })
		        }
		        else {
		        	if (text.user1.points < text.user2.points) {
		        		var winnerRoomId = message.original_message.roomId;
		        		var loserRoomId = text.user2.room;
		        		console.log(message.original_message.emails[0] + ", " + text.user2.email);
		        	} else {
		        		var winnerRoomId = text.user2.room;
		        		var loserRoomId = message.original_message.roomId;
		        	}

		        	var winnerText = `Well done! You won!`
		        	var loserText = `Sorry, you didn't win this time`

		        	spark.messageSend({roomId: winnerRoomId,
		        					   text: winnerText});
		        	spark.messageSend({roomId: loserRoomId,
		        					   text: loserText});

		        }
		    })
	}

		                		// spark.messageSend(
		                		// 	{roomId: room.id, 
		                		// 	 text: `Someone is looking for a game! Click dbb99cf8.ngrok.io/join/${gameId}/${spark.personGet(room.creatorId).emails[0]}/${spark.personGet(room.creatorId).id} to join!` })}}
		            
		        // if (text.score1) {
		        // 	var score1 = text.;
		        // 	var score2 = text.score2;
		        // 	var winner = 
		        // 	spark.message
		        // }
	      