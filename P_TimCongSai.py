lst = list(map(int, input("Nhap vao ds cac so nguyen, cach nhau boi dau phay: ").split(',')))
diffs = [lst[i] - lst[i-1] for i in range(1, len(lst))]
print(diffs[0] if all(diff == diffs[0] for diff in diffs) else "None")
