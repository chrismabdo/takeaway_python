describe("Game", function(){
    var game;

    beforeEach(function(){
        game = new Game();
    });

    it('should create a new game', function(){
        expect(game).toBeInstanceOf(Game);
    });

    it('will create a new scorecard', function() {
        expect(game.scorecard).toEqual([]);
    });

    it('will add 2 rolls and the total to the scorecard', function(){
        game.roll(3, 4, 7)
        expect(game.scorecard).toEqual([3, 4, 7])
    });

    it('will add totals of multiple rounds', function() {
        game.roll(3, 4)
        game.roll(9, 0)
        game.roll(6, 2)
        expect(game.scorecard).toEqual([3, 4, 7, 9, 0, 16, 6, 2, 24])
    });
});