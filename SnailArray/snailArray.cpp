#include <iostream>

using namespace std;

int main()
{
	int snailArray[5][5];
	int y = 0, x = 0;
	int column = 5;
	int row = 5;
	int insertNum = 0;
	int endPoint = row * column;
	
	// 배열의 0으로 셋팅
	for (int i = 0; i < column; i++)
	{
		for (int j = 0; j < column; j++)
		{
			snailArray[j][i] = 0;
		}
	}

	while (insertNum < endPoint)
	{
		// up	
		
		for (x; x < column && snailArray[y][x] == 0; x++)
		{
			snailArray[y][x] = ++insertNum;			
		}
		y++;		

		// right
		for (y; y < row && snailArray[y][x - 1] == 0; y++)
		{
			snailArray[y][x - 1] = ++insertNum;
		}
		
		// down
		for (x; x - 1 > 0 && snailArray[y - 1][x - 2] == 0; x--)
		{
			snailArray[y - 1][x - 2] = ++insertNum;
		}

		//left
		for (y; y > 2 && snailArray[y - 2][x - 1] == 0; y--)
		{
			snailArray[y - 2][x - 1] = ++insertNum;
		}		

		column--;
		row--;
		y--;
	}	
	
	// 출력 
	for (int j = 0; j < 5; j++)
	{
		for (int i = 0; i < 5; i++) {

			if (snailArray[j][i] < 10)
			{
				cout << " ";
			}
			cout << snailArray[j][i] << "  ";
		}
		cout << endl;
	}	
}