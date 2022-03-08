#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned int t;

int main()
{
    ifstream file;
    file.open("27-8b.txt");

    t n;
    file >> n;

    vector<t> nums;
    nums.reserve(n);

    while (file >> n)
    {
        nums.push_back(n);
    }

    file.close();

    t mn = 10000000;

    for (int i = 0; i < nums.size() - 5; i++)
    {
        n = nums[i];

#if 0
        vector<t> r;
        r.assign(nums.begin() + i + 5, nums.end());

//        if (r.size() != 0)
        {
            t v = r[distance(r.begin(), min_element(r.begin(), r.end()))];
            mn = min(mn, n*n + v*v);
        }
#else

        auto start = nums.begin() + i + 5;
        auto finish = nums.end();

        t v = nums[distance(nums.begin(), min_element(start, finish))];
        mn = min(mn, n*n + v*v);
#endif

    }

    cout << mn << "\n";

    return 0;
}
