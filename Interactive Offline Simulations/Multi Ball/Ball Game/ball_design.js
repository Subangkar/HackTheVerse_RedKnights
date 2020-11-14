class Ball {
    
    constructor(x, y, radius){
        this.radius = radius;
        this.x = x;
        this.y = y;
        
        this.dx = randomDx();
        this.dy = randomDy();

        this.mass = this.radius * this.radius * this.radius;
        // Mass = Density *  Volume
        // We denote MASS as a function of volume by considering VOLUME = radius^3
        this.color = randomColor();
    };    

    draw() {
        ctx.beginPath();
        ctx.arc(Math.round(this.x), Math.round(this.y), this.radius, 0, 2*Math.PI);
        ctx.fillStyle = this.color;
        ctx.fill();
        ctx.strokeStyle = 'rgba(0, 0, 0, 0.6)';
        ctx.stroke();
        ctx.closePath();
    };

    speed() {
        // Magnitude of Velocity n 2D
        return Math.sqrt(this.dx * this.dx + this.dy * this.dy);
    };
    angle() {
        // Velocity's Angle with the x axis
        return Math.atan2(this.dy, this.dx);
    };
    onGround() {
        // Sitting on the Ground Checking
        return (this.y + this.radius >= canvas.height)
    };
};