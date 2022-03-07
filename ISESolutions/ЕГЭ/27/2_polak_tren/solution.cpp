#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned int t;

typedef struct M
{
    t a;
    t b;
    t diff;
} M;

bool cmp(M a, M b)
{
    return a.diff < b.diff;
}

int main()
{
    ifstream file;
    file.open("27-2b.txt");

    t n;
    file >> n;

    vector<M> nums;
    nums.reserve(n);

    unsigned long s;
    t a, b;
    while (file >> a >> b)
    {
        if (a < b)
            swap(a, b);

        nums.push_back({a, b, a - b});
        s += a;
    }
    file.close();

    if (s % 3 == 0)
    {
        cout << s << "\n";
        return 0;
    }

    sort(nums.begin(), nums.end(), cmp);

    for (long i = 0; i < nums.size(); i++)
    {
        M m = nums[i];
        s -= m.diff;
        if (s % 3 == 0)
        {
            cout << s << "\n";
            return 0;
        }
        s += m.diff;
    }

    return 0;
}
