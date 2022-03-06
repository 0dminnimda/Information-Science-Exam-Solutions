#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

// long
// -2147483648
// 2147483647

typedef unsigned int ut;

typedef struct M
{
    ut mx;
    ut mn;
    ut diff;
} M;

bool cmp(M a, M b)
{
    return a.diff < b.diff;
}

int main()
{
    ifstream file;
    file.open("27-1b.txt");

    ut n;
    file >> n;

    vector<M> nums;
    nums.reserve(n);

    long s;
    ut a, b;
    while (file >> a >> b)
    {
        if (a < b)
            swap(a, b);

        nums.push_back({a, b, a - b});
        s += b;
    }
    file.close();

    if (s % 3 != 0)
    {
        cout << s << "\n";
        return 0;
    }

    sort(nums.begin(), nums.end(), cmp);

    for (int i = 0; i < nums.size(); i++)
    {
        s += nums[i].diff;
        if (s % 3 != 0)
        {
            cout << s << "\n";
            return 0;
        }
        s -= nums[i].diff;
    }

    return 0;
}
