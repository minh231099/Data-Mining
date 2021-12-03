# **Chapter 2**
# **Describing Web Resources**
# **RDF**

# **Table of contents**
- [**2.1 Giới thiệu**](#21-giới-thiệu)  
- [**2.2 RDF: Mô hình dữ liệu**](#22-rdf-mô-hình-dữ-liệu)  
	- **2.2.1 Tài nguyên**  
	- **2.2.2 Thuộc tính**  
	- **2.2.3 Phát biểu**  
	- **2.2.4 Đồ thị**  
	- **2.2.5 Trỏ tới những Phát biểu và Đồ Thị**  
	- **2.2.6 Đối phó với những dự đoán phong phú hơn**  
- [**2.3 Cú pháp RDF**](#23-cú-pháp-rdf)  

---
## **2.1 Giới thiệu**
- HTML là một ngôn ngữ tiêu chuẩn dùng để xây dựng nên các trang web. Nó cho phép chúng ta xuất bản tài liệu và đảm bảo rằng tài liệu sẽ được hiển thị chính xác trên bất kỳ trình duyệt web nào.  
- Gồm có ba phần hợp thành HTML (và bất kỳ ngôn ngữ chuyển đổi) là: 
	- Cú pháp (syntax): Chỉ cho chúng ta cách để biểu diễn dữ liệu;  
	- Mô hình dữ liệu (data model): Chỉ cho chúng ta về cấu trúc hoặc cách tổ chức của dữ liệu;  
  	- Ngữ nghĩa (semantic): Chỉ cho chúng ta cách thông dịch dữ liệu đó.  

```html
<html>
	<head>
		<title>Apartments for Rent</title>
	</head>
	<body>
		<ol>
			<li> Studio apartment on Florida Ave.
			<li> 3 bedroom Apartment on Baron Way
		</ol>
	</body>
</html>
```  

- Cú pháp của HTML là văn bản gồm các thẻ được biểu diễn bằng các dấu ngoặc nhọn.  
- Mô hình dữ liệu của HTML hay Mô hình Đối tượng Tài Liệu (Document Object Model), xác định cách tổ chức của các thành phần được định nghĩa bằng các thẻ thành một cấu trúc cây phân cấp.  
- Ngữ nghĩa của HTML cho ta biết về cách trình duyệt thông dịch trang web. Ví dụ, trình duyệt hiển thị nội dung phần thân của trang web trong cửa sổ trình duyệt và phần tử `<ol>` sẽ được hiển thị dưới dạng danh sách có thứ tự.  
- Cú pháp, mô hình dữ liệu và ngữ nghĩa đều được xác định trong tiêu chuẩn HTML.  
- HTML được thiết kế để truyền đạt thông tin về cấu trúc của tài liệu đến người dùng. Nhưng **Mạng ngữ nghĩa** cần một cái gì đó tốt hơn. Ta cần một mô hình dữ liệu có thể sử dụng bởi nhiều ứng dụng hơn, không chỉ để mô tả tài liệu cho con người và con diễn tả thông tin dành riêng cho ứng dụng.  
- Mô hình dữ liệu này cần trở nên không phụ thuộc vào miền để các ứng dụng từ bất động sản đến mạng xã hội đều có thể tận dụng nó. Ngoài ra, một mô hình dữ liệu linh hoạt, chúng ta cần một cơ chế để gán ngữ nghĩa cho thông tin được biểu diễn bằng cách sử dụng mô hình dữ liệu này. Nó sẽ cho phép người dùng mô tả cách ứng dụng giải nghĩa từ "bạn bè" trong mạng xã hội và "thành phố" trong một mô tả địa lý.  
- Cuối cùng chúng ta cần một cách để có thể thể hiện tất của những thông tin này - một cú pháp.  
- RDF (Resource Description Framework) cung cấp đúng mô hình linh hoạt như vậy. Nền móng của nó là thực thể-thuộc tính-giá trị, gọi là phát biểu (statement). 
Ví dụ như:
	- “The Baron Way Apartment is an Apartment” 
	- “The Baron Way Apartment is part of The Baron Way Building” 
	- “The Baron Way Building is located in Amsterdam”
- Vì RDF không dành riêng cho bất kỳ miền hay mục đích sử dụng nào, nó cần thiết để người dùng tự định nghĩa thuật ngữ họ sử dụng trong các phát biểu này.  
- Để làm được điều này, họ sử dụng RDF Schema (RDFS), nó cho phép người dùng định nghĩa chính xác cách từ vựng (hay là thuật ngữ) của họ được diễn giải như thế nào.  
- Kết hợp lại, các công nghệ này xác định thành phần của một ngôn ngữ chuẩn để trao đổi dữ liệu tùy ý giữa các máy:
	- RDF - Mô hình dữ liệu;  
	- RDFS - Ngữ nghĩa;  
	- Turtle/ RDFa/ RDF-XML - Cú pháp.  

## **2.2 RDF: Mô hình dữ liệu**
### **2.2.1 Tài nguyên**
- Chúng ta có thể nghĩ rằng tài nguyên chính là đối tượng, thứ mà chúng ta muốn nhắc tới. Tài nguyên có thể là địa điểm, con người, truy xuất tìm kiếm, ... .  
- Mỗi một tài nguyên sẽ có một URI. Một URI có thể là URL (Uniform Resource Locator, hoặc địa chỉ web) hoặc một các gì đấy dùng để định danh. 
- URI cung cấp một cơ chế để xác định rõ ràng "thứ" mà chúng ta muốn nói đến. Vì vậy, khi ta nói swimming pool, chung ta sẽ sử dụng URI gán cho swimming pool và nó sẽ không bị nhầm lẫn với billiards (pool) or a group of people (the pool of programmers). Đây gọi là vấn đề đồng âm.   
- Việc sử dụng URI không nhất cần cho phép truy chấp vào tài nguyên. Sử dụng các URL có thể tham chiếu được cho mã định danh tài nguyên được coi là một phương pháp hay. Nó cho phép người dùng truy xuất chính tài nguyên (trong trường hợp là h ình ảnh) hoặc mô tả thêm về tài nguyên (trong trường hợp là người).  
- Việc sử dụng URI là một trong những quyết định thiết kế quan trọng đằng sau RDF. Nó cho phép kế hoạch đặt tên một cách toàn cầu, và mỗi tên là duy nhất trên toàn thế giới diễn ra.  
- Việc sử dụng một kế hoạch như vậy giảm thiểu đáng kể về vấn đề đồng âm cản trở việc biểu diễn dữ liệu phân tán cho đến nay.  

### **2.2.2 Thuộc tính**
- Thuộc tính là một loại đặc biệt của tài nguyên; chúng mô tả mối quan hệ giữa các tài nguyên khác - ví dụ như: "bạn của", "được viết bởi" và "đặt tại".  
- Như tất cả các tài nguyên, thuộc tính cũng được định danh bằng URI.  
- Chúng ta có thể tham chiếu các URL thuộc tính để tìm các mô tả của chúng.  

### **2.2.3 Phát biểu**
- Phát biểu xác nhận những thuộc tính của tài nguyên.  
- Một phát triểu là một bộ ba thực thể-thuộc tính-giá trị gồm một tài nguyên, một thuộc tính và một giá trị.  
- Giá trị có thể là một tài nguyên hoặc là một trực nghĩa (nghĩa đen - literals).  
- Trực nghĩa là atomic value - ví dụ như: số, chuỗi hoặc ngày tháng.  
- Chúng ta thường sử dụng từ chủ thể (subject) để chỉ thực thể (entity) trong một phát biểu và đối tượng để chỉ giá trị của nó.  
Ví dụ: Có một phát biểu: "Baron Way Buildings is located in Amsterdam"  
Ta sẽ viết thành:  
```
<http://www.semanticwebprimer.org/ontology/apartments.ttl#BaronWayBuilding>
<http://dbpedia.org/ontology/location>
<http://dbpedia.org/resource/Amsterdam>
```  

### **2.2.4 Đồ thị**
- Chúng ta cũng có thể viết cùng một phiểu mẫu dưới dạng đồ thị.  
![Đồ thị ví dụ 1](./pic/RDF_graph_1.png)

- Những nốt được gán nhãn được kết nối bởi các đường được gán nhãn. Các đường có hướng từ chủ thể phát biểu đến đối tượng phát biểu, với nhãn trên đường là thuộc tính của phát biểu.  
- Nhãn trên các nốt là định danh của chủ thể và đối tượng.  
- Đối tượng của phát biểu này có thể là chủ thể của phát biểu khác ("Amsterdam is a city").  
- Biểu diễn đồ thị nhàm làm nổi bật rằng RDF là một mô hình dữ liệu có trọng tâm là đồ thị.  
- Biểu đồ này có thể tạo ra theo kiểu phân tán bởi nhiều người tham gia khác nhau chỉ bằng sử dụng các URL giống nhau. Điều này cho phép chúng ta tạo ra *Web of Data* cho phép tri thức được tái sử dụng - ví dụ: nếu ta tìm thấy RDF trên trang web mô tả về Amsterdam, ta có thể tái sử dụng thông tin đó bằng việc sử dụng URL đó. Thật vậy, có một tập hợp các phương pháp tối ưu nhất, gọi là *nguyên tắc Dữ Liệu liên kết (Linked Data principles)*, nó khuyến khích ta tái sử dụng và cung cấp thông tin khả dụng để hỗ trợ tạo ra đồ thị toàn cầu.  
	1. Sử dụng URI làm tên cho mọi thứ.  
	2. Sử dụng những HTTP URI để mọi người có thể tra cứu những cái tên đó.  
	3. Khi ai đó tra cứu một URL, cung cấp những thông tin hữu ích, sử dụng những tiêu chuẩn (RDF).  
	4. Bao gồm liên kết tới các URI khác để họ có thể khám phá nhiều thứ hơn.  
- Khi mô hình dữ liệu RDF không yêu cầu ta tuân theo những tiêu chuẩn này, nhưng nếu đi theo tiêu chuẩn, ta có thể tận dụng tri thức được đóng góp từ người khác.  

### **2.2.5 Trỏ tới những Phát biểu và Đồ thị** 
- Đôi khi rất hữu ích khi có thể trỏ tới những phát biểu cụ thể và những phần của đồ thị, chẳng hạn như khi ấn định mức độ tin tưởng vào một phát biểu hoặc xác định nguồn gốc của phát biểu. Ví dụ như: ta muốn nói rằng phát biểu về vị trí của Baron Way Building được tạo ra bởi một người tên Frank. RDF cung cấp hai cơ chế để làm điều này.  
- Cái thứ nhất được gọi là *reification*. Ý tưởng chính đằng sau reification là đưa vào một đối tượng bổ trợ cẳng hạn như LocationStatement và liên hệ nó với từng phần trong ba phần của phát biểu ban đầu thông qua các thuộc tính chủ thể, vị từ và đối tượng.  
![Đồ thị *reification*](./pic/reification_graph_1.png)  
- Trong ví dụ trước, chủ thể của *LocationStatement* sẽ là *BaronWayBuilding*, vị từ sẽ là *location* và đối tượng sẽ là Amsterdam. Sau đó, ta có thể dẫn tới phát biểu trong chủ thể của bộ ba khác điều đó xác định người tạo ra (creator).  
- Việc tiếp cận này khá rườm rà này là cần thiết vì bộ ba chỉ nằm trong RDF; vậy nên ta không thể thêm một định danh trực tiếp vào một bộ ba. Do chi phí sửa đổi lớn, trong phiên bản mới hơn của RDF, khái niệm về các đồ thị được đặt tên đã được đưa ra. Ở đây, một số nhận dạng rõ ràng (một URL) được cấp cho một phát biểu hoặc một tập hợp những phát biểu. Mã định danh này sau đó có thể được tham chiếu trong bộ ba thông thường. Đây là một cơ chế đơn giản hơn để xác định các phát biểu cũng như đồ thị. Nói một cách đơn giản, một đồ thị được đặt tên cho phép ta khoanh tròn một tập hợp các phát biểu RDF và cung cấp cho các phát biểu này một mã định danh.  

### **2.2.6 Đối phó với những dự đoán phong phú hơn**
- Ta có thể nghĩ rằng bộ ba *(x, P, y)* là một biểu thức logic *P(x, y)*, khi đó vị từ nhị phân (binary predicate) P liên hệ đối tượng x và đối tượng y. Thực tế, RDF chỉ cung chấp vị từ nhị phân (các thuộc tính). Tuy nhiên, vài trường hợp ta có thể cần vị từ có nhiều hơn 2 đối số. May thay, các vị từ như vậy có thể mô phỏng bởi một số vị từ nhị phân.  
Ví dụ như sau: broker(X, Y, Z) nghĩa là "X is broker in home sale between seller Y and purchaser Z.  
Bây giờ ta cần thêm một tài nguyên phụ trợ mới *home-sale* và một vị từ nhị phân *broker*, *seller* và *purchaser*. Sau đó ta biểu diễn broker(X, Y, Z) như sau:  
broker(home-sale, X)  
seller(home-sale, Y)
purchaser(home-sale, Z)  

- Mặc dù vị từ ba đối số sẽ được viết ngắn gọn hơn, nhưng việc dùng các vị từ nhị phân sẽ đơn giản hóa mô hình dữ liệu tổng thể.  

## **2.3 Cú pháp RDF**
### **2.3.1 Turtle**
- Terse RDF Triple Language (Turtle) là một cú pháp dựa trên dạng văn bản cho RDF.  
- File Turtle có đuôi là `.ttl`.  
Ví dụ:  
```Turtle
<http://www.semanticwebprimer.org/ontology/apartments.ttl#BaronWayBuilding>
<http://dbpedia.org/ontology/location>
<http://dbpedia.org/resource/Amsterdam>.
```  
- Các URL được đặt trong dấu ngoặc nhọn. Chủ thể, thuộc tính và đối tượng của phát biểu xuất hiện theo thứ tự, theo sau là một dấu chấm.  
- Chúng ta có thể mô tả toàn bộ đồ thị RDF chỉ bằng cách này.  
```Turtle
<http://www.semanticwebprimer.org/ontology/apartments.ttl#>
<http://www.semanticwebprimer.org/ontology/apartments.ttl#isPartOf>
<http://www.semanticwebprimer.org/ontology/apartments.ttl#BaronWayBuilding>.
<http://www.semanticwebprimer.org/ontology/apartments.ttl#BaronWayBuilding>
<http://dbpedia.org/ontology/location>
<http://dbpedia.org/resource/Amsterdam>.
```  

#### **2.3.1.1 Trực nghĩa**
- Chúng ta đã định nghĩa rằng phát biểu là thứ liên kết những tài nguyên lại với nhau. Như đã nói ở trên phát biểu còn có thể bao gồm cả trực nghĩa, nó là một atomic value trong RDF.  
- Trong Turtle, ta biểu diễn trực nghĩa trong cặp nháy kép và kèm theo đó là kiểu dữ liệu.  
- Kiểu dữ liệu cho chúng ta biết liệu chúng ta có nên diễn giải một giá trị với string, một ngày, số nguyên hay một kiểu dữ liệu khác.  
- Các kiểu dữ liệu lại được biểu diễn dưới dạng URL. Nên sử dụng những kiểu dữ liệu được định nghĩa bằng Lược đồ XML, khi này các giá trị sẽ tuân theo định nghĩa Lược đồ XML.  
- Nếu không có kiểu dữ liệu được khai báo phía sau một trực nghĩa, nó sẽ được coi là một string.  
```Turtle
string - "Baron Way"
integers - "1"^^<http://www.w3.org/2001/XMLSchema#integer>
decimals - "1.23" <http://www.w3.org/2001/XMLSchema#decimal>
dates - "1982-08-30"^^<http://www.w3.org/2001/XMLSchema#date>
time - "11:24:00"^^<http://www.w3.org/2001/XMLSchema#time>
date with a time - "1982-08-30T11:24:00"^^<http://www.w3.org/2001/XMLSchema#dateTime>
```  
- Giả sử nếu ta muốn thêm vào đồ thị rằng Căn hộ Baron Way có ba phòng ngủ. Ta sẽ thêm một phát biểu trong Turtle vào đồ thị như sau:  
```Turtle
<http://www.semanticwebprimer.org/ontology/apartments.ttl#BaronWayApartment>
<http://www.semanticwebprimer.org/ontology/apartments.ttl#hasNumberOfBedrooms>
"3"^^<http://www.w3.org/2001/XMLSchema#integer>.

<http://www.semanticwebprimer.org/ontology/apartments.ttl#BaronWayApartment>
<http://www.semanticwebprimer.org/ontology/apartments.ttl#isPartOf>
<http://www.semanticwebprimer.org/ontology/apartments.ttl#BaronWayBuilding>.

<http://www.semanticwebprimer.org/ontology/apartments.ttl#BaronWayBuilding>
<http://dbpedia.org/ontology/location>
<http://dbpedia.org/resource/Amsterdam>.
```  

