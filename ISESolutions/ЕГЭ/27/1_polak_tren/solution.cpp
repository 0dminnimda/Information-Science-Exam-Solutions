#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

typedef unsigned long t;

#define D 3

int main()
{
    ifstream file;
    file.open("27-1a.txt");

    t n;
    file >> n;

    vector<t> sums;
    sums.resize(D, 0);

    vector<t> cur_sums;
    cur_sums.resize(D, 0);

    t step = 0;
    t elem = 10000000;
    t a, b;
    while (file >> a >> b)
    {
        fill(cur_sums.begin(), cur_sums.end(), elem);

        for (t s: sums)
        {
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

        cout << "[";
        for (t s: sums)
        {
            cout << s << ", ";
        }
        cout << "] ";

        cout << a << " " << b << "\n";

        step++;
    }

    file.close();

    cout << min(sums[1], sums[2]) << "\n";

    return 0;
}
