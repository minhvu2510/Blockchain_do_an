# Thí sinh làm bài thi trắc nghiệm sau đó lưu kết quả bài làm và đáp án lên mạng fabric b
## Project Structure
    ├── api                   // backend cho web thi trắc 
    ├── frontend                    // Giao diện làm bài 
    ├── docker                    // run api, web bằng docker 
    ├── network_blockchain                          // mang fabric blockchain
    │   ├── be_eng                     // project backend api (python Flask)
    │   ├── fe_end                    // project frontend (Vuejs)
    │   ├── reminder                // gửi thông báo nhắc nhở qua telegram
## Các chức năng chính của web
* Log in, log out theo mã thí sinh
* Xác thực hai bước otp
* Login một lần duy nhất trên một trình 


| 1 | 2 | 3 | 4 |
| --- | --- | --- | --- |
| <img width="468" alt="login" src="https://user-images.githubusercontent.com/36092539/94156390-41335500-feaa-11ea-8934-53d9ef3a65ed.png"> | <img width="468" alt="Picture1" src="https://user-images.githubusercontent.com/36092539/94155993-c66a3a00-fea9-11ea-84e1-6bbab4b8998e.png">| <img width="468" alt="Picture3" src="https://user-images.githubusercontent.com/36092539/94157321-4f35a580-feab-11ea-8c7c-d7d9f077afa2.png"> | <img width="468" alt="Picture14png" src="https://user-images.githubusercontent.com/36092539/94156046-d2ee9280-fea9-11ea-92cf-1ce60662760d.png">
* Màn hình chính (hệ thống tự động nộp kết quả bài làm lên mạng blockchain khi hết giờ)
<img width="468" alt="Picture4" src="https://user-images.githubusercontent.com/36092539/94156022-ce29de80-fea9-11ea-9ea1-b1b0a90cab66.png">
## Build, run code
* Thay đổi thông tin db tại file api/
* Chạy lệnh sau để build tại localhost: (api, mongo, vuejs)
```bash
set .env && docker-compose up -d --build
```
### Chạy netword_blockchain dưới dạng docker: miêu tả chi tiết trong thư mục network_blockchain