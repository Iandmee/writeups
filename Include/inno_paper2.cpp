#include <bits/stdc++.h>
typedef long long ll;
std::vector<std::string>str_tec;
void generate(ll len,std::string last){
    if(len==last.size()){
        str_tec.push_back(last);
        return;
    }
    generate(len,last+'0');
    generate(len,last+'1');
}
int main() {
    std::string s = "Innopolis Open Information Security competition";
    std::map<char, ll> a;
    for (int i = 0; i < s.size(); i++) {
        a[s[i]]++;      //считаем количество элементов каждого типа
    }
    std::vector<std::pair<ll, char>> pairs;
    for (auto i:a)
        pairs.push_back(std::make_pair(i.second, i.first)); //переводим в vector
    std::sort(pairs.rbegin(), pairs.rend());//сортируем по невозрастанию количества каждого элемента
    for (int i = 1; i < 10; i++) // генерируем битовые строчки в лексиграфическом порядке
        generate(i, "");
    std::map<char, std::string> cipher;
    for (int i = 0; i < pairs.size(); i++) // составляем словарь,где каждому элементу(по возрастанию количества) будем сопоставлять битовую строчку
        cipher[pairs[i].second] = str_tec[i]; // лексиграфически минимальную на данный момент
    std::string ans = "";
    for (int i = 0; i < s.size(); i++)
        ans += cipher[s[i]];
    std::cout << "#############" << '\n' << "ans --->" << ans << '\n' << "#############"<<'\n';//выводим закодированное сообщение
    for (int i = 0; i < pairs.size(); i++) {
        std::cout << pairs[i].second << " " << pairs[i].first << " "
                  << (double) pairs[i].first / (double) s.size() * 100 << '%' << " " << cipher[pairs[i].second] << '\n';//выводим нужную таблицу
    }
    return 0;
}