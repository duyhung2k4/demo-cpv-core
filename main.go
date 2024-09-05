package main

import (
	"fmt"
	"log"
	"os/exec"
	"strings"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	var listPath = []string{
		"test/chum.png",
		"test/chum2.png",
		"test/tienlees.png",
		"test/obama.png",
	}

	for _, path := range listPath {
		wg.Add(1)
		go func(p string) {
			defer wg.Done()
			log.Println(runFace(p))
		}(path)
	}

	wg.Wait()
	log.Println("Done")
}

func runFace(path string) string {
	// Tạo câu lệnh để chạy Python script
	cmd := exec.Command("python3", "run_model.py")

	// Tạo pipe để truyền dữ liệu đầu vào (stdin) cho script
	stdin, err := cmd.StdinPipe()
	if err != nil {
		return fmt.Sprintln("Error creating StdinPipe:", err)
	}

	// Lấy output từ câu lệnh (stdout) và (stderr)
	var output strings.Builder
	cmd.Stdout = &output
	cmd.Stderr = &output

	// Dữ liệu bạn muốn gửi tới script.py
	inputData := path

	// Gửi dữ liệu vào stdin của script
	go func() {
		defer stdin.Close()
		_, err := stdin.Write([]byte(inputData))
		if err != nil {
			fmt.Println("Error writing to Stdin:", err)
		}
	}()

	// Chạy câu lệnh
	err = cmd.Start()
	if err != nil {
		return fmt.Sprintln("Error starting command:", err)
	}

	// Chờ lệnh hoàn tất
	err = cmd.Wait()
	if err != nil {
		return fmt.Sprintln("Error waiting for command:", err)
	}

	// In ra kết quả sau khi script chạy xong
	return fmt.Sprintln(strings.TrimSpace(output.String()))
}
