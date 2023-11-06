// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <unistd.h>
// #include <arpa/inet.h>

// int main() {
// 	int server_fd, client_fd;
// 	struct sockaddr_in server_addr, client_addr;
// 	socklen_t addr_len = sizeof(client_addr);
	
// 	// 서버 소켓 생성
// 	server_fd = socket(AF_INET, SOCK_STREAM, 0);
// 	if (server_fd == -1) {
// 		printf("소켓 생성 오류\n");
// 		exit(1);
// 	}
	
// 	// 서버 주소 설정
// 	memset(&server_addr, 0, sizeof(server_addr));
// 	server_addr.sin_family = AF_INET;
// 	server_addr.sin_addr.s_addr = INADDR_ANY;
// 	server_addr.sin_port = htons(9999);
	
// 	// 서버에 주소 할당
// 	if (bind(server_fd, (struct sockaddr *)&server_addr, sizeof(server_addr)) == -1) {
// 		printf("주소 할당 오류\n");
// 		close(server_fd);
// 		exit(1);
// 	}
	
// 	// 클라이언트의 연결 대기
// 	if (listen(server_fd, 5) == -1) {
// 		printf("연결 대기 오류\n");
// 		close(server_fd);
// 		exit(1);
// 	}
	
// 	printf("서버가 대기 중...\n");
	
// 	// 클라이언트와 연결
// 	client_fd = accept(server_fd, (struct sockaddr *)&client_addr, &addr_len);
// 	if (client_fd == -1) {
// 		printf("연결 오류\n");
// 		close(server_fd);
// 		exit(1);
// 	}
	
// 	// 파일 크기 읽기
// 	uint32_t file_size;
// 	if (read(client_fd, &file_size, sizeof(file_size)) != sizeof(file_size)) {
// 		printf("파일 크기 읽기 오류\n");
// 		close(client_fd);
// 		close(server_fd);
// 		exit(1);
// 	}
	
// 	printf("수신된 파일 크기: %u 바이트\n", file_size);
	
// 	// 버퍼 동적 할당
// 	void *buffer = malloc(file_size);
// 	if (buffer == NULL) {
// 		printf("메모리 할당 오류\n");
// 		close(client_fd);
// 		close(server_fd);
// 		exit(1);
// 	}
	
// 	printf("생성된 버퍼 주소 : %p\n", buffer);
    
// 	// 연결 종료
// 	close(client_fd);
// 	close(server_fd);
	
// 	// 할당된 메모리 해제
// 	free(buffer);
	
// 	return 0;
// }

#include <stdio.h>

int main() {
	FILE *file;
	const char *filename = "/tmp/test.txt";
	
	// 파일 열기
	file = fopen(filename, "w");
	if (file == NULL) {
		printf("파일 열기 오류\n");
		return 1;
	} else {
		printf("파일 열기 성공\n");
	}
    return 0;
}