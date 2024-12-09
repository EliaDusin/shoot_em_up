input.onButtonEvent(Button.A, input.buttonEventClick(), function () {
    basic.pause(100)
    Player.change(LedSpriteProperty.X, -1)
})
input.onButtonEvent(Button.AB, input.buttonEventClick(), function () {
    Shoot = game.createSprite(Player.get(LedSpriteProperty.X), 3)
    for (let index = 0; index < 4; index++) {
        basic.pause(100)
        Shoot.change(LedSpriteProperty.Y, -1)
    }
})
input.onButtonEvent(Button.B, input.buttonEventClick(), function () {
    Player.change(LedSpriteProperty.X, 1)
    basic.pause(100)
})
let Shoot: game.LedSprite = null
let Player: game.LedSprite = null
Player = game.createSprite(2, 4)
let Enemy = game.createSprite(2, 0)
loops.everyInterval(2000, function () {
    if (Enemy.get(LedSpriteProperty.X) == "4") {
        Enemy.change(LedSpriteProperty.X, -1)
    } else {
        if (Enemy.get(LedSpriteProperty.X) == 0) {
            Enemy.change(LedSpriteProperty.X, 1)
        } else {
            if (Math.randomBoolean()) {
                Enemy.change(LedSpriteProperty.X, 1)
            } else {
                Enemy.change(LedSpriteProperty.X, -1)
            }
        }
    }
})
basic.forever(function () {
	
})
