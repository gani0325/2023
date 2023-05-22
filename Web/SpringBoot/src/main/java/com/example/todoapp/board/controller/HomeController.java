package com.todoapp.board.controller;

import org.springframework.stereotype.Controler;
import org.springframework.web.bind.annotation.GetMapping;

@Controler
public class HomeController {
    // 기본 주소 요청 "/"
    @GetMapping("/")
    // index() 메소드 호출 -> resources/templates 으로!
    public String index() {
        return "index";
    }
}
