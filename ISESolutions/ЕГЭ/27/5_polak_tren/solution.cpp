#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

typedef unsigned long t;

#define D 5

int main()
{
    ifstream file;
    file.open("27-5b.txt");

    vector<t> sums;
    sums.resize(D, 0);

    vector<t> cur_sums;
    cur_sums.resize(D, 0);

    t n;
    file >> n;

    t elem = 10000000000;
    t a, b;
    t step = 0;
    while (file >> a >> b)
    {
        if (a < b)
            swap(a, b);

        fill(cur_sums.begin(), cur_sums.end(), elem);

        for (int i = 0; i < sums.size(); i++)
        {
            t s = sums[i];
            t r, x;

            x = a;
            r = (s + x) % D;
            if (step == 0 | s != 0)
                cur_sums[r] = min(cur_sums[r], s+x);

            x = b;
            r = (s + x) % D;
            if (step == 0 | s != 0)
                cur_sums[r] = min(cur_sums[r], s+x);
        }

        sums = cur_sums;
//
//        cout << "[";
//        for (t e: sums)
//        {
//            cout << e << ", ";
//        }
//        cout << "] ";
//
//        cout << a << " " << b << "\n";

        step++;
    }

    file.close();

    cout << sums[0] << "\n";
}
