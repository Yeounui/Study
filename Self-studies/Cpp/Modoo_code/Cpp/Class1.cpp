#include <iostream>

class Animal {
    private: // private 내 변수, 함수는 외부 접근 불가. (불가: animal.food = 100)
        int food;
        int weight; // food, weight: 멤버 변수
    public: // public 내 변수, 함수는 외부 접근 가능.
        void set_animal(int _food, int _weight) {
            food = _food;
            weight = _weight;
        }
        void increase_food(int inc) {
            food += inc;
            weight += (inc / 3);
        }
        void view_stat() {
            std::cout << "이 동물의 food : " << food << std::endl;
            std::cout << "이 동물의 weight : " << weight << std::endl;
        } // set_animal, increase_food, view_stat: 멤버 함수 (member function)
}; // 세미콜론

int main() {
    Animal animal; //Class Animal의 Instance animal
    animal.set_animal(100, 50);
    animal.increase_food(30);
    animal.view_stat();
    return 0;
}
