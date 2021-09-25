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
### **1.2.1 Explicit Metadata**
- Hiện tại, nội dung web được định dạng để phù hợp với người đọc, thay vì với những chương trình. Với con người, thông tin được trình một cách phù hợp, nhưng với máy thì tồn tại nhiều vướng mắc.    
```html
<h1>Trung tâm vật lý trị liệu Agilitas</h1>
Chào mừng đến với trung tâm vật lý trị liệu Agilitas
Bạn cảm thấy đau mỏi? Bạn bị chấn thương? Hãy để nhân viên của chúng tôi
Lisa Davenport, Kelly Townsend (Thư ký)
và Steve Matthews giúp đỡ bạn
<h2>Giờ tư vấn</h2>
Mon 11am - 7pm<br>
Tue 11am - 7pm<br>
Wed 3pm - 7pm<br>
Thu 11am - 7pm<br>
Fri 11am - 3pm<p>
Lưu lý rằng chúng tôi không chúng cấp các giờ tư vấn
trong các tuần của trò chơi
<a href=¨. . .¨>State of Origin</a>.
```
- Các tìm kiếm dựa trên từ khóa sẽ xác định những từ *vật lý trị liệu* và *giờ tư vấn*. Và một agent thông minh thậm trí xác định đươc cả nhân viên của trung tâm. 
Nhưng chúng sẽ gặp vấn đề khó khăn trong việc phân biệt các *nhà trị liệu* với *thư ký*, hay khó khăn trong việc tìm *giờ tư vấn* chính xác.  
- Cách tiếp cận của **Mạng ngữ nghĩa** để giải quyết vấn đề này không phải là sự phát triển của các tác nhân siêu thông minh, mà nó đề xuất tiếp cận vấn đề từ phía 
trang web. Nếu HTML được thay thế bằng các ngôn ngữ thích hợp hơn, thì các trang web có thể mang nội dung của chúng ở lớp bên ngoài. Ngoài việc chứa các thông tin 
về định dạng nhằm tạo ra tài liệu cho người đọc, chúng có thể chứa thông tin về nội dung của chúng.  
- Ở bước đầu tiên theo hướng đi này là **eXtensible Markup Language (XML)**, thứ cho phép ta xác định cấu trúc của thông tin trên các trang web. Ở ví dụ trên chúng 
ta sẽ có những thông tin như sau:  
```xml
<company>
	<treatmentOffered>Physiotherapy</treatmentOffered>
	<companyName>Agilitas Physiotherapy Centre</companyName>
	<staff>
		<therapist>Lisa Davenport</therapist>
		<therapist>Steve Matthews</therapist>
		<secretary>Kelly Townsend</secretary>
	</staff>
</company>
```  
- Cách biểu diễn này sẽ khiến cho máy dễ dàng xử lý hơn. Đặc biệt, nó hữu ích cho việc trao đổi thông tin trên web, một trong những ứng dụng nổi bật của XML.  
- Tuy nhiên, XML vẫn còn ở cấp độ cú pháp, vì nó mô tả cấu trúc của thông tin, nhưng không mô tả được *ý nghĩa* của nó. Ngôn ngữ cơ bản của **Web ngữ nghĩa** 
là RDF, là ngôn ngữ để đưa ra các phát biểu (statement) về các mẩu của thông tin. Trong ví dụ của chúng ta, gồm những phát biểu sau:  
	Company A offer physiotherapy.  
	The name of A is "Agitilitas Physiotherapy".  
	Lisa Davenport is a therapist.  
	Lisa Davenport works for A.  
	...  
- Với người đọc, sự khác biệt giữa cách biểu diễn XML và danh sách những phát biểu RDF có thể rất nhỏ, nhưng chúng hoàn toàn khác nhau về bản chất: XML mô tả 
cấu trúc còn RDF tạo ra những phát biểu về những mẩu thông tin.  
- Thuật ngữ *metadata* đề cập đến những thông tin như vậy: dữ liệu về dữ liệu. *Metadata* nắm bắt phần *ý nghĩa* của dữ liệu, và đó là thuật ngữ *ngữ nghĩa* 
trong **Web ngữ nghĩa**.  

### **1.2.2 Ontologies**
- Thuật ngữ *bản thể luận (ontology)* là tên của một lĩnh vực triết học, nghiên cứu về bản chất của sự tồn tại, nhánh của siêu hình học liên quan đến việc xác 
định những thứ thực sự tồn tại và cách mô tả chúng. Ví dụ, nhận xét rằng thế giới được tạo thành từ các đối tượng cụ thể có thể nhóm lại thành các lớp trừu 
tượng dựa trên các thuộc tính được chia sẻ.  
- *Bản thể luận* là một đặc tả rõ ràng và chính thức của một khái niệm hóa.  
- Nói chung, *bản thể luận* mô tả chính thức một miền (domain) của vấn đề đang nói đến. Thông thường, *bản thể luận* bao gồm một danh sách hữu hạn các thuật 
ngữ (term) và mối quan hệ giữa các thuật ngữ này. Các thuật ngữ biểu thị các khái niệm quan trọng (các lớp đối tượng) của miền.  
- Các *mối quan hệ (relationship)* thường bao gồm phân cấp của các lớp. Một hệ thống phân cấp chỉ định lớp C1 là một lớp con của một lớp C2 khác, thì mọi đối 
tượng trong C1 cũng nằm trong C2.  
- Ngoài các mối quan hệ lớp con, *bản thể luận* còn có thể bao gồm các thông tin như:  
	- Tính chất (ví dụ: X dạy Y);  
	- Các ràng buộc giá trị (ví dụ: chỉ giảng viên mới có thể dạy các khóa học);  
	- Các phát biểu rời rạc (disjointness statments) (ví dụ: giảng viên và nhân viên là rời rạc);  
	- Đặc tả mối quan hệ logic giữa các đối tượng (ví dụ: mọi khoa phải bao gồm ít nhất 10 giảng viên).  
- Trong ngữ cảnh web, *bản thể luận* cung cấp sự hiểu biết chung về một miền. Sự chia sẻ như vậy là cần thiết để vượt qua sự khác biệt về thuật ngữ. Mã zip của 
một ứng dụng (application) có thể giống với mã bưu điện của ứng dụng khác. Hay hai ứng dụng có thể sử dụng cùng một thuật ngữ nhưng khác nhau về ý nghĩa.  
- Những khác biệt như vậy có thể được khắc phục bằng cách ánh xạ thuật ngữ cụ thể tới *bản thể luận* dùng chung hoặc xác định ánh xạ trực tiếp giữa các *bản thể luận*.  
- *Bản thể luận* hữu dụng trong việc tổ chức và điều hướng của trang web.  
- *Bản thể luận* cũng hữu dụng trong việc cải thiện độ chính xác của web tìm kiếm. Các công cụ tìm kiếm có thể tìm kiếm các trang đề cập đến một khái niệm chính 
xác trong *bản thể luận* thay vì thu thập tất cả các trang trong đó với những từ khóa nhất định, mơ hồ. Bằng cách này, sự khác biệt thuật ngữ giữa các trang web và truy 
vấn được khắc phục.  
- Web tìm kiếm có thể khai thác các thông tin tổng quát hoặc chuyên môn. Nếu một truy vấn thất bại trong việc tìm tài liệu thích hợp, công cụ tìm kiếm có thể gợi ý người 
dùng một truy vấn tổng quát hơn. Thậm chí nó có thể chủ động chạy các truy vấn tổng quát để giảm thời gian tiếp nhận trong trường hợp người dùng chấp nhận một đề xuất. 
Hoặc nếu quá nhiều câu trả lời được truy xuất, công cụ có thể gợi ý người dùng một số chuyên môn.  
- Các ngôn ngữ quan trọng của *bản thể luận* là:  
	- Lược đồ RDF là một ngôn ngữ mô tả từ vựng dùng để mô tả các thuộc tính và lớp của tài nguyên RDF, với ngữ nghĩa để phân cấp tổng quát các thuộc tính và lớp đó. 
Ngoài ra, miền và phạm vi thuộc tính có thể được xác định.  
	- OWL là một ngôn ngữ mô tả từ vựng phong phú hơn để mô tả các thuộc tính và lớp, chẳng hạn như quan hệ giữa các lớp (ví dụ: tính rời rạc), số lượng (ví dụ: chính xác một), 
đồng cấp, cách nhập phong phú hơn của các thuộc tính, đặc điểm của các thuộc tính (ví dụ: đối xứng), và các lớp được liệt kê.  

### **1.2.3 Logic**


