/* 수정된 weird.h*/
#ifndef WEIRD_H
#define WEIRD_H

struct Weird {
    char arr[2];
    int i;
};
#endif
/* #include "weird.h"에서 WEIRD_H 가 정의가 안 되어,
   #ifndef 가 참이 되어 #define WEIRD_H 가 수행되어 WEIRD_H가 정의.
   stdio.h를 까보면 _MSV_VER > 1000(_MSV_VER: Compiler 버젼 상수)이면 pragma once 사용
   구 버전의 컴파일러는 그 아래 C 표준 따라 사용되도록 코드.*/