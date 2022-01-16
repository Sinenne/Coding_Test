#include <bits/stdc++.h>


using namespace std;

// Method No.1
int main(void)
{
  int n, m, k;
  cin >> n >> m >> k;

  vector<int> v;

  int sum = 0;
  int cnt = 0;
  int biggest = 0;
  int twoiggest = 0;


  for(int i = 0 ; i < n ; i++)
  {
    int x;
    cin >> x;
    v.push_back(x);
  }

  sort(v.begin(), v.end());

  biggest = v[n-1];
  twoiggest = v[n-2];

  for(int i = 0; i < m; i++)
  {
    if(cnt == k)
    {
      sum += twoiggest;
      cnt = 0;
    }
    else
    {
      sum += biggest;
      cnt++;
    }
  }

  cout << sum << endl;
  return 0;
}


// Method No.2

int main(void)
{
  int n, m, k;
  vector<int> v;
  int biggest_cnt = 0;
  int sum = 0;
  cin >> n >> m >> k;
  
  
  for(int = 0 ; i < n ; i++)
  {
    int x;
    x >> cin;
    v.push_back(x);
  }
  
  sort(v.begin(), v.end());
  
  biggest_cnt = (m/(k+1)) * k;
  biggest_cnt += m % (k+1);
  
  sum += biggest_cnt * v[n-1];
  sum += (m - biggest_cnt) * v[n-2];
  
  cout << sum << endl;
  
  return 0;
}
