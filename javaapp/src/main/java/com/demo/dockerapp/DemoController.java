package com.demo.dockerapp;

import java.time.Instant;
import java.util.Map;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;

@Controller
public class DemoController {

    @Value("${spring.application.name:java-docker-demo}")
    private String applicationName;

    @GetMapping("/")
    public String home(Model model) {
        model.addAttribute("applicationName", applicationName);
        model.addAttribute("javaVersion", System.getProperty("java.version"));
        model.addAttribute("runtime", System.getProperty("java.runtime.name"));
        model.addAttribute("os", System.getProperty("os.name"));
        model.addAttribute("time", Instant.now());
        return "index";
    }
}

@RestController
class ApiController {

    @GetMapping("/api/hello")
    public Map<String, String> hello() {
        return Map.of(
            "message", "Hello from Java!",
            "status", "running",
            "application", "java-docker-demo"
        );
    }

    @GetMapping("/api/info")
    public Map<String, String> info() {
        return Map.of(
            "javaVersion", System.getProperty("java.version"),
            "os", System.getProperty("os.name"),
            "architecture", System.getProperty("os.arch"),
            "runtime", System.getProperty("java.runtime.name")
        );
    }
}
