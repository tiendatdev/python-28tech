# %%
# In ra một chuỗi bất kỳ ra màn hình
print('Ròm Tiến Đạt')

a = 100
b = 200
c = 300

print(a, b, c)

# Nếu không có tham số sep thì khi in ra mặc định sẽ có một khoảng trắng giữa các giá trị được in ra.

print(a, b, c, sep='|')
# 100|200|300

# Khi mà in ra một chuỗi ký tự thì đẩy chuỗi ký tự đó vào trong dấu nháy đơn hoặc nháy kép đều được

print('Ròm Tiến Đạt')  # Ròm Tiến Đạt
print("Ròm Tiến Đạt")  # Ròm Tiến Đạt

# Nếu muốn in ra một chuỗi ký tự chứa dấu nháy đơn hoặc nháy kép thì phải sử dụng dấu nháy kép để bao quanh chuỗi ký tự đó

# In ra xâu ký tự (được đặt trong nháy đơn hoặc nháy kép)

print("Ròm Tiến Đạt")

print('Ròm Tiến Đạt')

# In nhiều object

print("Ròm", "Tiến", "Đạt")

print("html", "css", "javascript", "python")

# print có tham số sep

print("Ròm", "Tiến", "Đạt", sep="#")
print("html", "css", "javascript", "python", sep="|")

# print có tham số end

print("Ròm", end=" ")
print("Tiến", end="--")
print("Đạt", end="***")

# print có tham số end và sep

print("Ròm", "Tiến", "Đạt", sep="|", end="***")

print("html", "css", "javascript", "python", sep="|", end="***\n")



