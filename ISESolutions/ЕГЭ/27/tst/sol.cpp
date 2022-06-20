#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <thread>
#include <memory>
using namespace std;

typedef unsigned long long t;


void proc(vector<t> &nums, vector<t> &mxnums, int num)
{
    t n;
    t mx = 0;
    //    #pragma omp parallel for
    for (auto i = mxnums.size() / num; i < mxnums.size() / (num+1); i++)
    {
        cout << i << "\n";
//        #pragma omp parallel for
        for (auto j = i + 1; j<nums.size(); j++)
        {
            n = nums[i] * nums[j];
            if (n % 14 == 0)
            {
                mx = max(mx, n);
//                n = max(mx, n);

//                #pragma omp critical
//                mx = n;
//                mxnums[i] = max(n, mxnums[i]);
            }
        }
    }
    mxnums[num] = mx;
}

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
    mxnums.resize(thread::hardware_concurrency(), 0);


    vector<thread> threads;
    for (int i = 0; i < mxnums.size(); i++)
    {
        threads.push_back(move(thread(proc, mxnums, i)));
    }


    t mx = 0;
    for (thread thrd: threads)
    {
        thrd.join();
    }


//    for_each(execution::par, nums.begin(), nums.end(),
//             [](auto&& item)
//             {
//                 cout << item << "\n";
//             });



    cout << "size: " << mxnums.size() << "\n";
    cout << *max_element(mxnums.begin(), mxnums.end()) << "\n";
//    cout << mx << "\n";
}
