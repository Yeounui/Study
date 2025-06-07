// 디폴트 생성자 정의해보기
#include <iostream>

class Date {
    int year_;
    int month_; // 1 부터 12 까지.
    int day_; // 1 부터 31 까지.
    
public:
    Date() = default; //C++11부터; 명시적 디폴트 생성자 정의
    void ShowDate();
};

void Date::ShowDate() {
    std::cout << "오늘은 " << year_ << " 년 " << month_ << " 월 " << day_
    << " 일 입니다 " << std::endl;
}

int main() {
    Date day = Date(); // 디폴트 생성자 호출; A a()
    // 인자가 없는 생성자를 호출하기 위해선 A a.
    Date day2;
    day.ShowDate();
    day2.ShowDate();
    return 0;
}