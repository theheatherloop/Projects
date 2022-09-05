using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
us



namespace TwentyOne
{
    class Program
    {
		static void Main(string[] arcs)
        {
            Console.WriteLine("Welcome the Grand Hotel and Casino. Let's start by telling me your name.");
            string playerName = Console.ReadLine();
            Console.WriteLine("And how much did you bring today?");
            int bank = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Hello,{0}. Would you like to join a game of 21 right now?", playerName);
            string answer = Console.ReadLine().ToLower();
            if (answer == "yes" || answer == "ya" || answer == "y" || answer == "yeah")
            {
                Player player = new Player(playerName, bank);
                Game game = new TwentyOneGame();
                game += player;
                player.isActivelyPlaying = true;
                while (player.isActivelyPlaying && player.Balance > 0)
                {
                    game.Play();
                }
                game -= player;
                Console.WriteLine("Thank you for playing!");
            }
            Console.WriteLine("Feel free to look around the casino. Bye for now.");
        }
    }
}
        
    

