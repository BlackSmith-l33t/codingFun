using System;
using System.Diagnostics;

namespace rock_paper_scissors
{
    class Program
    {
        enum Choice
        {
            Scissors = 0,
            Rock = 1,
            Paper = 2            
        }
        static void Main(string[] args)
        {
            Random random = new Random();

            int aiChoice = random.Next(0, 3);
            int myChoice;
            bool bIsCorrect = false;

            Console.WriteLine("가위 : 0,  바위 : 1, 보 : 2 ");
            Console.Write("숫자 선택 : ");
            myChoice = int.Parse(Console.ReadLine());
            Console.Write("컴퓨터의 숫자 : ");
            Console.WriteLine(aiChoice);

            switch (myChoice)
            {
                case (int)Choice.Scissors:
                    Console.WriteLine("가위입니다.");
                    break;
                case (int)Choice.Rock:
                    Console.WriteLine("바위입니다.");
                    break;
                case (int)Choice.Paper:
                    Console.WriteLine("보입니다.");
                    break;

                default: 
                    Console.WriteLine("잘못된 선택입니다.");
                    bIsCorrect = true;
                    break;
            }                     

            Debug.Assert(!bIsCorrect);           

            if (myChoice == (int)Choice.Scissors && aiChoice == (int)Choice.Paper)
            {
                Console.WriteLine("이겼습니다.");
                if (myChoice == (int)Choice.Scissors && aiChoice == (int)Choice.Rock)
                    Console.WriteLine("졌습니다.");
            }
            else if (myChoice == (int)Choice.Rock && aiChoice == (int)Choice.Scissors)
            {
                Console.WriteLine("이겼습니다.");
                if (myChoice == (int)Choice.Rock && aiChoice == (int)Choice.Paper)
                    Console.WriteLine("졌습니다.");
            }
            else if (myChoice == (int)Choice.Paper && aiChoice == (int)Choice.Rock)
            {
                Console.WriteLine("이겼습니다.");
                if (myChoice == (int)Choice.Paper && aiChoice == (int)Choice.Scissors)
                    Console.WriteLine("졌습니다.");
            }
            else
                Console.WriteLine("비겼습니다.");


            
        }
    }
}
