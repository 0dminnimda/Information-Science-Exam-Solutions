#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

typedef unsigned long long t;

// https://inf-ege.sdamgia.ru/problem?id=27891
int main()
{
    ifstream file;
    file.open("27-B_2.txt");

    t len;
    file >> len;

    vector<t> nums;
    nums.reserve(len);

    t n;
    while (file >> n)
    {
//        cout << n << "\n";
        nums.push_back(n);
    }

    cout << "size: " << nums.size() << "\n";

    file.close();

    cout << "starting\n";

    vector<t> mxnums;
    mxnums.resize(len, 0);

    t mx = 0;

//    for_each(execution::par, nums.begin(), nums.end(),
//             [](auto&& item)
//             {
//                 cout << item << "\n";
//             });

//    #pragma omp parallel for
    for (auto i = 0; i<nums.size(); i++)
    {
        cout << i << "\n";
//        #pragma omp parallel for
        for (auto j = i + 1; j<nums.size(); j++)
        {
            n = nums[i] * nums[j];
            if (n % 14 == 0)
            {
//                n = max(mx, n);

//                #pragma omp critical
//                mx = n;
                mxnums[i] = max(n, mxnums[i]);
            }
        }
    }

    cout << "size: " << mxnums.size() << "\n";
    cout << *max_element(mxnums.begin(), mxnums.end()) << "\n";
//    cout << mx << "\n";
}
