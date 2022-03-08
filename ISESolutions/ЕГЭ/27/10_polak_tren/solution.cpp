#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long t;

#define D 4

int main()
{
    ifstream file;
    file.open("27-10b.txt");

    t n;
    file >> n;

    vector<t> sums;
    sums.resize(D, 0);

    vector<t> cur_sums;
    cur_sums.resize(D, 0);

    vector<t> x_s;
    x_s.resize(D, 0);

    t elem = 0;

    t step = 0;
    t a, b, c;
    while (file >> a >> b >> c)
    {
       fill(cur_sums.begin(), cur_sums.end(), elem);

       x_s = {a, b, c};

       for (t s: sums)
       {
           for (t x: x_s)
           {
               if (s != 0 | step == 0)
               {
                   t r = (s + x) % D;
                   cur_sums[r] = max(cur_sums[r], s + x);
               }
           }
       }

       sums = cur_sums;

//       cout << "[";
//       for (t s: sums)
//       {
//           cout << s << ", ";
//       }
//       cout << "] ";
//
//       cout << a << " " << b << " " << c << "\n";

       step++;
    }

    file.close();

    cout << sums[distance(sums.begin(), max_element(sums.begin() + 1, sums.end()))] << "\n";

    return 0;
}
