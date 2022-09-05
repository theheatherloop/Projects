using System;
using System.Collections.Generic;

namespace FortuneTeller
{
    class Program
    {
        static void Main(string[] args)
        {   // number array
            int[] luckNum = { 13, 7, 8, 42 };
            // string array
            string[] daily = {"He who laughs at himself never runs out of things to laugh at.\n",
                              "He who throws dirt is losing ground.\n",
                              "A conclusion is simply the place where you got tired of thinking.\n",
                              "You will always find happiness at work on Friday.\n"};
            List<string> monthly = new List<string>();
            // adding elements in list
            monthly.Add("The fear of death follows from the fear of life. A man who lives fully is prepared to die at any time.\n");
            monthly.Add("The early bird gets the worm, but the second mouse getst he cheese.\n");
            monthly.Add("A cynic is only a frustrated optimist.\n");
            monthly.Add("If you tell the truth, you don't have to remember anything.\n");
            Console.WriteLine("Fortune Teller 9000");
            Console.WriteLine("Pick a number between 0 - 3");
            Console.WriteLine("to get your daily fortune!");
                string getDaily = Console.ReadLine();
            int indexDF = Convert.ToInt32(getDaily);
            if (indexDF > 3)
            {
                Console.WriteLine(indexDF + " is out of range.\n");
            }
            else
            {
                Console.WriteLine("Your Daily fortune is :\n" + daily[indexDF]);
            }
            Console.WriteLine("Pick a number between 0 - 3");
            Console.WriteLine("to get your monthly fortune!");
            string getMonthly = Console.ReadLine();
            int indexM = Convert.ToInt32(getMonthly);
            if (indexM > 3)
            {
                Console.WriteLine(indexM + " is out of range.\n");
            }
            else
            {
                Console.WriteLine("Your monthly fourtune is:\n" + monthly[indexM]);
            }
            Console.WriteLine("Pick a number between 0 - 3");
            Console.WriteLine("to get your lucky number!");
            string getLuck = Console.ReadLine();
            int indexL = Convert.ToInt32(getLuck);
            if (indexL > 3)
            {
                Console.WriteLine(indexL + "is out of range.\n");
            }
            else
            {
                Console.WriteLine("Your lucky number is :\n " + luckNum[indexL]);
            }
        }
    }
}
