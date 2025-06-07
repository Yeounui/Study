#include <iostream>

class Date {
    int year_;
    int month_; // 1 부터 12 까지.
    int day_; // 1 부터 31 까지.
    
public:
    void ShowDate();
    Date() { // Default constructor (디폴트 생성자) 정의
        std::cout << "기본 생성자 호출!" << std::endl;
        year_ = 2012;
        month_ = 7;
        day_ = 12;
    }
    Date(int year, int month, int day) { //Constructor overloading
        std::cout << "인자 3개인 생성자 호출!" << std::endl;
        year_ = year;
        month_ = month;
        day_ = day;
    }
};

void Date::ShowDate() {
    std::cout << "오늘은 " << year_ << " 년 " << month_ << " 월 " << day_
    << " 일 입니다 " << std::endl;
}

int main() {
    Date day = Date(); // 디폴트 생성자 호출; A a()
    // 인자가 없는 생성자를 호출하기 위해선 A a.
    Date day2(2012, 10, 31);

    day.ShowDate();
    day2.ShowDate();
    return 0;
}