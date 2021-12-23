# Chapter 3
# Truy Vấn Mạng Ngữ Nghĩa (Querying the Semantic Web)

**Table of Content**  
- [**3.1 Cơ sở hạ tầng SPARQL**](#31-cơ-sở-hạ-tầng-sparql)  
- [**3.2 Khái niệm cơ bản: Mẫu phù hợp**](#32-khái-niệm-cơ-bản-mẫu-phù-hợp)  
- [**3.3 Bộ lọc**](#33-bộ-lọc)  
- [**3.4 Các cấu trúc để xử lý với một Thế Giới Mở**](#34-các-cấu-trúc-để-xử-lý-với-một-thế-giới-mở)  
- [**3.5 Tổ chức các bộ kết quả**](#35-tổ-chức-các-bộ-kết-quả)  
- [**3.6 Các hình thức truy vấn khác của SPARQL**](#36-các-hình-thức-truy-vấn-khác-của-sparql)  
- [**3.7 Lược đồ truy vấn**](#37-lược-đồ-truy-vấn)  
- [**3.8 Thêm một thông tin bằng SPARQL Update**](#38-thêm-một-thông-tin-bằng-SPARQL-update)  
- [**3.9 Làm theo nguyên tắc mũi của bạn**](#39-làm-theo-nguyên-tắc-mũi-của-bạn)  
- [**3.10 Tổng kết**](#310-tổng-kết)  
---  

## 3.1 Cơ sở hạ tầng SPARQL
Để thực hiện một truy vấn SPARQL, ta cần phần mềm để thực thi truy vấn. Phần mềm phổ biến nhất để thực hiện điều này được gọi là một *triple store*. Về cơ bản, một triple store là một cơ sở dữ liệu cho RDF. Có thể tải một số triple store một cách trực tuyến. Với các thông số kỹ thuật cho SPARQL một triple store được đề nghị là Graph Store.  
Trước khi có thể truy vấn một triple store, nó cần phải được nằm trong RDF. Đa số các triple store đều cung cấp tùy chọn tải lên hàng loạt. Ngoài ra còn có một cơ chế được gọi là SPARQL Update, cung cấp một loạt các lựa chọn cho việc chèn và tải cũng như xóa RDF trong một triple store. SPARQL sẽ được bàn luận sau.  
Một khi dữ liệu được tải lên một triple store, nó có thể được truy vấn bằng việc gửi các truy vấn SPARQL sử dụng giao thức SPARQL. Mỗi triple store cung cấp thứ gọi là *điểm cuối (endpoint)*, nơi các truy vấn SPARQL được gửi đi. Một điểm quan trọng là những client gửi truy vấn tới một điểm cuối sử dụng giao thức HTTP. Vậy nên ta có thể đưa ra một truy vấn SPARQL tới điểm cuối bằng việc nhập nó vào trong thanh URL của trình duyệt! Tuy nhiên, chúng ta nên sử dụng một ứng dụng được thiết kế đặc biệt cho SPARQL.  
Vì SPARQL sử dụng các công nghệ web tiêu chuẩn, bạn sẽ tìm thấy nhiều điểm cuối SPARQL trên web. Những điểm cuối này cung cấp quyền truy cập vào lượng lớn dữ liệu. Ví dụ, *dpedia.org/sparql* cung cấp một điểm cuối truy vấn qua để truy vấn qua biểu diễn RDF của Wikipedia. Có thể tìm thấy danh sách các điểm cuối SPARQL tại *CKAN.org*.  
Khi đã có các cơ sở hạ tầng này chúng ta có thể bắt đầu viết truy vấn SPARQL.  

## 3.2 Khái niệm cơ bản: Mẫu phù hợp
Ở chương trước, RDF mô tả về căn hộ Baron Way và vị trí của nó:  
```Turtle
@prefix swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
@prefix dbpedia: <http://dbpedia.org/resource/>.
@prefix dbpedia-owl: <http://dbpedia.org/ontology/>.

swp:BaronWayApartment swp:hasNumberOfBedrooms 3;
		swp:isPartOf swp:BaronWayBuilding.
swp:BaronWayBuilding dbpedia-owl:location dbpedia:Amsterdam,
					dbpedia:Netherlands.
```  

Ta sẽ đưa ra một truy vấn về dữ liệu này. Ví dụ: Tìm vị trí của tòa nhà. Ta sẽ xây dựng truy vấn này như sau. Ta sẽ muốn ánh xạ những bộ ba sau:  
&emsp; swp:BaronWayBuilding dbpedia-owl:location dbpedia:Amsterdam.  
Trong SPARQL, ta có thể thay thế bất kỳ một thành một của bộ ba với một biến. Các biến được ký hiệu bằng một dấu ? ở đầu. Để đưa ra một biến cho vị trí, ta sẽ viết như sau:  
&emsp; swp:BaronWayBuilding dbpedia-owl:location ?location.  
Triple store sẽ tiếp nhận *mẫu đồ thị (graph pattern)* này và cố gắng tìm kiếm tập hợp các bộ ba ứng với mẫu. Do đó, chạy mẫu này trên RDF ban đầu, một triple store sẽ trả về dbpedia:Amsterdam và dbpedia:Netherlands. Về cơ bản, nó tìm tất cả bộ ba mà swp:BaronWayBuilding là đứng ở vị trí chủ thể và dbpedia-owl:location là vị từ.  
Để biến nó thành một truy vấn SPARQL hoàn thiện, cần phải thực hiện một số bổ sung. Đầu tiên, tất cả các tiền tố (prefix) cần được định nghĩa. Ta cũng cần nói với triple store rằng ta quan tâm đến kết quả cho một biến cụ thể. Do đó, một truy vấn hoàn thiện cho truy vấn phía trên như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?location
WHERE {
	swp:BaronWayBuilding dbpedia-owl:location ?location.
}
```  
Tương tự Turtle, từ khóa PREFIX biểu thị các chữ viết tắt cho các URL. Từ khóa SELECT chỉ ra những biến được quan tâm. Mẫu đồ thị được xuất hiện trong cặp dấu ngoặc nhọn ({}) sau từ khóa WHERE. Kết quả của truy vấn sẽ được trả về trong một tập hợp các ánh xạ được gọi là các *liên kết* biểu thị những phần từ nào tương ứng với biến nào. Mỗi hàng trong bảng là một kết quả hay liên kết. Vậy kết quả của truy vấn này sẽ là:  

|?location|  
|:-------:|  
|http://dbpedia.org/resources/Amsterdam.|  
|http://dbpedia.org/resources/Netherlands.|  

Toàn bộ cơ sở của SPARQL là khá niệm đơn giản về việc cố gắng tìm tập hợp các bộ ba phù hợp với mẫu đồ thị được cho. SPARQL cung cấp chức năng tăng cương để chỉ định các mẫu phức tạp hơn và cung cấp kết quả ở các định dạng khác nhau; nhưng không quan tâm mẫu phức tạp như nào, quy trình tương tự vẫn được áp dụng. Một ví dụ khác: tìm vị trí của Baron Way Apartment. Truy vấn cho ví dụ này như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?location
WHERE {
	swp:BaronWayApartment swp:isPartOf ?building.
	?building dbpedia-owl:location ?location.
}
```  
Ta đã mở rộng mẫu đồ thì. Có vài điều cần lưu ý về truy vấn này: Đầu tiên, các biến có thể xuất hiện ở bất kỳ vị trí nào trong truy vấn SPARQL. Thứ hai, truy vấn sử dụng lại biến ?building. Bằng cách này, triple store biết rằng nó cần tìm các bộ ba mà đối tượng của phát biểu đầu tiên chính là chủ thể của phát biểu thứ hai.  
  
Chúng ta không bị giới hạn bởi một biến duy nhất. Chúng ta có thể muốn tìm kiếm tất cả thông tin về Baron Way Apartment trong triple store. Ta có thể sử dụng truy vấn sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?p ?o
WHERE {
	swp:BaronWayApartment ?p ?o.
}
```  
Nó sẽ trả về kết quả sau:  
|?p |?o |  
|:-:|:-:|  
|swp:hasNumberOfBedrooms|3|  
|swp:isPartOf|swp:BaronWayBuilding|  

Một lần nữa mỗi hàng trong bảng sẽ là một kết quả tương ứng với mẫu đồ thị. Với tập dữ liệu khá nhỏ của ta, tất cả câu trả lời đều có thể được trả về dễ dàng. Tuy nhiên, ở bộ dữ liệu lớn hơn, ta không thể biết được có bao nhiêu kết quả hoặc truy vấn của ta có thể trả về cả bộ dữ liệu. Thật vậy, có thể dễ dàng viết truy vấn trả về một triệu bộ ba. Do đó, bạn nên hạn chế số lượng câu trả lời mà truy vấn trả về, đặc biệt là khi sử dụng điểm cuối công khai (public endpoint). Nó có thể dễ dàng sử lý bằng việc sử dụng từ khóa LIMIT.  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?p ?o
WHERE {
	swp:BaronWayApartment ?p ?o.
}
LIMIT 10
```  

Trước đây ta đã thấy ta có thể ánh xạ các mẫu đơn hoặc chuỗi của các mẫu ba. SPARQL cung cấp một cách diễn đạt gắn gọn các chuỗi thuộc tính, được gọi là *đường dẫn thuộc tính (property paths)*. Với ví dụ sau: Tìm tất cả các căn hộ mà là một phần của tòa nhà đặt tại Amsterdam.  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?apartment
WHERE {
	?apartment swp:isPartOf ?building.
	?building dbpedia-owl:location dbpedia:Amsterdam.
}
```  
hoặc ta có thể biểu diễn như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?apartment
WHERE {
	?apartment swp:isPartOf ?building/dbpedia-owl:location dbpedia:Amsterdam.
}
```  
Có một vài đường dẫn thuộc tính khác có thể được sử dụng để hỗ trợ việc biểu diễn đường dẫn dài hoặc ngẫu nhiên trong các truy vấn. Nhưng cấu trúc này sẽ được làm nổi bật trong chương này. Tuy nhiên, khi ta viết SPARQL phức tạp hơn những lối tắt thuộc tính sẽ trở nên hữu ích hơn.  
Ta có thể đạt được nhiều thứ chỉ thông qua các mẫu đồ thị phù hợp. Tuy nhiên, đôi khi ta muốn đặt những ràng buộc phức tạp hơn đối với kết quả các truy vấn. Phần tiếp theo sẽ thảo luận về các thể hiện những ràng buộc đó bằng cách sử dụng các bộ lọc (filter).  

## 3.3 Bộ lọc
Tiếp tục với ví dụ về những căn hộ, hãy cùng tìm tất cả các căn hộ có 3 phòng ngủ. Đến nay, ta đã thấy rất nhiều ví dụ mà ta phải truy vấn chỉ sử dụng tài nguyên trong mẫu đồ thị mà không phải là trực nghĩa. Tuy nhiên trực nghĩa có cả được đưa vào trong các mẫu đồ thị một cách đơn giản. Truy vấn SPARQL như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?apartment
WHERE {
	?apartment swp:hasNumberOfBedrooms 3.
}

```  
Giống như Turtle, SPARQL cho phép viết tắt một số trực nghĩa cơ bản. Trong ví dụ này, *3* là viết tắt của *"3"xsd:interger*. Các cú pháp khác trong SPARQL cũng tương tự như Turtle.  
Tuy nhiên, truy vấn này không thực tế. Có thể ta muốn tìm tất cả những căn hộ với nhiều hoặc ít phòng ngủ hơn một số nhất định. Ta có thể đặt câu hỏi này cho SPARQL bằng việc sử dụng từ khóa FILTER:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?apartment
WHERE {
?apartment swp:hasNumberOfBedrooms ?bedrooms.
	FILTER (?bedrooms > 2).
}
```  
Kết quả:  
|?apartment|  
|:--------:|  
|swp:BaronWayApartment|  

Ít hơn, nhỏ hơn và bằng đều được hỗ trợ cho các kiểu dữ liệu số (ví dụ như integer, decimal) và cả date/time/ SPARQL cũng cho phép lọc trên các chuỗi (string).  
Ví dụ, giả sử bộ dữ liệu của ta có chứa bộ ba:  
&emsp; swp:BaronWayApartment swp:address "4 Baron Way Circle".  
Chúng ta sẽ muốn tìm kiếm tất cả tài nguyên có chứa "4 Baron Way" trong địa chỉ của chúng. Điều này có thể xử lý bằng việc sử dụng biểu thức chính quy có trong SPARQL. Biểu thức chính quy là một cách hiệu quả để biểu diễn các tìm kiếm chuỗi. Biểu thức chính quy cho việc tìm kiếm chuỗi "4 Baron Way" nằm ở đầu của một chuỗi khác là *"^4 Baron Way". Nó sẽ được biểu diễn như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?apartment
WHERE {
	?apartment swp:address ?address.
	FILTER regex(?address, "^4 Baron Way").
}
```  

Tại đây, sau từ khóa FILTER, một tên hàm lọc cụ thể được đưa ra, *regex*. Các tham số nằm trong cặp dấu ngoặc đơn sau đó. Có nhiều loại bộ lọc trong SPARQL có tác dụng trong các trường hợp khác nhau. Tuy nhiên, bộ lọc số và chuỗi là được sử dụng thường xuyên nhất. Một hàm cuối thường được sử dụng là hàm *str*. Nó sẽ chuyển tài nguyên và trực nghĩa về dạng chuỗi để có thể được sử dụng trong *regex*. Ví dụ, ta muốn tìm kiếm Baron trong URL của những tài nguyên thay vì sử dụng nhãn như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?apartment ?address
WHERE {
	?apartment swp:address ?address.
	FILTER regex(str(?apartment), "Baron").
}
```  
Bộ lọc cung cấp một cơ chế để đạt được sự linh hoạt. SPARQL đưa ra nhiều cấu trúc hơn để xử lý thông tin thường không nhất quán và đa dạng được tìm thấy trong Mạng Ngữ Nghĩa.  

## 3.4 Các cấu trúc để xử lý với một Thế Giới Mở
Không như những cơ sở dữ liệu truyền thống, không phải tất cả tài nguyên trên Mạng Ngữ Nghĩa sẽ được mô tả sử dụng cùng một lược đồ hoặc tất cả đều có chung toàn bộ thuộc tính. Điều này được gọi là giả thiết thế giới mở. Ví dụ, vài căn hộ có thể được mô tả tốt hơn những cái khác. Xa hơn nữa, chúng có thể được mô tả bằng những từ vựng khác nhau. Với vị dụ dưới đây bằng RDF:  
```RDF
@prefix swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
@prefix dbpedia: <http://dbpedia.org/resource/>.
@prefix dbpedia-owl: <http://dbpedia.org/ontology/>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.

swp:BaronWayApartment swp:hasNumberOfBedrooms 3.
swp:BaronWayApartment dbpedia-owl:location dbpedia:Amsterdam.
swp:BaronWayApartment refs:label "Baron Way Apartment for Rent".

swp:FloridaAveStudio swp:hasNumberOfBedrooms 1.
swp:FloridaAveStudio dbpedia-owl:locationCity dbpedia:Amsterdam.
```  
Trong trường hợp này, Florida Ave studio không có nhãn (label) và vị trí của nó được mô tả bằng vị từ *dbpedia-owl:locationCity* chứ không phải *dbpedia-owl:location*. Kể cả với mâu thuẫn như vậy, ta vẫn muốn truy vấn tới dữ liệu và tìm những căn hộ nằm tại Amsterdam và trả về nhãn của nó nếu có. SPARQL cung cấp hai cấu trúc để diễn tả một truy vấn như vậy.  
Ví dụ:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX geo: <http://www.geonames.org/ontology#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?apartment ?label
WHERE {
	{?apartment dbpedia-owl:location dbpedia:Amsterdam.}
	UNION
	{?apartment dbpedia-owl:locationCity dbpedia:Amsterdam.}
	OPTIONAL
	{?apartment rdfs:label ?label.}
}
```  
Kết quả của truy vấn là:  
|?apartment|?label|  
|:--------:|:----:|  
|swp:BaronWayApartment|Baron Way Apartment for Rent|  
|swp: FloridaAveStudio||  

Từ khóa UNION cho biết rằng kết quả trả về sẽ tương ứng với một hoặc cả hai mẫu đồ thị. Từ khóa OPTIONAL cho biết rằng triple store sẽ trả về kết quả cho mẫu đồ thị cụ thể nếu có. Điều đó có nghĩa là mẫu truy vấn không cần nhất thiết phải được thỏa mãn để truy vấn trả về. Do đó, trường hợp này, nếu không có OPTIONAL, *swp: FloridaAveStudio* sẽ không được trả về trong kết quả truy vấn.  
Tương tự, các đường dẫn thuộc tính cũng có thể sử dụng để tạo ra một truy vấn SPARQL ngắn gọn hơn. Sử dụng toán tử |, ta có thể biểu diễn một hoặc nhiều khả năng. Do đó, truy vấn SPARQL có thể được viết lại như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.
SELECT ?apartment ?label
WHERE {
	{?apartment dbpedia-owl:location | dbpedia-owl:locationCity dbpedia:Amsterdam.}
	OPTIONAL
	{?apartment rdfs:label ?label.}
}
```  
Đó là vài ví dụ về cách SPARQL được thiết kế để dễ dàng truy vấn tri thức tới từ nhiều nguồn khác nhau.  

## 3.5 Tổ chức các bộ kết quả
Thông thường, ta sẽ muốn kết quả của các truy vấn của mình được trả về theo một cách cụ thể như là được nhóm lại, được đếm hoặc theo một thứ tự. SPARQL hộ sợ một vài hàm để giúp ta tổ chức bộ kết quả. Ta đã thấy được cách để hạn chế số lượng kết quả khi sử dụng từ khóa LIMIT. Ta cũng có thể triệt tiêu những kết quả trùng lặp bằng việc sử dụng từ khóa DISTINCT bằng việc đặt nó sau từ khóa SELECT (ví dụ SELECT DISTINCT ?name WHERE). Điều này sẽ đảm bảo rằng chỉ các liên kết biến duy nhất (unique variable binding) được trả về.  
SPARQL cũng cho phép sắp xếp một bộ kết quả trả về bằng việc sử dụng ORDER BY. Ví dụ ta có thể hỏi rằng các căn hộ được sắp xếp theo số lượng phòng ngủ.  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT ?apartment ?bedrooms
WHERE {
	?apartment swp:hasNumberOfBedrooms ?bedrooms.
}
ORDER BY DESC(?bedrooms)
```  
Kết quả trả về sẽ là:  
|?apartment|?bedrooms|  
|:--------:|:-------:|  
|swp:BaronWayApartment|3|  
|swp:FloridaAveStudio|1|  

DESC nghĩa là giảm dần, ngược lại, ASC sẽ là tăng dần. Ngoài ra, việc sắp xếp một chuỗi hay url cũng được thực hiện theo thứ tự trong bảng chữ cái.  

Ta cũng có thể thu thập các bộ kết qảu cùng nhau sử dụng *hàm tổng hợp (aggregate function)*. Đặc biệt, ta có thể đếm số lượng kết cả (COUNT), tính tổng của chúng (SUM), và tính giá trị nhỏ nhất, giá trị lớn nhất và trung bình (MIN, MAX, AVG). Dưới đây là ví dụ về tính giá trị trung bình của số lượng phòng ngủ trong bộ dữ liệu:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

SELECT (AVG(?bedrooms) AS ?avgNumRooms)
WHERE {
	?apartment swp:hasNumberOfBedrooms ?bedrooms.
}
```  
Nó sẽ trả về:  
|?avgNumRooms|  
|:----------:|  
|2|  

Hàm tổng hợp được kết hợp với từ khóa AS để biểu thị biến trong tập kết quả. Chúng ta không bị giới hạn về việc áp dụng những hàm tổng hợp này trên toàn bộ bộ kết quả. Ta cũng có thể tổng hợp cho các nhóm cụ thể bằng việc sử dụng GROUP BY.  
SPARQL do đó cung cấp các cơ thế mạnh mẽ để tổ chức kết quả theo cách phù hợp nhất với ứng dụng hiện có.  

## 3.6 Các hình thức truy vấn khác của SPARQL
Đến nay, ta đã tập trung vào việc lựa chọn những giá trị nhất định từ một bộ của RDF. SPARQL cũng hỗ trợ vài hình thức khác của các truy vấn. Hai truy vấn được sử dụng phổ biến bên lạnh SELECT là ASK và CONSTRUCT.  
Hình thức truy vấn ASK đơn giản là kiểm tra xem liệu mẫu đồ thị có tồn tại trong bộ dữ liệu không thay vì trả về một kết quả. Ví dụ, truy vấn dưới đây sẽ trả về *true*.  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX dbpedia-owl: <http://dbpedia.org/ontology/>.

ASK ?apartment
WHERE {
	?apartment swp:hasNumberOfBedrooms 3.
}
```  

Các truy vấn ASK được sử dụng bởi vì chúng tính toán nhanh hơn tìm toàn bộ bộ kết quả.  
Hình thức truy vấn COUNSTRUCT được sử dụng để lấy ra một đồ thị RDF từ một bộ RDF lớn hơn. Do đó, ta có thể truy vấn một triple store và lấy ra một đồ thị RDF chứ không phải một danh sách các liên kết biến. Ví dụ, ta có thể tạo một đồ thị với có nhãn là "big apartments" với những các có hơn 2 phòng ngủ.  
```SPARQL
PREFIX ex: <http://www.example.org/>.
PREFIX dbpedia: <http://dbpedia.org/resource/>.
PREFIX geo: <http://www.geonames.org/ontology#>.

CONSTRUCT {?apartment swp:hasNumberOfBedrooms ?bedrooms. ?apartment swp:isBigApartment true.}
WHERE{
	?apartment swp:hasNumberOfBedrooms ?bedrooms.
}
FILTER (?bedrooms > 2)
```  
Nó sẽ trả về đồ thị dưới đây:  
```Turtle
@prefix swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
@prefix dbpedia: <http://dbpedia.org/resource/>.
@prefix dbpedia-owl: <http://dbpedia.org/ontology/>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#>.

swp:BaronWayApartment swp:hasNumberOfBedrooms 3.
swp:BaronWayApartment swp:isBigApartment true.
```  
Các truy vấn CONSTRUCT thường được sử dụng để phiên dịch giữa các lược đồ bằng cách truy vấn các mẫu cụ thể và thay thế trong các thuộc tính từ lược đồ được nhắm tới.  

## 3.7 Lược đồ truy vấn
Một điều quan trọng rằng, vì thông tin lược đồ được biểu diễn bằng RDF, SPARQL có thể được sử dụng để truy vấn thông tin về chính lược đồ. Ví dụ, tiếp theo sẽ là một phần của bản thể luận nhà ở từ chương trước.  
```Turtle
@prefix swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>.
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>.

swp:Unit rdf:type rdfs:Class.

swp:ResidentialUnit rdf:type rdfs:Class.
swp:ResidentialUnit rdfs:subClassOf swp:Unit.

swp:Apartment rdf:type rdfs:Class.
swp:Apartment rdfs:subClassOf swp:ResidentialUnit.
```  

Sử dụng SPARQL, ta có thể xác định Residential Units trong cơ bộ dữ liệu bằng cách truy vấn cả dữ liệu instance và lược đồ cùng một lúc:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>.

SELECT ?apartment
WHERE{
	?apartment a ?unitType.
	?unitType rdfs:subClassOf swp:ResidentialUnit.
}
```  
Ở đây, ta sử dụng một cách viết tắt tương tự như trong Turtle, *a* nghĩa là rdf:type. Khả năng truy vấn đến lược đồ vô cùng quan trọng với SPARQL và RDF, nó cho phép ta không chỉ lấy thông tin mà còn truy vấn đến ngữ nghĩa của thông tin.  

## 3.8 Thêm một thông tin bằng SPARQL Update
Như đã đề cập ở 3.1, SPARQL cũng định nghĩa một phương thức để cập nhật nội dung của một triple store. Đó là phương thức SPARQL Update. Về bản chất, nó thêm một loạt từ khóa mới vào SPARQL cho phép chèn (insert), tải (load), và xóa (delete) các bộ ba.  
  
**Chèn và Tải các bộ ba:* Chèn một phát biểu rằng Luxury Apartment là một lớp con của Apartment. Nó sẽ thêm một bộ ba vào bất kỳ nội dung nào nằm trong triple store.  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>.

INSERT DATA
{
	swp:LuxuryApartment rdfs:subClassOf swp:Apartment.
}
```  

Lưu ý rằng bản chất dữ liệu cũng chỉ là cú pháp Turtle.  
Nếu bạn có một file lớn chứa RDF có sẵn trên web, bạn có thể tải nó vào một triple store bằng câu lệnh sau:  
```SPARQL
LOAD <http://example.com/apartment.rdf>
```  
  
**Xóa các bộ ba:** Có nhiều cách để xóa bộ ba từ một triple store. Một là xác định chính xác bộ ba bạn muốn xóa bằng từ khóa DELETE DATA. Xóa một bộ ba sẽ như sau:  
```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

DELETE DATA
{
	swp:LuxuryApartment rdfs:subClassOf swp:Apartment.
}
```  

Với hình thức này sẽ không có biến được truyền vào và tất cả bộ ba phải được xác định rõ ràng.  
Một hình thức linh hoạt hơn, là sử dụng cấu trúc DELETE WHERE. Nó xóa các bộ ba tương ứng với mẫu đồ thị được đưa ra. Các câu lệnh dưới đây sẽ xóa tất cả các bộ ba chứa thông tin về các căn hộ với nhiều hơn 2 phòng ngủ.  

```SPARQL
PREFIX swp: <http://www.semanticwebprimer.org/ontology/apartments.ttl#>.
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>.

WHERE{
?apartment swp:hasNumberOfBedrooms ?bedrooms.
	FILTER (?bedrooms > 2)
}
```  

Trong cả 2 trường hợp, nếu mẫu không phù hợp hoặc các bộ ba không nằm trong triple store thì không có gì xảy ra cả.  
Cuối cùng, để xóa toàn bộ các nội dung của một triple store cấu trúc CLEAR được sử dụng như sau:  
```SPARQL
CLEAR ALL
```  

SPARQL Update cung cấp vài cấu trúc khác để quản lý các phần của triple store.  Các thao tác cập nhật thực sự hữu ích nếu ta thêm dần các dữ liệu vào triple store.  

## 3.9 Làm theo nguyễn tắc mũi thuyền của bạn
SPARQL cung cấp các cơ sở để truy vấn và cập nhật triple store. Nhưng làm cách nào để triple store được lưu trữ? Như đã đề cập dến trước đây, nhiều nhà cung cấp dữ liệu cung cấp dữ liệu thông qua các điểm cuối SPARQL. Tuy nhiên, những nhà cung cấp những liệu khác chỉ cung cấp dữ liệu của họ dưới dạng Dữ liệu được liên kết (Linked Data). Tức là, dữ liệu RDF được cung cấp dưới dạng tệp trên web hoặc được nhúng trong các trang web. Chúng ta có thể chèn các bộ ba này vào triple store cục bộ của mình. Tuy nhiên, Mạng Ngữ Nghĩa cho phép bất kỳ nhà cung cấp nào mô tả thông tin của họ sử dụng tài nguyên và thông tin khác trên web. Trong những trường hợp này, nguyên tắc mũi thuyền có thể áp dụng: Đưa ra 1 URL trỏ đến một vài RDF, ta có thể tham chiếu URL đó và tải dữ liệu tương ứng. Ta cứ làm như vậy cho đến khi có đủ bộ ba để trả lời truy vấn được đưa ra.  
Một vài công cụ truy vấn như [SQUIN](http://squin.sourceforge.net/index.shtml) triển khai tính năng này. Tất nhiên, phiên bản mới nhất của SPARQL có chứa các lệnh cho truy vấn liên kết như vậy. Tuy nhiên, nhưng truy vấn liên kết đó thường tốn nhiều thời gian vì dữ liệu phải được thu thập tại thời điểm truy vấn.  

## 3.10 Tổng kết
Trong chương này, ta đã giới thiệu về SPARQL, cả phần truy vấn và cập nhật của nó, cũng như các cơ sở hạ tầng cơ bản hỗ trợ SPARQL.  
- SPARQL lựa chọn thông tin bằng cách ánh xạ với mẫu đồ thị, và cung cấp phương thức để lọc dựa trên cả so sánh số và chuỗi.  
- Các truy vấn SPARQL đi theo một cú pháp tương tự với Turtle.  
- Cả dữ liệu và lược đồ đều có thể được truy vấn sử dụng SPARQL.  
- UNION và OPTIONAL là cấu trúc cho phép SPARQL dễ tương tác hơn với thế giới mở.  
- SPARQL Update cung cấp cơ chế để cập nhật và xóa thông tin từ triple stores.  






