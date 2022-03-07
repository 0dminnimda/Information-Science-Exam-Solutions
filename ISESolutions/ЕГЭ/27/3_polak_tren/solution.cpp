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

bool cmp2(M a, M b)
{
    return a.diff > b.diff;
}

//
//bool operator <(M a, M b)
//{
//    return cmp(a, b);
//}

int main()
{
    ifstream file;
    file.open("27-3a.txt");

    t n;
    file >> n;

    vector<M> nums;
    nums.reserve(n);

    long s = 0;

    t a, b;
    while (file >> a >> b)
    {
        if (a < b)
            swap(a, b);

        nums.push_back({a, b, a - b});
        s += b;
    }
    file.close();

    if (s % 3 == 0)
    {
        cout << s << "\n";
        return 0;
    }

    cout << "s: " << s << "\n";

    sort(nums.begin(), nums.end(), cmp);

    long mn = 0;

    int K;

    for (K = 1; K < nums.size(); K++)
    {
        do {
            cout << "[";
            for (int i = 0; i < nums.size(); ++i)
            {
                M m = nums[i];
                cout << m.a << " " << m.b << " " << m.diff << ", ";
            }
            cout << "]\n\n";
        } while (prev_permutation(nums.begin(), nums.end(), cmp2));
    }

//    for (int i = 0; i < nums.size(); i++)
//    {
//        M m = nums[i];
//        cout << m.a << " " << m.b << " " << m.diff << " ";
//        s += m.diff;
//        cout << s << "\n";
////        if (s % 3 == 0)
////        {
////            cout << s << "\n";
////            return 0;
////        }
//        s -= m.diff;
//    }

    return 0;
}
