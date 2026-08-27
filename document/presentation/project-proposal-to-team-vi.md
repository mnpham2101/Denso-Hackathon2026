---
title: Ứng Dụng ERM Đề Xuất Cho Nhà Máy
description: Denso-FPT Hackathon 2026 — phạm vi dự án, mức độ phù hợp thị trường, và kế hoạch triển khai
---

# Denso-FPT Hackathon 2026

**Đề Xuất Dự Án**

Ứng dụng quản lý nhà máy được đề xuất cho các đề bài công nghệ D1, D2, D3 của Denso-FPT Hackathon 2026.

## Giới Thiệu Dự Án

Dự án đề xuất một ứng dụng web, triển khai tại chỗ (on-premise), phục vụ thu thập dữ liệu nhà máy, dự đoán, và báo cáo, xây dựng cho Denso-FPT Hackathon 2026.

- Hướng đến ba đề bài D1, D2, D3: kết nối thiết bị cũ, dự báo và mô phỏng logistics, dự đoán tác động chuỗi sản xuất.
- Kết hợp giao diện web, nền tảng dữ liệu tại chỗ, và mô hình AI/ML hoạt động ngoại tuyến.
- Nằm giữa thực tiễn ERM/ERP phổ biến và yêu cầu kỹ thuật riêng của cuộc thi.

# Phạm Vi Dự Án

Các nhóm tính năng, và mức độ phù hợp của đề xuất với ERM phổ biến cũng như yêu cầu của D1–D3.

## Nhóm Tính Năng

![](assets/feature-groups-vi.svg)

## Mức Độ Phù Hợp Với Thị Trường ERM

- **Tính năng phổ biến.** Truy cập web, bảng điều khiển trực tiếp, nhập liệu thủ công, triển khai tại chỗ, lưu trữ cục bộ, báo cáo, và dự đoán đã có sẵn ở các sản phẩm ERM phổ biến.
- **Giá trị gia tăng.** Xây dựng quy trình kéo-thả, cấu hình không cần lập trình, kết nối máy móc, thu thập đa nguồn, và AI đa mô hình vượt ra ngoài mức nền tảng ERM thông thường.
- **Năng lực mới.** Vận hành ngoại tuyến và suy luận AI ngoại tuyến chưa được ghi nhận ở các sản phẩm ERM khảo sát — có thể là điểm khác biệt.

![h:220 Phân bố tính năng so với phạm vi ERM phổ biến — Có 8, Một phần 9, Không 5 (n = 22)](assets/04-common-erm-breakdown.svg)

## Mức Độ Phù Hợp Với D1, D2, D3

- **Điểm mạnh.** Bảng điều khiển trực tiếp, kết nối máy móc, thu thập đa nguồn, báo cáo, và dự đoán khớp trực tiếp với các hạng mục bàn giao của D1–D3.
- **Rủi ro ngoài phạm vi.** Cấu hình không cần lập trình, hỗ trợ đa định dạng, lưu trữ cục bộ, chuẩn hóa dữ liệu, và AI đa mô hình chỉ hỗ trợ gián tiếp; cần xác minh mức độ đáp ứng thực tế.
- **Không được yêu cầu.** Kiểu giao diện, vị trí triển khai, vận hành ngoại tuyến, lựa chọn mô hình, và toàn bộ tính năng bảo mật không được D1/D2/D3 yêu cầu; ban giám khảo có thể xem đây là phạm vi không cần thiết.

![h:220 Phân bố tính năng so với yêu cầu D1/D2/D3 — Có 6, Một phần 5, Không 11 (n = 22)](assets/04-d1d3-breakdown-overall.svg)

# Điểm Mạnh, Điểm Yếu, Và Tính Khả Thi

Đánh giá vị thế, rủi ro, và kế hoạch triển khai của đề xuất.

## Điểm Mạnh

- Hoạt động như Jira cho phát triển phần mềm, hoặc như ERM cho sản xuất, được áp dụng như một công cụ vận hành thực tế cho nhà máy.
- Thích ứng với nhiều quy trình làm việc, thủ tục, và loại dữ liệu khác nhau, thay vì một quy trình cố định duy nhất.
- Cung cấp các tính năng chưa có ở các sản phẩm ERM phổ biến, dựa trên kết quả nghiên cứu thị trường.
- Có thể tùy chỉnh theo từng nhà máy và từng yêu cầu khác nhau.
- Máy chủ tại chỗ, AI triển khai on-premise, và hệ thống bảo mật giúp bảo vệ thông tin sản xuất độc quyền.

## Điểm Yếu Và Giải Pháp

- **Khối lượng công việc lớn, thời gian ngắn.** Nhiều tính năng thuộc năm nhóm cần được xây dựng nhanh chóng. *Giải pháp:* sản xuất song song theo từng nhóm tính năng, trình bày ở phần tiếp theo.
- **Tính năng không được yêu cầu có thể bị từ chối.** Các năng lực vượt ngoài D1/D2/D3 có thể không được ban giám khảo hoặc khách hàng đánh giá cao.
- **Rủi ro bị sao chép.** Một tập đoàn hoặc đội nhóm lớn hơn có thể tái tạo lại ứng dụng sau khi ý tưởng đã được chứng minh.

## Tính Khả Thi

- Năm nhóm tính năng — Giao diện, Hạ tầng, Nghiệp vụ, Bảo mật, AI — đủ tách biệt để phát triển song song.
- Phát triển song song rút ngắn thời gian bàn giao dù số lượng tính năng lớn.
- Mỗi nhóm có thể giao cho một luồng công việc riêng, giảm rủi ro từ thời gian ngắn đã nêu ở điểm yếu.

# Xin cảm ơn!

Ứng Dụng ERM Đề Xuất Cho Nhà Máy · Denso-FPT Hackathon 2026
