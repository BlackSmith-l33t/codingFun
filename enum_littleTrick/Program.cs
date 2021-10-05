using System;

namespace enum_littleTrick
{
    class Program
    {
        enum EDirection
        {
            North,
            South,
            East,
            West,
            Max,
        };

        static void Main(string[] args)
        {
            // 어느 함수
            string[] directions = new string[(int)EDirection.Max];
            
            for (int i = 0; i < directions.Length; i++)
            {
                // 코드
            }
        }
    }
}
