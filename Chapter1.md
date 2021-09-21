# **Chapter 1**
# **The Semantic Web Vision**

**Table of Content**
- [1.1 Introduction)(#11-introduction)
	- 1.1.1 Motivation for the Semantic Web
	- 1.1.2 Design Decisions for the Semantic Web
	- 1.1.3 Basic Technology for the Semantic Web
	- 1.1.4 From Data to Knowledge
	- 1.1.5 The Web Architecture of the Semantic Web
- [1.2 Semantic Web Technologies](#12-semantic-web-technologies)
- [1.3 ]()
- [1.4 ]()
---

## **1.1 Introduction**
### **1.1.1 Motivation for the Semantic Web**
- Tầm nhìn khái quát của "Mạng ngữ nghĩa" là: *Làm cho máy tính dễ dàng truy cập web hơn*.  
- Máy tính đóng vai trò rất *hạn chế* trong trang web hiện nay: lập chỉ mục từ khóa, và đưa thông tin từ server đến clients, và chỉ có vậy.  
- Những công việc thông minh (chọn lọc, kết hợp, tổng hợp, ...) đều được xử lý bởi người đọc.  
- Điều gì xảy ra nếu chúng ta làm web gần gũi hơn với máy móc, để nó chưa đầy dữ liệu máy có thể đọc được, *"hiểu được"*? 
Một trang web như vậy sẽ tạo ra nhiều điều kiện thuật lợi mà trang web hiện nay không có: Tìm kiếm không còn chỉ đơn giản là việc tìm từ 
khóa, nó có thể trở nên nhiều ngữ nghĩa hơn, gồm tìm kiếm từ đồng nghĩa, nhận thức được từ đồng âm và tính đến ngữ cảnh và mục đích 
của truy vấn. Trang web có thể trở nên cá nhân hóa hơn nếu các *agent trình duyệt cá nhân* (personal browsing agent) có thể hiểu được nội 
dung của một trang web và điều chỉnh cho nó phù hợp với hồ sơ quan tâm cá nhân (personal interest profile). Liên kết (Linking) có thể trở 
nên ngữ nghĩa hơn bằng việc quyết định một cách linh động xem trang nào sẽ là đích đến, dựa trên hoạt động của người dùng hiện tại, thay 
vì cố định các liên kết giống nhau cho tất cả các người dùng. Nó cũng khả thi trong việc *tính hợp* thông tin giữa các trang web, thay vì 
người dùng phải tạo ra một "mental copy-paste" (sao chép tinh thần) mỗi khi tìm kiếm thông tin ở một trang và muốn kết hợp với thông tin 
ở trang khác.  

### **1.1.2 Design Decisions for the Semantic Web**
- **Mạng ngữ nghĩa** tuân theo các nguyên tắc thiết kế khác nhau, có thể tóm gọn lại như sau:  
	1. Cung cấp dữ liệu có cấu trúc và bán câu trúc ở các định dạng chuẩn hóa trên web;  
	2. Không chỉ với các bộ dữ liệu, mà cả các phần tử dữ liệu riêng lẻ ([data-element](https://en.wikipedia.org/wiki/Data_element)) 
và các mối quan hệ của chúng cũng có thể truy cập được trên web;  
	3. Mô tả ngữ nghĩa dự định của dữ liệu (intended semantics) theo một hình thức quy định cụ thể, để máy có thể xử lý ngữ nghĩa 
dự định này.  
- Chúng ta sẽ đạt được bước tiến lớn đối với tầm nhìn của **Mạng ngữ nghĩa** khi mà chúng ta có thể xuất bản và liên kết với các bộ dữ 
liệu có cấu trúc cơ sở.  

### **1.1.3 Basic Technology for the Semantic Web**
- Những nguyên tắc ở trên đã được chuyển về những công nghệ thực tế như sau:
	1. Sử dụng *Đồ thị có nhãn** (labeled graphs) làm mô hình dữ liệu (data model) cho đối tượng và mối quan hệ của chúng, với đối 
tượng là các node và các đường đi là mối quan hệ của chúng. RDF (Resource Description Framework) là phương thức chính được sử dụng để 
mô tả các đồ thị này.  
	2. Sử dụng *Định danh Web* (web identifiers - Uniform Resource Identifiers - URI) để định danh các mục dữ liệu riêng biệt ([data-items](https://www.pcmag.com/encyclopedia/term/data-item)) 
và mối quan hệ của chúng ở trong bộ dữ liệu (datasets). Và điều này cũng được biểu diễn bằng RDF.  
	3. Sử dụng những *Ontology* (Hệ thống từ vựng phân cấp về kiểu và quan hệ) làm mô hình dữ liệu chính thức thể hiện ngữ nghĩa dự định 
của dữ liệu. Các hình thức như Lược đồ RDF (RDF Schema) và Ngôn ngữ bản thể học Web (The Web Ontology Language - OWL) được sử dụng cho mục đích 
này, một lần nữa sử dụng URI để đại diện cho các kiểu và thuộc tính của chúng.  

### **1.1.4 From Data to Knowledge**
- Để có thể nắm bắt toàn bộ ngữ nghĩa của dữ liệu, các hình thức như là Lược đồ RDF và OWL không chỉ là ngôn ngữ biểu diễn dữ liệu, mà con là *ngôn 
ngữ biển diễn tri thức nhẹ* (lightweight knowledge representation languages). Chúng là "những logic" cho phép suy luận thêm thông tin từ các thông 
tin đã được đưa ra.  
	- Lược đồ Schema biểu diễn logic rất nghèo nàn chỉ cho phép một số suy luận đơn giản, chẳng hạn như thừa kế thuộc tính qua hệ thống phân cấp các kiểu 
và suy luận về kiểu của các giới hạn về và phạm vị.  
	- OWL phong phú hơn về logic (nhưng vẫn rất nhẹ) cho phép các suy luận bổ sung như bình đẳng và bất bình đẳng, giới hạn số lượng, sự tồn tại của các 
đối tượng và những thứ khác.  
	- Những suy luận như vậy trong Lược đồ RDF và OWL cung cấp cho các nhà phát hành (Publisher) thông tin khả năng tạo ra một giới hạn (lower-bound) tổi 
thiểu của các dữ kiện mà người đọc phải tin vào dữ liệu đã phát hành. Ngoài ra, OWL còn cung cấp cho các nhà pháp hành thông tin khả năng ngăn cả người đọc 
tin một số điều nhất định về dữ liệu đã phát hành.  
- Cùng với nhau, việc thực hiện các suy luận như vậy đối với các logic này đặt ra cả giới hạn dươi (lower-bound) và giới hạn trên (upper bound) trên ngữ nghĩa 
dự định của dữ liệu được phát hành. Bằng cách tinh chỉnh các Ontology, các giới hạn này có thể di chuyển tạm thời gần nhau, do đó xác định được chính xác hết 
ngữ nghĩa dự định của dữ liệu, trong phạm vi yêu cần của cá trường hợp sử dụng.  

### **1.1.5 The Web Architecture of the Semantic Web** 
- Trên web truyền thống, nôi dung của nó được phân phố cả về vị trí lẫn người sở hữu: các trang web liên kết với nhau thường nằm ở những máy chủ khác nhau và các 
máy chủ này vị trí địa lý cũng khác nhau và được sở hữu bởi những nhóm khác nhau.  
- *Bất kỳ ai cũng có thể tham khảo trang web của bất kỳ ai mà không cần phải thương lượng trước về quyền hoặc yêu cầu về địa chỉ hoặc định danh phù hợp để sử dung. 
Một cơ chế tương tự hoạt động trong Semantic Web: Bên thứ nhất có thể phát hành tập dữ liệu trên web, bên thứ hai phát hành độc lập từ vựng của các term và bên 
thứ ba có thể quyết định chú thích đối tượng của bên thứ nhất bằng một thuật ngữ do bên thứ hai xuất bản mà không cần xin phép một trong hai bên và trên thực tế, 
một trong hai bên kia cũng không cần biết về điều đó. Chính sự phân tách này là bản chất của đặc tính giống như web của **Mạng ngữ nghĩa**.  

### **1.1.6 How to Get There from Here**
- Tất nhiên, cần có một số bước quan trọng để biến tầm nhìn và các quy tắc kiến trúc trên thành sự thật:  
	1. Chúng ta cần đồng thuận về cú pháp tiêu chuẩn để đại diện cho dữ liệu và siêu dữ liệu (metadata).  
	2. Chúng ta cần phải có đủ thỏa thuận về từ vựng siêu dữ liệu để chia sẻ ngữ nghĩa dự định của dữ liệu.  
	3. Chúng ta cần phát hành khối lượng lớn dữ liệu ở các định dạng của bước 1 và sử dụng từ vựng của bước 2.  
- Trong thập kỷ qua, tiến bộ đáng kể đã đạt được trên cả ba bước này: ngôn ngữ RDF, RDF Schema và OWL (và các biến thể của chúng) đều nhận được sự hỗ trợ chính thức 
của (W3C)[https://vi.wikipedia.org/wiki/W3C], nâng chúng lên thành các tiêu chuẩn thực tế trên web.  
- Hàng nghìn từ vựng được phát hành bằng các định dạng này và sự hội tụ của các từ vựng này bắt đầu xảy ra, vừa là kết quả của công nghệ lập ánh xạ bản thể học tự động (automated ontology mapping technology) 
vừa dưới áp lực của các nhu cầu xã hội và kinh tế. Và sự tăng trưởng của Linked Data Cloud đã dẫn đến hàng tỷ đối tượng và các mối quan hệ của chúng trở nên khả dụng một cách trực tuyến, bằng việc sử dụng các từ vựng và cú pháp được chia sẻ.  

## **1.2 Semantic Web Technologies**
