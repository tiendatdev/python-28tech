# Bài 2 : Câu lệnh print và các kiểu dữ liệu trong Python

## 1. Câu lệnh print: 

Giúp **in ra nội dung lên màn hình**, nội dung có thể là các xâu ký tự, các đối tượng bất kỳ trong Python. Trước khi được in ra màn hình, các đối tượng này được chuyển thành các xâu ký tự.

### Cú pháp: 

> print(object, sep = seperator, end = end)

### Các tham số của hàm print()

**Object:** Các đối tượng trong Python: Số, các xâu đối tượng, là những cái sẽ in ra màn hình

**sep:** Phân cách giữa các đối tượng khi in, nếu không có tham số này thì mặc định sẽ là dấu cách (tham số này có cũng được không có cũng được)

**end:** Chỉ ra các ký tự được in ở cuối của dòng, nếu không có tham số này thì mặc định sẽ là dấu xuống dòng: Chỉ định hàm print() sau khi in ra dòng sẽ kết thúc bởi cái gì, nó sẽ quy định (tham số này có cũng được không có cũng được, không có mặc định sẽ là phím Enter khi hàm kết thúc)

### Ví dụ

**In ra xâu ký tự (được đặt trong nháy đơn hoặc nháy kép)**

```python
print("Ròm Tiến Đạt")

print('Ròm Tiến Đạt')
```

**In nhiều object**

```python
print("Ròm", "Tiến", "Đạt")

print("html", "css", "javascript", "python")
```

**print có tham số sep**

```python
print("Ròm", "Tiến", "Đạt", sep="#")

print("html", "css", "javascript", "python", sep="|")
```

**print có tham số end**

```python
print("Ròm", end=" ")

print("Tiến", end="--")

print("Đạt", end="***")
```

```python
print("html", "css", "javascript", "python", sep="|", end="***\n")
```