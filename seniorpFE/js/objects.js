
(function (global) {

    //capitalize to show its a class, this is NOT a literal
    function Rectangle(x, y) {
        this.x = x;
        this.y = y;
    }
    //makes this function shared between all rectangles, so
    //when we create a new rectangle, this is not EXECUTED
    //note proto must be outside the class declaration
    Rectangle.prototype.getArea =
        function () {
            return this.x*this.y;
        }

        //notice, this is an object literal (same as saying "new")
        let literalRectangle = {
            length: 20,
            width: 10,
            getArea: function() {
                console.log(this);
                return this.length*this.width;
            }
        };

        //display our normal object with new keyword
        let rectangle = new Rectangle(4,5);
        console.log(rectangle.getArea());
        //display our literal info, which also prints its object contents
        console.log(literalRectangle.getArea());


})(window);