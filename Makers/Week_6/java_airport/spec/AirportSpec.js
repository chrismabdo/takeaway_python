describe("Airport", function(){

    var airport;

        beforeEach(function() {
            airport = new Airport;
        });

        it('should create a new instance of Airport', function() {
            expect(airport).toBeInstanceOf(Airport);
        });

        it('should have a hangar upon creation', function() {
            expect(airport.hangar).toEqual([]);
        });

        describe('land function', function() {

            it('should land a plane ', function() {
                airport.land("plane");
                expect(airport.hangar).toEqual(["plane"]);
            });


        })




});
