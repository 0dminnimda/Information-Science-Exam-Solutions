#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

typedef unsigned int t;

#define D 5

int main()
{
    ifstream file;
    file.open("27-4b.txt");

    vector<t> sums;
    sums.resize(D, 0);

    t n;
    file >> n;

//    int step = 0;
    t a, b;
    t elem = 0;//100000;
    while (file >> a >> b)
    {
        if (a < b)
            swap(a, b);

        vector<t> cur_sums;
        cur_sums.resize(D, elem);

        for (int i = 0; i < sums.size(); i++)
        {
            t x, r;
            t s = sums[i];

            x = a;
            r = s + x;
            //if (s != 0 | step == 0)
                cur_sums[r%D] = max(cur_sums[r%D], s + x);

            x = b;
            r = s + x;
            //if (s != 0 | step == 0)
                cur_sums[r%D] = max(cur_sums[r%D], s + x);

        }

        sums = cur_sums;

//        cout << "[";
//        for (t i: sums)
//        {
//            cout << i << ", ";
//        }
//        cout << "]";
//
//        cout << " " << a << " " << b << "\n";
//        step++;
    }

    file.close();


    cout << sums[0] << "\n";

    return 0;
}
