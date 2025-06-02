#include <iostream>

namespace header1 {
    int foo() {
        std::cout << "header1 foo called\n";
        return 42;
    }

    void bar() {
        std::cout << "header1 bar called\n";
    }
}

namespace header2 {
    int foo() {
        std::cout << "Header2 foo called\n";
        return 37;
    }

    void bar() {
        std::cout << "Header2 bar called\n";
    }
}