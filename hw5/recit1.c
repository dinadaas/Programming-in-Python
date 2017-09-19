//Write a program that asks the user to input the name of his/her favorite Duke basketball
// player, the player’s height in inches (this height should be an integer), 
//and the player’s average number of points scored per game 
//(this last input should be an integer). The program should then output the player’s 
//name followed by “scored an average of X points per inch”, where X is the average
// points divided by the height in inches. 
//IMPORTANT: X must be a floating point number, which means you must do some type casting 
//to compute it.
int main (){
	char c[50];
	printf("Input your favorite Duke basketball player: \n");
	scanf ("%s", c)
	int h;
	printf("Input player's height in inches: \n");
	scanf ("%i", h)
	int p;
	printf("Input average points per game: \n");
	scanf ("%i", p);
	float X = (float)p / (float)h;
	(int)X;

	printf("%s",c, "scored an average of %i", X, "points per inch." );
}
