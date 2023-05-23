package com.example.todoapp.board.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {
    // 기본 주소 요청 "/"
    @GetMapping("/")
    // index() 메소드 호출 -> resources/templates 으로!
    public String index() {
        return "index";
    }
}
