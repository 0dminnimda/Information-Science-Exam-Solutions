#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

#define D2 7
#define D 49

int main()
{
    ifstream file;
    file.open("27-7b.txt");

    int n;
    file >> n;

    vector<int> nums;
    nums.resize(D, 0);

    int mx = 0;

    int x;
    while (file >> x)
    {
        for (int n: nums)
        {
            if ((n * x) % D != 0 & (n * x) % D2 == 0)
                mx = max(mx, n * x);
        }

        int r = x % D;
        nums[r] = max(nums[r], x);
    }

    file.close();

    cout << "[";
    for (int x: nums)
        cout << x << ", ";
    cout << "]\n";

    cout << mx;

    return 0;
}
