#include <iostream>
#include <fstream>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

typedef unsigned short int numt;

typedef struct M {
    bool a;
    bool b;
    numt s;
} M;

bool cmp(M op1, M op2)
{
    return op1.s < op2.s;
}

int main(int argc, char * argv[])
{
    vector<M> leftovers;
    vector<M> nums_even_odd;
    vector<M> nums_odd_even;
    vector<M> nums_odd_odd;

    {
        fstream file;
        file.open("..\\inf_26_04_21_27a.txt", ios_base::in);

        int n;
        file >> n;

        cout << "n: " << n << "\n";

        numt a, b;
        while (file >> a >> b)
        {
            if(b % 2 != 1)
                continue;

            if(a < b)
                swap(a, b);
//            {
//                numt t;
//                t = a;
//                a = b;
//                b = t;
//            }

            bool mx_even = a % 2 == 0;
            bool mn_even = b % 2 == 0;

            if (mx_even & mn_even)
                // cannot happen because at least one is odd
                return -1;
            else if (mx_even & !mn_even)
                nums_even_odd.push_back({!mx_even, !mn_even, a + b});
            else if (!mx_even & mn_even)
                nums_odd_even.push_back({!mx_even, !mn_even, a + b});
            else if (!mx_even & !mn_even)
                nums_odd_odd.push_back({!mx_even, !mn_even, a + b});
        }
        file.close();

    //    vector<M> nums;

    //    for(decltype(nums)::const_iterator m = nums.begin(); m != nums.end(); ++m)
    //    {
    //        cout << (*m).a << " " << (*m).b << "\n";
    //    }

    //    for(M m: nums)
    //    {
    //        cout << m.a << " " << m.b << "\n";
    //    }

    //    M m;
    //    for(int i = 0; i < nums.size(); i++)
    //    {
    //        m = nums[i];
    //        cout << m.a << " " << m.b << "\n";
    //    }
    //
    //    numt sum_of_max = 0;
    //    numt sum_of_min = 0;
    }

    M m;
    int diff;
    long s = 0;

    // goal: even odd

    // 0, 1
    // need odd size
    sort(nums_even_odd.begin(), nums_even_odd.end(), cmp);
    int needed_even_odd = nums_even_odd.size();
    if(nums_even_odd.size() % 2 == 0)
        needed_even_odd--;
    diff = nums_even_odd.size() - needed_even_odd;
    while (diff)
    {
        leftovers.push_back(nums_even_odd.front());
        nums_even_odd.erase(nums_even_odd.begin());
        diff--;
    }
//    cout << "\neven odd\n";
//    cout << "actual: " << nums_even_odd.size() << ", needed: " << needed_even_odd << "\n";
    for(int i = 0; i < nums_even_odd.size(); i++)
    {
        m = nums_even_odd[i];
        s += m.s;
//        cout << m.a << " " << m.b << " " << m.s << ", ";
    }

    // 1 0
    // 1 0
    // need even size
    sort(nums_odd_even.begin(), nums_odd_even.end(), cmp);
    diff = nums_odd_even.size() - nums_odd_even.size() / 2 * 2;
    while (diff)
    {
        leftovers.push_back(nums_odd_even.front());
        nums_odd_even.erase(nums_odd_even.begin());
        diff--;
    }
//    cout << "\nodd even\n";
//    cout << "actual: " << nums_odd_even.size() << ", needed: " << nums_odd_even.size() / 2 * 2 << "\n";
    for(int i = 0; i < nums_odd_even.size(); i++)
    {
        m = nums_odd_even[i];
        s += m.s;
//        cout << m.a << " " << m.b << " " << m.s << ", ";
    }

    // 1 1
    // 1 1
    // need even size
    sort(nums_odd_odd.begin(), nums_odd_odd.end(), cmp);
    diff = nums_odd_odd.size() - nums_odd_odd.size() / 2 * 2;
    while (diff)
    {
        leftovers.push_back(nums_odd_odd.front());
        nums_odd_odd.erase(nums_odd_odd.begin());
        diff--;
    }
//    cout << "\nodd odd\n";
//    cout << "actual: " << nums_odd_odd.size() << ", needed: " << nums_odd_odd.size() / 2 * 2 << "\n";
    for(int i = 0; i < nums_odd_odd.size(); i++)
    {
        m = nums_odd_odd[i];
        s += m.s;
//        cout << m.a << " " << m.b << " " << m.s << ", ";
    }

    cout << "s: " << s << "\n";

    for(M m: leftovers)
    {
        cout << m.a << " " << m.b << " " << m.s << "\n";
    }

    return 0;
}
