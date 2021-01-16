'use strict';

class Game {

    constructor() {
        this.scorecard = [];
    }

    roll(first, second) {
        this.first = first;
        this.second = second;
        this.scorecard.push(first);
        this.scorecard.push(second);

        this.addTotal();
    }

    addTotal() {
        if (this.scorecard.length < 4) {
            this.scorecard.push(this.first + this.second);
        // } else if (this.scorecard[-5] + this.scorecard[-4] == 10 && this.scorecard[-5] != 10) {
        //     addSpareBonus
        // } else if (this.scorecard[-5] == 10) {
        //     addStrikeBonus
        // } else if (this.first == 0 & this.second == 0) {
        //     gutter
        // } else if (this.scorecard.length >= 30) {
        //     endGame
        } else {
            this.scorecard.push(this.first + this.second + this.scorecard[-3]);
        }
    }

    isFirstFrame() {
        this.scorecard.length < 4 ? true : false;
    }

    addSpareBonus() {
        this.firstFrame() == true ? this.scorecard.push(first + first + second) : this.scorecard.push(this.scorecard[-3] + first + first + second);
    }

    addStrikeBonus() {
        this.firstFrame() == true ? this.scorecard.push(first + first + second + second) : this.scorecard.push(this.scorecard[-3] + first + first + second + second);
    }

    gutter() {
        console.log("Double Gutter! Bad Luck");
    }

    endGame() {

    }
}