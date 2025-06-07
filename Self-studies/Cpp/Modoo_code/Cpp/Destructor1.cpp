#include <string.h>
#include <iostream>

class Marine {
    int hp; // 마린 체력
    int coord_x, coord_y; // 마린 위치
    int damage; // 공격력
    bool is_dead;
    public:
        Marine(); // 기본 생성자; Constructor의 이름은 Class 이름과 같음.
        Marine(int x, int y); // x, y 좌표에 마린 생성
        Marine(int x, int y, const char* marine_name); // 이름까지 지정
        ~Marine(); // Destructor(소멸자)의 이름은 Class 이름 앞 ~ 붙임.
        int attack(); // 데미지를 리턴한다.
        void be_attacked(int damage_earn); // 입는 데미지
        void move(int x, int y); // 새로운 위치
        void show_status(); // 상태를 보여준다.
};

Marine::Marine() {
    hp = 50;
    coord_x = coord_y = 0;
    damage = 5;
    is_dead = false;
    name = NULL;
}
Marine::Marine(int x, int y) {
    coord_x = x;
    coord_y = y;
    hp = 50;
    damage = 5;
    is_dead = false;
    name = NULL;
}
Marine::Marine(int x, int y, const char* marine_name) {
    name = new char[strlen(marine_name) + 1];
    strcpy(name, marine_name); //from string.h

    coord_x = x;
    coord_y = y;
    hp = 50;
    damage = 5;
    is_dead = false;
}
void Marine::move(int x, int y) {
    coord_x = x;
    coord_y = y;
}
int Marine::attack() { return damage; }
void Marine::be_attacked(int damage_earn) {
    hp -= damage_earn;
    if (hp <= 0) is_dead = true;
}
void Marine::show_status() {
    std::cout << " *** Marine *** " << std::endl;
    std::cout << " Location : ( " << coord_x << " , " << coord_y << " ) "
    << std::endl;
    std::cout << " HP : " << hp << std::endl;
}
Marine::~Marine() { //소멸자는 Arg(인자)를 가지지 않음.
    std::cout << name << " 의 소멸자 호출 ! " << std::endl;
    if (name != NULL) {
        delete[] name;
        //NewDel2.cpp 참고; 이름이 동적 할당(실행 단계에서 할당(경우에 따라 할당 여부 결정))
        //되어있기에 추가적으로 소멸시켜야함.
    }
}

int main() {
    Marine* marines[100];
    marines[0] = new Marine(2, 3); //new: 동시에 객체 생성, 생성자 호출
    marines[1] = new Marine(3, 5);

    std::cout << std::endl << "마린 1 이 마린 2 를 공격! " << std::endl;

    marines[0]->show_status(); // C/Struct6.c 참고; 포인터->멤버변수 = 값.
    marines[1]->show_status();

    marines[0]->be_attacked(marines[1]->attack())
    
    marines[0]->show_status();
    marines[1]->show_status();

    delete marines[0]; //언제나 동적 할당 메모리는 해제되어야
    delete marines[1];
}
